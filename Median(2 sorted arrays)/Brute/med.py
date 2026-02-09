class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ans =[]
        i =0
        j =0
        
        m= len(nums1)
        n = len(nums2)

        while(i<m and j<n):
            if nums1[i] < nums2[j]:
                ans.append(nums1[i])
                i += 1
            else:
                ans.append(nums2[j])
                j += 1
        
        while(i<m):
            ans.append(nums1[i])
            i += 1
        while(j<n):
            ans.append(nums2[j])
            j += 1

        total = m+n

        if (total % 2)==0:
            return ((ans[total//2-1] + ans[total//2])/2.0)

        else:
            return (ans[total//2])
