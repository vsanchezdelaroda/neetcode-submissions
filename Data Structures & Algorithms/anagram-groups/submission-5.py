class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Time - O(n*k)
        # Space - O (n*k)
        # n is the number of strings in strs
        # k is the max leng of a str in strs
        
        dict_res = defaultdict(list)

        for s in strs:
            # Declaramos un array de 0s con 26 posiciones, una para cada letra
            counter = [0] * 26
            # Para cada caracter
            for c in s:
                # Cogemos el código unicode del caracter y le restamos el de a, para quedarnos con un numero entra 0 y 26
                counter[ord(c) - ord('a')] += 1
            # Añadimos a la clave de conteo de caracteres, cada anagrama
            dict_res[tuple(counter)].append(s)
        
        return list(dict_res.values())