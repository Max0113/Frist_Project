#include <stdio.h>
int Inverse(int T[100], int N)
{
    int temp ;
    for (int i = 0; i < N / 2; i++) {
        temp = T[i];
        T[i] = T[N - 1 - i];
        T[N - 1 - i] = temp;
    }
}

int main() {
    int T[100], N, i;

    printf("Entrer la taille du tableau : ");
    scanf("%d", &N);

    // Lecture du tableau
    for (i = 0; i < N; i++) {
        printf("T[%d] = ", i);
        scanf("%d", &T[i]);
    }

    Inverse(T,N);

    // Affichage du tableau inversé
    printf("Tableau inversé : ");
    for (i = 0; i < N; i++) {
        printf("%d ", T[i]);
    }

    return 0;
}

