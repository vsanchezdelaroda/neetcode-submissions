class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # Al estar ordenado, podemos utilizar dos punteros. Uno al final y otro al principio.
        # Si sumamos los elementos de los punteros y el resultado es más grande que lo que buscamos, decrementamos el puntero del final (para buscar un número más pequeño)
        # Si el resultado es más pequeño, incrementamos el puntero inicial (para buscar un numero más grande)

        ini = 0
        fin = len(numbers) - 1

        while ini < fin:
            
            suma = numbers[ini] + numbers[fin]

            if suma == target:
                return [ini + 1, fin + 1]
            elif suma < target:
                ini += 1
            else: 
                fin -= 1
        
        return None