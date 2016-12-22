#include <iostream>
#include <string>
#include <array>
#include <algorithm>
#include <sstream>

int main()
{
    char input;
    std::string xtr;
    int counter;
    std::string words[] = {"CAT", "DOG", "ANT"};
    std::cin >> input;
    std::stringstream ss;
    ss << input;
    ss >> xtr;
    for(int z = 0; z < sizeof(words); z++)
    {
        for(int x = 0; x <sizeof( words[z] ); x++)
        {
            if (words[x].find(xtr) != std::string::npos)
            {
                std::cout << "_" << std::endl;    
            }
            else
            {
                std::cout << xtr << std::endl;    
            }
        }
    }

    
}
