class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        pref = strs[0]

        for i in range(1, len(strs)):
            while not strs[i].startswith(pref):
                pref = pref[:-1]
                if not pref:
                    return ""

        return pref
