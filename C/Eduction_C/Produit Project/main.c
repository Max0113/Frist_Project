#include <stdio.h>

int main() {
    int N;
    int S = 1; // نبدأ بـ 1 بدل 0
    int i;

    printf("Entrer un nombre N : ");
    scanf("%d", &N);

    for (i = 1; i <= N; i++) {
        S = S * i;
    }

    printf("Le produit des nombres pairs de 1 à %d est : %d\n", N, S);
    return 0;
}

