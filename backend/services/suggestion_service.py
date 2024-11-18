from datetime import datetime
from utils import get_last_used

# Listes de vêtements par températures
vetements_froids = [
    "Manteau", "Doudoune longue", "Doudoune courte", "Manteau long", 
    "Pull col roulé", "Pull col rond", "Pull col en V", "Cardigan oversize",
    "Gilet boutonné", "Sweat à capuche (hoodie)", "Veste puffer", 
    "Veste en cuir", "Veste coupe-vent", "Veste bomber", "Veste en jean", "Manteau classique",
    "Manteau imperméable", "Jean skinny", "Jean droit", "Jean bootcut", "Jean boyfriend",
    "Jean mom fit", "Jean taille haute", "Jean taille basse", "Jean baggy", "Pantalon droit",
    "Pantalon slim", "Pantalon cargo", "Pantalon chino", "Pantalon large", "Pantalon jogging",
    "Pantalon de survêtement", "Pantalon de tailleur", "Pantalon 7/8", "Bonnet", "Écharpe légère",
    "Écharpe longue", "Foulard", "Gants classiques", "Mitaines", "Ceinture classique", "Ceinture large",
    "Ceinture fine"
]

vetements_moyens = [
    "Veste", "Cardigan classique", "Sweat sans capuche", "Sweat col rond",
    "Chemise à manches longues", "T-shirt à manches longues", "Chemise oversize",
    "Pull col en V", "Pull oversize", "Veste de blazer", "Veste zippée",
    "Veste en jean", "Pantalon jogging", "Pull col rond", "Chemise à col boutonné",
    "Polo à manches longues", "Cardigan zippé", "Gilet boutonné", "Gilet sans manches",
    "Cardigan oversize", "Jean skinny", "Jean droit", "Jean bootcut", "Jean boyfriend",
    "Jean mom fit", "Jean taille haute", "Jean taille basse", "Jean cropped", "Jean baggy",
    "Pantalon droit", "Pantalon slim", "Pantalon cargo", "Pantalon chino", "Pantalon large",
    "Pantalon jogging", "Pantalon de survêtement", "Pantalon de tailleur", "Pantalon 7/8",
    "Bermuda", "Jupe midi", "Jupe longue", "Jupe évasée", "Jupe droite", "Jupe portefeuille",
    "Jupe patineuse", "Casquette", "Bonnet", "Bob", "Casquette de sport", "Écharpe légère",
    "Foulard", "Ceinture classique", "Ceinture large", "Ceinture fine"
]

vetements_chauds = [
    "T-shirt à manches courtes", "T-shirt col en V", "T-shirt basique", "T-shirt oversized",
    "T-shirt crop-top", "T-shirt col rond", "Chemise à manches courtes", "Polo à manches courtes",
    "Short classique", "Bermuda", "Jupe courte", "Cycliste", "Casquette", "Bob", "Chemise classique",
    "Chemise oversize", "Gilet sans manches", "Jean skinny", "Jean droit", "Jean bootcut", "Jean boyfriend",
    "Jean mom fit", "Jean taille haute", "Jean taille basse", "Jean cropped", "Pantalon droit", "Pantalon slim",
    "Pantalon cargo", "Pantalon chino", "Pantalon large", "Pantalon jogging", "Pantalon de survêtement",
    "Pantalon de tailleur", "Pantalon 7/8", "Short en jean", "Short classique", "Short de sport", "Bermuda",
    "Cycliste", "Jupe courte", "Jupe midi", "Jupe longue", "Jupe évasée", "Jupe droite", "Jupe portefeuille",
    "Jupe patineuse", "Casquette de sport", "Ceinture classique", "Ceinture large", "Ceinture fine"
]

# Listes de vêtements spécifiques pour la pluie et le vent
vetements_pluie = [
    "Manteau imperméable", "Trench-coat", "Veste coupe-vent", "Veste en Gore-Tex",
    "Doudoune longue", "Doudoune courte", "Parka", "Poncho imperméable", "Sweat à capuche (hoodie)",
    "Bonnet", "Bob", "Ceinture fine"
]

vetements_vent = [
    "Veste coupe-vent", "Manteau imperméable", "Veste bomber", "Veste en Gore-Tex", "Bonnet", "Foulard",
    "Écharpe longue", "Gants classiques"
]

# Textures des vêtements en fonction de la météo
materiaux_impermeables = ["Gore-Tex", "Polyester", "Nylon"]
materiaux_chauds = ["Laine", "Cachemire", "Élasthanne", "Acrylique", "Alpaga", "Cuir", "Polaire", "Duvet (rembourrage)", "Oxford", "Soie", "Flanelle", "Laine mérinos", "Cuir véritable", "Simili cuir", "Denim avec élasthanne"]
materiaux_legers = ["Coton", "Satin", "Lin", "Denim 100% coton", "Toile", "Viscose", "Métal", "Jersey", "Bambou", "Mélange coton-polyester", "Modal", "Chambray", "Popeline", "Piqué de coton", "Coton biologique", "Coton mélangé", "Mélange coton-élastane", "Denim"]

