#include <stdio.h>
#include <stdlib.h>

int fibo(int N) {
    if (N<2) return N;
    else return fibo(N-2) + fibo(N-1) ;
}

int fiboplus(int N) {
    if (N<2) return N;
    else return fibo(N-2) + fibo(N-1) ;
}

int fibo_New(int N) {
    if (N<2) return N;
    else return fiboplus(N-2) + fiboplus(N-1) ;
}

int main() {
    for(int i = 0 ; i < 255 ; i++) {
        printf("%d : %d \n",i,fibo_New(i));
    }
}