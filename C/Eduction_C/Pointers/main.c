#include <stdio.h>

int main() {
    int arr[3] = {10, 20, 30};
    int *p = arr; // p يشير لأول عنصر

    for(int i=0; i<3; i++) {
        printf("arr[%d] = %d\n", i, *(p+i)); // استخدام المؤشر للوصول للعناصر
    }

    return 0;
}