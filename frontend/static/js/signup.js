let map = L.map("map").setView([48.8566, 2.3522], 8); // Paris comme position par défaut

        // Charger les tuiles d'OpenStreetMap
        L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
            attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        }).addTo(map);

        let marker;

        // Fonction pour ajouter un marqueur à l'endroit cliqué et enregistrer les coordonnées
        function onMapClick(e) {
            let lat = e.latlng.lat;
            let lng = e.latlng.lng;

            // Supprimer le marqueur existant si l'utilisateur clique à un autre endroit
            if (marker) {
                map.removeLayer(marker);
            }

            // Ajouter un nouveau marqueur
            marker = L.marker([lat, lng]).addTo(map);

            // Mettre à jour les champs cachés avec les nouvelles coordonnées
            document.getElementById("latitude").value = lat;
            document.getElementById("longitude").value = lng;

            // Appel à l'API Nominatim pour obtenir les informations sur la ville et le pays
            fetch(`https://nominatim.openstreetmap.org/reverse?format=json&lat=${lat}&lon=${lng}`)
                .then(response => response.json())
                .then(data => {
                    document.getElementById("city").value = data.address.city || data.address.town || data.address.village;
                    document.getElementById("country").value = data.address.country;
                });
        }

        // Attacher un événement "click" sur la carte pour capturer les clics de l'utilisateur
        map.on("click", onMapClick);

        // Détecter la langue du navigateur et la stocker dans le champ caché
        document.getElementById("language").value = navigator.language || navigator.userLanguage;