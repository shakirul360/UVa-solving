#include<bits/stdc++.h>
#include<cstdio>
#include<algorithm>


using namespace std;

int main() 
{
    int i, tcase,a ,b ,c,j;
    cin >> tcase;
    int arr[3];
    
    for (i = 0; i < tcase; i++) {
        for(j=0; j<3; j++){
            cin>>arr[j];
        }
        sort(arr,arr+3);
        printf("Case %d: %d\n",i + 1,arr[1]);
    }   
    
}   