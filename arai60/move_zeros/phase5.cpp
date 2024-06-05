class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        auto result = nums.begin();
        auto last = nums.end();
        int non_zero_length = 0;
        for (auto first = nums.begin();first != last; first++){
            if (!(*first == 0)){
                *result++ = std::move(*first);
                non_zero_length++;
            }
        }
        for (; non_zero_length < nums.size(); non_zero_length++){
            *result++ = 0;
        }
    }
};
