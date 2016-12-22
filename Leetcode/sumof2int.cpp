class Solution {
public:
    int getSum(int num1, int num2) {
    int counter = 0;
    int numcounter = 0;
    while(true)
    {
        counter++;
        if(counter == num1)
        {
            while(true)
            {
                numcounter++;
                counter++;
                if(numcounter == num2)
                {
                    return counter;
                    break;

                }
            
            }
        }
    }
    
}
};
