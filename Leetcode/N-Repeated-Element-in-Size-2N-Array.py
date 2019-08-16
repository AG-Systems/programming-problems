class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        threshold = (len(A) / 2)
        threshold_table = {}
        
        threshold_leader = {
            "max_counter": 0,
            "element": None
        }
        
        for num_element in A:
            if num_element in threshold_table:
                threshold_table[num_element]["counter"] += 1
                
                current_num_element = threshold_table[num_element]["counter"]
                if current_num_element >= threshold:
                    return num_element
                
                
                if current_num_element > threshold_leader["max_counter"]:
                    threshold_leader["element"] = num_element
                    threshold_leader["max_counter"] = current_num_element
                
            else:
                 threshold_table[num_element] = { 
                    "key": num_element,
                    "counter":  1
                }     
        
        
        return threshold_leader["element"]