# Couleurs des vêtements possible
clothesColors = [
    "Noir", "Blanc", "Gris", "Bleu", "Rouge", "Vert", "Jaune", "Beige", "Rose", 
    "Violet", "Orange", "Marron", "Bleu marine", "Indigo", "Kaki", "Turquoise", "Bordeaux"
]

# Fonction pour suggérer les vêtements (En fonction de la garde-robe et de la météo)
def suggest_clothes_algo(wardrobe, summarized_weather):
    ### TRIE PAR RAPPORT A LA METEO
    # Récupérer les informations météo
    temperature, humidity, wind, meteo = summarized_weather
    
    # Catégories de vêtements
    suggestions = {"Vestes": [], "Hauts": [], "Bas": [], "Accessoires": []}

    # Choisir les vêtements et matières selon la température
    # Si il fait moins de 10 degrés
    if temperature < 10:
        # Ajouter les textures/vêtements adaptés
        selected_clothes = vetements_froids
        selected_textures = materiaux_chauds
    # Si il fait entre 10 et 20
    elif 10 <= temperature <= 20:
        # Ajouter les textures/vêtements adaptés
        selected_clothes = vetements_moyens
        selected_textures = materiaux_chauds + materiaux_legers
    # Si il fait plus de 20
    else:
        # Ajouter les textures/vêtements adaptés
        selected_clothes = vetements_chauds
        selected_textures = materiaux_legers

    # Choisir les vêtements et matières selon la météo
    # Si il pleut ou que l'humidité est au de là de 90%
    if meteo == "Rain" or humidity > 90:
        selected_clothes += vetements_pluie
        selected_textures += materiaux_impermeables
    # Si le vent va à plus de 20km/h
    if wind > 20:
        selected_clothes += vetements_vent

    # Liste des vêtements filtrés
    filtered_clothes = []
    # Pour chaque vêtement dans la garde-robe
    for clothe in wardrobe:
        # Si un vêtement/texture (Parmis les listes) est présents dans l'une des listes (Par rapport à la météo)
        if clothe["subtype"] in selected_clothes and clothe["texture"] in selected_textures:
            # Alors ajouté à la liste filté
            filtered_clothes.append(clothe)

    # Choisir un vêtement par catégorie en prenant le moins récemment utilisé
    for category in suggestions:
        # Récupérer les vêtements de la catégorie
        category_clothes = []
        for clothe in filtered_clothes:
            if clothe["type"] == category:
                category_clothes.append(clothe)
        
        # Trier et ajouter le moins utilisé
        if len(category_clothes) > 0:
            category_clothes.sort(key=get_last_used)  # Trier par dernière utilisation
            suggestions[category].append(category_clothes[0])  # Ajouter le premier (moins utilisé)


    ### TRIE PAR RAPPORT A LA COULEUR
    # Liste pour les couleurs des vêtements (sélectionné à la création/modification)
    clothes_colors = []
    # Parcourt toutes les listes de vêtements dans suggestions (par catégorie)
    for clothes in suggestions.values():
        # Parcourt chaque vêtement parmis les vêtements
        for clothe in clothes:
            # Si la couleur du vêtement n'est pas déjà dans la liste on l'ajoute
            if clothe["color"] not in clothes_colors:
                clothes_colors.append(clothe["color"])

    # Liste pour les deux couleurs qu'on sélectionne
    selected_colors = []
    # Parcourt toutes les couleurs disponibles dans la liste "clothesColors"
    for color in clothesColors:
        # Si la couleur est dans clothes_colors et qu'on n'a pas encore 2 couleurs on l'ajoute
        if color in clothes_colors and len(selected_colors) < 2:
            selected_colors.append(color)

    # Compléter les catégories vides avec les couleurs sélectionné
    for clothe in filtered_clothes:
        category = clothe["type"]
        # Si aucune suggestion n'existe pour cette catégorie:
        if len(suggestions[category]) == 0:
            # Si la couleur du vêtement est dans selected_colors ou si on peut ajouter une nouvelle couleur:
            if clothe["color"] in selected_colors or len(selected_colors) < 2:
                suggestions[category].append(clothe)  # Ajoute le vêtement à la catégorie
                # Si la couleur du vêtement ajouté n'est pas déjà dans selected_colors on l'ajoute: 
                if clothe["color"] not in selected_colors:
                    selected_colors.append(clothe["color"])

    

    ### REMPLISSEMENT FINAL (SI CATEGORIE VIDE)
    # Parcourt toutes les catégories dans suggestions
    for category in suggestions:
        # Si une catégorie est encore vide
        if len(suggestions[category]) == 0:
            # Liste pour les vêtements de remplissage
            filling_clothes = [] 

            # Parcourt tous les vêtements dans la garde robe
            for clothe in wardrobe:
                # Si le vêtement appartient à la catégorie actuelle
                if clothe["type"] == category:
                    filling_clothes.append(clothe)

            # Si des vêtements de remplissage sont disponible
            if len(filling_clothes) > 0:
                # Trier les vêtements de remplissage par dernière utilisation
                filling_clothes.sort(key=get_last_used)
                # Ajouter le vêtement le moins récemment utilisé à la catégorie
                suggestions[category].append(filling_clothes[0])

    return suggestions
