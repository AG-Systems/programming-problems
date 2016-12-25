class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums)
    {
        std::vector <int> main;
        std::vector <int> output;
        std::sort(nums.begin(), nums.end());
        for(int z = 1; z < nums.size() + 1; z++)
        {
            main.push_back(z);
        }
        for(int x = 0; x < nums.size(); x++)
        {
            bool checker = false;
            for(int z = 0; z < nums.size(); z++)
            {
                if(main[x] == nums[z])
                {
                    checker = true;
                }
            }
            if(!checker)
            {
                output.push_back(main[x]);
            }
        }
        return output;
    }
};
// TIME LIMIT EXCEEDED : (
