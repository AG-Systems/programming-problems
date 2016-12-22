#include <iostream>
#include <array>

int main()
{
    int request[3] = {'1','2','3'};
    int requestLength = 3;
    int counter = 0;
    for(int x = 0; x < requestLength - 1; x++)
    {
        for(int z = x + 1; z < requestLength; z++)
        {
            if ( request[x] == request[z])
            {
                counter++;    
            }
        }
    }
    std::cout << "return: " << counter << std::endl;
}
