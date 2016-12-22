#include <iostream>
#include <vector>
#include <algorithm>

int main()
{
   std::vector <int> list;
   int n, c, first = 0, second = 1, next;
   int input;
   std::cout << "Please choose how many terms: " << std::endl;
   std::cin >> n;
   std::cout << "Please choose the number you want: " << std::endl;
   std::cin >> input;
   std::cout << "-----------------------------------------------" << "\n" << "Started:" << std::endl;
   for ( c = 0 ; c < n ; c++ )
   {
      if ( c <= 1 )
         next = c;
      else
      {
         next = first + second;
         first = second;
         second = next;
      }
      std::cout << next << std::endl;
      list.push_back (next);
   }
   if ( std::find(list.begin(), list.end(), input) != list.end() )
   {
        std::cout << "Congrats. We have found your number " << std::endl;        
   }
}
