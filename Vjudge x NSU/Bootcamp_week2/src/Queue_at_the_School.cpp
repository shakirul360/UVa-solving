#include <bits/stdc++.h>
using namespace std;

int main(){

    ios_base::sync_with_stdio(false); cin.tie(nullptr);

    int length, iter;
    char temp;
    int flag;
    scanf("%d", &length);
    scanf("%d", &iter);

    char str[length];

    scanf("%s", str);

    //printf("%s", str);

    for (int i = 0; i < iter; i++){
        flag = 0;
        for (int j = 0; j < length - 1; j++){
            printf("flag = %d\n", flag);
            printf("%c %c\n", str[j], str[j+ 1]);
            if (str[j] == 'B' && str[j + 1] == 'G' && flag == 0){
                temp = str[j];
                str[j] = str[j + 1];
                str[j + 1] = temp;
                flag = 1;
            } else {
                flag = 1;
            }
        }
        printf("%s\n", str);
    }



}
