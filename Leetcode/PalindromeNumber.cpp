class Solution {
public:
    bool isPalindrome(int x) 
    {
        std::string str = std::to_string(x);
        if (str == std::string(str.rbegin(), str.rend())) 
    	{
    		return true;
    	}
    	else
    	{
    	    return false;
    	}
    }
};
