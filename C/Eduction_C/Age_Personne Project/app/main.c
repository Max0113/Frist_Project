#include <stdio.h>
#include <stdlib.h>

int main() {
    char name[50];
    int annee_naissance, age;

    printf("Entrez votre nom : ");
    scanf("%s", name);

    printf("Entrez votre ann�e de naissance : ");
    scanf("%d", &annee_naissance);

    age = 2025 - annee_naissance;

    printf("Bonjour %s ! Votre �ge en 2025 est : %d ans.\n", name, age);

    return 0;
}
