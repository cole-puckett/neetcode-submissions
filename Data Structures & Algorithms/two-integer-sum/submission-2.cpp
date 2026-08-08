#include <unordered_map>
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // create a hashmap with the difference needed as the key and the
        // index as the value

        std::unordered_map<int, int> map;

        for (int i{}; i < nums.size(); ++i) {
            int difference = target - nums[i];
            if (map.count(difference)) {
                std::vector<int> answer = {map[difference], i};
                return answer;
            }
            map[nums[i]] = i;
        }
        std::vector<int> answer = {};
        return answer;

    }
};
