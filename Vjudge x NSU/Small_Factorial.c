#include<stdio.h>

int factorial(n);

int main(){
    int tcase, n;

    scanf("%d", &tcase);

    for (int i = 0; i < tcase; i++){
        scanf("%d", &n);
        printf("%lld\n", factorial(n));
    }


    return 0;
}


int factorial(n){
    if (n == 1)
        return 1;
    else
        return n * factorial(n - 1);
}
