// Classe d'un élément de la simulation
class Element {
    // Nouvel élément, avec la masse en kg, et x, y, vx et vy en mètres
    constructor(mass, x, y, vx, vy) {
        this.mass = mass;

        // Définition de la position, la vitesse, et l'accélération converties en pixels
        this.position = new Vector(Conversion.metersToPixel(x), Conversion.metersToPixel(y));
        this.velocity = new Vector(Conversion.metersToPixel(vx), Conversion.metersToPixel(vy));
        this.acceleration = new Vector(Conversion.metersToPixel(0), Conversion.metersToPixel(0));

        this.r = this.mass * 15; // Le rayon de l'ellipse est arbitrairement 15 fois sa masse
    }


    // Mise à jour de l'élément
    update(progress) {
        // Mise à jour des composantes des vecteurs
        this.acceleration.mult(progress);
        this.velocity.add(this.acceleration);
        this.position.add(this.velocity);
    }


    // Affichage de l'élément
    draw() {
        // Bordures de l'élément
        stroke(0);
        strokeWeight(2);

        // Dessine une ellipse
        fill(255, 127);
        ellipse(this.position.x, this.position.y, this.r * 2);

        // Point rouge au centre de l'ellipse
        stroke(255, 0, 0, 255);
        strokeWeight(5);
        point(this.position.x, this.position.y);
    }
}
