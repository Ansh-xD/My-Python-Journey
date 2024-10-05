friends = ["Apple","Oragne","5","345.06",False,"Akash","Rohan"]
print(friends)

friends.append("Ansh")
print(friends)
                                                        #• l1.sort(): updates the list to [1,2,7,8,15,21]
                                                        # • l1.reverse(): updates the list to [15,21,2,7,8,1]
                                                        # • l1.append(8): adds 8 at the end of the list
                                                        # • l1.insert(3,8): This will add 8 at 3 index
                                                        # • l1.pop(2): Will delete element at index 2 and return its value.
                                                        # • l1.remove(21): Will remove 21 from the list. 
#

l1 = ["1","3","5","2","6"]
# l1.sort()
# l1.reverse()
# l1.insert(3, 69)   #its means insert 69 after 3 index
# l1.pop(3)            # its means they remove 3rd index
# value = l1.pop(3)
# print(value)
l1.remove(2)
print(l1)