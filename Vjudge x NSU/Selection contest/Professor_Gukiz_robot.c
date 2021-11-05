#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int x1, y1, x2, y2, res;
    scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
    if (abs(x2 - x1) > abs(y2 - y1)){
        res = abs(x2 - x1);
    } else {
        res = abs(y2 - y1);
    }
    printf("%d\n", res);

    return 0;
}
