#include <iostream>
#include <algorithm> 
#include <cstdlib>

int main()
{
    int antler1[3] = {3, 2, 5};
    int antler2[3] = {3, 5, 5};
    
    int capacity;

    for (int z = 0; z < 3; z++)
    {
        for (int x = 0; x < 3; x++)
        {
            if (antler1[z] != antler2[x])
            {
                //int diff = std::max(x,y)-std::min(x,y);  
                int diff = std::abs(antler1[z]-antler2[x]);
                int final = antler2[x] - diff;
                std::cout << final << std::endl;
            }
        }
    }
}
