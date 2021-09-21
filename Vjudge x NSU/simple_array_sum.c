#include<stdio.h>

int simpleArraySum(int ar[]);
int s;

int main(){

    int num, sum = 0, i, res;

    scanf("%d", &num);
    int arr[num];
    s = sizeof(arr)/sizeof(int);

    for (i = 0; i < num; i++){
        scanf("%d", &arr[i]);
    }

    res = simpleArraySum(arr);
    printf("%d\n", res);



    return 0;
}
int simpleArraySum(int ar[]){
    int sum = 0,
        size = s;

    for (int i = 0; i < size; i++){
        sum += ar[i];
    }
    return sum;
}
