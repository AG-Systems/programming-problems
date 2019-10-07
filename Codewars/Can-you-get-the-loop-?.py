def loop_size(node):
    if node is None: 
        return 0
    slow = node
    fast = node 
    flag = 0
    while(slow and slow.next and fast and
          fast.next and fast.next.next): 
        if slow == fast and flag != 0: 
            count = 1
            slow = slow.next
            while(slow != fast): 
                slow = slow.next
                count += 1
            return count 
          
        slow = slow.next
        fast = fast.next.next
        flag = 1
    return 0
    
