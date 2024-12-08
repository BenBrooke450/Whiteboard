"""
Given an array nums of size n, return the
 majority element.
The majority element is the element that appears
 more than ⌊n / 2⌋ times. You may assume that the
 majority element always exists in the array.


Example 1:
Input: nums = [3,2,3]
Output: 3
Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2

"""


def highest(list1: list[int]):
    dic1 = {}
    for index, num in enumerate(list1):
        if num not in dic1.keys():
            dic1[num] = 1
        else:
            dic1[num] = dic1.get(num) + 1
    return max(dic1, key=dic1.get)


nums = [2, 2, 1, 1, 1, 1, 1, 2, 2]
print(highest(nums))

"""
We start with "if num not in dic1.keys():" this 
    provides us with a check so that key isn´t already in the dictionary

    Step two we have dic1[0] = 1, this builds the key and gives it the value of 1

    step three, when all elements have one key dic[#] then begin the count

    step four, we take the next number which is again 1, so... dic1[1] = dic1.get(1) + 1
            "Returns the value of the specified key"

    step five, so now we have dic1[1] = 2 and we continue.

"""