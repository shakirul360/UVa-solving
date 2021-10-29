#include <bits/stdc++.h>
using namespace std;

int main(){

    ios_base::sync_with_stdio(false); cin.tie(nullptr);

    vector<long long int>v;

    long long int n, k, i , j;

    scanf("%lld", &n);
    scanf("%lld",&k);
    //printf("%lld %lld\n", n, k);

    for (i = 1; i * i <= n; i++){
        if (n % i == 0){
            v.push_back(i);

            j = n / i;
            if (j != i){
                v.push_back(j);
            }
        }
    }

    sort(v.begin(),v.end());

//    for (i = 0; i < v.size(); i++) {
//        printf("%lld ", v[i]);
//    }

    ///printf("size = %d\nk = %d\n", v.size(), k);

    if (k <= v.size()){
        printf("%d\n", v[k - 1]);
    } else {
        printf("%d\n", -1);
    }
}
