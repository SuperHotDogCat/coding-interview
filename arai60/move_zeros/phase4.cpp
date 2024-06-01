class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        auto result = nums.begin();
        auto last = nums.end();
        int non_zero_count = 0;
        for (auto first = nums.begin();first != last; first++){
            if (!(*first == 0)){
                *result++ = std::move(*first);
                non_zero_count++;
            }
        }
        for (; non_zero_count < nums.size(); non_zero_count++){
            *result++ = 0;
        }
    }
};
