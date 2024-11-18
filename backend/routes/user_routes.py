from flask import Blueprint, request, render_template, redirect, session
from utils import connection_db, validate_email, ifpassword_verified, get_user_by_email, middleware_login
import bcrypt

##################### INSCRIPTION #####################
## Blueprint pour importer la route dans le app.py
signup_routes = Blueprint('signup_routes', __name__)

# Permet de hacher le mot de passe et de le saler
def password_encryption(password):
    sel = bcrypt.gensalt()
    password_hashed = bcrypt.hashpw(password.encode('utf-8'), sel)
    return password_hashed

# Permet de vérifier si un compte existe avec cette adresse email
def is_account_already_existing(email):
    # Connexion à la Base de données
    conn = connection_db()
    cur = conn.cursor()

    # Requête pour sélectionner toutes les informations lié à un utilisateur en fonction de son email
    cur.execute('SELECT * FROM Users WHERE email = ?', (email,))
    data = cur.fetchone()

    # Fermeture de la Base de données
    conn.close()
    return data

# Route d'inscription
@signup_routes.route('/signup', methods=['GET', 'POST'])
def signup():
    # Si la demande est un envoie
    if request.method == 'POST':
        # Récupère les entrées de formulaires
        email = request.form.get('email')
        password = request.form.get('password')
        latitude = request.form.get('latitude')
        longitude = request.form.get('longitude')
        city = request.form.get('city')
        country = request.form.get('country')
        language = request.form.get('language')

        # Vérification que tous les champs sont remplis
        if not email or not password or not latitude or not longitude or not city or not country or not language:
            print("Erreur : Tous les champs doivent être remplis.")
            return render_template('signup.html'), 400
        
        # Valider le format de l'email
        if not validate_email(email):
            print("Erreur : Email invalide.")
            return render_template('signup.html'), 400
        
        # Hachage du mot de passe
        hashed_password = password_encryption(password)

        # Vérification du mot de passe
        if ifpassword_verified(password):
            data = is_account_already_existing(email)
            # Si un compte existe déjà :
            if data:
                print("Erreur : Un compte avec cet email existe déjà.")
                return render_template('signup.html'), 400
            # Sinon :
            else:
                # Connexion à la base de données/Création d'un nouveau compte
                conn = connection_db()
                cur = conn.cursor()
                cur.execute('INSERT INTO Users (email, password, latitude, longitude, city, country, language) VALUES (?, ?, ?, ?, ?, ?, ?)', 
                            (email, hashed_password, latitude, longitude, city, country, language))
                conn.commit()
                conn.close()
                print("Inscription réussie.")
                return redirect("/login")
        else:
            print("Erreur : Les mots de passe ne correspondent pas.")
            return render_template('signup.html'), 400
    
    return render_template('signup.html')


##################### CONNEXION #####################
## Blueprint pour importer la route dans le app.py
login_routes = Blueprint('login_routes', __name__)

# Route de connexion
@login_routes.route('/login', methods=['GET', 'POST'])
def login():
    # Si la demande est un envoie
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # Vérification que tous les champs sont remplis
        if not email or not password:
            print("Erreur : Tous les champs doivent être remplis.")
            return render_template('login.html'), 400
        
        # Valider le format de l'email
        if not validate_email(email):
            print("Erreur : Email invalide.")
            return render_template('login.html'), 400
        
        # Récupérer l'utilisateur avec l'email
        user = get_user_by_email(email)
        if user is None:
            print("Erreur : Email ou mot de passe incorrect.")
            return render_template('login.html'), 401
        
        # Vérifier et récupérer le mot de passe haché
        hashed_password = user['password']

        # Vérifier que le mot de passe fourni correspond au mot de passe haché
        if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
            session['user_id'] = user['id']
            print("Connexion réussie.")
            return redirect("/clothes_suggested")
        else:
            print("Erreur : Email ou mot de passe incorrect.")
            return render_template('login.html'), 401
    
    return render_template('login.html')


##################### MODIFICATION DE COMPTE #####################
## Blueprint pour importer la route dans le app.py
usermodify_routes = Blueprint('usermodify_routes', __name__)

# Route de modification de compte
@usermodify_routes.route('/user_modify', methods=['GET', 'POST'])
@middleware_login
def user_modify():
    user_id = session.get('user_id')
    
    # Si la demande est un envoie
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        password_confirm = request.form.get('password_confirm')
        city = request.form.get('city')
        country = request.form.get('country')
        latitude = request.form.get('latitude')
        longitude = request.form.get('longitude')
        delete_account = request.form.get('delete_account')

        # Création de liste pour prendre en compte les entrées modifiés et les valeurs
        updatefields = []
        updatevalues = []

        # Si le bouton supprimer est pressé
        if delete_account:
            conn = connection_db()
            conn.execute('DELETE FROM Users WHERE id = ?', (user_id,))
            conn.commit()
            conn.close()
            session.clear()
            print("Compte supprimé.")
            return redirect("/")

        # Vérifier et ajouter chaque champ modifié dans la liste des mises à jour
        if email:
            if not validate_email(email):
                print("Erreur : Email invalide.")
                return render_template('user_modify.html'), 400
            updatefields.append('email = ?')
            updatevalues.append(email)

        # Si le mot de passe correspond au mot de passe de confirmation
        if password and password_confirm:
            # Sinon
            if not ifpassword_verified(password):
                print("Erreur : Les mots de passe ne correspondent pas.")
                return render_template('user_modify.html'), 400
            # Hasher le nouveau mot de passe
            password_hashed = password_encryption(password)
            updatefields.append('password = ?')
            updatevalues.append(password_hashed)

        # Si il y les informations de la carte
        if city and country and latitude and longitude:
            updatefields.append('city = ?, country = ?, latitude = ?, longitude = ?')
            updatevalues.extend([city, country, latitude, longitude])

        # Si aucun champ n'a été modifié, retourner une erreur
        if not updatefields:
            print("Erreur : Aucune modification n'a été détectée.")
            return render_template('user_modify.html'), 400

        # Requête SQL de mise à jour avec les informations dans les listes
        query = f"UPDATE Users SET {', '.join(updatefields)} WHERE id = ?"
        updatevalues.append(user_id)

        # Connexion à la base de données
        conn = connection_db()
        conn.execute(query, updatevalues)
        conn.commit()
        conn.close()
        print("Modifications réussies.")

    # Si c'est une requête GET , on récupère les informations de l'utilisateur
    conn = connection_db()
    user = conn.execute('SELECT * FROM Users WHERE id = ?', (user_id,)).fetchone()
    conn.close()

    # Si l'utilisateur existe
    if user:
        return render_template('user_modify.html', user=user)
    else:
        print("Erreur : Utilisateur non trouvé.")
        return render_template('user_modify.html'), 404


##################### DECONNEXION #####################
## Blueprint pour importer la route dans le app.py
logout_routes = Blueprint('logout_routes', __name__)

# Route de déconnexion
@logout_routes.route('/logout')
@middleware_login
def logout():
    # Suppression de la session
    session.clear()
    print("Déconnexion réussie.")
    return redirect("/")
