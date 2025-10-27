#include <stdio.h>
#include <stdlib.h>
#define NB 3

int Input(int* ,int);
int Afficher(int* , int) ;

int Somme (int* , int* , int* , int) ;
int Soustraction (int* , int* , int* , int) ;
int Multiplication (int* , int* , int* , int) ;
int Division (int* , int* , int* , int) ;

int Max(int* ,int);
int Min(int* ,int);

int monotone(int* , int) ;

int main () {
    int arrayA[NB];
    int arrayB[NB];
    int O_Tab[NB];

    int CH ;
    char AB ;

    // ETAP1

    printf("Entrer les valeur de TABLAUE A : \n");  
    Input(arrayA , NB);
    system("cls");

    printf("Entrer les valeur de TABLAUE B : \n");  
    Input(arrayB , NB);
    system("cls");

    // ETAP2

    printf("LES VALEUR DE TABLAUE A et B : \n");
    Afficher(arrayA , NB) ;
    Afficher(arrayB , NB);

    printf("MENU : \n"
           "1 - Operation de deux tableux \n"
           "2 - la montone de Tableau \n"
           "3 - Max et Min de Tableau \n"
           "CHoise 1-3 : ");
    scanf("%d",&CH);
    
    // Operation de deux tableaux

    if (CH == 1) {
        system("cls");
        Afficher(arrayA , NB) ;
        Afficher(arrayB , NB);
        printf("----------------------------------------------------- \n");
        printf("Choise le Type de Operations (-|+|*|/) : ");
        scanf(" %c", &AB);
        if (AB == '+') {
            Somme(arrayA,arrayB,O_Tab,NB);
            Afficher(O_Tab , NB) ;
        }else if (AB == '-') {
            Soustraction(arrayA,arrayB,O_Tab,NB);
            Afficher(O_Tab , NB) ;
        }else if (AB == '*'){
            Multiplication(arrayA,arrayB,O_Tab,NB);
            Afficher(O_Tab , NB) ;
        }
        else {
            Division(arrayA,arrayB,O_Tab,NB);
            Afficher(O_Tab , NB) ;
        }
    }
    
    // La montone de tableaux

    else if (CH == 2) {  
        system("cls");   
        for (int i = 0 ; i <2 ; i++) {
            printf("Choise Entrer Tableau A et B : \n");
            scanf(" %c", &AB);
            if (AB == 'A' || AB == 'a') {
               monotone(arrayA , NB);
            }else if (AB == 'b' || AB == 'B') {
               monotone(arrayB , NB);
            }else {
                printf("chaqui que la valeur est A ou B");
            }
        } 
    }

    // Max & Min de tableaux
    
    else {
        system("cls");
        printf("Choise Entrer Tableau A et B : \n");
        scanf(" %c", &AB);
        if (AB == 'A' || AB == 'a') {
            printf("Le Max done Tableau A : %d \n", Max(arrayA,NB));
            printf("Le Min done Tableau A : %d \n", Min(arrayA,NB));
        }else if (AB == 'b' || AB == 'B') {
            printf("Le Max done Tableau B : %d \n", Max(arrayB,NB));
            printf("Le Min done Tableau B : %d \n", Min(arrayA,NB));
        }else {
            printf("chaqui que la valeur est A ou B");
        }
    }
    printf("\n Merce ???????? \n");
}

//  ========= LES METHODS =============

// Max & Min

int Max(int* array_ , int nb) {
    int M = 0 ; 
    for (int i = 0 ; i < nb ; i++) {
        if (M <= array_[i] ){
            M = array_[i] ;
        }
    }
    return M ;
}

int Min(int* array_ , int nb) {
    int Mi = 0 ; 
    for (int i = 0 ; i < nb ; i++) {
        if (Mi >= array_[i] ){
            Mi = array_[i] ;
        }
    }
    return Mi ;
}

// Operations

int Somme (int* arrayA_ , int* arrayB_ , int* Somme_ , int nb) {
    for (int i = 0 ; i < nb ; i++) {
        Somme_[i] = arrayA_[i] + arrayB_[i] ;
    }
}

int Soustraction (int* arrayA_ , int* arrayB_ , int* Somme_ , int nb) {
    for (int i = 0 ; i < nb ; i++) {
        Somme_[i] = arrayA_[i] - arrayB_[i] ;
    }
}

int Multiplication (int* arrayA_ , int* arrayB_ , int* Somme_ , int nb) {
    for (int i = 0 ; i < nb ; i++) {
        Somme_[i] = arrayA_[i] * arrayB_[i] ;
    }
}

int Division (int* arrayA_ , int* arrayB_ , int* Somme_ , int nb) {
    for (int i = 0 ; i < nb ; i++) {
        Somme_[i] = arrayA_[i] / arrayB_[i] ;
    }
}

// La montone

int monotone(int* array_ , int nb) {
    int i = 0 ;
    while (i < nb - 1  && array_[i] == array_[i+1]){i++ ;}
    if ( i == nb - 1 ) {
        printf("Le tableau est constant\n");
        return 0 ;
    }

    i = 0 ;
    while (i < nb - 1 && array_[i] <= array_[i+1]){i++ ;}
    if ( i == nb - 1) {
        printf("Le tableau est croissant\n");
        return 0 ;
    }

    i = 0 ;
    while (i < nb - 1 && array_[i] >= array_[i+1]){i++ ;}
    if ( i == nb - 1) {
        printf("Le tableau est decroissant\n");
        return 0 ;
    }
    printf("\n");

}

// Afficher & Saiser 

int Afficher(int* array_ , int nb) {
    printf("=> [");
    for (int i = 0 ; i < nb ; i++) {
        printf(" %d ", array_[i]);
    }
    printf("] \n");
}

int Input (int* array_ , int nb){
    for (int i = 0; i < nb ; i++) {
        printf("Array[%d] = ",i+1);
        scanf("%d", &array_[i]);
    }
}
