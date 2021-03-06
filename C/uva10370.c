#include<stdio.h>

int main(){
    int i, j, tcases, n;
    double total, avg, count, result, arr[1001];

    while (scanf("%d", &tcases) == 1){

        for (i = 0; i < tcases; i++){
            total = 0;
            count = 0;
            scanf("%d", &n);
            for (j = 0; j < n; j++){
                scanf("%lf", &arr[j]);
                total += arr[j];
            }
            avg = total / n;

            for (j = 0; j < n; j++){
                if (arr[j] > avg){
                    count++;
                }
            }
            result=(double)(100*count/n);
            printf("%.3lf%\n", result);
        }
    }

    return 0;

}
