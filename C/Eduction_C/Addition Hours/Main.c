#include <stdio.h>

void Entrer(int* , int* );
void Afficher(int* , int* );
void Addition(int* , int* , int* );

int main() {
    int array1[3], array2[3], somme[3];

    Entrer(array1, array2);
    Afficher(array1,array2);
    Addition(array1,array2,somme);

    printf("\n=== Somme des deux temps ===\n");
    printf("%02d:%02d:%02d\n", somme[0], somme[1], somme[2]);

    return 0;
}

void Entrer(int *x, int *y) {
    printf("=== Entrer le premier temps (HH MM SS) ===\n");
    for (int i = 0; i < 3; i++)
        scanf("%d", &x[i]);

    printf("=== Entrer le deuxieme temps (HH MM SS) ===\n");
    for (int i = 0; i < 3; i++)
        scanf("%d", &y[i]);
}

void Afficher(int *x, int *y) {
    printf("\nPremier  : %02d:%02d:%02d", x[0], x[1], x[2]);
    printf("\nDeuxieme : %02d:%02d:%02d\n", y[0], y[1], y[2]);
}

void Addition(int *x,int *y,int *S) {
    int carry = 0;

    // Ajouter les secondes
    S[2] = x[2] + y[2];
    if (S[2] >= 60) {
        S[2] -= 60;
        carry = 1;
    } else carry = 0;

    // Ajouter les minutes
    S[1] = x[1] + y[1] + carry;
    if (S[1] >= 60) {
        S[1] -= 60;
        carry = 1;
    } else carry = 0;

    // Ajouter les heures
    S[0] = x[0] + y[0] + carry;
    if (S[0] >= 24)
        S[0] -= 24; // pour éviter de dépasser 24h
}
