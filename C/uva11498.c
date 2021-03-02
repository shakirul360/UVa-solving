#include<stdio.h>

int main(){

    int tcase, x, y, div_x, div_y;

    while (scanf("%d", &tcase) == 1 && tcase){


        scanf("%d %d", &div_x, &div_y);
        while(tcase--){
            scanf("%d %d", &x, &y);

            if (x == div_x || y == div_y) {
                printf("divisa\n");

            } else if (x > div_x) {
                if ( y > div_y) {
                    printf("NE\n");
                } else {
                    printf("SE\n");
                }
            } else {
                if (y > div_y){
                    printf("NO\n");
                } else {
                    printf("SO\n");
                }

            }
        }
    }
    return 0;
}

