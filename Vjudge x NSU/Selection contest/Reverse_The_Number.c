#include<stdio.h>
#include <string.h>
#include <stdlib.h>

int main(){
    int tcases, i, position;
    char string[1000001];

    scanf("%d", &tcases);
    fflush(stdin);
    for (i = 0; i < tcases; i++){
        gets(string);

        printf("%d\n", atoi(strrev(string)));

    }



    return 0;
}


