#include<stdio.h>
#include <string>
#include<iostream>

using namespace std;

int main(){

    int tcase;
    int length, idx;
    string str;

    cin >> tcase;

    for (int i = 0; i < tcase; i++){

        cin >> length;
        cin >> str;
        int bal = 0;

        char letters[26];
        int visits[26] = {0};

        idx = 0;

        for (int i = 65; i < 91; i++){
            letters[idx] = i;
            idx++;
        }

        for (int i = 0; i < length; i++){

            for (int j = 0; j < 26; j++){

                if (str[i] == letters[j]){
                    if (visits[j] == 0){
                        bal += 2;
                        visits[j] = 1;
                    } else {
                        bal++;
                    }
                }
            }
        }

        cout << bal << endl;

    }


    return 0;
}
