#include<stdio.h>
#include <stdlib.h>

int main(){

    int length, lucky = 1, fcount = 0, scount = 0, digit;
    char number[52];

    scanf("%d", &length);
    scanf("%s", number);

    for (int i = 0; i < length / 2; i++){
        digit = number[i] - '0';

        if (digit != 4 && digit != 7){
            lucky = 0;
            break;
        } else{
            fcount += digit;
        }

    }

    for (int i =  length / 2; i < length; i++){
        digit = number[i] - '0';

        if (digit != 4 && digit != 7){
            lucky = 0;
            break;
        } else{

            scount += digit;
        }
    }

    if (lucky == 1 && fcount == scount){
        printf("YES\n");
    } else{
        printf("NO\n");
    }



    return 0;
}
