class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        crry = 0

        for i in range(len(digits)-1,-1,-1):
            if crry != 0:
                if digits[i] + crry == 10:
                    digits[i] = 0
                    crry = 1
                else:
                    digits[i] += crry
                    crry = 0
                    break
        
            if i == len(digits)-1:
                if digits[i] + 1 == 10:
                    crry = 1
                    digits[i] = 0
                else:
                    digits[i] += 1
                    break
            
        
        if crry == 1:
            digits.insert(0, 1)

        return digits

