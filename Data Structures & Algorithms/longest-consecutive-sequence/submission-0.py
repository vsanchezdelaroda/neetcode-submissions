class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # Este podemos hacerlo en time O(n) asumiendo que no todos los números son inicio de secuencia. De hecho, solo pueden ser inicio de secuencia aquellos numeros cuyo anterior
        # no exista en el set. A partir de esto, iteramos sobre un set, con busqueda constante y avanzamos de uno en uno en los elementos 
        
        nums_set = set(nums)

        res = 0

        for num in nums_set:
            # Si el numero es inicio de secuencia
            if (num - 1) not in nums_set:
                length = 1
                # Comprobamos si existen de uno en uno 
                while (num + length) in nums_set:
                    length += 1
                
                # Vemos si la secuencia es mas grande que la anterior encontrada
                res = max(res, length)

        return res