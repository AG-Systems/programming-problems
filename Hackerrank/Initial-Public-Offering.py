#
# Complete the 'getUnallottedUsers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY bids
#  2. INTEGER totalShares
#

def getUnallottedUsers(bids, totalShares):
    # Write your code here
    # <user id, num of shares, bidding price, timestamp >
    if bids == []:
        return None
    if totalShares == 0:
        return [i[0] for i in bids]
    sorted_bids = sorted(bids, key=lambda x : x[2] ,reverse=True)
    remaning_shares = totalShares

    num_of_same_price = {}
    for index, row in enumerate(sorted_bids):
        if row[2] in num_of_same_price:
            num_of_same_price[row[2]] = [num_of_same_price[row[2]][0] + 1, index]
        else:
            num_of_same_price[row[2]] = [1]
    left_out_users = []
    
    for index, bid_info in enumerate(sorted_bids):
        if remaning_shares > 0:
            if num_of_same_price[bid_info[2]][0] == 1: 
                if remaning_shares < bid_info[1]:
                    print(remaning_shares, bid_info)
                    left_out_users.append(bid_info[0])
                remaning_shares -= bid_info[1]
            else:
                sorted_timestamp = sorted(sorted_bids[index: num_of_same_price[bid_info[2]][1] + 1 ], key=lambda x : x[3])                
                queue = list(sorted_timestamp)
                if len(queue) < remaning_shares: # 1 or more users WONT get atleast one share
                    while remaning_shares > 0 or queue != []: 
                        bid = queue.pop(0)
                        if bid[1] > remaning_shares:
                            remaning_shares -= 1
                            bid[1] -= 1
                            if bid[1] > 0:
                                queue.append(bid)

                    if remaning_shares <= 0:
                        for user in queue:
                            left_out_users.append(user[0])
                else: # this means all of the users in the same bid price range WILL get all of their shares
                    while queue != []: 
                        bid = queue.pop(0)
                        if bid[1] > remaning_shares:
                            remaning_shares -= 1
                            bid[1] -= 1
                            if bid[1] > 0:
                                queue.append(bid)                    
                num_of_same_price[bid_info[2]][0] = 1
        else:
            left_out_users.append(bid_info[0]) # user id
    
    ordered_left_out_users = []
    for bid_info in bids:
        if bid_info[0] in left_out_users:
            ordered_left_out_users.append(bid_info[0])
        
    return ordered_left_out_users
        
    
