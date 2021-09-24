#include<stdio.h>


int main(){

    int n, k, t, count = 0;

    scanf("%d %d", &n, &k);

    for (int i = 0; i < n; i++){
        scanf("%d", &t);
        if (t % k == 0){
            count += 1;
        }
    }

    printf("%d\n", count);
    return 0;
}
