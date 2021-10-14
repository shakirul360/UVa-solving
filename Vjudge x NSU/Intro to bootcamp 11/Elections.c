#include<stdio.h>


int main(){

    int tcase;
    long long a ,b ,c;

    scanf("%d", &tcase);

    for (int i = 0; i < tcase; i++){
        scanf("%lld %lld %lld", &a, &b, &c);

        if (a > b && a > c){
            printf("%d %lld %lld\n", 0, a + 1 - b, a + 1 - c);
        } else if (b > a && b > c){
            printf("%lld %d %lld\n", b + 1 - a, 0, b + 1 - c);
        } else if ( c > a && c > b){
            printf("%lld %lld %d\n", c + 1 - a, c + 1 - b, 0);
        } else{
            printf("%d %d %d\n", 1, 1, 1);
        }



    }

    return 0;
}
