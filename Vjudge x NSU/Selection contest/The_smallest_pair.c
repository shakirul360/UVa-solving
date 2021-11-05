#include<stdio.h>


int main(){
    int position, j, k;
    long tcase, n, temp;

    scanf("%ld", &tcase);

    for (int i = 0; i < tcase; i++){
        scanf("%d", &n);
        long arr[n];

        for (j = 0; j < n; j++){
            scanf("%ld", &arr[j]);
        }

        for (j = 0; j < n - 1; j++){
            position = j;

            for (k = j + 1; k < n; k++){
                if (arr[k] < arr[position]){
                    position = k;
                }
            }

            if (position != j){
                temp = arr[j];
                arr[j] = arr[position];
                arr[position] = temp;
            }
        }


        printf("%d", arr[0] + arr[1]);


    }

    return 0;
}
