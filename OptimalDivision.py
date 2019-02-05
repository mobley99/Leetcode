from functools import reduce

class Solution:
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        
        arr = [float(i) for i in nums]
        s = ''
        r,s = self.InnerOptimalDivision(arr, True, s)
        if s.startswith('(') and s.endswith(')'):
            s = s[1:-1]
        s = s.replace('.0','')
        return s
    
    def InnerOptimalDivision(self, arr, prior_max, st):

        if len(arr) == 1:
            st += str(arr[0])
            return arr[0] , st
        elif len(arr) == 2:
            st += '({}/{})'.format(arr[0],arr[1])
            return arr[0]/arr[1], st
        elif len(arr) == 3:
            a = arr[0]
            b = arr[1]
            c = arr[2]
            if prior_max:
                mmax = 0
                if a/b/c >= (a/b)/c and a/b/c >= a/(b/c):
                        st += '({}/{}/{})'.format(a,b,c)
                        mmax = a/b/c
                elif a/(b/c) <= (a/b)/c:
                    st += '({}/{})/{}'.format(a,b,c)
                    mmax = (a/b)/c
                else:
                    st += '{}/({}/{})'.format(a,b,c)
                    mmax = a/(b/c)
                return mmax, st
            else:
                mmin = 0
                if a/b/c <= (a/b)/c and a/b/c <= a/(b/c):
                        st += '({}/{}/{})'.format(a,b,c)
                        mmin = a/b/c
                elif a/(b/c) >= (a/b)/c:
                    st += '({}/{})/{}'.format(a,b,c)
                    mmin = (a/b)/c
                else:
                    st += '{}/({}/{})'.format(a,b,c)
                    mmin = a/(b/c)
                return mmin, st
        else:
            n = len(arr)
            m = int(n / 2)
            max_part = reduce(lambda x,y: x/y, arr)
            a = max_part
            
            for j in range(1,m+1):
                partition2= arr[j:]
                partition1= arr[:j]
                partition4= arr[n-j:]
                partition3= arr[:n-j]

                p = ''
                q = ''
                r = ''
                s = ''

                if prior_max:

                    b1, p = self.InnerOptimalDivision(partition1,True,p) 
                    b2, q = self.InnerOptimalDivision(partition2,False,q)
                    b = b1 / b2

                    c1, r = self.InnerOptimalDivision(partition3,True,r) 
                    c2, s = self.InnerOptimalDivision(partition4,False,s)
                    c = c1 / c2

                    if b >= c and b >= max_part:
                        st = '({}/{})'.format(p,q)
                        max_part = b
                    elif c >= b and c >= max_part:
                        st = '({}/{})'.format(r,s)
                        max_part = c
                    elif a >= max_part:
                        st = '('
                        st += '/'.join(str(k) for k in arr)
                        st += ')'
                else:

                    b1, p = self.InnerOptimalDivision(partition1,False,p) 
                    b2, q = self.InnerOptimalDivision(partition2,True,q)
                    b = b1 / b2

                    c1, r = self.InnerOptimalDivision(partition3,False,r) 
                    c2, s = self.InnerOptimalDivision(partition4,True,s)
                    c = c1 / c2

                    if b <= c and b <= max_part:
                        st = '({}/{})'.format(p,q)
                        max_part = b
                    elif c <= b and c <= max_part:
                        st = '({}/{})'.format(r,s)
                        max_part = c
                    elif a <= max_part:
                        st = '('
                        st += '/'.join(str(k) for k in arr)
                        st += ')'
        return max_part, st
