class Solution:

    def encode(self, strs: List[str]) -> str:
        # Para hacer encode, vamos a generar una string nueva, que sea len1|word1len2|word2...
        res = ""

        for s in strs:
            res += str(len(s)) + '|' + s
        
        return res

    def decode(self, s: str) -> List[str]:
        # Para decodear, hay que leer el numero y el hashtag (doble puntero)
        
        res = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != '|':
                j += 1
            
            # Los caracteres que hay entre el primer puntero y el anterior al pipe, indican la longitud
            size_word = int(s[i:j])
            # Me coloco despues del pipe
            i = j+1
            # Avanzo la longitud de la palabra
            j = i + size_word
            # Leo la palabra
            res.append(s[i:j])
            i = j
        
        return res