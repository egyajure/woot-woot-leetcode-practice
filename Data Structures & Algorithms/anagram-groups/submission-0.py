class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # make a mapping of code -> word (anagrams of eachother will have the same code (sorted))

        groupings = defaultdict(list)

        for s in strs:
            code = ''.join(sorted(s))
            groupings[code].append(s)
        
        return [l for l in groupings.values()]