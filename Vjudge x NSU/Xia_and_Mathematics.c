#include<stdio.h>


int main(){

    char num[15];

    int size;

    fflush(stdin);

    gets(num);
    printf("%s\n", num);

    size = sizeof(num) / sizeof(num[0]);
    printf("%d\n", size);

    for (int i = 15; i > 0; i--){
        printf("%c ", num[i]);
    }



    return 0;
}
