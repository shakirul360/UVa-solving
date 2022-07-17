#include<stdio.h>
#include <string>
#include<iostream>

using namespace std;

int main(){

    int n;
    string str;
    bool flag;

    cin >> n;

    for (int i = 0; i < n; i++){
        cin >> str;
         flag = 0;

        if (str[0] == 'Y' || str[0] == 'y'){
            if (str[1] == 'E' || str[1] == 'e'){
                if (str[2] == 'S' || str[2] == 's'){
                    flag = 1;
                }
            }
        }
        if (flag == 1){
            cout << "YES" << endl;
        }else {
            cout << "NO" << endl;
        }
    }


    return 0;
}
