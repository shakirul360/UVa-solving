#include<stdio.h>

int main(){

    int tcases, n, result, x, i, j;

    scanf("%d", &tcases);

    for (x = 0; x < tcases; x++){
        scanf("%d", &n);
        int students[n];
        for (i = 0; i < n; i++){
            scanf("%d", &students[i]);
        }


        int max = students[0];
        for (j = 0; j < n; j++){
            if (students[j] > max){
                max = students[j];
            }
        }
        printf("Case %d: %d\n", x+1, max);
    }


    return 0;
}
