class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ln = len(nums)
        l_arr = [0] * ln
        r_arr = [0] * ln

        l_run = 1
        r_run = 1

        for i in range(ln):
            j = ln -1 -i #opposite of i, [1(i), 2, 4, 6(j)]

            l_arr[i] = l_run
            r_arr[j] = r_run

            l_run *= nums[i]
            r_run *= nums[j]

        return[l*r for l, r in zip(l_arr, r_arr)] #short for [x,..] * [x,..]

