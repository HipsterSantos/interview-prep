def longest_common_prefix(str):
    #potentinal hedge cases
    if not str: return ""
    if len(str)==1: return str[0]
    # initialize the longest commom prefix as being the first string
    longest_commom_prefix = str[0]
    for s in str[1:]:
        while not s.startswith(longest_commom_prefix):
            longest_commom_prefix = longest_commom_prefix[:-1]
            if not longest_commom_prefix: return ""
    return longest_commom_prefix

strs1 = ["flower", "flow", "flight"]
print(f"Longest common prefix: {longest_common_prefix(strs1)}")