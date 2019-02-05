class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        def aslice(i,j,A):
            if A[j-1] - A[i] == A[j] - A[j-1]:
                return True
            return False
        
        count = 0
        seq = 0
        previous = False
        
        for i in range(2, len(A)):
            if aslice(i-2,i,A):
                seq +=1
                count += seq
            else:
                seq = 0
        return count
