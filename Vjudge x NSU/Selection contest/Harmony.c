#include<stdio.h>
#include <math.h>

int main(){
    int a, b, temp, k = -3;

    scanf("%d %d", &a, &b);

    if (b < a){
        temp = a;
        a = b;
        b = temp;
    }

    for (int i = a; i <= b; i++){
        if (abs(a - i) == abs(b - i)){
            k = i;
            break;
        }
    }

    if (k > 0){
        printf("%d", k);
    } else{
        printf("IMPOSSIBLE");
    }
    return 0;
}
