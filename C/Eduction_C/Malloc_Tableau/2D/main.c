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
int free(int** T,int nb);


int main() {
    int** T ;
    int x ;
    T = malloc_1d(NB) ;
    // saisir_1d(T, NB);
    // system("cls");
    // affechr_1d(T, NB);
    rendem(T, NB);
    affechr_1d(T, NB);
    printf("\n ---------------------- \n");
    x = matrice(T,NB);
    switch (x)
    {
    case 1:
        printf("symtrique");
        break;
    case -1:
        printf("antsymtrique");
        break;
    case -2:
        printf("null");
        break;
    default:
        printf("Matrice Normal");
        break;
    }
    return 0;

    free_net(T,NB);
}

int** malloc_1d(int nb){
    int** Res ;
    Res = (int**)malloc(NB*sizeof(int*)) ;
    for (int i = 0 ; i < nb ; i++) {
        Res[i] = (int*)malloc(NB*sizeof(int)) ;
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
    int i , j;
    for (i = 0 ; i < nb ; i++){
       for (j = 0 ; j< nb ; j++) {
          if (T[i][j] != T[j][i]) symtrique = 0 ;

          if(T[i][i] != 0)
            if (T[i][j] != -T[j][i]) antsymtrique = 0 ;
       }
    }
    if(symtrique == 1) return 1;
    if(antsymtrique == 1) return -1;
}

int matrice(int** T ,int nb) {
    int null = 1;
    for (int i = 0 ; i < nb ; i++){
       for (int j = 0 ; j< nb ; j++) {
          if(T[i][j] != 0) {
            null = 0;
          }
       }
    }
    if(null == 1) return -2;
    return symtrique_ant(T,nb); 
}

// int free_net(int** T,int nb) {
//     int i ;
//     for (i = 0 ; i < nb ; i++) {
//         free(T[i][i]);
//     }
//     free(T);
// }