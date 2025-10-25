#include <stdlib.h>
#include <stdio.h>

int main() {
    int n , S , d;
    printf("Entrer un nombre");
    scanf("%d",&n);
    for (int i = 0 ; i <= 20 ; i++) {
        printf("Entrer la valeur de %d :",i);
        scanf("%d", &d);
        if (d == n) {
            S += 1 ;
        }
    }
    printf("%d",S);

}