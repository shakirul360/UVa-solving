#include<stdio.h>

int main(){

    char string[102];

    int n1 = 0, n2 = 0, n3 = 0, i, j;

    scanf("%s", string);

    for (i = 0; i < 102; i++){
        if (string[i] == '1')
            n1 += 1;
        else if (string[i] == '2')
            n2 += 1;
        else if (string[i] == '3')
            n3 += 1;
    }

    for (j = 0; j < n1; j++){
        printf("%d+", 1);
    }
    for (j = 0; j < n2; j++){
        printf("%d+", 2);
    }
    for (j = 0; j < n3; j++){
        printf("%d+", 3);
    }

    return 0;
}
