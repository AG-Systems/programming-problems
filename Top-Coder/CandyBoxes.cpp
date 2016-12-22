#include <iostream>
using namespace std;

int main ()
{
    int array []= {7,21,14};
    int max = 0;
    int smallest = array[0] ;
    for (int i = 1;  i < sizeof(array)/sizeof(array[0]); i++)
    {
        if ( array[i] < smallest )
        {
             smallest = array[i];
        }
    }
    std::cout << "Min: "<< smallest << std::endl;
    for(int i = 0; i < sizeof(array)/sizeof(array[0]); i++)
    {
        if(array[i] > max)
        max= array[i];
    }
    std::cout << "Max: " << max << std::endl;

    if (max == smallest)
    {
        std::cout << "The kid did not need to eat any candy " << std::endl; 
        return 0;
    }
    int final = max - smallest;
    for(int z = 0; z < sizeof(array)/sizeof(array[0]); z++)
    {
        if (max != smallest)
        {
            for (int i = 1;  i < sizeof(array)/sizeof(array[0]); i++)
            {
                if ( array[i] < smallest )
                {
                    smallest = array[i];
                }
            }
            std::cout << "Min: "<< smallest << std::endl;
            for(int i = 0; i < sizeof(array)/sizeof(array[0]); i++)
            {
                if(array[i] > max)
                {
                    max= array[i];
               }
            }    
        }
    
    }
}
