class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows <= 0:
            return []
        
        def gen_cell(i,j):
            if i == j or j == 1:
                return 1
            return gen_cell(i - 1, j - 1) + gen_cell(i - 1, j)
        
        rows = []
        
        counter = 1
        while counter <= numRows:
            row = []
            index = 1
            
            while len(row) < counter:
                row.append(gen_cell(counter,index))
                index += 1
                
            rows.append(row)
            counter += 1
        
        return rows
                
            
        
