from flask import Blueprint, request, render_template, redirect, session, current_app, jsonify
from utils import connection_db, middleware_login
from services.suggestion_service import suggest_clothes_algo
from services.weather_service import summarize_weather_info, get_current_weather
from datetime import datetime
import base64

##################### CREATION DE VETEMENT #####################
# Listes des extensions autorisés pour les images
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}

# Vérification des extensions des fichiers en fonction de ceux autorisés
def allowed_file(filename):
    # Vérifie si le nom du fichier contient un point
    if '.' in filename:
        # Récupère l'extension du fichier après le dernier point et la met en minuscule
        extension = filename.rsplit('.', 1)[1].lower()
        # Vérifie si l'extension fait partie des extensions autorisées
        return extension in ALLOWED_EXTENSIONS
    return False

## Blueprint pour importer la route dans le app.py
clothescreate_routes = Blueprint('clothescreate_routes', __name__)

# Route de Création de vêtement
@clothescreate_routes.route('/clothes_create', methods=['GET', 'POST'])
@middleware_login
def clothes_create():
    # Récupère l'identifiant de l'utilisateur connecté depuis les données de session.
    user_id = session.get('user_id')
    
    # Si la demande est un envoie
    if request.method == 'POST':
        # Récupère les entrées de formulaires
        image_file = request.files.get('clothes_image')
        clothes_type = request.form.get('clothes_type')
        clothes_subtype = request.form.get('clothes_subtype')
        clothes_texture = request.form.get('clothes_material')
        clothes_color = request.form.get('clothes_color')

        # Vérification que tous les champs sont remplis
        if not image_file or not clothes_type or not clothes_texture or not clothes_color:
            print("Erreur: Tous les champs doivent être remplis.")
            return render_template('clothes_create.html'), 400
        
        # Si le fichier n'est pas dans le bon format
        if not allowed_file(image_file.filename):
            print("Erreur: Le fichier doit être une image valide.")
            return render_template('clothes_create.html'), 400

        # Encodage de l'image en Base64
        image_data = image_file.read()
        clothes_image_base64 = base64.b64encode(image_data).decode('utf-8')
        clothes_name = f"{clothes_type} - {clothes_subtype} ({clothes_texture})"
        
        # Connexion à la base de données et création du vêtement
        conn = connection_db()
        conn.execute('''
            INSERT INTO Wardrobe (user_id, name, type, subtype, color, texture, last_used, cloth_image) 
            VALUES (?, ?, ?, ?, ?, ?, datetime('now'), ?)
        ''', (user_id, clothes_name, clothes_type, clothes_subtype, clothes_color, clothes_texture, clothes_image_base64))
        conn.commit()
        conn.close()

        print("Vêtement ajouté avec succès.")
        return redirect("/clothes_list") 

    return render_template('clothes_create.html')


##################### MODIFICATION DE VETEMENT #####################
## Blueprint pour importer la route dans le app.py
clothesmodify_routes = Blueprint('clothesmodify_routes', __name__)

# Route de modification de compte
@clothesmodify_routes.route('/clothes_modify/<int:wardrobe_id>', methods=['GET', 'POST'])
@middleware_login
def clothes_modify(wardrobe_id):
    # Récupère l'identifiant de l'utilisateur connecté depuis les données de session.
    user_id = session.get('user_id')
    
    # Récupération des informations du vêtement sélectionné depuis la DB
    conn = connection_db()
    wardrobe = conn.execute('SELECT * FROM Wardrobe WHERE id = ? AND user_id = ?', (wardrobe_id, user_id)).fetchone()
    conn.close()

    # S'il n'y a pas d'informations par rapport au vêtement
    if not wardrobe:
        print("Erreur: Vêtement non trouvé.")
        return redirect("/clothes_list")

    # Si la demande est un envoie
    if request.method == 'POST':
        # Récupère les entrées de formulaires
        image_file = request.files.get('clothes_image')
        clothes_type = request.form.get('clothes_type')
        clothes_subtype = request.form.get('clothes_subtype')
        clothes_texture = request.form.get('clothes_material')
        clothes_color = request.form.get('clothes_color')

        # Vérification que tous les champs sont remplis
        if not clothes_type or not clothes_texture or not clothes_color:
            print("Erreur: Tous les champs doivent être remplis.")
            return render_template('clothes_modify.html', wardrobe=wardrobe), 400

        # Si une nouvelle image est choisis on l'utilise
        if image_file and allowed_file(image_file.filename):
            image_data = image_file.read()
            clothes_image_base64 = base64.b64encode(image_data).decode('utf-8')
        # Sinon on garde l'ancienne
        else:
            clothes_image_base64 = wardrobe['cloth_image']

        clothes_name = f"{clothes_type} - {clothes_subtype}"
        
        # Connexion à la base de données et mise à jour du vêtement
        conn = connection_db()
        conn.execute('''
            UPDATE Wardrobe SET name = ?, type = ?, subtype = ?, color = ?, texture = ?, last_used = datetime('now'), cloth_image = ? 
            WHERE id = ? AND user_id = ?
        ''', (clothes_name, clothes_type, clothes_subtype, clothes_color, clothes_texture, clothes_image_base64, wardrobe_id, user_id))
        conn.commit()
        conn.close()
        
        print("Modification du vêtement réussie.")
        return redirect("/clothes_list")

    # On affiche la page en fournissant les informations des vêtements à celle-ci
    return render_template('clothes_modify.html', wardrobe=wardrobe)

