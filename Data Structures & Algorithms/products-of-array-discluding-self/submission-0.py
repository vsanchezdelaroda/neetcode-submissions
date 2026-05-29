class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # La solucion naive aquí, en O(n2), es iterar dos veces
        res = [0] * len(nums)

        for i, num_i in enumerate(nums):
            print(i, num_i)
            aux = 1
            
            for j, num_j in enumerate(nums):
                if i != j:
                    aux *= num_j
            
            res[i] = aux
        
        return res