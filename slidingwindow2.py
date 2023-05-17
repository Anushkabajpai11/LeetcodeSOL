def areAnagram(s1, s2):
    m = {}
    for i in range(len(s1)):
        if s1[i] not in m:
            m[s1[i]] = 1
        else:
            cnt = m[s1[i]]
            m.pop(s1[i])
            m[s1[i]] = cnt + 1

    for j in range(len(s2)):
        if ((s2[j] in m) == False):
            return False
        else:
            cnt = m[s2[j]]
            m.pop(s2[j])
            m[s2[j]] = cnt - 1

    for it in m.values():
        if (it != 0):
            return False
    return True


def countAnagrams(text, word):

    # Initialize result
    res = 0
    for i in range(len(text) - len(word)+1):

        # Check if the word and substring are
        # anagram of each other.

        if (areAnagram(text[i:i+len(word)], word)):
            res += 1
    return res

# Driver Code


text = "forxxorfxdofr"
word = "for"

print(countAnagrams(text, word))
