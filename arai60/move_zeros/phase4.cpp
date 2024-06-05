class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        auto result = nums.begin();
        int non_zero_length = 0;
        for (auto it = nums.begin();it != nums.end(); it++){
            if (*it != 0){
                *result++ = *it;
                non_zero_length++;
            }
        }
        std::fill(result, nums.end(), 0);
    }
};
