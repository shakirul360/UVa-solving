#include <iostream>

using namespace std;

int main()
{
    int a,b;
    
     while (cin >> a >> b) {
         int result = 2 * a * b;
         std::cout << result << "\n";
     }

    return 0;
}
