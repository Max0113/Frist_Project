#include <stdio.h>
#include <stdlib.h>

int main() {
    int val;
    int max, min , pmax , pmin;
    int i = 0;

    pmax = pmin = 0 ;

    printf("Entrez un nombre (0 pour arrêter) : ");
    scanf("%d", &val);

    if (val == 0) {
        printf("Aucun nombre saisi.\n");
        return 0;
    }

    // Initialiser max et min avec la première valeur
    max = min = val;

    while (val != 0) {
        i++;
        printf("Entrez un nombre %d (0 pour arrêter) : ", i + 1);
        scanf("%d", &val);

        if (val != 0) {
            if (val > max) {
                max = val;
                pmax = i + 1;
            }
            if (val < min) {
                min = val;
                pmin = i + 1;
            }
        }
    }

    printf("\nLe maximum est : %d | Le position : %d \n", max, pmax);
    printf("Le minimum est : %d | Le position : %d \n", min, pmin);

    return 0;
}
