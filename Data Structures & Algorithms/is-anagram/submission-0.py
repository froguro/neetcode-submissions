class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        res = False

        s_list = sorted(list(s))
        t_list = sorted(list(t))
        print(s_list)
        print(t_list)
        if s_list == t_list:
            res = True
        return res


