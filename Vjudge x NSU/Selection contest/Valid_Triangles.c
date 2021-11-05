#include<stdio.h>


int main(){
    int tcase, a, b, c;

    scanf("%d", &tcase);

    for (int i = 0; i < tcase; i++){
        scanf("%d %d %d", &a, &b, &c);

        if (a + b + c == 180)
            printf("YES\n");
        else
            printf("NO\n");

    }

    return 0;
}
