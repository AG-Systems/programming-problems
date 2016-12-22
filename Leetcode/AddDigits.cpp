class Solution {
public:
    int counter(int var)
    {
        int length = 1;
        while ( var /= 10 )
        {
            length++;
        }
        return length;
    }
    int addDigits(int num) 
    {

        int sum = 0;
        while ( num > 0 ) 
        {
            sum += num % 10;
            num /= 10;
        }
        if(counter(sum) == 1)
        {
            return sum;
        }
        else
        {
            while (counter(sum) > 1) 
            {
                sum += num % 10;
                num /= 10;
            }
            return sum;
        }
    }
};
