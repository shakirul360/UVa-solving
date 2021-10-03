#include<stdio.h>

int main(){

    int n, half, a, b, i, j, k, flag1, flag2;

    scanf("%d", &n);
    half = n / 2;

    for (i = half; i < n; i++){
        flag1 = 0;
        for (j = 2; j < i; j++){
            if (i % j != 0){
                flag1 = 1;
            } else{
                flag1 = 0;
                break;
            }
        }

        if (flag1 == 1){
            b = n - i;
            flag2 = 0;
            for (k = 2; k < b; k++){
                if (b % k != 0){
                    flag2 = 1;
                } else{
                    flag2 = 0;
                    break;
                }
            }
        }
        if (flag1 == 1 && flag2 == 1)
            break;
    }
    printf("%d %d\n", i, b);


    return 0;
}
