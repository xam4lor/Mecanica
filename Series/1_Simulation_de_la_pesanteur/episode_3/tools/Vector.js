// Classe des vecteurs
class Vector {
    // Nouveau vecteur (x, y)
    constructor(x, y) {
        this.x = x;
        this.y = y;
    }

    // Ajoute le vecteur v à celui en instance
    add(v) {
        this.x += v.x;
        this.y += v.y;
        return this;
    }

    // Multiplie le vecteur par n
    mult(n) {
        this.x *= n;
        this.y *= n;
        return this;
    }
}
