import requests
from collections import Counter
from datetime import datetime

#Fonction pour récupérer les informations météo de OpenWeatherAPI avec la localisation
def get_current_weather(lat, lon, api_key):
    response = requests.get(
        f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&units=metric&appid={api_key}'
    )

    data = response.json()
    return data['list']

#Fonction pour "résumé" (regrouper) les informations météo collectées
def summarize_weather_info(weather_data):
    # Listes pour les différentes catégories d'informations météo
    temperatures = []
    humidities = []
    winds = []
    conditions = []
    current_date = datetime.now().strftime('%Y-%m-%d')

    # Filtrage de la météo du jour ou de la date la plus proche (si non disponible)
    date_found = False
    for data in weather_data:
        fetch_date = datetime.fromtimestamp(data['dt']).strftime('%Y-%m-%d')

        if fetch_date == current_date or not date_found:
            temperatures.append(data['main']['temp'])
            humidities.append(data['main']['humidity'])
            winds.append(data['wind']['speed'])
            conditions.append(data['weather'][0]['main'])
            date_found = True  # Stop une fois la première date trouvée

    # Moyenne des informations météo récupéré
    temperatures_moyenne = round(sum(temperatures) / len(temperatures), 2)
    humidites_moyenne = round(sum(humidities) / len(humidities), 2)
    vitesse_vent_moyen = round(sum(winds) / len(winds), 2)
    # Valeur météo la plus fréquente récupéré
    meteo_moyenne = Counter(conditions).most_common(1)[0][0]

    return temperatures_moyenne, humidites_moyenne, vitesse_vent_moyen, meteo_moyenne
