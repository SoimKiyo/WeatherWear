import sqlite3
from utils import connection_db, init_db
from services.suggestion_service import suggest_clothes_algo
import bcrypt

#Fonction pour remplir la garde-robe
def populate_wardrobe(user_id):
    conn = connection_db()
    cursor = conn.cursor()
    script_sql = f"""
    INSERT INTO Wardrobe (user_id, name, type, subtype, color, texture, last_used, cloth_image) VALUES
    -- T-shirts
    ({user_id}, "T-shirt à manches courtes en Coton", "Hauts", "T-shirt à manches courtes", "Noir", "Coton", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "T-shirt à manches courtes en Polyester", "Hauts", "T-shirt à manches courtes", "Noir", "Polyester", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "T-shirt à manches courtes en Viscose", "Hauts", "T-shirt à manches courtes", "Noir", "Viscose", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "T-shirt à manches courtes en Bambou", "Hauts", "T-shirt à manches courtes", "Noir", "Bambou", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "T-shirt à manches longues en Coton", "Hauts", "T-shirt à manches longues", "Noir", "Coton", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "T-shirt à manches longues en Mélange coton-polyester", "Hauts", "T-shirt à manches longues", "Noir", "Mélange coton-polyester", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "T-shirt à manches longues en Lin", "Hauts", "T-shirt à manches longues", "Noir", "Lin", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "T-shirt à manches longues en Viscose", "Hauts", "T-shirt à manches longues", "Noir", "Viscose", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "T-shirt oversized en Coton", "Hauts", "T-shirt oversized", "Noir", "Coton", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "T-shirt oversized en Jersey", "Hauts", "T-shirt oversized", "Noir", "Jersey", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "T-shirt oversized en Mélange coton-polyester", "Hauts", "T-shirt oversized", "Noir", "Mélange coton-polyester", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "T-shirt crop-top en Coton", "Hauts", "T-shirt crop-top", "Noir", "Coton", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "T-shirt crop-top en Modal", "Hauts", "T-shirt crop-top", "Noir", "Modal", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "T-shirt crop-top en Viscose", "Hauts", "T-shirt crop-top", "Noir", "Viscose", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "T-shirt crop-top en Polyester", "Hauts", "T-shirt crop-top", "Noir", "Polyester", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "T-shirt basique en Coton biologique", "Hauts", "T-shirt basique", "Noir", "Coton biologique", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "T-shirt basique en Coton peigné", "Hauts", "T-shirt basique", "Noir", "Coton peigné", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "T-shirt basique en Polyester", "Hauts", "T-shirt basique", "Noir", "Polyester", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "T-shirt col rond en Coton", "Hauts", "T-shirt col rond", "Noir", "Coton", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "T-shirt col rond en Jersey", "Hauts", "T-shirt col rond", "Noir", "Jersey", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "T-shirt col rond en Mélange coton-modal", "Hauts", "T-shirt col rond", "Noir", "Mélange coton-modal", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "T-shirt col en V en Coton", "Hauts", "T-shirt col en V", "Noir", "Coton", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "T-shirt col en V en Modal", "Hauts", "T-shirt col en V", "Noir", "Modal", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "T-shirt col en V en Mélange coton-polyester", "Hauts", "T-shirt col en V", "Noir", "Mélange coton-polyester", '2023-01-01 00:00:00', "default_image.png"),

    -- Chemises
    ({user_id}, "Chemise à manches courtes en Coton", "Hauts", "Chemise à manches courtes", "Noir", "Coton", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "Chemise à manches courtes en Lin", "Hauts", "Chemise à manches courtes", "Noir", "Lin", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "Chemise à manches courtes en Polyester", "Hauts", "Chemise à manches courtes", "Noir", "Polyester", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "Chemise à manches courtes en Chambray", "Hauts", "Chemise à manches courtes", "Noir", "Chambray", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "Chemise à manches longues en Coton", "Hauts", "Chemise à manches longues", "Noir", "Coton", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "Chemise à manches longues en Popeline", "Hauts", "Chemise à manches longues", "Noir", "Popeline", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "Chemise à manches longues en Lin", "Hauts", "Chemise à manches longues", "Noir", "Lin", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "Chemise à manches longues en Oxford", "Hauts", "Chemise à manches longues", "Noir", "Oxford", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "Chemise classique en Coton", "Hauts", "Chemise classique", "Noir", "Coton", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "Chemise classique en Soie", "Hauts", "Chemise classique", "Noir", "Soie", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "Chemise classique en Mélange coton-polyester", "Hauts", "Chemise classique", "Noir", "Mélange coton-polyester", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "Chemise oversize en Flanelle", "Hauts", "Chemise oversize", "Noir", "Flanelle", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "Chemise oversize en Chambray", "Hauts", "Chemise oversize", "Noir", "Chambray", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "Chemise oversize en Lin", "Hauts", "Chemise oversize", "Noir", "Lin", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "Chemise à col boutonné en Popeline", "Hauts", "Chemise à col boutonné", "Noir", "Popeline", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "Chemise à col boutonné en Oxford", "Hauts", "Chemise à col boutonné", "Noir", "Oxford", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "Chemise à col boutonné en Coton", "Hauts", "Chemise à col boutonné", "Bleu", "Coton", '2023-01-01 00:00:00', "default_image.png"),

    -- Polos
    ({user_id}, "Polo à manches courtes en Piqué de coton", "Hauts", "Polo à manches courtes", "Bleu", "Piqué de coton", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "Polo à manches courtes en Mélange coton-polyester", "Hauts", "Polo à manches courtes", "Bleu", "Mélange coton-polyester", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "Polo à manches courtes en Coton biologique", "Hauts", "Polo à manches courtes", "Bleu", "Coton biologique", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "Polo à manches longues en Piqué de coton", "Hauts", "Polo à manches longues", "Bleu", "Piqué de coton", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "Polo à manches longues en Coton mélangé", "Hauts", "Polo à manches longues", "Bleu", "Coton mélangé", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "Polo à manches longues en Lin", "Hauts", "Polo à manches longues", "Bleu", "Lin", '2023-01-01 00:00:00', "default_image.png"),

    -- Sweats
    ({user_id}, "Sweat à capuche (hoodie) en Polaire", "Hauts", "Sweat à capuche (hoodie)", "Bleu", "Polaire", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "Sweat à capuche (hoodie) en Coton", "Hauts", "Sweat à capuche (hoodie)", "Bleu", "Coton", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "Sweat à capuche (hoodie) en Mélange coton-polyester", "Hauts", "Sweat à capuche (hoodie)", "Bleu", "Mélange coton-polyester", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "Sweat sans capuche en Polaire", "Hauts", "Sweat sans capuche", "Bleu", "Polaire", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "Sweat sans capuche en Mélange coton-polyester", "Hauts", "Sweat sans capuche", "Bleu", "Mélange coton-polyester", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "Sweat sans capuche en Laine", "Hauts", "Sweat sans capuche", "Bleu", "Laine", '2023-01-01 00:00:00', "default_image.png"),

    -- Pulls
    ({user_id}, "Pull col rond en Laine", "Hauts", "Pull col rond", "Bleu", "Laine", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "Pull col rond en Cachemire", "Hauts", "Pull col rond", "Bleu", "Cachemire", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "Pull col rond en Coton", "Hauts", "Pull col rond", "Bleu", "Coton", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "Pull col rond en Acrylique", "Hauts", "Pull col rond", "Bleu", "Acrylique", '2023-01-01 00:00:00', "default_image.png"),

    -- Vestes
    ({user_id}, "Veste en jean en Denim", "Vestes", "Veste en jean", "Bleu", "Denim", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "Veste en jean en Mélange coton-élastane", "Vestes", "Veste en jean", "Bleu", "Mélange coton-élastane", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "Veste en cuir en Cuir véritable", "Vestes", "Veste en cuir", "Bleu", "Cuir véritable", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "Veste en cuir en Simili cuir", "Vestes", "Veste en cuir", "Bleu", "Simili cuir", '2023-01-01 00:00:00', "default_image.png"),

    -- Vestes
    ({user_id}, "Veste bomber en Nylon", "Vestes", "Veste bomber", "Bleu", "Nylon", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "Veste bomber en Polyester", "Vestes", "Veste bomber", "Bleu", "Polyester", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "Veste bomber en Satin", "Vestes", "Veste bomber", "Bleu", "Satin", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "Veste zippée en Nylon", "Vestes", "Veste zippée", "Bleu", "Nylon", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "Veste zippée en Coton", "Vestes", "Veste zippée", "Bleu", "Coton", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "Veste zippée en Polyester", "Vestes", "Veste zippée", "Bleu", "Polyester", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "Veste de blazer en Laine", "Vestes", "Veste de blazer", "Bleu", "Laine", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "Veste de blazer en Polyester", "Vestes", "Veste de blazer", "Bleu", "Polyester", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "Veste de blazer en Lin", "Vestes", "Veste de blazer", "Blanc", "Lin", '2023-01-01 00:00:00', "default_image.png"),

    -- Manteaux
    ({user_id}, "Manteau classique en Laine", "Vestes", "Manteau classique", "Blanc", "Laine", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "Manteau classique en Cachemire", "Vestes", "Manteau classique", "Blanc", "Cachemire", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "Manteau classique en Mélange laine-polyester", "Vestes", "Manteau classique", "Blanc", "Mélange laine-polyester", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "Manteau long en Laine", "Vestes", "Manteau long", "Blanc", "Laine", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "Manteau long en Cachemire", "Vestes", "Manteau long", "Blanc", "Cachemire", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "Manteau long en Mélange laine-coton", "Vestes", "Manteau long", "Blanc", "Mélange laine-coton", '2023-01-01 00:00:00', "default_image.png"),

    -- Pantalons
    ({user_id}, "Jean skinny en Denim avec élasthanne", "Bas", "Jean skinny", "Blanc", "Denim avec élasthanne", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "Jean skinny en Mélange coton-polyester", "Bas", "Jean skinny", "Blanc", "Mélange coton-polyester", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "Jean droit en Denim 100% coton", "Bas", "Jean droit", "Blanc", "Denim 100% coton", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "Jean droit en Coton biologique", "Bas", "Jean droit", "Blanc", "Coton biologique", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "Jean bootcut en Denim avec élasthanne", "Bas", "Jean bootcut", "Blanc", "Denim avec élasthanne", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "Jean bootcut en Mélange coton-polyester", "Bas", "Jean bootcut", "Blanc", "Mélange coton-polyester", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "Jean boyfriend en Denim 100% coton", "Bas", "Jean boyfriend", "Blanc", "Denim 100% coton", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "Jean boyfriend en Mélange coton-élastane", "Bas", "Jean boyfriend", "Blanc", "Mélange coton-élastane", '2023-01-01 00:00:00', "default_image.png"),

    -- Shorts
    ({user_id}, "Short en jean en Denim", "Bas", "Short en jean", "Blanc", "Denim", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "Short en jean en Mélange coton-polyester", "Bas", "Short en jean", "Blanc", "Mélange coton-polyester", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "Short classique en Coton", "Bas", "Short classique", "Blanc", "Coton", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "Short classique en Lin", "Bas", "Short classique", "Blanc", "Lin", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "Short classique en Polyester", "Bas", "Short classique", "Blanc", "Polyester", '2023-01-01 00:00:00', "default_image.png"),

    -- Jupes
    ({user_id}, "Jupe courte en Coton", "Bas", "Jupe courte", "Blanc", "Coton", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "Jupe courte en Polyester", "Bas", "Jupe courte", "Blanc", "Polyester", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "Jupe courte en Cuir", "Bas", "Jupe courte", "Blanc", "Cuir", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "Jupe midi en Lin", "Bas", "Jupe midi", "Blanc", "Lin", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "Jupe midi en Viscose", "Bas", "Jupe midi", "Blanc", "Viscose", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "Jupe midi en Mélange laine-polyester", "Bas", "Jupe midi", "Blanc", "Mélange laine-polyester", '2023-01-01 00:00:00', "default_image.png"),

    -- Accessoires
    ({user_id}, "Casquette en Coton", "Accessoires", "Casquette", "Blanc", "Coton", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "Casquette en Polyester", "Accessoires", "Casquette", "Blanc", "Polyester", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "Casquette en Nylon", "Accessoires", "Casquette", "Blanc", "Nylon", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "Bonnet en Laine", "Accessoires", "Bonnet", "Blanc", "Laine", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "Bonnet en Acrylique", "Accessoires", "Bonnet", "Blanc", "Acrylique", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "Bonnet en Coton", "Accessoires", "Bonnet", "Blanc", "Coton", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "Écharpe légère en Lin", "Accessoires", "Écharpe légère", "Blanc", "Lin", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "Écharpe légère en Viscose", "Accessoires", "Écharpe légère", "Blanc", "Viscose", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "Écharpe légère en Coton", "Accessoires", "Écharpe légère", "Blanc", "Coton", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "Ceinture classique en Cuir", "Accessoires", "Ceinture classique", "Blanc", "Cuir", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "Ceinture classique en Simili cuir", "Accessoires", "Ceinture classique", "Blanc", "Simili cuir", '2023-01-01 00:00:00', "default_image.png"),
    ({user_id}, "Ceinture classique en Toile", "Accessoires", "Ceinture classique", "Blanc", "Toile", '2023-01-01 00:00:00', "default_image.png")
    ;
    """

    # Exécuter le script SQL
    cursor.executescript(script_sql)
    conn.commit()
    print("Les vetements on correctement etait ajouter.")

    # Fermeture de la connexion
    cursor.close()
    conn.close()


