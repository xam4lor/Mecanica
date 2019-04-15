// Cette classe s'occupera de gérer les objets de notre simulation (mise à jour puis affichage)
class Instance {
    constructor() {
        this.elements = [];

        // Création de 10 éléments aux positions et masses aléatoires
        for (let i = 0; i < 10; i++) {
            this.elements[i] = new Element(random(1, 4), random(5, 70), 20, 0, 0);
        }
    }


    // Mise à jour de l'Instance et des éléments
    update(progress) {
        for (let i = 0; i < this.elements.length; i++) {
            this.applyForces(this.elements[i]); // applique une force

            this.elements[i].update(progress); // mise à jour
        }
    }


    // Affichage de l'Instance et des éléments
    draw() {
        for (let i = 0; i < this.elements.length; i++) {
            this.elements[i].draw();
        }
    }


    // Application des forces sur un élément
    applyForces(el) {
        el.acceleration.mult(0); // annulation de l'accélération

        // Ajout des forces (vent aléatoire et poids relatif à la masse de l'objet)
        let vent = new Vector(1, 0);
        let poids = new Vector(0, el.mass * 9.81);
        el.applyForce(vent);
        el.applyForce(poids);

        // Application de la 2nd loi de Newton
        el.acceleration.div(el.mass);
    }
}
