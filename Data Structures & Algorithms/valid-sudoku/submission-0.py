class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for i in range(9)] 
        column = [set() for i in range(9)] 
        subbox = [set() for i in range(9)] 


        #rowbox iterates through vertically -> up to down
        # columnbox iterates through horizontally -> left to right
        # board is accessed by board[rowbox][columnbox]
        # row is updated by row[rowbox 0 to rowbox 8], column updated by row[columnbox 0 to 8]
        for rowbox in range(9):
            for columnbox in range(9):
                value = board[rowbox][columnbox]
                sqindex = (rowbox // 3) * 3 + (columnbox //3)
                if value not in row[rowbox] and value not in column[columnbox] and value not in subbox[sqindex] and value != ".":
                    row[rowbox].add(value)
                    column[columnbox].add(value)
                    subbox[sqindex].add(value)
                elif value == ".":
                    pass
                else:
                    return False

        
        return True
        
