class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = ""
        for word in strs:
            if common == "":
                common = word
            else:
                for i in range(len(word)):
                    try:
                        if common[i] != word[i]:
                            common = common[0:i]
                            if common == "": return common
                    except:
                        continue
        return common