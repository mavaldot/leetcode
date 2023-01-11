class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        if length >= pow(10, 4) or width >= pow(10,4) or height >= pow(10, 4) or length*width*height >= pow(10, 9):
            if mass >= 100:
                return "Both"
            else:
                return "Bulky"
        elif mass >= 100:
            return "Heavy"
        return "Neither"