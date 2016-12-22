class Solution {
public:
    vector<string> fizzBuzz(int n) {
        vector<string> fb(n);
        for(int z=1; z<=n; z++)
        {
            if(z %3 == 0)
            {
                fb[z-1] += string("Fizz");
            }
            if(z%5 == 0)
            {
                fb[z-1] += string("Buzz");
            }
            if(fb[z-1] == "")
            {
                fb[z-1] += to_string(z);
            }
        }
        return fb;
    }
};
