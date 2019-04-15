// Liste des constantes admises
const c = {
    TIME_UNIT: 0.1,      // 0.1 seconde réelle correspond à 1 seconde en simulation
    PIXELS_EN_METRE: 10  // 10 pixels en simulation correspondent à 1 m réel
};

// Classe s'occupant des conversions de notre programme (temps, longueurs, ...)
class Conversion {
    // Prend en paramètre les secondes écoulés dans le monde réel et les converties en celles du programme
    static secRealToSimu(n) {
        //  TIME_UNIT secondes réelles => 1 seconde en simulation
        //  x secondes réelles         <= n secondes en simulation
        return (c.TIME_UNIT * n) / 1;
    }


    /** Convertis des mètres en pixels */
    static metersToPixel(n) {
        //  PIXELS_EN_METRE pixels  =>  1 mètre
        //  x pixels                <=  n mètre
        return (c.PIXELS_EN_METRE * n) / 1;
    }
}
