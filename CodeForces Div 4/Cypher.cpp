
#include<stdio.h>
#include <string>
#include<iostream>

using namespace std;

int main(){

    int tcase;
    int w;
    int moves;
    string str;

    cin >> tcase;

    for (int i = 0; i < tcase; i++){

        cin >> w;
        int wheels[w];
        int init[w];

        for (int i = 0; i < w; i++){
            cin >> wheels[i];
        }

        for (int i = 0; i < w; i++){

            cin >> moves;
            cin >> str;

            for (int j = 0; j < moves; j++){
                if (str[j] == 'U'){

                    if (wheels[i] == 0){
                        wheels[i] = 9;

                    } else {
                        wheels[i]--;
                    }
                } else {

                    if (wheels[i] == 9){
                        wheels[i] = 0;
                    } else {
                        wheels[i]++;
                    }
                }

            }
        }

        for (int i = 0; i < w; i++){
            cout << wheels[i] << " ";
        }
        cout << endl;

    }




    return 0;
}
