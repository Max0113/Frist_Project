#include <stdio.h>
#include <stdlib.h>

int main() {
    for(int i = 0 ; i < 6 ; i++){
        for(int j = 6 ; j >= i-1 ; j--) printf(" + ");
        for(int j  = 0 ; j < i ; j++)
            printf(" * ");
        printf("\n");
    }

}