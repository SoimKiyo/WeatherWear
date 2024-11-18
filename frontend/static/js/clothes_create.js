// Boolean permetant de dire si une image est sélectionné ou non
let isImageSelected = false;

// Liste de tout les vêtements par rapport au types
const subtypesByType = {
    "Vestes": [
        "Veste en jean", "Veste en cuir", "Veste bomber", "Veste zippée", "Veste de blazer", "Veste coupe-vent",
        "Veste puffer", "Manteau classique", "Manteau long", "Doudoune courte", "Doudoune longue", "Trench-coat",
        "Manteau imperméable", "Cardigan classique", "Cardigan zippé", "Gilet boutonné", "Gilet sans manches", "Cardigan oversize"
    ],
    "Hauts": [
        "T-shirt à manches courtes", "T-shirt à manches longues", "T-shirt oversized", "T-shirt crop-top", "T-shirt basique",
        "T-shirt col rond", "T-shirt col en V", "Chemise à manches courtes", "Chemise à manches longues", "Chemise classique",
        "Chemise oversize", "Chemise à col boutonné", "Polo à manches courtes", "Polo à manches longues", "Sweat à capuche (hoodie)",
        "Sweat sans capuche", "Sweat col rond", "Pull col rond", "Pull col en V", "Pull col roulé", "Pull oversize"
    ],
    "Bas": [
        "Jean skinny", "Jean droit", "Jean bootcut", "Jean boyfriend", "Jean mom fit", "Jean taille haute",
        "Jean taille basse", "Jean cropped", "Jean baggy", "Pantalon droit", "Pantalon slim", "Pantalon cargo", 
        "Pantalon chino", "Pantalon large", "Pantalon jogging", "Pantalon de survêtement", "Pantalon de tailleur", "Pantalon 7/8",
        "Short en jean", "Short classique", "Short de sport", "Bermuda", "Cycliste", "Jupe courte", "Jupe midi", "Jupe longue", 
        "Jupe évasée", "Jupe droite", "Jupe portefeuille", "Jupe patineuse"
    ],
    "Accessoires": [
        "Casquette", "Bonnet", "Bob", "Casquette de sport", "Écharpe légère", "Écharpe longue", "Foulard", 
        "Gants classiques", "Mitaines", "Ceinture classique", "Ceinture large", "Ceinture fine"
    ]
};

