//Source-https://leetcode.com/problems/median-of-two-sorted-arrays/
//Author-Uditanshu

Question-
****************************************
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
****************************************
Solution-
****************************************
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new=nums1+nums2
        new.sort()
        a=len(new)
        z=int((a+1)/2)
        y=int(a/2)
        if len(new)%2==0:
            mean=(new[y-1]+new[y])/2.0
        else:
            
            mean=float(new[z-1])
        return mean
****************************************
