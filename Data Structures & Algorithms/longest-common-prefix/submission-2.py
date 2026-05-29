class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        # We take the first word. We should check char by char if all words contains it
        preffix = strs[0]
        
        # Iteramos en el rango de caracteres de la primera palabra
        for i in range(len(preffix)):
            # Para todas las palabras del array
            for word in strs:
                # Si el caracter no corresponde, paramos en el anterior. Hay que comprobar, que no haya fuera de limites (por ejemplo cadenas vacías)
                if i == len(word) or word[i] != preffix[i] :
                    return word[:i]
        # Si termina, es la palabra entera
        return preffix





