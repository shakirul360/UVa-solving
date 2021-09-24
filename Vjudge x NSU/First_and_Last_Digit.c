#include<stdio.h>
#include <stdlib.h>

int main(){
    char string[10], a, b;
    int tcase, res = 0, x;

    scanf("%d", &tcase);

    for (int i= 0; i < tcase; i++){
        scanf("%s", string);
        b = (atoi(string) %10);

        a = string[0];
        x = a - '0';

        printf("%d\n", x + b);

    }

    return 0;
}
