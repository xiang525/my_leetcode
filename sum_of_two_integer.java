"""
1. exclusive or (^) handles these cases: 1+0 and 0+1
2. AND (&) handles this case: 1+1, where carry occurs, in this case, we'll have to shift 
carry to the left, why? Think about this example: 001 + 101 = 110 (binary format), 
the least significant digits of the two operands are both '1', thus trigger a carry = 1,
with this carry, their least significant digits: 1+1 = 0, thus we need to shift the carry 
to the left by 1 bit in order to get their correct sum: 2
"""

public class Solution {
    public int getSum(int a, int b) {
        if(b==0) return a;
        int carry = (a&b) << 1;
        int sum = a^b;
        return getSum(sum, carry);
    }
}

"""
Python 表示一个数不止32位。。

Of course, Python doesn’t use 8-bit numbers. It USED to use however many bits were 
native to your machine, but since that was non-portable, it has recently switched to 
using an INFINITE number of bits. Thus the number -5 is treated by bitwise operators 
as if it were written “…1111111111111111111011”.
来自 https://wiki.python.org/moin/BitwiseOperators

因此。。做这题蛋疼啊
"""