import sqlite3, re
from flask import request, session, redirect
from functools import wraps

# Connexion à la DB
def connection_db():
    conn = sqlite3.connect('../database/weatherwear.db')
    conn.row_factory = sqlite3.Row
    return conn

# Initialisation de la base de données
def init_db():
    conn = connection_db()
    conn.executescript('''
    CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email VARCHAR(255) UNIQUE NOT NULL,
        password VARCHAR(255) NOT NULL,
        city VARCHAR(100),
        country VARCHAR(100),
        latitude DECIMAL(10, 8),
        longitude DECIMAL(11, 8),
        language VARCHAR(10),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS Wardrobe (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        name VARCHAR(255),
        type VARCHAR(100),
        subtype VARCHAR(100),
        color VARCHAR(7),
        texture VARCHAR(100),
        last_used TIMESTAMP,
        cloth_image VARCHAR(255),
        FOREIGN KEY (user_id) REFERENCES Users(id)
    );
    ''')
    conn.commit()
    conn.close()

# Valider l'email pour s'assurer qu'il est bien formaté
def validate_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

# Vérifier si le mot de passe correspond au "Confirmer le mot de passe"
def ifpassword_verified(password):
    password_confirm = request.form.get('password_confirm')
    return password == password_confirm

# Fonction pour récupérer les informations de l'utilisateurs depuis l'email
def get_user_by_email(email):
    conn = connection_db()
    cursor = conn.execute('SELECT id, email, password, city, country, latitude, longitude, language, created_at FROM Users WHERE email = ?', (email,))
    user = cursor.fetchone()
    conn.close()
    return user

# Fonction pour obtenir la dernière date d'utilisation d'un vêtement
def get_last_used(clothe):
    # Retourne la date de dernière utilisation, ou une date très ancienne si jamais utilisé
    return clothe['last_used'] if clothe['last_used'] else datetime.min
    
# Middleware pour vérifier si l'utilisateur est connecté
def middleware_login(f):  # F est la fonction protégé (Dans notre cas une route Flask)
    @wraps(f) # Conserve le nom/informations de la fonction d'origine
    def verify_connexion(*args, **kwargs):  # args/kwargs permet de recevoir tout les arguments possible recu par la fonction d'origine
        if 'user_id' not in session:  # Si l'utilisateur n'est pas connecté
            return redirect("/login")  # Redirige vers la page de connexion
        return f(*args, **kwargs)  # Si connecté, exécute la fonction normalement en renvoyant les arguments récupéré
    return verify_connexion  # Retourne la nouvelle fonction