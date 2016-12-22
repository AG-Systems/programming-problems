#include <iostream>
#include <vector>
#include <algorithm> 

std::vector <int> countinarray(std::vector <int> a)
{
    std::sort(a.begin(), a.end());
    std::vector <int> counter;
    std::vector <int> numlist;
    for(int i = 0; i < a.size(); i++)
    {
        numlist.push_back(i);
        counter.push_back(0);
    }
    for(int z = 0; z < a.size()-1; z++)
    {
        for(int x = (z+1); x < a.size(); x++)
        {
            if(a[z] == a[x])
            {
                if(a[z] != a[z-1])
                {
                    counter[(a[z])]++;
                }
            }
        }
    }
    for(int z = 0; z < a.size(); z++)
    {
        if(counter[z] > 0)
        {
            counter[z]++;
        }
        std::cout << numlist[z] << ": " << counter[z] << std::endl;
    }
    return counter;
}

int main()
{
    std::vector <int> list = {1,7,2,3,3,3,4,5,6,7,7,1,8,0,1,7,8,4,7};
    countinarray(list);
}
