#include <stdlib.h>
#include <stdio.h>
#include <time.h>

int Factroial(int N) {
    if(N == 1||N==0){
        return 1;
    }
    else return N*Factroial(N-1) ;
}

int main() {
    printf("%d",Factroial(15));

}