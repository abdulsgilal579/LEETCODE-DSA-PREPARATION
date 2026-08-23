from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = collections.deque()
        left = 0
        right = 0
        res = []

        while right < len(nums):            
            while dq and nums[dq[-1]] < nums[right]:
                dq.pop()
            dq.append(right)
        
            if dq and dq[0] < left:
                dq.popleft()
            if right + 1 >= k:
                res.append(nums[dq[0]])
                left +=1
            right +=1
        return res