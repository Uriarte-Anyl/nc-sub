class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        nt = 9 # number of tiles

        # row 
        for i in range(nt):
            unique = set()

            for j in range(nt):
                item = board[i][j]

                if item in unique:
                    return False
                elif item != '.':
                    unique.add(item)
        
        # col
        for i in range(nt):
            unique = set()

            for j in range(nt):
                item = board[j][i]

                if item in unique:
                    return False
                elif item != '.':
                    unique.add(item) 

        # sub-box
        starts = [(0,0), (0,3), (0,6),
                      (3,0), (3,3), (3,6),
                      (6,0), (6,3), (6,6),]

        for i, j in starts:
            unique = set()
            
            for row in range(i, i+3):
                for col in range(j, j+3):
                    item = board[row][col]
                    
                    if item in unique:
                        return False
                    elif item != '.':
                        unique.add(item)
        return True