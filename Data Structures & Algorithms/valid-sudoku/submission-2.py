class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        No_OF_TILES = 9

        # row
        for i in range(No_OF_TILES):
            has_duplicate = set()
            for j in range(No_OF_TILES):
                item = board[i][j]
                if item in has_duplicate:
                    return False
                elif item != '.':
                    has_duplicate.add(item)

        # col
        for i in range(No_OF_TILES):
            has_duplicate = set()
            for j in range(No_OF_TILES):
                item = board[j][i]
                if item in has_duplicate:
                    return False
                elif item != '.':
                    has_duplicate.add(item)

        #sub-box
        for i in range(0, 9, 3): # start of the boxes per row
            for j in range(0, 9, 3): # start of the boxes per col
                has_duplicate = set()
                for row in range(i, i+3): # iteration starts at 0 and ends at 3
                    for col in range(j, j+3):
                        item = board[row][col]
                        if item in has_duplicate:
                            return False
                        elif item != '.':
                            has_duplicate.add(item)
        return True

            