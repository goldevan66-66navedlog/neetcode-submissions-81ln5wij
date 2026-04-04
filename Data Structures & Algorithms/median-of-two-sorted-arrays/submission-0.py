class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1
        B = nums2
        total = len(A) + len(B)
        half = total//2

        if(len(A) > len(B)):
            A,B = B,A

        l,r = 0, len(A)-1
        while(True):
            i = (l+r)//2
            j = half - i - 2

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i+1] if i+1 < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j+1] if j+1 < len(B) else float("infinity")

            if(Aleft <= Bright and Bleft <= Aright):
                if(total % 2):
                    return min(Aright,Bright)
                return (max(Aleft,Bleft) + min(Aright,Bright)) / 2
            elif(Aleft > Bright):
                r = i-1
            else:
                l = i+1
        
        # l1,r1 = 0, len(nums1)-1

        # while(l1 <= r1):
        #     m1 = (l1+r1)//2
        #     target = nums1[m1]
        #     l2,r2 = 0, len(nums2)-1

        #     while(l2 < r2):
        #         m2 = (l2+r2)//2
        #         if(nums2[m2] <= target):
        #             l2 = m2+1
        #         else:
        #             r2 = m2-1
        #     idx = l2+1
        #     less = idx + m1
        #     greater = (len(nums2)-1-idx) + (len(nums1)-1-m1)

        #     if(abs(less-greater)<=1):
        #         if(len(nums2)+len(nums1)%2 == 1):
        #             return nums2[idx]
        #         else:
        #             if (greater > less):


