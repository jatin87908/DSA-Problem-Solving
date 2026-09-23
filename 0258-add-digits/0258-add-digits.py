class Solution:
    def addDigits(self, num: int) -> int:
        number = num

        while number >= 10:
            digit_sum = 0

            while number > 0:
                digit_sum += number % 10
                number //= 10

            number = digit_sum

        return number