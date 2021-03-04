#include<stdio.h>

int main(){
    long long n, result, i, x;

    scanf("%lld", &n);

    for (i = 0; i < n; i++){
        scanf("%lld", &x);
        result = (x*63+7492)*5-498;
        if (result < 0){
            result = result * -1;
        }
        result = result / 10;
        printf("%d\n", result % 10);
    }
    return 0;
}
