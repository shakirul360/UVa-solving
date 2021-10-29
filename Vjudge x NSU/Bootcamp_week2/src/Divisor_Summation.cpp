#include <bits/stdc++.h>
using namespace std;

int main(){

    ios_base::sync_with_stdio(false); cin.tie(nullptr);

    int tcase, t, n, i;
    long long total;

    scanf("%d", &tcase);

    for(t = 0; t < tcase; t++){
        scanf("%d", &n);
        total = 0;

        for (i = 1; i < n; i++){
            if (n % i == 0)
                total += i;
        }
        printf("%d\n", total);
    }


}
