# #default args

# def net_price(list_price,discount = 0,tax = 0.05):
#     return list_price * (1 - discount) * ( 1 + tax)

# # print(net_price(500))
# # print(net_price(500,0.1))
# print(net_price(500,0.1,0))

import time

def count(end,start = 0):
    for x in range(start,end + 1):
        print(x)
        time.sleep(1)
    print("done")

count(10,5)

#postional args are before keyword agr and default args