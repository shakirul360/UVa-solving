#include<stdio.h>
long long highest(long long acount,long long bcount);

int main(){
    int tcase;
    long long n, i, j;
    char rooms[100002];

    scanf("%d", &tcase);
    for (i = 0; i < tcase; i++){
        scanf("%lld", &n);
        fflush(stdin);

        gets(rooms);

        long long rcount = 0, bcount = 0, gcount = 0, fcount = 0;

        for(j = 0; j < n; j++){

            if (rooms[j] == 'R')
                rcount += 1;
            else if (rooms[j] == 'B')
                bcount += 1;
            else
                gcount += 1;

        }


        fcount = highest(rcount, bcount);
        fcount = n - highest(fcount, gcount);


        printf("%lld\n", fcount);
    }


    return 0;
}

long long highest(long long acount,long long bcount){
    if (acount > bcount)
        return acount;
    else
        return bcount;
}
