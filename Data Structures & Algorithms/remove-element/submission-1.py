class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        # Al ser in-place, no podemos declarar estructuras adicionales.
        # Para ello, creo que es necesario crear dos punteros, uno al principio y otro al final, de cara a poder a hacer un swap de valores al final

        i = 0
        n = len(nums)


        while i < n:
            print(f"Iteracion {i} de {n}")
            if nums[i] != val:
                print(f"No hay coincidencia. Res: {nums}")
                i += 1
            else:
                n -= 1
                aux = nums[i]
                nums[i] = nums[n]
                nums[n] = aux
                print(f"Hay coincidencia. Res: {nums}")
        return i
