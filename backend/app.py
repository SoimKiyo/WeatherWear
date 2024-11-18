#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template, jsonify
import os
from config import Config
from routes.user_routes import signup_routes, login_routes, logout_routes, usermodify_routes
from routes.wardrobe_routes import clotheslist_routes, clothescreate_routes, clothesmodify_routes, clothessuggested_routes
from utils import connection_db, init_db
from testcode import populate_wardrobe, delete_wardrobe_for_user

app = Flask(__name__, template_folder="../frontend/templates", static_folder="../frontend/static")
app.config.from_object(Config)

# Route Principal
@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


# Gestion des erreurs
@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Resource non trouvé"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Une erreur interne est survenue"}), 500

# Enregistrement des blueprints
### User Routes
app.register_blueprint(signup_routes)
app.register_blueprint(login_routes)
app.register_blueprint(logout_routes)
app.register_blueprint(usermodify_routes)

### Wardrobe Routes
app.register_blueprint(clothescreate_routes)
app.register_blueprint(clothesmodify_routes)
app.register_blueprint(clotheslist_routes)
app.register_blueprint(clothessuggested_routes)

# Démarrage du serveur et initialisation de la DB
if __name__ == '__main__':
    if not os.path.exists('../database'):
        os.makedirs('../database')

    init_db()
    #populate_wardrobe(1)
    #delete_wardrobe_for_user(1)

    app.run(debug=app.config['DEBUG'], host='0.0.0.0', port=5000)
