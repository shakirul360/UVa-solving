#include<stdio.h>

int main(){
    int lucky_count = 0, i, j;
    long long num;

    scanf("%lld", &num);

    while (num != 0){
        i = num % 10;
        if (i == 7 || i == 4){
            lucky_count += 1;
        }
        num = num / 10;
    }

    if (lucky_count == 4 || lucky_count == 7){
        printf("YES");
    } else{
        printf("NO");
    }

    return 0;
}
