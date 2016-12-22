#include <iostream>
#include <string>
#include <vector>
 
std::vector <char> list;
const char AlphabetLower[26] =
{
	'a', 'b', 'c', 'd', 'e', 'f', 'g',
	'h', 'i', 'j', 'k', 'l', 'm', 'n',
	'o', 'p', 'q', 'r', 's', 't', 'u',
	'v', 'w', 'x', 'y', 'z'
};
 
std::string input = "abbbxcxabcx";
// ABBBXCXABCX
 
int counter = 0;
 
int main()
{
 
	for(int x = 0; x < input.length(); x++)
	{
		for(int v = 0; v < input.length(); v++)
		{
			if(input[x] == input[x + v])
    		{
				counter++;
				if (counter > 1)
				{
					list.push_back('.');
					int counter = 0;
				}
 
        	}
        	else if (input[x] != input[x + v])
    		{
    			list.push_back(input[x]);		
    		}
		}
 	}
for (std::vector<char>::const_iterator i = list.begin(); i != list.end(); ++i)
    std::cout << *i << ' ';
}

// this needs to be fixed.
