#include <iostream>
#include <vector>

std::vector <int> countinarray(std::vector <int> a)
{
    std::vector <int> counter = a;
    for(int z = 0; z < a.size()-1; z++)
    {
        for(int x = (z+1); x < a.size(); x++)
        {
            if(a[z] == a[x])
            {
                counter[z]++;  
                std::cout << a[z] << std::endl;
            }
        }
    }
    return counter;
}

int main()
{
    std::vector <int> list = {1,1,2,3,4,5,6,7,7,8,0,1};
    countinarray(list);
}
