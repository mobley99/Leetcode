class Solution(object):
    def fizzBuzz(self, n):
        fizz = 'Fizz'
        buzz = 'Buzz'
        ret = []
        for i in range(1,n + 1):
            sol = ''
            if i % 3 == 0:
                sol += fizz
            if i % 5 == 0:
                sol += buzz
            if sol == '':
                ret.append(str(i))
            else:
                ret.append(sol)
        return ret
            
        
