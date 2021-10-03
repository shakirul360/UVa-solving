#include <stdio.h>
#include <math.h>

int main(){

    int tcase;
    double r, sq, circ, res;

    scanf("%d", &tcase);

    for (int i = 0; i < tcase; i++){
        scanf("%lf", &r);

        sq = pow(2 * r, 2);
        circ = acos(0.0) * 2 * r * r;

        res = sq - circ;

        printf("Case %d: %.2lf\n", i + 1, res);


    }

    return 0;
}
