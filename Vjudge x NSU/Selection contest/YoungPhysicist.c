#include<stdio.h>


int main(){

    int planes, i, x1, y1, z1, tx = 0, ty = 0, tz = 0;

    scanf("%d", &planes);

    for (i = 0; i < planes; i++){
        scanf ("%d %d %d", &x1, &y1, &z1);
        tx += x1;
        ty += y1;
        tz += z1;
    }

    if (tx == 0 && ty == 0 && tz == 0)
        printf("YES\n");
    else
        printf("NO\n");
    return 0;
}
