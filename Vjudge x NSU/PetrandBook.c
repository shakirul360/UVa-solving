#include<stdio.h>


int main(){

    int pages, i, arr[7], read;
    scanf ("%d", &pages);

    for (i = 0; i < 7; i++){
        scanf("%d", &arr[i]);
    }

    read = arr[0];
    i = 0;

    while (read < pages){
        i++;
        //printf("arr[i + 1] = %d, i = %d\n", arr[i + 1], i);
        i = i % 7;
        read += arr[i];
    }

    printf("%d\n", i + 1);
    return 0;
}
