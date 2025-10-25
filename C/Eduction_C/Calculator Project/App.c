#include <stdio.h>

int main() {
    int N1,N2;
    char op;

    printf("Entrez  nombres 1 : ");
    scanf("%d", &N1);   // إدخال رقمين
    
    printf("Entrer le type de operation (+,-,/,*) :");
    scanf(" %c", &op);

    printf("Entrez  nombres 2 : ");
    scanf("%d", &N2);   // إدخال رقمين

    if (op == '+') {
      printf("c'est ca : %d \n", N1 + N2 );
    }
    else if (op == '-') {
      printf("c'est ca : %d \n", N1 - N2 );
    }
    else if (op == '/') {
      if (N2 != 0) {
        printf("c'est ca : %d \n", N1 / N2 );
      } else {
        printf(" 0 next pas dans cet operation ");
      }
    }
    else if (op == '*')  {
      printf("c'est ca : %d \n", N1 * N2 );
    } 
    else {
      printf("la opreation next pas");
    }
    
    return 0;
}