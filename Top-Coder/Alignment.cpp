#include <iostream>
#include <string>
int main()
{
    std::string str1 = "AAABA";
    std::string str2 = "ABA";
    for(int x = 0; x < str1.length(); x++)
    {
        if(str1[x] != str2[x])
        {
            str2.insert(x,"-");      
        }
        
    }
    std::cout << str1 << "\n" << str2 << std::endl;
}
