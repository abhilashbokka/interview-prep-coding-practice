## This is a crazy problem, and I got stuck at updating the boundaries properly, I was only uopdating immediate boundaires, but that has consequences. Ideally you should uodaet the boundary lengths.

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        lengths = {}

        for num in nums:

            if num in lengths:
                continue

            left = lengths.get(num - 1, 0)
            right = lengths.get(num + 1, 0)

            total = left + right + 1

            lengths[num] = total

            lengths[num - left] = total
            lengths[num + right] = total
        return max(lengths.values())
    

# The other solution below uses while loop, but we only visit each number once including the while loop because of the stucture it follows, so it is also O(n) time complexity.

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        num_set = set(nums)

        for n in num_set:
            if (n-1) not in num_set:
                length = 1
                while (n+length) in num_set:
                    length += 1
                longest = max(longest, length)
        
        return longest

    