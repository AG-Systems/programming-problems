class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if strs == [""]:
            return [[""]]
        duplicate_counter = {}
        for word in strs:
            count = [0] * 26
            for letter in word:
                index = ord(letter) - ord('a')
                count[index] += 1
            key = tuple(count)
            if key in duplicate_counter:
                duplicate_counter[key].append(word)
            else:
                duplicate_counter[key] = [word]
        return list(duplicate_counter.values())