##################### LISTE DE VETEMENT #####################
## Blueprint pour importer la route dans le app.py
clotheslist_routes = Blueprint('clotheslist_routes', __name__)

# Route de modification de compte
@clotheslist_routes.route('/clothes_list', methods=['GET'])
@middleware_login
def clothes_list():
    # Récupère l'identifiant de l'utilisateur connecté depuis les données de session.
    user_id = session.get('user_id')

    # Connexion à la base de données et récupération de tout les vêtements correspondant au user_id fournis
    conn = connection_db()
    wardrobe = conn.execute('SELECT * FROM Wardrobe WHERE user_id = ?', (user_id,)).fetchall()
    conn.close()

    # On affiche la page en fournissant les informations des vêtements à celle-ci
    return render_template('clothes_list.html', wardrobe=wardrobe)


##################### SUPPRESSION DE VETEMENT #####################
@clotheslist_routes.route('/clothes_delete/<int:clothes_id>', methods=['POST'])
@middleware_login
def delete_clothes(clothes_id):
    # Récupère l'identifiant de l'utilisateur connecté depuis les données de session.
    user_id = session.get('user_id')

    # Connexion à la base de données et suppression du vêtement
    conn = connection_db()
    conn.execute('DELETE FROM Wardrobe WHERE id = ? AND user_id = ?', (clothes_id, user_id))
    conn.commit()
    conn.close()
    return '', 204


##################### SUGGESTIONS DE VETEMENT #####################
## Blueprint pour importer la route dans le app.py
clothessuggested_routes = Blueprint('clothessuggested_routes', __name__)

# Route pour afficher les suggestions de vêtements sans mettre à jour `last_used`
@clothessuggested_routes.route('/clothes_suggested', methods=['GET', 'POST'])
@middleware_login
def clothes_suggested():
    # Récupère l'identifiant de l'utilisateur connecté depuis les données de session.
    user_id = session.get('user_id')
    WEATHER_APIKEY = current_app.config['WEATHER_APIKEY']

    # Connexion à la base de données pour récupérer la localisation de l'utilisateur
    conn = connection_db()
    user_data = conn.execute('SELECT latitude, longitude FROM Users WHERE id = ?', (user_id,)).fetchone()
    conn.close()
    latitude = user_data['latitude']
    longitude = user_data['longitude']

    # Récupération de la garde-robe de l'utilisateur
    conn = connection_db()
    wardrobe = conn.execute('SELECT * FROM Wardrobe WHERE user_id = ?', (user_id,)).fetchall()
    conn.close()

    # Transformation des données de la garde-robe pour le format requis par l'algorithme
    wardrobe_data = []
    for item in wardrobe:
        last_used = datetime.strptime(item['last_used'], '%Y-%m-%d %H:%M:%S') if item['last_used'] else None
        wardrobe_data.append({
            "type": item['type'],
            "subtype": item['subtype'],
            "texture": item['texture'],
            "color": item['color'],
            "last_used": last_used,
            "id": item['id'],
            "cloth_image": item['cloth_image']
        })

    # Utilisation des fonctions météo pour récupérer la météo actuel
    weather_data = get_current_weather(latitude, longitude, WEATHER_APIKEY)
    summarized_weather = summarize_weather_info(weather_data)
    temperature, humidity, wind_speed, weather_condition = summarized_weather

    current_weather = weather_data[0]  # Sélection du premier élément de la liste
    weather_icon_code = current_weather['weather'][0].get('icon', '01d')  # Accéder à l'icône
    weather_icon_url = f"https://openweathermap.org/img/wn/{weather_icon_code}@2x.png"


    # Suggestions des vêtements avec l'algorithme
    suggested_clothes = suggest_clothes_algo(wardrobe_data, summarized_weather)

    # Si le bouton "refresh" est pressé (requête POST), on met à jour `last_used`
    if request.method == 'POST':
        # Connexion à la Base de données
        conn = connection_db()

        # Mise à jour de last_used
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        for category, items in suggested_clothes.items():
            for item in items:
                conn.execute('UPDATE Wardrobe SET last_used = ? WHERE id = ?', (current_time, item['id']))
        conn.commit()
        conn.close()
        
        # On renvoie en json les informations des vêtements suggérés
        return jsonify(suggested_clothes=suggested_clothes)

    # On affiche la page en fournissant les informations météo
    return render_template(
        'clothes_suggested.html',
        suggested_clothes=suggested_clothes,
        temperature=temperature,
        humidity=humidity,
        wind_speed=wind_speed,
        weather_condition=weather_condition,
        weather_icon_url=weather_icon_url
    )