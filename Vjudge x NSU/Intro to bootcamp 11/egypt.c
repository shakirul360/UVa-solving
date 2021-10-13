#include<stdio.h>

int main(){
    int a, b, c, temp, x = 1;

    while (x == 1){
        scanf("%d %d %d", &a, &b, &c);

        if (a == 0 && b == 0 && c == 0)
            break;

        if (b > c && b > a){
            temp = a;
            a = b;
            b = temp;
        }

        if (c > b && c > a){
            temp = a;
            a = c;
            c = temp;
        }

        if (pow(a, 2) == pow(b, 2) + pow(c, 2)){
            printf("right\n");
        } else{
            printf("wrong\n");
        }
    }




    return 0;
}
