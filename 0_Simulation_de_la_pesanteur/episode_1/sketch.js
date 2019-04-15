// Fonction appelée automatiquement dès le lancement du code par P5
function setup() {
    createCanvas(900, 900); // création d'une fenêtre 900 x 900 pixels

    noLoop();
    requestAnimationFrame(gLoop); // appelle gLoop() dès que possible
}

// Boucle principale de la simulation
function gLoop() {
    requestAnimationFrame(gLoop);
}
