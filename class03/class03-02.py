# pizza party planner
# ask user how many friends are coming
# if fewer: than 3, order a small pizza
# if betweem 3-6, order medium pizza
# if more than 6, order large pizza

friends = int(input(" How many friends are coming?"))
if friends <= 3: 
    print(" You should order a small pizza")
elif friends >= 3 and friends <= 6:
    print("You should order a medium pizza")
elif friends >= 6:
    print("You should order a large pizza")
else:
    print ("Go big")