class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # Aqui vamos a seguir una estrategia de doble puntero. Simplemente, tenemos que limpiar la palabra y después empezar por el final y por el principio y ver si todos los caracteres son iguales
        # Como es en O(1), no puedo crear una nueva string, hare una funcion para comprobar el rango en unicode

        i = 0
        j = len(s) - 1
    
        while i < j:
            
            # Buscamos un caracter valido por izquierda
            while i < j and not self.is_alphanum(s[i]):
                i += 1
            # Buscamos un caracter valido por derecha
            while i < j and not self.is_alphanum(s[j]):
                j -= 1

            if s[i].lower() != s[j].lower():
                return False
            
            i += 1
            j -= 1
        return True

    def is_alphanum(self, s:str) -> bool:

        return (
                ord('A') <= ord(s) <= ord('Z') or
                ord('a') <= ord(s) <= ord('z') or
                ord('0') <= ord(s) <= ord('9')
        )