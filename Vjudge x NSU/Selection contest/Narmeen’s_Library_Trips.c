#include<stdio.h>


int main(){

    int a, b, i, trips;

    scanf("%d %d", &a, &b);

    i = 0;
    trips = 0;

    while (i < a){
        i += b;
        trips += 1;
    }

    printf("%d\n", trips);
    return 0;
}
