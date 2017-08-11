class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        container = []
        counter = 0 
        index = 0
        min_num = 99
        small_pair = [99,99]
        checker = False
        while counter < len(people):
            if people[counter][1] == len(container) and people[counter][0] <= min_num:
                index = counter
                min_num = people[counter][0]
                print "1st option:" + str(people[counter])
                checker = False
            else:
                if people[counter][1] <= small_pair[1]:
                    small_pair[1] = people[counter][1]
                    print "2nd option: " + str(people[counter])
                    if people[counter][0] <= small_pair[0] and checker:
                        if small_pair[0] > min_num and people[counter][0] > min_num:
                            print small_pair,min_num
                            small_pair[0] = people[counter][0]
                            index = counter
                            print "2nd option confirmed: " + str(people[counter])
            counter += 1
            if counter == len(people):
                if len(container) != len(people):
                    counter = 0 
                    checker = True
                    container.append(people[index])
                    people[index] = [999,999]
                    small_pair = [99,99]
                    index = 0
                else:
                    return container
            
                    
                    
        
