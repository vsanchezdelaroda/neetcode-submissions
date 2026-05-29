class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # Aqui vamos a utilizar sets para ver los duplicados
        # La idea es tener 3 sets, uno por columnas, uno por filas y otro por cuadrados
        # Para identificar las columnas y las filas, utilizaremos sus indices
        # Para identificar los cuadrados, utilizaremos (r//3, c // 3 ) así hay 9 claves diferentes


        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if ( board[r][c] in rows[r] or
                     board[r][c] in cols[c] or
                     board[r][c] in squares[(r//3,c//3)]
                
                ):
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r//3,c//3)].add(board[r][c])
        
        return True
                