class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex <= 0:
            return [1]
        
        def gen_cell(i,j):
            if i == j or j == 1:
                return 1
            return gen_cell(i - 1, j - 1) + gen_cell(i - 1, j)
        
        row = []
            
        index = 1
        while len(row) < rowIndex + 1:
            row.append(gen_cell(rowIndex + 1,index))
            index += 1
                
        
        return row
                
            
        
