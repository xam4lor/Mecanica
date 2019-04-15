// Cette classe s'occupera de gérer les objets de notre simulation (mise à jour puis affichage)
class Instance {
    constructor() {
        this.elements = [];

        // Création de 10 éléments aux propriétés aléatoires
        for (let i = 0; i < 10; i++) {
            this.elements[i] = new Element(random(1, 4), random(5, 70), 50, random(-0.1, 0.1), random(-0.3, 0.3));
        }
    }


    // Mise à jour de l'Instance et des éléments
    update(progress) {
        for (let i = 0; i < this.elements.length; i++) {
            this.elements[i].update(progress);
        }
    }


    // Affichage de l'Instance et des éléments
    draw() {
        for (let i = 0; i < this.elements.length; i++) {
            this.elements[i].draw();
        }
    }
}
