#include <bits/stdc++.h>
using namespace std;

int main(){

    ios_base::sync_with_stdio(false); cin.tie(nullptr);

    vector<int>v;
    int n, i, temp;

    scanf("%d", &n);

    for (i = 0; i < n; i++){
        scanf("%d", &temp);
        v.push_back(temp);
    }
    sort(v.begin(),v.end());

    for (i = 0; i < n; i++) {
			if (i == n - 1)
				printf("%d", v[i]);
			else
				printf("%d ", v[i]);
		}


}
