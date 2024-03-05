"""
Problem: LeetCode 167 - Two Sum II

Key Idea:
The input array 'numbers' is already sorted in non-decreasing order. To find the two numbers that add up to the target, we can use a two-pointer approach. We initialize two pointers, one at the beginning of the array (left) and the other at the end of the array (right). We then check the sum of the elements at these two pointers. If the sum is equal to the target, we have found the pair. If the sum is less than the target, it means we need to increase the sum, so we move the left pointer one step to the right. If the sum is greater than the target, it means we need to decrease the sum, so we move the right pointer one step to the left. We continue this process until we find the pair or the two pointers meet or cross each other.

Time Complexity:
The time complexity of this solution is O(n), where n is the number of elements in the input array 'numbers'. The two pointers approach iterates through the array once, and at each step, we move at least one of the pointers, so we do not revisit any element.

Space Complexity:
The space complexity is O(1) since we are not using any additional data structures that depend on the input size. We only use a constant amount of extra space for the two pointers and other variables.
"""
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left,right=0,len(numbers)-1
        while left<right:
            currentSum = numbers[left] + numbers[right]
            if currentSum == target:
                return [left+1,right+1]
            elif currentSum<target:
                left +=1
            else :
                right -=1
        return [-1,-1]
        