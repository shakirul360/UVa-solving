#include <iostream>
#include <map>

using namespace std;

int main()
{
    std::map<char, char> my_map = {
    { '2', '1' },{ '3', '2' },{ '4', '3' },{ '5', '4' },{ '6', '5' },{ '7', '6' },{ '8', '7' },{ '9', '8' },{ '0', '9' }, { '-','0' },
    {'=','-'},{'W', 'Q'}, { 'E', 'W' }, { 'R', 'E'},{'T','R'}, {'Y','T'}, { 'U','Y'}, {'I','U'}, {'O','I'}, {'P','O'}, {'[','P'},
    {']','['}, {'\\',']'}, {'S','A'}, {'D','S'}, {'F','D'}, {'G', 'F'}, { 'H', 'G' }, {'J','H'}, {'K','J'}, {'L','K'},
    {';','L'}, {'\'',';'}, {'X','Z'}, {'C','X'}, {'V','C'}, {'B','V'}, {'N','B'}, {'M','N'}, {',','M'}, { '.',','}, {'/','.'}
};
    //std::cout << my_map['2'];
    
    char c;
	while (scanf("%c", &c) != EOF) {
	    if (my_map[c]){
		    printf("%c", my_map[c]);
	    } else if (c == ' ') {
	       printf(" "); 
	    } else {
	        printf("\n");
	    }
	}

    return 0;
}