// Liste de toutes les textures par rapport au vêtements
const materialsBySubtype = {
    "T-shirt à manches courtes": ["Coton", "Polyester", "Viscose", "Bambou"],
    "T-shirt à manches longues": ["Coton", "Mélange coton-polyester", "Lin", "Viscose"],
    "T-shirt oversized": ["Coton", "Jersey", "Mélange coton-polyester"],
    "T-shirt crop-top": ["Coton", "Modal", "Viscose", "Polyester"],
    "T-shirt basique": ["Coton biologique", "Coton peigné", "Polyester"],
    "T-shirt col rond": ["Coton", "Jersey", "Mélange coton-modal"],
    "T-shirt col en V": ["Coton", "Modal", "Mélange coton-polyester"],
    "Chemise à manches courtes": ["Coton", "Lin", "Polyester", "Chambray"],
    "Chemise à manches longues": ["Coton", "Popeline", "Lin", "Oxford"],
    "Chemise classique": ["Coton", "Soie", "Mélange coton-polyester"],
    "Chemise oversize": ["Flanelle", "Chambray", "Lin"],
    "Chemise à col boutonné": ["Popeline", "Oxford", "Coton"],
    "Polo à manches courtes": ["Piqué de coton", "Mélange coton-polyester", "Coton biologique"],
    "Polo à manches longues": ["Piqué de coton", "Coton mélangé", "Lin"],
    "Sweat à capuche (hoodie)": ["Polaire", "Coton", "Mélange coton-polyester"],
    "Sweat sans capuche": ["Polaire", "Mélange coton-polyester", "Laine"],
    "Sweat zippé": ["Polaire", "Mélange coton-polyester", "Acrylique"],
    "Sweat col rond": ["Polaire", "Coton", "Mélange coton-viscose"],
    "Pull col rond": ["Laine", "Cachemire", "Coton", "Acrylique"],
    "Pull col en V": ["Laine mérinos", "Cachemire", "Mélange laine-acrylique"],
    "Pull col roulé": ["Laine", "Cachemire", "Laine mérinos"],
    "Pull oversize": ["Laine", "Coton", "Mohair", "Alpaga"],
    "Veste en jean": ["Denim", "Mélange coton-élastane"],
    "Veste en cuir": ["Cuir véritable", "Simili cuir"],
    "Veste bomber": ["Nylon", "Polyester", "Satin"],
    "Veste zippée": ["Nylon", "Coton", "Polyester"],
    "Veste de blazer": ["Laine", "Polyester", "Lin"],
    "Veste coupe-vent": ["Nylon", "Polyester", "Gore-Tex"],
    "Veste puffer": ["Nylon", "Polyester", "Duvet (rembourrage)"],
    "Manteau classique": ["Laine", "Cachemire", "Mélange laine-polyester"],
    "Manteau long": ["Laine", "Cachemire", "Mélange laine-coton"],
    "Doudoune courte": ["Nylon", "Polyester", "Duvet (rembourrage)"],
    "Doudoune longue": ["Nylon", "Polyester", "Duvet"],
    "Trench-coat": ["Coton", "Polyester", "Nylon"],
    "Manteau imperméable": ["Gore-Tex", "Polyester", "Nylon"],
    "Cardigan classique": ["Laine", "Coton", "Cachemire", "Acrylique"],
    "Cardigan zippé": ["Laine", "Mélange coton-polyester", "Polaire"],
    "Gilet boutonné": ["Laine mérinos", "Cachemire", "Acrylique"],
    "Gilet sans manches": ["Laine", "Coton", "Polaire"],
    "Cardigan oversize": ["Laine", "Cachemire", "Mohair", "Alpaga"],
    "Jean skinny": ["Denim avec élasthanne", "Mélange coton-polyester"],
    "Jean droit": ["Denim 100% coton", "Coton biologique"],
    "Jean bootcut": ["Denim avec élasthanne", "Mélange coton-polyester"],
    "Jean boyfriend": ["Denim 100% coton", "Mélange coton-élastane"],
    "Jean mom fit": ["Denim 100% coton", "Coton biologique"],
    "Jean taille haute": ["Denim avec élasthanne", "Mélange coton-polyester"],
    "Jean taille basse": ["Denim avec élasthanne", "Mélange coton-polyester"],
    "Jean cropped": ["Denim 100% coton", "Mélange coton-élastane"],
    "Jean baggy": ["Denim", "Mélange coton-polyester"],
    "Pantalon droit": ["Coton", "Lin", "Laine", "Polyester"],
    "Pantalon slim": ["Coton avec élasthanne", "Polyester", "Laine"],
    "Pantalon cargo": ["Coton", "Nylon", "Polyester"],
    "Pantalon chino": ["Coton", "Lin", "Mélange coton-polyester"],
    "Pantalon large": ["Lin", "Viscose", "Coton", "Polyester"],
    "Pantalon jogging": ["Polaire", "Coton", "Mélange coton-polyester"],
    "Pantalon de survêtement": ["Nylon", "Polyester", "Coton"],
    "Pantalon de tailleur": ["Laine", "Polyester", "Mélange laine-polyester"],
    "Pantalon 7/8": ["Coton", "Polyester", "Lin"],
    "Short en jean": ["Denim", "Mélange coton-polyester"],
    "Short classique": ["Coton", "Lin", "Polyester"],
    "Short de sport": ["Nylon", "Polyester", "Élasthanne"],
    "Bermuda": ["Coton", "Lin", "Mélange coton-polyester"],
    "Cycliste": ["Polyester", "Nylon", "Élasthanne"],
    "Jupe courte": ["Coton", "Polyester", "Cuir"],
    "Jupe midi": ["Lin", "Viscose", "Mélange laine-polyester"],
    "Jupe longue": ["Coton", "Viscose", "Polyester"],
    "Jupe évasée": ["Coton", "Lin", "Mélange coton-polyester"],
    "Jupe droite": ["Laine", "Polyester", "Mélange laine-polyester"],
    "Jupe portefeuille": ["Coton", "Lin", "Soie"],
    "Jupe patineuse": ["Coton", "Polyester", "Viscose"],
    "Casquette": ["Coton", "Polyester", "Nylon"],
    "Bonnet": ["Laine", "Acrylique", "Coton"],
    "Bob": ["Coton", "Polyester", "Nylon"],
    "Casquette de sport": ["Polyester", "Nylon", "Élasthanne"],
    "Écharpe légère": ["Lin", "Viscose", "Coton"],
    "Écharpe longue": ["Laine", "Cachemire", "Alpaga"],
    "Foulard": ["Soie", "Viscose", "Coton"],
    "Gants classiques": ["Laine", "Cuir", "Polyester"],
    "Mitaines": ["Laine", "Coton", "Acrylique"],
    "Ceinture classique": ["Cuir", "Simili cuir", "Toile"],
    "Ceinture large": ["Cuir", "Simili cuir"],
    "Ceinture fine": ["Cuir", "Simili cuir", "Métal"]
};

// Liste des couleurs des vêtements
const clothesColors = [
    "Noir", "Blanc", "Gris", "Bleu", "Rouge", "Vert", "Jaune", "Beige", "Rose", 
    "Violet", "Orange", "Marron", "Bleu marine", "Indigo", "Kaki", "Turquoise", "Bordeaux"
];

// Fonction pour mettre à jour/activer la sélection des sous-types par rapport aux types
function updateSubtypes() {
    // Récupère les éléments de sélection par leurs ID
    const typeSelect = document.getElementById("clothes_type");
    const subtypeSelect = document.getElementById("clothes_subtype");
    const selectedType = typeSelect.value;

    // Réinitialise le champ des sous-types avec une option par défaut
    subtypeSelect.innerHTML = '<option value="" disabled selected>Choisir un sous-type</option>';
    
    // Vérifie si le type sélectionné a des vêtements liés
    if (subtypesByType[selectedType]) {
        // Ajoute chaque vêtements comme option dans le champ de sélection
        subtypesByType[selectedType].forEach(subtype => {
            const option = document.createElement("option");
            option.value = subtype;
            option.textContent = subtype;
            subtypeSelect.appendChild(option);
        });
    }
}