#Supprimer toute la garde-robe
def delete_wardrobe_for_user(user_id):
    conn = connection_db()
    cursor = conn.cursor()
    
    script_sql = f"DELETE FROM Wardrobe WHERE user_id = {user_id};"
    
    cursor.executescript(script_sql)
    conn.commit()
    print(f"Tous les éléments de la garde-robe de l'utilisateur avec l'ID {user_id} ont été supprimés.")
    
    cursor.close()
    conn.close()

# Créer un utilisateur test
def test_create_user(email):
    conn = connection_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Users (email, password, city, country, latitude, longitude, language) VALUES 
        (?, "1234", "Paris", "France", 48.8566, 2.3522, "fr")
    ''', (email,))
    conn.commit()
    print("Utilisateur créé avec succès.")
    cursor.close()
    conn.close()

# Vérifie si un utilisateur existe
def test_user_exists(email):
    conn = connection_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Users WHERE email = ?', (email,))
    user = cursor.fetchone()
    if user:
        print(f"L'utilisateur avec l'email {email} existe.")
    else:
        print(f"Aucun utilisateur trouvé pour l'email {email}.")
    cursor.close()
    conn.close()

# Supprimer un utilisateur via Email
def delete_user(email):
    conn = connection_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Users WHERE email = ?', (email,))
    conn.commit()
    print(f"L'utilisateur avec l'email {email} a été supprimé.")
    cursor.close()
    conn.close()

# Afficher les vêtements dans la garde-robe dans utilisateur
def test_view_clothes(user_id):
    conn = connection_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Wardrobe WHERE user_id = ?', (user_id,))
    clothes = cursor.fetchall()
    for clothe in clothes:
        print(f"ID: {clothe['id']}, Nom: {clothe['name']}, Type: {clothe['type']}, Couleur: {clothe['color']}")
    cursor.close()
    conn.close()

# Test suggestion (Simulation)
def test_suggestions(user_id):
    conn = connection_db()
    cursor = conn.cursor()
    
    # Récupérer les vêtements et la localisation utilisateur
    cursor.execute('SELECT * FROM Wardrobe WHERE user_id = ?', (user_id,))
    wardrobe = cursor.fetchall()
    cursor.execute('SELECT latitude, longitude FROM Users WHERE id = ?', (user_id,))
    user_location = cursor.fetchone()
    conn.close()

    # Simuler une météo (exemple de données météo)
    weather_data = (12, 85, 15, "Rain")  # (température, humidité, vent, météo)

    # Tester l'algorithme de suggestion
    suggestions = suggest_clothes_algo(wardrobe, weather_data)

    print("Suggestions générées :")
    for category, items in suggestions.items():
        # Afficher le nom et la couleur des vêtements pour chaque catégorie
        print(f"{category} : {[f'{item['name']} (Couleur: {item['color']})' for item in items]}")

# Test connexion
def test_login_user(email, password):
    user = get_user_by_email(email)
    if user is None:
        print("Erreur : Aucun utilisateur trouvé avec cet email.")
        return
    hashed_password = user['password']
    if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
        print("Connexion réussie.")
    else:
        print("Erreur : Mot de passe incorrect.")



##############################################################################################
##############################################################################################
#####################                                                    #####################
#####################          LANCEMENT DE L'APP POUR LES TEST          #####################
#####################                                                    #####################
##############################################################################################
##############################################################################################


def run_all_tests():
    try:
        print("\n=== Exécution de tous les tests ===")
        # Obtenir l'email et l'ID utilisateur directement de l'utilisateur
        email = input("Entrez l'email de test : ")
        user_id = int(input("Entrez l'ID de l'utilisateur : "))

        print("\n1. Test de création d'utilisateur")
        test_create_user(email)

        print("\n2. Vérification de l'existence de l'utilisateur")
        test_user_exists(email)

        print("\n3. Ajout de vêtements dans la garde-robe")
        populate_wardrobe(user_id)

        print("\n4. Visualisation des vêtements")
        test_view_clothes(user_id)

        print("\n5. Suggestions de vêtements basées sur la météo")
        test_suggestions(user_id)

        print("\n6. Suppression de l'utilisateur")
        delete_user(email)

        print("\n7. Suppression des vêtements de la garde-robe")
        delete_wardrobe_for_user(user_id)

        print("\nTous les tests ont été exécutés avec succès.")
    except Exception as e:
        print(f"\nErreur lors de l'exécution des tests : {e}")


def show_menu():
    print("\n=== Menu des tests ===")
    print("1. Créer un utilisateur")
    print("2. Vérifier l'existence d'un utilisateur")
    print("3. Ajouter des vêtements")
    print("4. Afficher les vêtements")
    print("5. Tester les suggestions")
    print("6. Supprimer un utilisateur")
    print("7. Supprimer tous les vêtements")
    print("8. Exécuter tous les tests")
    print("9. Quitter")


def main():
    init_db()
    email = ""
    user_id = None

    while True:
        show_menu()
        choice = input("\nEntrez le numéro du test à exécuter : ")

        if choice == "1":
            if not email:
                email = input("Entrez l'email du compte à créer : ")
            test_create_user(email)
        elif choice == "2":
            if not email:
                email = input("Entrez l'email à vérifier : ")
            test_user_exists(email)
        elif choice == "3":
            if not user_id:
                user_id = int(input("Entrez l'ID de l'utilisateur : "))
            populate_wardrobe(user_id)
        elif choice == "4":
            if not user_id:
                user_id = int(input("Entrez l'ID de l'utilisateur : "))
            test_view_clothes(user_id)
        elif choice == "5":
            if not user_id:
                user_id = int(input("Entrez l'ID de l'utilisateur : "))
            test_suggestions(user_id)
        elif choice == "6":
            if not email:
                email = input("Entrez l'email de l'utilisateur à supprimer : ")
            delete_user(email)
        elif choice == "7":
            if not user_id:
                user_id = int(input("Entrez l'ID de l'utilisateur : "))
            delete_wardrobe_for_user(user_id)
        elif choice == "8":
            run_all_tests()
        elif choice == "9":
            print("Fin du programme.")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")


if __name__ == "__main__":
    main()
