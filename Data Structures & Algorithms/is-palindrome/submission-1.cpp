class Solution {
public:
    bool isPalindrome(string s) {
       s.erase(std::remove_if(s.begin(), s.end(), [](unsigned char c) {
        return !std::isalnum(c);
        }), s.end());

        for (int i = 0; i < s.size(); i++) {
            if (isupper(s[i])) s[i] = tolower(s[i]);
        }
       string s_reverse = s;
       reverse(s_reverse.begin(), s_reverse.end());
       return s_reverse == s;
    }
};
