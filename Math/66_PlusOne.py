class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        digits[-1] += 1
        if digits[-1] >= 10:
            digits[-1] -= 10
            carry = 1
        for i in range(len(digits) - 2, -1, -1):
            digits[i] += carry
            carry = 0
            if digits[i] >= 10:
                digits[i] -= 10
                carry = 1
            if not carry:
                break
        if carry:
            digits.insert(0, 1)

        return digits