class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        n = str(x)

        sum_ = 0

        for i in n:
            sum_ += int(i)

        if x % sum_ == 0:
            return sum_
        else:
            return -1
