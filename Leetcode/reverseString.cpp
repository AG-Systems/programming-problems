#include <algorithm>
#include <iostream>

class Solution {
public:
    string reverseString(string s) 
    {
            reverse(s.begin(),s.end());
            return s;
    }
};
