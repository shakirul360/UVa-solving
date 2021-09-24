#include<stdio.h>

int main(){

    int tcase, quan, price, i;
    double total;
    scanf("%d", &tcase);

    for (i = 0; i < tcase; i++){
        scanf("%d %d", &quan, &price);
        total = quan * price;

        if (quan > 1000)
            total = total * 0.9;

        printf("%.6f\n", total);
    }

    return 0;
}
