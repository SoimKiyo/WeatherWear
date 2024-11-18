document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("usermodifyform");
    const emailInput = document.getElementById("email");
    const passwordInput = document.getElementById("password");
    const passwordConfirmInput = document.getElementById("password_confirm");
    const cityInput = document.getElementById("city");
    const countryInput = document.getElementById("country");
    const latitudeInput = document.getElementById("latitude");
    const longitudeInput = document.getElementById("longitude");
    const savePopup = document.getElementById("save-popup");

    // Boolean pour savoir s'il y a un changement ou pas
    let changesDetected = false;

    // Stocker les valeurs initiales pour détecter les changements
    const initialEmail = emailInput.value;
    const initialPassword = passwordInput.value;
    const initialLatitude = latitudeInput.value;
    const initialLongitude = longitudeInput.value;

    // Initialiser la carte avec Leaflet
    const map = L.map("map").setView([latitudeInput.value || 48.8566, longitudeInput.value || 2.3522], 8); // Paris par défaut

    // Charger les tuiles d'OpenStreetMap
    L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    // Si une position est déjà stockée dans la base de données, afficher le marqueur à cet endroit
    let marker;
    if (latitudeInput.value && longitudeInput.value) {
        marker = L.marker([latitudeInput.value, longitudeInput.value], { draggable: true }).addTo(map);
        map.setView([latitudeInput.value, longitudeInput.value], 8);
    }

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
        latitudeInput.value = lat;
        longitudeInput.value = lng;

        // Appeler l'API Nominatim pour récupérer la ville et le pays
        fetch(`https://nominatim.openstreetmap.org/reverse?format=json&lat=${lat}&lon=${lng}`)
            .then(response => response.json())
            .then(data => {
                cityInput.value = data.address.city || data.address.town || data.address.village;
                countryInput.value = data.address.country;
                detectChanges();  // Vérifier les changements après mise à jour de la carte
            });
    }

    // Attacher un événement "click" sur la carte pour capturer les clics de l'utilisateur
    map.on("click", onMapClick);

    // Fonction pour afficher la popup si des changements sont détectés
    const showSavePopup = () => {
        savePopup.classList.remove("hidden");
    };

    // Fonction pour cacher la popup
    const hideSavePopup = () => {
        savePopup.classList.add("hidden");
    };

    // Fonction pour détecter les changements dans les champs
    const detectChanges = () => {
        if (emailInput.value !== initialEmail || passwordInput.value !== initialPassword ||
            latitudeInput.value !== initialLatitude || longitudeInput.value !== initialLongitude) {
            if (!changesDetected) {
                changesDetected = true;
                showSavePopup();
            }
        } else {
            if (changesDetected) {
                changesDetected = false;
                hideSavePopup();
            }
        }
    };

    // Écouteur pour détecter les changements dans les champs texte
    [emailInput, passwordInput, passwordConfirmInput].forEach(input => {
        input.addEventListener("input", () => {
            detectChanges();
        });
    });

    // Enregistre les changements
    document.getElementById("confirm-save").addEventListener("click", async () => {
        const formData = new FormData(form);

        try {

            // Envoie une requête au serveur
            const response = await fetch("/user_modify", {
                method: "POST",
                body: formData
            });


            // Si la réponse est correcte
            if (response.ok) {
                changesDetected = false;
                hideSavePopup();
                window.location.reload();  // Recharge la page
            } else {
                console.error("Erreur lors de la sauvegarde des modifications");
            }
        } catch (err) {
            console.error("Erreur lors de la sauvegarde :", err);
        }
    });

    // Annule les changements
    document.getElementById("cancel-changes").addEventListener("click", () => {
        hideSavePopup();
        changesDetected = false;
    });

    
});
