let instance; // instance de jeu principale
let lastRender;
let st;


// Fonction appelée automatiquement dès le lancement du code par P5
function setup() {
    createCanvas(900, 900); // création d'une fenêtre 900 x 900 pixels

    instance = new Instance();
    lastRender = Date.now() / 1000;
    st = false;

    noLoop();
    requestAnimationFrame(gLoop); // appelle gLoop() dès que possible
}


// Boucle principale de la simulation
function gLoop() {
    let current = Date.now() / 1000; // current = temps actuel converti en secondes
    let progress = current - lastRender;

    instance.update(Conversion.secRealToSimu(progress)); // mise à jour de l'instance de jeu en fonction du temps écoulé

    background(29, 26, 27);
    instance.draw(); // affichage des éléments

    lastRender = current;

    if(!st) requestAnimationFrame(gLoop); // si le programme ne doit pas être arrêté, appelle gLoop() dès que possible
}


// Fonction pouvant être appelée dans la console stoppant le programme "proprement"
function stop() {
    st = true;
}
