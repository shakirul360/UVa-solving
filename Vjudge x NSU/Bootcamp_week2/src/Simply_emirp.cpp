#include <bits/stdc++.h>
using namespace std;

bool isPrime(long long int n);
long long int reverse_a_num(long long int n);

int main(){
    long long int n, rev;
    int rev_bool, n_bool;

    while (scanf("%lld", &n) == 1){
        rev = reverse_a_num(n);
        n_bool = isPrime(n);
        rev_bool = isPrime(rev);

        if (n_bool == true){
            if (rev_bool == false || n == rev)
                printf("%lld is prime.\n", n);
            if (rev_bool == true && n != rev)
                printf("%lld is emirp.\n", n);
        } else{
            printf("%lld is not prime.\n", n);
        }

    }
    return 0;
}

bool isPrime(long long int n){
    if (n <= 1){
        return 0;
    }
    for (int i = 2; i * i <= n; i++){
        if (n % i == 0){
            return 0;
        }
    }
    return 1;
}

long long int reverse_a_num(long long int n){
    int num = 0;
    while (n > 0){
        num = num * 10 + n % 10;
        n = n / 10;
    }
    return num;
}
