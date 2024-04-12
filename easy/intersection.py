"""
Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must be unique and you may return the result in any order.
"""

def intersaction(num1,num2):
    unique1= set(num1)
    unique2 = set(num2).
    intersection = list(unique1.intersection(unique2))
    return intersection
print(intersaction([1,2,3],[2,34,243,4,2,1]))


#how can this be done withou aid of set 