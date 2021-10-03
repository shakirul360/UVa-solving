#include<stdio.h>

int main(){

    int tcase;
    long long a, b, c, i;

    scanf("%d", &tcase);

    for (i = 0; i < tcase; i++){
        scanf("%lld %lld %lld", &a, &b, &c);

        if (a + b <= c || b + c <= a || c + a <= b){
            printf("Case %d: Invalid\n", i + 1);
        } else if (a == b && b == c){
            printf("Case %d: Equilateral\n", i + 1);
        } else if (a == b || b == c || a == c){
            printf("Case %d: Isosceles\n", i + 1);
        } else {
            printf("Case %d: Scalene\n", i + 1);
        }
    }

    return 0;
}
