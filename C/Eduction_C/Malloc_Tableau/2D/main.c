#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define NB 2   // عدد عناصر الجدول

// دالة لتبديل قيمتين في الجدول

int** malloc_1d(int);
void affechr_1d(int** , int) ;
void saisir_1d(int** , int) ;\
void rendem(int** ,int ) ;



int main() {
    int** T ;
    T = malloc_1d(NB) ;
    saisir_1d(T, NB);
    system("cls");
    affechr_1d(T, NB);
    printf("\n ---------------------- \n");
    rendem(T, NB);
    affechr_1d(T, NB);
    return 0;
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
    printf("[");
    for (int i =0 ; i < nb ; i++) {
        for (int j =0 ; j < nb ; j++) {
            printf(" %d " , T[i][j]);
        } 
    } 
    printf("]");
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

