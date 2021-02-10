
#include <iostream>

using namespace std;

int main()
{   
    int i,j, total,tcase,a,b;
    
    cin >> tcase;
    
    for (int i = 0; i < tcase; i++) {
        cin >> a >> b;
        total = 0;
        for (a; a <= b; a++) {
            if (a % 2  != 0) {
                total += a;
            }
        }
        //std::cout << Case 1:  << total << "\n";
        printf("Case %d: %d\n", i + 1, total);
    }
    
    
    

    return 0;
}
