class Solution {
public:
    int hammingDistance(int x, int y) {
        x=x^y;
        int res=0;
        // get the total 1 digits
        while(x>0){
            if(x&1) res++; // if its final bit is 1, res++
            x=x>>1;
        }
        return res;
    }
};
