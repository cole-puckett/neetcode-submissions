#include <unordered_map>
class Solution {
public:
    bool isAnagram(string s, string t) {
        std::unordered_map<char, int> first_map;
        std::unordered_map<char, int> second_map;

        for (char c : s){
            first_map[c] += 1;
        }
        for (char c : t) {
            second_map[c] += 1;
        }

        if (first_map != second_map){
            return false;
        }
        return true;
    }
};
