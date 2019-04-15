// Liste des constantes admises
const c = {
    TIME_UNIT: 0.1 // 0.1 seconde réelle correspond à 1 seconde en simulation
};

// Classe s'occupant des conversions de notre programme (temps, longueurs, ...)
class Conversion {
    // Prend en paramètre les secondes écoulés dans le monde réel et les converties en celles du programme
    static secRealToSimu(n) {
        return (c.TIME_UNIT * n) / 1;
    }
}
