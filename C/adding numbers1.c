#include<stdio.h>

int main(){

    long long int x;
    int res;
    while(scanf("%lld",&x)==1){
        if(x==0)
            break;
        res = 0;
        while (x > 9){
            while (x > 0){
                res += x % 10;
                x = x / 10;
            }
        x = res;
        res = 0;
        }

    printf("%d\n", x);
    }

    return 0;
}
