class Solution {
public:
    char findTheDifference(string s, string t) 
    {
        std::sort(s.begin(), s.end());
        std::sort(t.begin(), t.end());
        bool lastchar = true;
        char op = '0';
        for(int z = 0; z < s.size(); z++)
        {
            if(s[z] != t[z])
            {
                op = t[z];
                lastchar = false;
            }
        }
        if(lastchar)
        {
            op = t[s.size()];
        }
        return op;
    }
};
