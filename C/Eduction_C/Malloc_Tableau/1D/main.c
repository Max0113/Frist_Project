#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define NB 6   // عدد عناصر الجدول

// دالة لتبديل قيمتين في الجدول

int* malloc_1d(int);
void affechr_1d(int* , int) ;
void saisir_1d(int* , int) ;\
void rendem(int* ,int ) ;



int main() {
    int* T ;
    T = malloc_1d(NB) ;
    saisir_1d(T, NB);
    affechr_1d(T, NB);
    printf("\n ---------------------- \n");
    rendem(T, NB);
    affechr_1d(T, NB);
    free(T);
    return 0;
}

int* malloc_1d(int nb){
    int *Res ;
    Res = (int*)malloc(NB*sizeof(int)) ;
    if (Res == NULL) { printf("Erreur realloc\n"); exit (33); }
    return Res ;
}

void affechr_1d(int* T, int nb) {
    printf("[");
    for (int i =0 ; i < nb ; i++) {
        printf(" %d " , *(T+i));
    } 
    printf("]");
}

void saisir_1d(int* T, int nb) {
    for (int i =0 ; i < nb ; i++) {
        printf("Donne valeur [%d] :" , i);
        scanf(" %d" , T+i);
    } 
}

void rendem(int* T ,int nb) {
    int Vmin = 1 , Vmax = 20 ;
    srand(time(NULL));
    for(int i = 0 ; i < nb ; i++) {
        T[i] = Vmin+rand()%(Vmax-Vmin+1);
    }
}

