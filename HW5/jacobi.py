# Copyright (c) 2012 the authors listed at the following URL, and/or
# the authors of referenced articles or incorporated external code:
# http://en.literateprograms.org/Jacobi_Symbol_(Python)?action=history&offset=20110203234923
# 
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
# 
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# 
# Retrieved from: http://en.literateprograms.org/Jacobi_Symbol_(Python)?oldid=17037


def jacobi(a,n):
    if a == 0:
        return 0

    if a == 1:
        return 1
    if a == 2:
        n8 = n%8
        if n8 == 3 or n8 == 5:
            return -1
        else:
            return 1
    if a%2 == 0:
        return jacobi(2,n) * jacobi(a//2,n)
    if a >= n:
        return jacobi(a%n,n)
    if a%4 == 3 and n%4 == 3:
        return -jacobi(n,a)
    else:
        return jacobi(n,a)

if __name__ == '__main__':
    print(jacobi(11,181))

