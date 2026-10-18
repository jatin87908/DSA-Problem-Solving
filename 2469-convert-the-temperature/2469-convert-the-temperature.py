class Solution:
    def convertTemperature(self, celsius: float) -> list[float]:
        val1 = celsius + 273.15
        val2 = celsius * 1.80 + 32
        return [val1, val2]