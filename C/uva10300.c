#include<stdio.h>

int main(){
    long int tcases, size, num, env, prem, farmers,i, j;
    while (scanf("%ld", & tcases) == 1) {
        for (i = 0; i < tcases; i++){
            scanf("%ld", &farmers);
            prem = 0;
            for (j = 0; j < farmers; j++){
                scanf("%ld %ld %ld", &size, &num, &env);
                prem += size * env;
            }
            printf("%ld\n", prem);
        }
    }
    return 0;
}
