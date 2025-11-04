// #include <stdio.h>
// #include <stdlib.h>
// #define NB 3

// int** malloc_3d(int);
// int saisir(int** , int);
// int symtrique_not(int** , int);

// int main() {
//     int** Matrce ;
//     Matrce = malloc_3d(NB);
//     printf("[00,01,02]\n");
//     printf("[10,11,12]\n");
//     printf("[20,21,22]\n");
//     saisir(Matrce,NB);
//     system("cls");

//     int ch = symtrique_not(Matrce , NB) ;
//     switch (ch)
//     {
//     case 1 :
//         printf("la matrice est symtrique");
//         break;

//     case -1 :
//         printf("la matrice est not symtrique");
//         break;
    
//     default:
//         break;
//     }




// }

// int** malloc_3d(int nt) {
//     int** Res ;
//     Res = (int**)malloc(nt*sizeof(int*));
//     if (Res == NULL) {
//             printf("Erreur d'allocation ligne %d\n");
//             exit (33);
//     }
//     for (int i = 0 ; i < nt ; i++) {
//         Res[i] = (int*)malloc(nt*sizeof(int));
//         if (Res[i] == NULL) {
//             printf("Erreur d'allocation ligne %d\n", i);
//             exit (33);
//         }
//     }
//     return Res ;
// }

// int saisir (int** T , int nt) {
//     for (int i = 0; i < nt; i++) {
//         for (int j = 0; j < nt; j++) {
//            printf("Entrer la valeur[%d][%d] : ", i, j);
//            scanf("%d", &T[i][j]);
//         }
//     }
// }

// int symtrique_not(int** T , int nt){
//      for (int i = 0; i < nt; i++) {
//         for (int j = 0; j < nt; j++) {
//             // if (i == j) continue;
//             if (T[i][j] != T[j][i]) {
//                 return 1;
//             }
//             if (T[i][j] != -T[j][i]) {
//                 return -1;
//             }
//         }
//      }
// }

#include <stdio.h>
#include <stdlib.h>
#define NB 3

int** malloc_3d(int);
void saisir(int**, int);
int symtrique_not(int**, int);
void liberer_memoire(int**, int);
void afficher_matrice(int**, int);

int main() {
    int** Matrice;
    Matrice = malloc_3d(NB);
    
    printf("Structure de la matrice :\n");
    printf("[00,01,02]\n");
    printf("[10,11,12]\n");
    printf("[20,21,22]\n\n");
    
    saisir(Matrice, NB);
    system("cls");  // Note: system("cls") ne fonctionne que sur Windows

    int ch = symtrique_not(Matrice, NB);
    
    printf("Matrice saisie :\n");
    afficher_matrice(Matrice, NB);
    printf("\n");
    
    switch (ch) {
    case 1:
        printf("La matrice est symetrique\n");
        break;
    case -1:
        printf("La matrice est antisymetrique\n");
        break;
    case 2:
        printf("La matrice diagonale \n");
        break;
    case 0:
        printf("La matrice n'est ni symetrique ni antisymetrique\n");
        break;
    default:
        printf("Erreur inattendue\n");
        break;
    }

    liberer_memoire(Matrice, NB);
    return 0;
}

int** malloc_3d(int nt) {
    int** Res;
    Res = (int**)malloc(nt * sizeof(int*));
    if (Res == NULL) {
        printf("Erreur d'allocation memoire\n");
        exit(33);
    }
    for (int i = 0; i < nt; i++) {
        Res[i] = (int*)malloc(nt * sizeof(int));
        if (Res[i] == NULL) {
            printf("Erreur d'allocation ligne %d\n", i);
            exit(33);
        }
    }
    return Res;
}

void saisir(int** T, int nt) {
    for (int i = 0; i < nt; i++) {
        for (int j = 0; j < nt; j++) {
            printf("Entrer la valeur[%d][%d] : ", i, j);
            scanf("%d", &T[i][j]);
        }
    }
}

int symtrique_not(int** T, int nt) {
    int symetrique = 1;      // 1 pour symétrique
    int antisymetrique = 1; // 1 pour antisymétrique   
    int diagonale = 1 ;
    int null = -2 ;  
    for (int i = 0; i < nt; i++) {
        for (int j = 0; j < nt; j++) {
            // Vérifier la symétrie
            if (T[i][j] != T[j][i]) {
                symetrique = 0;
            }
            
            // Vérifier l'antisymétrie
            if (i == j) {
                // Pour l'antisymétrie, les éléments diagonaux doivent être 0
                if (T[i][i] != 0) {
                    antisymetrique = 0;
                }
            } else {
                if (T[i][j] != -T[j][i]) {
                    antisymetrique = 0;
                }
            }

            // Vérifier l'diagonale
            if ( i != j && T[i][j] != 0)
                diagonale = 0 ;

            if (T[i][j] != 0)
                null = 0;

        }
    }
    
    if (null)
    if (diagonale == 1)return 2 ;
    if (symetrique == 1) return 1;
    if (antisymetrique == 1) return -1;
    return 0;
}

void liberer_memoire(int** T, int nt) {
    for (int i = 0; i < nt; i++) {
        free(T[i]);
    }
    free(T);
}

void afficher_matrice(int** T, int nt) {
    for (int i = 0; i < nt; i++) {
        for (int j = 0; j < nt; j++) {
            printf("%d\t", T[i][j]);
        }
        printf("\n");
    }
}