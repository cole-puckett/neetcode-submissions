#include <unordered_map>
class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_map<int, int> numMap{};
        for (int num : nums) {
            numMap[num] += 1;
            if (numMap[num] > 1) {
                return true;
            }
        }
        return false;
    }
};