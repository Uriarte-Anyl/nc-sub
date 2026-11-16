class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #output: [[ab,ba], [ac, ca], [ad]], in any order
        #input: unsorted array strs

        res = defaultdict(list) # mostly used for grouping data

        for s in strs:
            count = [0] * 26 # makes a list of 26 zeros for letters, tally sheet

            for c in s: # Go through each letter
                count[ord(c) - ord('a')] += 1 # add one to its slot
            
            key = tuple(count) # converts the key to a tuple, to be immutable
            res[key].append(s) # key value pairing, k: count of letters, v: words 
                               # ~ with the same number of counted letters
            
        return list(res.values())