def isBadVersion(version: int) -> bool:
    return 

def firstBadVersion(n: int) -> int:
        if n == 1:
            return 1 if isBadVersion(1) else -1
        
        l, r = 1, n
        while l < r:
            mid = l + (r - l) // 2
            isBad = isBadVersion(mid)
            isPrevBad = isBadVersion(mid - 1)
            
            if isBad and not isPrevBad:
                return mid
            
            if isBad:
                r = mid - 1
            
            else:
                l = mid + 1
                
        if isBadVersion(l):
            return l   
