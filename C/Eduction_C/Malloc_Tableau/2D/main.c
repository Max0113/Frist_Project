#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define NB 3   // عدد عناصر الجدول

// دالة لتبديل قيمتين في الجدول

int** malloc_1d(int);
void affechr_1d(int** , int) ;
void saisir_1d(int** , int) ;
void rendem(int** ,int ) ;
int symtrique_ant(int** T ,int nb);
int matrice(int** T ,int nb);
int free_net(int** T,int nb);


int main() {
    int **T1 , **T2;
    int x , CH;
    // creaty Tableau
    T1 = malloc_1d(NB) ;
    T2 = malloc_1d(NB) ;
    printf("Matrice N1 :  \n");
    saisir_1d(T1, NB);
    printf("Matrice N2 :  \n");
    saisir_1d(T2, NB);
    system("cls");

    // Menu loop
    while (1) {  // Infinite loop until break
        printf("--------- Menu ---------- \n");
        printf("1 - Type de Matrice \n");
        printf("2 - Oppartion de Matrice \n");
        printf("3 - Matrice Inverse \n");
        printf("4 - Exit \n");  // Added exit option
        printf("Choix un seul chose : ");
        scanf("%d", &CH);
        system("cls");

        // Methode
        if (CH == 1) {
            system("cls");

            printf("Tableau 1 :\n");
            x = symtrique_ant(T1, NB);
            switch (x) {
            case 1:
                printf("symtrique\n");
                break;
            case -1:
                printf("antsymtrique\n");
                break;
            case 0:
                printf("null\n");
                break;
            default:
                printf("Matrice Normal\n");
                break;
            }

            printf("Tableau 2 :\n");
            x = symtrique_ant(T2, NB);
            switch (x) {
            case 1:
                printf("symtrique\n");
                break;
            case -1:
                printf("antsymtrique\n");
                break;
            case 0:
                printf("null\n");
                break;
            default:
                printf("Matrice Normal\n");
                break;
            }
            printf("Press Enter to continue...\n");
            getchar();  // Wait for user to press enter
            getchar();
            system("cls");
        } else if (CH == 4) {
            break;  // Exit the loop
        } else {
            printf("Option not implemented yet or invalid choice.\n");
            printf("Press Enter to continue...\n");
            getchar();
            getchar();
            system("cls");
        }
    }

    free_net(T1, NB);
    free_net(T2, NB);
    return 0;
}

int** malloc_1d(int nb){
    int** Res ;
    Res = (int**)malloc(nb * sizeof(int*));  // Fixed to use nb instead of NB for generality
    for (int i = 0 ; i < nb ; i++) {
        Res[i] = (int*)malloc(nb * sizeof(int));  // Same here
        if (Res[i] == NULL) { printf("Erreur realloc\n"); exit (33); }
    }
    if (Res == NULL) { printf("Erreur realloc\n"); exit (33); }
    return Res ;
}

void affechr_1d(int** T, int nb) {
    for (int i =0 ; i < nb ; i++) {
        for (int j =0 ; j < nb ; j++) {
            printf(" %2d " , T[i][j]);
        } 
        printf("\n");
    } 
}

void saisir_1d(int** T, int nb) {
    printf("[00,01,02] \n");
    printf("[10,11,12] \n");
    printf("[20,21,22] \n");
    for (int i =0 ; i < nb ; i++) {
        for (int j =0 ; j < nb ; j++) {
            printf("Donne valeur [%d] [%d]:" , i , j);
            scanf(" %d" , &T[i][j]);
        } 
    } 
}

void rendem(int** T ,int nb) {
    int Vmin = 1 , Vmax = 20 ;
    srand(time(NULL));
    for(int i = 0 ; i < nb ; i++) {
        for(int j = 0 ; j < nb ; j++) 
           T[i][j] = Vmin+rand()%(Vmax-Vmin+1);
    }
}

int symtrique_ant(int** T ,int nb) {
    int symtrique = 1;
    int antsymtrique = 1;
    int null = 1;
    int i , j;
    for (i = 0 ; i < nb ; i++){
       for (j = 0 ; j < nb ; j++) {
          if(T[i][j] != 0) {
            null = 0;
          }
          if (T[i][j] != T[j][i]) symtrique = 0 ;

          // Fixed antisymmetric check: must have T[i][j] == -T[j][i] for all i,j, and T[i][i] == 0
          if (T[i][j] != -T[j][i]) antsymtrique = 0;
          if (i == j && T[i][i] != 0) antsymtrique = 0;
       }
    }
    if(null == 1) return 0;
    if(symtrique == 1) return 1;
    if(antsymtrique == 1) return -1;
    return 2;  // Added return for normal matrix
}

int free_net(int** T,int nb) {
    int i ;
    for (i = 0 ; i < nb ; i++) {
        free(T[i]);
    }
    free(T);
    return 0;  // Added return, though not used
}
