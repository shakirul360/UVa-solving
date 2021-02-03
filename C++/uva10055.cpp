#include <iostream>


using namespace std;



int main()
{ 
   long long unsigned i,j;
 
   while (cin >> i >> j) {
 
       if (i > j) {
 
           std::cout << i - j << "\n";
 
       } else {

            std::cout << j - i << "\n";
        }


    }
    return 0;

}