class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) 
    {
        vector <int> list;
        for(int z = 0; z < nums.size()-1; z++)
        {
            for(int x = (z+1);x < nums.size(); x++)
            {
                if(nums[z] + nums[x] == target)
                {
                    std::cout << "Index numbers: " << z << " " << x  << std::endl;
                    std::cout << "Number in array: " << nums[z] << " " << nums[x] << std::endl;
                    list.push_back(z);
                    list.push_back(x);
                    return list;
                }
            }
        }
        return list;
    }
};
