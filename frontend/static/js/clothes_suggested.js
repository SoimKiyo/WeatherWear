// Fonction pour rafraîchir les vêtements
function refreshSuggestions() {
    // Envoyer une requête au serveur
    fetch("/clothes_suggested", {
        method: "POST",
        headers: { "Content-Type": "application/json" }
    })
    .then(response => response.json()) // Transformer la réponse en JSON
    .then(data => {
        const clothesFrame = document.querySelector(".clothes-frame");
        clothesFrame.innerHTML = ""; // Effacer les anciens vêtements

        // Parcourir chaque catégorie et ses vêtements
        for (let category in data.suggested_clothes) {
            // Créer le titre de la catégorie
            const categoryTitle = `<h3 class="category-title">${category}</h3>`;
            
            // Créer le conteneur pour les vêtements
            let categoryClothes = '<div class="category-clothes">';
            data.suggested_clothes[category].forEach(item => {
                categoryClothes += `
                    <div class="clothescard">
                        <img src="data:image/jpeg;base64,${item.cloth_image}" alt="${item.subtype}">
                        <div class="clothescard-info">
                            <h4>${item.subtype}</h4>
                            <p>Matériau : ${item.texture}</p>
                        </div>
                    </div>
                `;
            });
            categoryClothes += "</div>";

            // Ajouter la catégorie et ses vêtements
            clothesFrame.innerHTML += `<div class="category">${categoryTitle}${categoryClothes}</div>`;
        }
    })
    .catch(error => console.error("Erreur :", error)); // Afficher une erreur s'il y en a une
}
