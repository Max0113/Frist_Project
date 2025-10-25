#include <stdio.h>
#include <stdlib.h>

int main() {

    int N;
    int S = 0;
    printf("Entrer un nombre N : ");
    if (scanf("%d", &N) != 1) {
        printf("Erreur de lecture de N.\n");
        return 1;
    }
    for (int i = 0; i < N; i++) {
        S = i + S + 1;
    }
    printf("La somme des nombres de 1 a %d est : %d\n", N, S);

    return 0;
}
