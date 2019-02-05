class Solution(object):
    def subarrayBitwiseORs(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) == 1:
		    return 1

        m = 0
        for a in A:
            m |= a

        results = {A[0]}

        s = {A[0]}

        for i in range(1,len(A)):
            r = s
            s = {A[i]}
            results.add(A[i])
            for elem in r:
                tmp = A[i] | elem
                s.add(tmp)
                results.add(tmp)
            r = {}
        return len(results)
