#Big-O  
# O(1)      : Constant time       => Fastest
# O(logN)   : Log Time
# O(N)      : Linear Time
# O(NlogN)  : Log Linear Time
# O(N^2)    : Quadratic
# O(N^3)    : Cubric
# O(2^n)    : Exponential
# O(n!)     : Factorial           => Slowest

#             When N is 1,000
# O(N)          1,000
# O(NlogN)      10,000
# O(N^2)        1,000,000
# O(n^3)        1,000,000,000

#               When time constraint is 1 sec
# When N has range 500        : Can be solved with O(N^3) 
# When N has range 2,000      : Can be solved with O(N^2) 
# When N has range 100,000    : Can be solved with O(NlogN)
# When N has range 10,000,000 : Can be solved with O(N)
