// Fonction pour supprimer un vêtement
function deleteClothes(clothesId) {
    // Envoyer une requête au serveur avec l'id du vêtement
    fetch(`/clothes_delete/${clothesId}`, {
        method: "POST",
        body: JSON.stringify({ id: clothesId })
    })
    // S'il y a une réponse :
    .then(response => {
        // Si la réponse est correcte (suppression du compte) : 
        if (response.ok) {
            // Recharger la page
            window.location.reload();
        // Sinon : 
        } else {
            console.error("Erreur lors de la suppression du vêtement.");
        }
    });
}