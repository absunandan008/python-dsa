class Solution:

    def findKthPositive(self, arr: List[int], k: int) -> int:
        """
        so basically at any point in array the index is supposed to show index+1 number
        so if we do arr[index] - (index+1), it should be 0 but if its < k then our value is
        in right range else its in left range. so once we find where K fits.
        we add lo to k
        """
        if k <= arr[0] - 1:
            return k
        lo = 0
        hi = len(arr)
        while lo < hi:
            mid = lo + (hi-lo) //2
            if arr[mid] - mid - 1 < k:
                lo = mid+1
            else:
                hi = mid
        return lo + k

    def findKthPositiveBad(self, arr: List[int], k: int) -> int:
        """
        difference between curren and current + 1 should be equal to 1
        so arr[i+1] - arr[i] -1 should be equal to 0, but it its now then check
        how far this is than k if k <= arr[i+1] - arr[i] -1, which means our
        kth missing number is inbetween i and i+1. so return arr[i]+k
        else
        decrease k by curr_missing which is k -= arr[i+1] - arr[i] - 1
        edge case, if start is missing then first check if k <= arr[0] - 1, if yes then retrun k
        k -= arr[0] -1
        """
        if k <= arr[0] - 1:
            return k
        k -= arr[0] -1
        for i in range(len(arr)-1):
            curr_missing = arr[i+1] - arr[i] - 1
            if k <= curr_missing:
                return arr[i] + k
            else:
                k -= curr_missing
        return arr[-1]+k