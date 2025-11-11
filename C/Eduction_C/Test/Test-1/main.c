#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define NB 5

int** mallocT(int** T) {
    int** Res;
    Res = (int**)malloc(NB*sizeof(int*));
    for (int i =0 ; i<NB ; i++)
        Res[i] = (int*)malloc(NB*sizeof(int));
    return Res ;
}

int** callocT(int** T) {
    int** Res;
    Res = (int**)calloc(NB,sizeof(int*));
    for (int i =0 ; i<NB ; i++)
        Res[i] = (int*)calloc(NB,sizeof(int));
    return Res ;
}

int randT(int **T){
    srand(time(NULL));
    for (int i = 0 ; i<NB ; i++){
      for (int j =0 ; j<NB ; j++)
         T[i][j] = rand()%(100);
    }
}

int affecher(int **T) {
    for (int i = 0 ; i<NB ; i++){
      printf("|");
      for (int j =0 ; j<NB ; j++)
         printf(" %3d ",T[i][j]);
      printf("| \n");
    }
    return 0;
}
int main() {
    int i , j, **T ,**C;
    int max = 0;
    T = mallocT(T);
    C = callocT(T);

    printf("\n");
    affecher(T);
    printf("\n");
    affecher(C);
    
    randT(T);
    randT(C);

    printf("\n");
    affecher(T);
    printf("\n");
    affecher(C);

    return 0 ;
}