// Fonction pour mettre à jour la sélection des matières en fonction du sous-type sélectionné
function updateMaterials() {
    const subtypeSelect = document.getElementById("clothes_subtype");
    const materialSelect = document.getElementById("clothes_material");
    const selectedSubtype = subtypeSelect.value;

    // Réinitialise le champ des matières avec une option par défaut
    materialSelect.innerHTML = '<option value="" disabled selected>Choisir une matière</option>';
    
    // Vérifie si le sous-type sélectionné a des matières liés
    if (materialsBySubtype[selectedSubtype]) {
        // Ajoute chaque matière comme option dans le champ de sélection
        materialsBySubtype[selectedSubtype].forEach(material => {
            const option = document.createElement("option");
            option.value = material;
            option.textContent = material;
            materialSelect.appendChild(option);
        });
    }
}

// Fonction pour mettre à jour la sélection des couleurs
function updateColors() {
    const colorSelect = document.getElementById("clothes_color");

    // Réinitialise le champ des couleurs avec une option par défaut
    colorSelect.innerHTML = '<option value="" disabled selected>Choisir une couleur</option>';
    
    // Ajoute chaque couleur de la liste comme option dans le champ de sélection
    clothesColors.forEach(color => {
        const option = document.createElement("option");
        option.value = color;
        option.textContent = color;
        colorSelect.appendChild(option);
    });
}

// Fonction pour passer à l'étape suivante du formulaire
function nextStep(step) {
    const currentStep = document.querySelector(".form-step.active");
    const newStep = document.getElementById(`step${step}`);

    // Vérifie si la nouvelle étape existe
    if (!newStep) return;

    // Vérifie si une image est sélectionnée avant de passer à l'étape 2
    if (step === 2 && !isImageSelected) {
        alert("Veuillez sélectionner une image avant de continuer.");
        return;
    }

    // Change l'étape active du formulaire
    currentStep.classList.remove("active");
    currentStep.style.display = "none";
    newStep.style.display = "block";
    newStep.classList.add("active");
}

// Fonction pour revenir à l'étape précédente du formulaire
function prevStep(step) {
    const currentStep = document.querySelector(".form-step.active");
    const newStep = document.getElementById(`step${step}`);
    
    // Change l'étape active du formulaire
    currentStep.classList.remove("active");
    currentStep.style.display = "none";
    newStep.style.display = "block";
    newStep.classList.add("active");
}

// Gestionnaire d'événement pour la sélection d'image
const fileInput = document.getElementById("image");
fileInput.addEventListener("change", (e) => {
    const file = e.target.files[0];

    // Vérifie si le fichier sélectionné est une image
    if (file && file.type.startsWith("image/")) {
        isImageSelected = true;
        previewImage(file);
    } else {
        alert("Veuillez sélectionner une image valide.");
        isImageSelected = false;
    }
});

// Fonction pour prévisualiser l'image
function previewImage(file) {
    // Crée une nouvelle instance de FileReader pour lire le contenu du fichier
    const reader = new FileReader();

    // Définit une fonction à exécuter lorsque le fichier est complètement chargé
    reader.onload = () => {
        // Récupère l'élément HTML avec l'ID 'uploadBox'
        const uploadBox = document.getElementById("uploadBox");
        
        // Supprime l'icône et le texte d'instruction s'ils existent
        const icon = uploadBox.querySelector(".icon");
        const instructionText = uploadBox.querySelector("span");
        if (icon) icon.style.display = "none";
        if (instructionText) instructionText.style.display = "none";

        // Vérifie s'il y a déjà une image prévisualisée et la supprime si nécessaire
        const existingImg = uploadBox.querySelector("img");
        if (existingImg) {
            uploadBox.removeChild(existingImg);
        }

        // Crée un nouvel élément image et définit ses attributs
        const img = document.createElement("img");
        img.src = reader.result; // Définit la source de l'image
        img.alt = "Prévisualisation de l'image"; // Définit le texte alternatif de l'image
        img.style.maxWidth = "100%"; // Définit la largeur maximale de l'image
        img.style.maxHeight = "100%"; // Définit la hauteur maximale de l'image
        img.style.borderRadius = "8px"; // Ajoute des coins arrondis à l'image
        uploadBox.appendChild(img); // Ajoute l'image à l'élément 'uploadBox'
    };

    // Définit une fonction à exécuter en cas d'erreur
    reader.onerror = () => {
        alert("Une erreur est survenue. Veuillez réessayer.");
        isImageSelected = false; // Réinitialise la boolean de sélection de l'image
    };

    // Lit le contenu du fichier en tant qu'URL
    reader.readAsDataURL(file);
}
