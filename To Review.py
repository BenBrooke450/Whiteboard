


#############################################################
#
#############################################################
"""
You are given a string allowed consisting of
 distinct characters and an array of strings words.
  A string is consistent if all characters in the string appear in the string allowed.

Return the number of consistent strings in the array words.



Example 1:
Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
Output: 2
Explanation: Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.


Example 2:
Input: allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]
Output: 7
Explanation: All strings are consistent.


Example 3:
Input: allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]
Output: 4
Explanation: Strings "cc", "acd", "ac", and "d" are consistent.

"""



def word_find( list1:list[str], string: str):

    x = len(list1)
    for words in list1:
        for c in words:
            if c not in string:
                x = x - 1
                break
    return x



print(word_find(["cc","acd","b","ba","bac","bad","ac","d"], "cad"))



print("a" not in "bc")

















#############################################################
#
#############################################################



def selfDividingNumbers(self, left: int, right: int) -> list[int]:

        list2 = []

        number = [[str(x) for x in str(numbers)] for numbers in range(left, right+1) if numbers % 10 != 0 and "0" not in str(numbers)]

        a = list(filter(lambda nums: all(map(lambda y : int("".join(nums)) % int(y) == 0 ,(y for y in nums))) ,(nums for nums in number)))

        b = list(map(lambda x: int("".join(x)),a))

        return b

















#############################################################
#            482. License Key Formatting
#############################################################

"""

You are given a license key represented as
a string s that consists of only alphanumeric
characters and dashes. The string is separated
into n + 1 groups by n dashes. You are also
given an integer k.

We want to reformat the string s such that
each group contains exactly k characters,
except for the first group, which could be
shorter than k but still must contain at least
 one character. Furthermore, there must be a
 dash inserted between two groups, and you
 should convert all lowercase letters to uppercase.

Return the reformatted license key.



Example 1:

Input: s = "5F3Z-2e-9-w", k = 4
Output: "5F3Z-2E9W"
Explanation: The string s has been split
into two parts, each part has 4 characters.
Note that the two extra dashes are not
needed and can be removed.




Example 2:

Input: s = "2-5g-3-J", k = 2
Output: "2-5G-3J"
Explanation: The string s has been split into three parts, each part has 2 characters except the first part as it could be shorter as mentioned above.


"""


def reformant(string: str, k: int):
    upper_joined_string = list(string.upper().replace("-",""))
    ujr = upper_joined_string[::-1]
    for index,letters in enumerate(ujr):
        if (index +1 ) % k == 0 and len(ujr) != (index +1):
            ujr[index] = "-" + letters
    return "".join(ujr[::-1])


"""
What's going on. First we look at the first line, we use upper() and replace() to make all letters capital and
            replace all elements of "-" to a None space soo.. "2e-9-w" to "2E9W".
            
            On the second line we flip the whole line from "2E9W" to "W9E2".
            
            We then iterate through each letter 


"""




print(reformant("5F3ZT-2e-9-w", 4))
#5-F3ZT-2E9W


###################################################

def reformant(string :str, k : int):

    upper_string = string.upper()
    i = 0
    list1 = []
    for digits in upper_string:
        if digits != "-":
            i = i + 1
        elif digits == "-":
            list1.append(i)
            i = 0


    return list1


print(reformant("5F3Z-2e-9-w",4))
#[4, 2, 1]


















#############################################################
#                459. Repeated Substring Pattern
#############################################################



"""
Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.



Example 1:

Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.
Example 2:

Input: s = "aba"
Output: false
Example 3:

Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or the substring "abcabc" twice.


"""

def func(string:str):

    length = len(string)

    for x in range(1,length):

        if length % x == 0:

            substring = string[: x]

            repeated_substring = substring * ( length // x )

            if repeated_substring == string:
                return True

    return False



func("abcabcabcabc")



















#############################################################
#                496. Next Greater Element I
#############################################################


"""

The next greater element of some element x
 in an array is the first greater element
 that is to the right of x in the same array.

You are given two distinct 0-indexed integer
arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the
index j such that nums1[i] == nums2[j] and
 determine the next greater element of
 nums2[j] in nums2. If there is no next
 greater element, then the answer for this query is -1.

Return an array ans of length nums1.length
 such that ans[i] is the next greater element as described above.



Example 1:

Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
Example 2:

Input: nums1 = [2,4], nums2 = [1,2,3,4]
Output: [3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
- 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.


"""

def func(nums1: list[int], nums2: list[int]):

    list3 = []


    i=0

    for x in nums1:

        found_greater = False

        the_index_x = nums2.index(x)

        for y in nums2[the_index_x:]:

            if y > x:

                list3.append(y)

                found_greater = True

                break

        if found_greater is False:
            list3.append(-1)

    return list3


print(func([4,1,2], [1,3,4,2]))



















#############################################################
#                500. Keyboard Row
#############################################################


"""
Given an array of strings words, return the words
 that can be typed using letters of the alphabet
  on only one row of American keyboard like the image below.
Note that the strings are case-insensitive,
both lowercased and uppercased of the same
letter are treated as if they are at the same row.
In the American keyboard:
the first row consists of the characters "qwertyuiop",
the second row consists of the characters "asdfghjkl", and
the third row consists of the characters "zxcvbnm".


Example 1:
Input: words = ["Hello","Alaska","Dad","Peace"]
Output: ["Alaska","Dad"]
Explanation:
Both "a" and "A" are in the 2nd row of the American keyboard due to case insensitivity.
Example 2:
Input: words = ["omk"]
Output: []
Example 3:
Input: words = ["adsdf","sfd"]
Output: ["adsdf","sfd"
"""


def keyboard(list1 : list[str]):
    top = set([x for x in"qwertyuiop"])
    middle = set([x for x in "asdfghjkl"])
    bottom = set([x for x in "zxcvbnm"])
    list3 = []
    for words in list1:
        if set([x.lower() for x in words]) <= top:
            list3.append(words)
        elif set([x.lower() for x in words]) <= middle:
            list3.append(words)
        elif set([x.lower() for x in words]).issubset(bottom) is True:
            list3.append(words)
    return list3



print(keyboard(["Hello","Alaska","Dad","Peace"]))

#['Alaska', 'Dad']














#############################################################
#                506. Relative Ranks
#############################################################

"""
You are given an integer array score of size n, where score[i] is the score of the ith athlete in a competition. All the scores are guaranteed to be unique.
The athletes are placed based on their scores, where the 1st place athlete has the highest score, the 2nd place athlete has the 2nd highest score, and so on. The placement of each athlete determines their rank:
The 1st place athlete's rank is "Gold Medal".
The 2nd place athlete's rank is "Silver Medal".
The 3rd place athlete's rank is "Bronze Medal".
For the 4th place to the nth place athlete, their rank is their placement number (i.e., the xth place athlete's rank is "x").
Return an array answer of size n where answer[i] is the rank of the ith athlete.


Example 1:
Input: score = [5,4,3,2,1]
Output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
Explanation: The placements are [1st, 2nd, 3rd, 4th, 5th].
Example 2:
Input: score = [10,3,8,9,4]
Output: ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
Explanation: The placements are [1st, 5th, 3rd, 2nd, 4th].
"""

def findRelativeRanks(list1: list[int]):
    list2 = [0 for _ in range(len(list1))]
    i = 1
    for numbers in list1:
        max_value = max(list1)
        index_max = list1.index(max_value)
        list2[index_max] = str(i)
        list1[index_max] = -1
        i = i + 1
        if list2[index_max] == "1":
            list2[index_max] = "Gold Medal"
        elif list2[index_max] == "2":
            list2[index_max] = "Silver Medal"
        elif list2[index_max] == "3":
            list2[index_max] = "Bronze Medal"
    return list2

print(findRelativeRanks([5,4,3,2,1]))
#['Gold Medal', 'Silver Medal', 'Bronze Medal', '4', '5']

print(findRelativeRanks([10,3,8,9,4]))
#['Gold Medal', '5', 'Bronze Medal', 'Silver Medal', '4']







#################################################


def func(list1:list[int]):
    for index, numbers in enumerate(sorted(list1,reverse=True)):
        if index == 0:
            list1[index] = "Gold Medal"
        elif index == 1:
            list1[index] = "Bronze Medal"
        elif index == 2:
            list1[index] = "Silver Medal"
        else:
            list1[index] = index + 1
    return list1

print(func([5,4,3,2,1]))
#['Gold Medal', 'Bronze Medal', 'Silver Medal', 4, 5]


print(func([10,3,8,9,4]))
#['Gold Medal', 'Bronze Medal', 'Silver Medal', 4, 5]

















#####################################################################################
#                599. Minimum Index Sum of Two Lists
#####################################################################################



"""
Given two arrays of strings list1 and list2,
 find the common strings with the least index sum.

A common string is a string that appeared in both list1 and list2.

A common string with the least index sum
is a common string such that if it
appeared at list1[i] and list2[j]
then i + j should be the minimum
value among all the other common strings.

Return all the common strings
with the least index sum. Return the answer in any order.



Example 1:

Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"],
        list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]

Output: ["Shogun"]
Explanation: The only common string is "Shogun".
Example 2:

Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Shogun","Burger King"]
Output: ["Shogun"]
Explanation: The common string with the least index sum is "Shogun" with index sum = (0 + 1) = 1.
Example 3:

Input: list1 = ["happy","sad","good"], list2 = ["sad","happy","good"]
Output: ["sad","happy"]
Explanation: There are three common strings:
"happy" with index sum = (0 + 1) = 1.
"sad" with index sum = (1 + 0) = 1.
"good" with index sum = (2 + 2) = 4.
The strings with the least index sum are "sad" and "happy".

"""



def name(nums1:list[str],nums2:list[str]):

    dic1 = {}

    for index, words in enumerate(nums1):

        if words in nums2:

            index_two = nums2.index(words)

            if (index + index_two) in dic1:

                dic1[index + index_two] = dic1.get(index + index_two) + ',' + words

            else:
                dic1[index + index_two] = words

    return (dic1.get(min(dic1.keys()))).split(",")


print(name(["happy","sad","good"], ["sad","happy","good"]))
#['happy', 'sad']














#####################################################################################
#                         605. Can Place Flowers
#####################################################################################



"""


You have a long flowerbed in which some of the plots
are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's,
where 0 means empty and 1 means not empty, and an integer n,
 return true if n new flowers can be planted in the flowerbed
  without violating the no-adjacent-flowers rule and false otherwise.



Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true


Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: false


"""


def canPlaceFlowers(flowerbed: list[int], k: int):

    n = 0

    if len(flowerbed) == 1 and flowerbed[0] == 0:
        return True

    for index, nums in enumerate(flowerbed[:-1]):
        if nums == 0 and index < 1:
            if flowerbed[index + 1] == 0 and index < 1:
                flowerbed[index] = 1
                n = n + 1

        elif nums == 0 and index != len(flowerbed) - 2:
            if flowerbed[index + 1] == 0 and flowerbed[index - 1] == 0:
                flowerbed[index] = 1
                n = n + 1

        elif flowerbed[len(flowerbed) - 2] == 0:
            if flowerbed[len(flowerbed) - 1] == 0:
                flowerbed[(len(flowerbed) - 1)] = 1
                n = n + 1

    if k <= n:
        return True
    else:
        return False


print(canPlaceFlowers([0,0,0,0,0],3))
#True


print(canPlaceFlowers([0,0,0],2))
#True












#####################################################################################
#                         682. Baseball Game
#####################################################################################


"""

You are keeping the scores for a baseball game with strange rules.
 At the beginning of the game, you start with an empty record.

You are given a list of strings operations, where operations[i] is
 the ith operation you must apply to the record and is one of the following:

An integer x.
Record a new score of x.

'+'.
Record a new score that is the sum of the previous two scores.

'D'.
Record a new score that is the double of the previous score.

'C'.
Invalidate the previous score, removing it from the record.

Return the sum of all the scores on the record after applying all the operations.

The test cases are generated such that the answer and all intermediate calculations fit in a 32-bit integer and that all operations are valid.



Example 1:

Input: ops = ["5","2","C","D","+"]
Output: 30
Explanation:
"5" - Add 5 to the record, record is now [5].
"2" - Add 2 to the record, record is now [5, 2].
"C" - Invalidate and remove the previous score, record is now [5].
"D" - Add 2 * 5 = 10 to the record, record is now [5, 10].
"+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15].
The total sum is 5 + 10 + 15 = 30.



Example 2:

Input: ops = ["5","-2","4","C","D","9","+","+"]
Output: 27
Explanation:
"5" - Add 5 to the record, record is now [5].
"-2" - Add -2 to the record, record is now [5, -2].
"4" - Add 4 to the record, record is now [5, -2, 4].
"C" - Invalidate and remove the previous score, record is now [5, -2].
"D" - Add 2 * -2 = -4 to the record, record is now [5, -2, -4].
"9" - Add 9 to the record, record is now [5, -2, -4, 9].
"+" - Add -4 + 9 = 5 to the record, record is now [5, -2, -4, 9, 5].
"+" - Add 9 + 5 = 14 to the record, record is now [5, -2, -4, 9, 5, 14].
The total sum is 5 + -2 + -4 + 9 + 5 + 14 = 27.



Example 3:

Input: ops = ["1","C"]
Output: 0
Explanation:
"1" - Add 1 to the record, record is now [1].
"C" - Invalidate and remove the previous score, record is now [].
Since the record is empty, the total sum is 0.


"""

def game(list1:list[int]):

    list3 = []
    n = 0
    m = 0

    while n < len(list1):

        if list1[n] != "C" and list1[n] != "D" and list1[n] != "+":
            list3.append(int(list1[n]))
            n = n + 1
            m = m + 1

        elif list1[n] == "C":
            list3.pop(-1)
            n = n + 1
            m = m - 1

        elif list1[n] == "D":
            list3.append((int(list3[m-1]))*2)
            n = n + 1
            m = m + 1

        elif list1[n] == "+":
            list3.append(int(list3[m - 1]) + int(list3[m - 2]))
            n = n + 1
            m = m + 1

    return sum(list3)



print(game(["5","-2","4","C","D","9","+","+"]))






















#####################################################################################
#                         2974. Minimum Number Game
#####################################################################################




"""
You are given a 0-indexed integer array nums of even length
 and there is also an empty array arr. Alice and Bob decided
  to play a game where in every round Alice and Bob will do one
   move. The rules of the game are as follows:

Every round, first Alice will remove the minimum element from nums, and then Bob does the same.
Now, first Bob will append the removed element in the array arr, and then Alice does the same.
The game continues until nums becomes empty.
Return the resulting array arr.



Example 1:
Input: nums = [5,4,2,3]
Output: [3,2,5,4]
Explanation: In round one, first Alice removes 2 and
then Bob removes 3. Then in arr firstly Bob appends 3 and then Alice appends 2. So arr = [3,2].

At the begining of round two, nums = [5,4].
Now, first Alice removes 4 and then Bob removes 5. Then both append in arr which becomes [3,2,5,4].


Example 2:
Input: nums = [2,5]
Output: [5,2]
Explanation: In round one, first Alice removes 2 and then Bob removes 5.
 Then in arr firstly Bob appends and then Alice appends. So arr = [5,2].
"""



def number(list1:list[int]):

    list3 = []

    n = 0

    sorted_list = sorted(list1)

    for nums in range(len(list1)//2):

        double = sorted_list[n:n+2]

        list3.extend(double[::-1])

        n = n + 2

    return list3



print(number([5,4,2,3]))




#####################################################




def number(list1: list[int]):
    list3 = []

    sorted_list = sorted(list1)

    for a, b in zip(sorted_list, sorted_list[1:]):
        list3.extend([b, a])

    return list3


print(number([5, 4, 2, 3]))

































#####################################################################################
#                         1528. Shuffle String
#####################################################################################


"""
You are given a string s and an integer array indices of the same length.
The string s will be shuffled such that the character at the ith position
 moves to indices[i] in the shuffled string.

Example 1:
Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
Output: "leetcode"
Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.


Example 2:
Input: s = "abc", indices = [0,1,2]
Output: "abc"
Explanation: After shuffling, each character remains in its position.



"""

def func(string:str , indices:list[int]):

    abc = dict(zip(indices,[x for x in string]))
    return "".join([value for key,value in sorted(abc.items())])





print(func("codeleet", [4,5,6,7,0,2,1,3]))
#leetcode


































#####################################################################################
#           2535. Difference Between Element Sum and Digit Sum of an Array
#####################################################################################



"""

You are given a positive integer array nums.

The element sum is the sum of all the elements in nums.
The digit sum is the sum of all the digits (not necessarily distinct) that appear in nums.
Return the absolute difference between the element sum and digit sum of nums.

Note that the absolute difference between two integers x and y is defined as |x - y|.



Example 1:

Input: nums = [1,15,6,3]
Output: 9
Explanation:
The element sum of nums is 1 + 15 + 6 + 3 = 25.
The digit sum of nums is 1 + 1 + 5 + 6 + 3 = 16.
The absolute difference between the element sum and digit sum is |25 - 16| = 9.


Example 2:

Input: nums = [1,2,3,4]
Output: 0
Explanation:
The element sum of nums is 1 + 2 + 3 + 4 = 10.
The digit sum of nums is 1 + 2 + 3 + 4 = 10.
The absolute difference between the element sum and digit sum is |10 - 10| = 0.

"""


def func(list1:list[int]):

    split_numbers = [int(num2) for nums in list1 for num2 in str(nums)]
    return abs(sum(split_numbers) - sum(list1))

print(func([1,2,3,4]))
#66









































#####################################################################################
#                   1588. Sum of All Odd Length Subarrays
#####################################################################################


"""
Given an array of positive integers arr, return the sum of all possible odd-length subarrays of arr.

A subarray is a contiguous subsequence of the array.



Example 1:

Input: arr = [1,4,2,5,3]
Output: 58
Explanation: The odd-length subarrays of arr and their sums are:
[1] = 1
[4] = 4
[2] = 2
[5] = 5
[3] = 3
[1,4,2] = 7
[4,2,5] = 11
[2,5,3] = 10
[1,4,2,5,3] = 15
If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58


Example 2:

Input: arr = [1,2]
Output: 3
Explanation: There are only 2 subarrays of odd length, [1] and [2]. Their sum is 3.


Example 3:

Input: arr = [10,11,12]
Output: 66



"""


def func(list1:list[int]):

    list2 = [x for x in range(0,len(list1)+1) if x % 2 != 0]

    list3 = []
    list4 = []

    for nums in list2[::-1]:

        n = 0

        for nums2 in list1:

            if len(list1[n:n + nums]) == nums:

                x = sum(list1[n:n + nums])

                list3.append(x)

                n = n + 1

        list4.append(sum(x for x in list3))

        list3 = []


    return sum(list4)




print(func([1,4,2,5,3]))

























#####################################################################################
#                   2864. Maximum Odd Binary Number
#####################################################################################



"""

You are given a binary string s that contains at least one '1'.

You have to rearrange the bits in such a way that the resulting binary number is the maximum odd binary number that can be created from this combination.

Return a string representing the maximum odd binary number that can be created from the given combination.

Note that the resulting string can have leading zeros.



Example 1:

Input: s = "010"
Output: "001"
Explanation: Because there is just one '1', it must be in the last position. So the answer is "001".
Example 2:

Input: s = "0101"
Output: "1001"
Explanation: One of the '1's must be in the last position.
    The maximum number that can be made with the remaining digits is "100". So the answer is "1001".

"""



def func_bin(string:str):

    n = string.count("1")

    return ((n - 1)*"1") + (len(string) - n)*"0" + "1"

print(func_bin("0101"))
#1001































#####################################################################################
#                   2053. Kth Distinct String in an Array
#####################################################################################





"""

A distinct string is a string that is present only once in an array.

Given an array of strings arr, and an integer k, return the kth
    distinct string present in arr. If there are fewer than k distinct strings, return an empty string "".

Note that the strings are considered in the order in which they appear in the array.



Example 1:

Input: arr = ["d","b","c","b","c","a"], k = 2
Output: "a"
Explanation:
The only distinct strings in arr are "d" and "a".
"d" appears 1st, so it is the 1st distinct string.
"a" appears 2nd, so it is the 2nd distinct string.
Since k == 2, "a" is returned.
Example 2:

Input: arr = ["aaa","aa","a"], k = 1
Output: "aaa"
Explanation:
All strings in arr are distinct, so the 1st string "aaa" is returned.
Example 3:

Input: arr = ["a","b","a"], k = 3
Output: ""
Explanation:
The only distinct string is "b". Since there are fewer than 3 distinct strings, we return an empty string "".
"""
from bokeh.colors.named import fuchsia


def func(list1:list[str], k :str):

    dict1 = dict()

    for l in list1:

        if l in dict1.keys():

            dict1[l] = dict1.get(l) + 1

        else:
            dict1[l] = 1

    new_list = [x for x,y in dict1.items() if y == 1]

    if k > len(new_list):
            return '""'
    else:
        return new_list[k - 1]



print(func(["meio","l","xhb","p","psuzr","hrp","bhqxm","ccqrl","d","nix","ce","bkm","jvqh","c","mpah","uh","z","hin","ekaxo","cpcy","cmvj","glnrk","uqem","vq","tw","p","tqlrv","uxf","kzxf","tjd","arm","iqfc","fmze","txq","ij","rlqv","j","up","om","hdvku","tkp","hm","vdbdd","lbmc","bpx","mqy","ddecp","zmdg","ik","msy","pzohq","fuj","s","bbb","qhy","nbz","xbhvi","dh","w","nznd","lvl","nru","y","q","jciw","lmnmm","e","lvnrk","eoi","fp","neq","wuw","qsjga","fy","qvg","dqjd","rb","ck","uhall","qcly","q","igv","uq","ijjqt","er","yxx","wyx","jlasw","aln","ohy","vf","gpzy","mywlj","xf","cgwl","wyjli","pyow","i","upic","mpze","ol","z","mxwb","iouzk","zfx","f","y","gsvv","hi","x","qgj","zvnz","vb","yyl","m","uwyhh","qgd","qcbky","h","wqiyo","ey","uqjn","ma","h","phnc","ozptm","rwk","w","yfw","lkfbb","hvaq","hh","arhm","rz","gtvi","tgpyt","np","e","z","cmodm","jhhga","yal","unhsp","acg","yn","d","vndjs","ntrj","rmixt","fh","xjs","oib","mk","p","rrhep","zdk","dyy","eox","hrtr","n","ty","nj","o","s","ewt","dyvn","hrejt","vkzj","y","swzzb","dnelj","ow","pv","c","muc","unvy","vnbk","nkwte","ef","bminn","zjgcy","u","g","fwks","cjtv","ximu","oiwp","h","h","zpbm","w","h","h","vqbq","mg","xopv","m","zceki","rn","abiwc","bid","gjvsu","pv","i","cemf","x","jrxa","ye","vovg","uhlp","enpj","oyr","mgrvo","jk","kuqe","q","k","v","gzo","zcx","ylj","kmt","x","byudz","eh","lonmh","iqnx","apzod","vif","f","bq","ik","utjnj","bx","c","oyf","kqp","zc","oxpi","t","pagk","yrup","xly","o","ipndf","qy","rqfnp","c","abnh","gm","yvzh","jro","gjxq","ir","oicxq","yplnw","rxji","cdwr","nmnv","qeiht","bu","gg","jlg","ajvqg","bumzg","lpuf","lzypp","fpxj","uwyqf","c","e","flubx","cb","se","mfw","wmerw","xun","xq","hkuiw","z","ffop","qvc","xl","yp","v","lv","ij","au","m","yjlxq","oqfne","ave","oqc","qlly","zf","pa","h","pfr","vhee","gh","lswh","si","p","nwzeb","cy","fbddc","xkvqd","smhl","t","gdlvc","umj","xujwi","sqjvz","m","bkvv","tdkg","nbk","m","wvvc","d","mlpn","zi","wemrh","qv","xww","gzq","qa","nqcp","hat","jqdg","bjz","pozj","ehv","bqct","pihs","yodi","yaxhs","if","xlw","ums","v","pa","accg","wcfdf","t","j","tlijm","twibw","q","gq","w","cyrop","von","crdtn","tjt","sldvo","ykyg","wi","uej","zmqda","b","rbim","r","r","cknvt","drmac","mnxm","bsgw","c","vwyil","hblbj","ddzr","ixe","s","yd","dx","bj","fxtmw","mbxvz","kwut","cpnt","ctr","r","a","bmxg","ecr","guofg","c","eczhh","sunz","ic","d","nu","xtle","w","ckb","fnelp","z","kpdw","pe","lz","me","vbc","sk","n","gp","fud","qphr","bbius","jyqa","anhge","tuqse","d","fi","wmrn","heds","djyrj","vv","e","cf","gylm","mdswr","jxyc","stn","uo","hyjt","nl","wcay","oee","ng","dwaii","d","kkxpi","jxir","wsv","lkz","tyf","fenfb","xfzi","o","yf","xq","etvcv","c","ajv","qm","hbfy","krzac","nd","oymuu","fsok","sblyv","fgubg","bxy","clex","cbny","y","kfgi","e","lpjd","wuq","um","trv","mkgb","dtdcj","xuetk","cj","hhzl","jcni","wk","jtrcp","jbkju","hwrr","tlbw","xypv","qmsbe","gkzm","lmwz","gwyw","yuq","uz","cq","jatsr","jpd","xw","ebfoa","kbr","zvtl","bhqhj","en","jvj","ua","pth","joral","pw","wlw","vvddv","pnx","v","u","fy","drdf","m","xepi","e","rtk","byqvc","ewu","k","d","nef","lihc","puvu","hdi","ymcnd","vwo","dripr","jloqq","jyy","b","fbzn","fth","ptzw","u","rcjjy","udm","rb","nky","txz","w","wkx","kp","ay","ots","adkr","u","tmh","ayqc","cs","ulzbt","tnz","rha","he","ly","fhanm","julf","vwpap","m","fzlx","tc","sohc","x","u","hwdgu","tdlcd","dhlq","tvs","ftam","fyjg","kq","qlww","gbn","bw","tqx","kcfmg","lahfo","ipst","pyddr","ua","ilhj","fdor","ch","lp","gcduz","trjo","kuz","rizf","xmzg","pyykm","idr","adog","i","lrot","vu","r","phbq","sbvpo","x","tb","hh","xzco","xbx","z","ccgr","xdo","qb","mf","lcib","rsir","zgyxt","zpvai","yi","clyuu","nix","h","lndqw","odz","rkjnh","bl","hhuwe","eqnmj","yt","zb","dhm","mdxow","sdhd","ugybz","caf","jfjxw","ztuoz","mxoz","e","tdo","zp","yc","tg","rtki","z","icppp","ficph","oq","jmxj","nor","dlhp","iaca","qin","qghtw","n","mrjtx","bx","fmyfr","pp"], k = 374))
#jtrcp

print(func(["a","b","a"], k = 3))
#""









































#####################################################################################
#          2913. Subarrays Distinct Element Sum of Squares I
#####################################################################################




"""

You are given a 0-indexed integer array nums.

The distinct count of a subarray of nums is defined as:

Let nums[i..j] be a subarray of nums consisting of all the indices from i
    to j such that 0 <= i <= j < nums.length. Then the number of distinct values
    in nums[i..j] is called the distinct count of nums[i..j].

Return the sum of the squares of distinct counts of all subarrays of nums.

A subarray is a contiguous non-empty sequence of elements within an array.



Example 1:

Input: nums = [1,2,1]
Output: 15
Explanation: Six possible subarrays are:
[1]: 1 distinct value
[2]: 1 distinct value
[1]: 1 distinct value
[1,2]: 2 distinct values
[2,1]: 2 distinct values
[1,2,1]: 2 distinct values
The sum of the squares of the distinct counts in all subarrays is equal to 1 + 1 + 1 + 2 + 2 + 2 = 15.
Example 2:

Input: nums = [1,1]
Output: 3
Explanation: Three possible subarrays are:
[1]: 1 distinct value
[1]: 1 distinct value
[1,1]: 1 distinct value
The sum of the squares of the distinct counts in all subarrays is equal to 1 + 1 + 1 = 3.


"""



def unqieu(list1 : list[int]):

    list2 = []

    n = 1
    j = 0

    for x in list1:

        for m in range(len(list1)-j):

            x = list1[m:m+n]

            list2.append(len(set(x)))

        j = j + 1
        n = n + 1

    return sum((x)**2 for x in list2)

print(unqieu([1,2,1]))
#15




























#####################################################################################
#          1844. Replace All Digits with Characters
#####################################################################################




"""

You are given a 0-indexed string s that has lowercase English letters in its even indices and digits in its odd indices.

You must perform an operation shift(c, x), where c is a character and x is a digit, that returns the xth character after c.

For example, shift('a', 5) = 'f' and shift('x', 0) = 'x'.
For every odd index i, you want to replace the digit s[i] with the result of the shift(s[i-1], s[i]) operation.

Return s after replacing all digits. It is guaranteed that shift(s[i-1], s[i]) will never exceed 'z'.

Note that shift(c, x) is not a preloaded function, but an operation to be implemented as part of the solution.



Example 1:

Input: s = "a1c1e1"
Output: "abcdef"
Explanation: The digits are replaced as follows:
- s[1] -> shift('a',1) = 'b'
- s[3] -> shift('c',1) = 'd'
- s[5] -> shift('e',1) = 'f'
Example 2:

Input: s = "a1b2c3d4e"
Output: "abbdcfdhe"
Explanation: The digits are replaced as follows:
- s[1] -> shift('a',1) = 'b'
- s[3] -> shift('b',2) = 'd'
- s[5] -> shift('c',3) = 'f'
- s[7] -> shift('d',4) = 'h'

"""

x = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
     'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

y = range(1,len(x))

dict1 = dict()

for x,y in zip(x,y):
    dict1[y] = x





def lib(s:str):

    library = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h'
    , 9: 'i', 10: 'j', 11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o'
    , 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v'
    , 23: 'w', 24: 'x', 25: 'y',26:'z'}

    f = [x for x in s]
    s = [x for x in s]


    n = 2
    for x in s:
        for key,value in library.items():
            if value == x and n != len(s) + 1:
                q = int(s[n-1]) + key
                f[n-1] = library.get(q)
                n = n + 2

    print(f)

    return "".join(f)


print(lib("c4k9v1q9r0g"))
#cgktvwqzrrg

#####################################################









def lib(s:str):

    library = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5,
               'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
               'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15,
               'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20,
               'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25}

    list2 = []

    s = [x for x in s]
    n = 2

    for x in s:
        z = library.get(x)
        if z == None:
            continue
        else:
            q = int(s[n-1]) + z
            s[n-1] = q
        n = n + 2

    return s




#####################################################################################
#          1534. Count Good Triplets
#####################################################################################




"""
Given an array of integers arr, and three integers a, b and c.
    You need to find the number of good triplets.

A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are true:

0 <= i < j < k < arr.length
|arr[i] - arr[j]| <= a
|arr[j] - arr[k]| <= b
|arr[i] - arr[k]| <= c
Where |x| denotes the absolute value of x.

Return the number of good triplets.



Example 1:
Input: arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3
Output: 4
Explanation: There are 4 good triplets: [(3,0,1), (3,0,1), (3,1,1), (0,1,1)].


Example 2:
Input: arr = [1,1,2,2,3], a = 0, b = 0, c = 1
Output: 0
Explanation: No triplet satisfies all conditions.

"""
def func(arr: list[int], a: int, b: int, c: int):

    f = 0
    n = 0
    m = 0
    j = 0

    for x in arr:

        if f == len(arr) - 2:
            break

        else:
            f = f + 1
            n = 0

        for y in arr[f + n:]:
            n = n + 1
            m = 0

            for z in arr[f + n + m:]:
                m = m + 1

                print(x,y,z)

                if ((abs(x - y) <= a) and (abs(y - z) <= b) and (abs(x - z) <= c)):
                    print("PASSED: ",x,y,z)
                    j = j + 1
    return j

print(func(arr = [5,5,2,6,4], a = 5, b = 4, c = 5))
#10




























#####################################################################################
#          2103. Rings and Rods
#####################################################################################

"""
There are n rings and each ring is either red, green, or blue.
    The rings are distributed across ten rods labeled from 0 to 9.

You are given a string rings of length 2n that describes the n
    rings that are placed onto the rods. Every two characters in
     rings forms a color-position pair that is used to describe each ring where:

The first character of the ith pair denotes the ith ring's color ('R', 'G', 'B').
The second character of the ith pair denotes the rod that the ith ring is placed on ('0' to '9').
For example, "R3G2B1" describes n == 3 rings: a red
    ring placed onto the rod labeled 3, a green ring placed onto
     the rod labeled 2, and a blue ring placed onto the rod labeled 1.

Return the number of rods that have all three colors of rings on them.



Example 1:
Input: rings = "B0B6G0R6R0R6G9"
Output: 1
Explanation:
- The rod labeled 0 holds 3 rings with all colors: red, green, and blue.
- The rod labeled 6 holds 3 rings, but it only has red and blue.
- The rod labeled 9 holds only a green ring.
Thus, the number of rods with all three colors is 1.


Example 2:
Input: rings = "B0R0G0R9R0B0G0"
Output: 1
Explanation:
- The rod labeled 0 holds 6 rings with all colors: red, green, and blue.
- The rod labeled 9 holds only a red ring.
Thus, the number of rods with all three colors is 1.


Example 3:
Input: rings = "G4"
Output: 0
Explanation:
Only one ring is given. Thus, no rods have all three colors.


"""

def loop(rings: str):

    list_rings = list([y,x] for x,y in zip(rings[::2],rings[1::2]))
    dict1 = dict()

    for x in list_rings:
        if x[0] not in dict1.keys():
            dict1[x[0]] = x[1]
        else:
            dict1[x[0]] = x[1] + dict1.get(x[0])

    return sum(1 for x,y in dict1.items() if "R" in y and "G" in y and "B" in y)

print(loop("B0B6G0R6R0R6G9"))



##################################################################



def loop(rings: str):

    list_rings = list([y,x] for x,y in zip(rings[::2],rings[1::2]))
    dict1 = dict()

    for x in list_rings:
        if x[0] not in dict1.keys():
            dict1[x[0]] = x[1]
        else:
            dict1[x[0]] = x[1] + dict1.get(x[0])
    return dict1



print(loop("B0B6G0R6R0R6G9"))
#{'0': 'RGB', '6': 'RRB', '9': 'G'}






















#####################################################################################
#          1309. Decrypt String from Alphabet to Integer Mapping
#####################################################################################





"""

You are given a string s formed by digits and '#'. We want to map s to English lowercase characters as follows:

Characters ('a' to 'i') are represented by ('1' to '9') respectively.
Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.
Return the string formed after mapping.

The test cases are generated so that a unique mapping will always exist.



Example 1:

Input: s = "10#11#12"
Output: "jkab"
Explanation: "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".

Example 2:
Input: s = "1326#"
Output: "acz"

"""

import re


def freqAlphabets(s: str):
    V = {'1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e', '6': 'f',
         '7': 'g', '8': 'h', '9': 'i', '10': 'j', '11': 'k',
         '12': 'l', '13': 'm', '14': 'n', '15': 'o', '16': 'p',
         '17': 'q', '18': 'r', '19': 's', '20': 't', '21': 'u',
         '22': 'v', '23': 'w', '24': 'x', '25': 'y', '26': 'z'}

    string = ''
    n = -1

    while abs(n + 1) < len(s):
        if s[n] != "#":
            string = string + V.get(s[n])
            n = n - 1

        else:
            string = string + V.get(s[n - 2:n])
            n = n - 3
    return string[::-1]


print(freqAlphabets("10#11#12"))
# jkab

print(freqAlphabets("1326#"))
# acz


t = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10#',
     '11#', '12#', '13#', '14#', '15#', '16#', '17#',
     '18#', '19#', '20#', '21#', '22#', '23#', '24#', '25#', '26#']

q = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
     'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

V = {'1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e', '6': 'f',
     '7': 'g', '8': 'h', '9': 'i', '10#': 'j', '11#': 'k',
     '12#': 'l', '13#': 'm', '14#': 'n', '15#': 'o', '16#': 'p',
     '17#': 'q', '18#': 'r', '19#': 's', '20#': 't', '21#': 'u',
     '22#': 'v', '23#': 'w', '24#': 'x', '25#': 'y', '26#': 'z'}












#####################################################################################
#          1380. Lucky Numbers in a Matrix
#####################################################################################



"""
Given an m x n matrix of distinct numbers,
    return all lucky numbers in the matrix in any order.

A lucky number is an element of the matrix such
    that it is the minimum element in its
    row and maximum in its column.



Example 1:
Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
Output: [15]
Explanation: 15 is the only lucky number since
    it is the minimum in its row and the maximum in its column.

Example 2:
Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
Output: [12]
Explanation: 12 is the only lucky number
    since it is the minimum in its
     row and the maximum in its column.


Example 3:
Input: matrix = [[7,8],[1,2]]
Output: [7]
Explanation: 7 is the only lucky
    number since it is the minimum
    in its row and the maximum in its column.

"""
import numpy as np


def luckyNumbers(matrix: list[list[int]]):

    matrix_np = np.array(matrix)
    list1 = []
    n = 0
    for row in matrix:
        min_row = min(row)
        n = row.index(min_row)
        if  all(min_row >= x for x in matrix_np[:,n]):
            list1.append(min_row)

    return list1


print(luckyNumbers([[1,10,4,2],[9,3,8,7],[15,16,17,12]]))
#[12]

print(luckyNumbers([[3,7,8],[9,11,13],[15,16,17]]))
#[15]









#####################################################################################
#          1436. Destination City
#####################################################################################


"""
You are given the array paths, where paths[i] = [cityAi, cityBi]
    means there exists a direct path going from cityAi to cityBi.
    Return the destination city, that is, the city without any
    path outgoing to another city.

It is guaranteed that the graph of paths forms a line
    without any loop, therefore, there will be exactly one destination city.



Example 1:
Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
Output: "Sao Paulo"
Explanation: Starting at "London" city you will reach "Sao Paulo"
    city which is the destination city. Your
    trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".

Example 2:
Input: paths = [["B","C"],["D","B"],["C","A"]]
Output: "A"
Explanation: All possible trips are:
"D" -> "B" -> "C" -> "A".
"B" -> "C" -> "A".
"C" -> "A".
"A".
Clearly the destination city is "A".

"""

def destCity(paths: list[list[str]]) -> str:

    for i,two in enumerate(paths):
        if (two[1] not in [y for x in paths[:i] for y in x]) and (two[1] not in [y for x in paths[i+1:] for y in x]):
            return two[1]


print(destCity([["B","C"],["D","B"],["C","A"]]))
#A

















#####################################################################################
#          2500. Delete Greatest Value in Each Row
#####################################################################################



"""
You are given an m x n matrix grid consisting of positive integers.

Perform the following operation until grid becomes empty:

Delete the element with the greatest value from each row.
    If multiple such elements exist, delete any of them.

Add the maximum of deleted elements to the answer.

Note that the number of columns decreases by one after each operation.

Return the answer after performing the operations described above.



Example 1:
Input: grid = [[1,2,4],[3,3,1]]
Output: 8
Explanation: The diagram above shows the removed values in each step.
- In the first operation, we remove 4 from the first row and 3 from
    the second row (notice that, there are two cells with value 3 and we can remove any of them). We add 4 to the answer.

- In the second operation, we remove 2 from the first row and 3 from the second row. We add 3 to the answer.

- In the third operation, we remove 1 from the first row and 1 from the second row. We add 1 to the answer.
The final answer = 4 + 3 + 1 = 8.


Example 2:
Input: grid = [[10]]
Output: 10
Explanation: The diagram above shows the removed values in each step.
- In the first operation, we remove 10 from the first row. We add 10 to the answer.
The final answer = 10.

"""

import numpy as np

def deleteGreatestValue(grid: list[list[int]]) -> int:

    array_grid = np.sort(np.array(grid))

    c = np.shape(array_grid)[1]

    nums_max = 0

    for n in range(0,c):
        nums_max = np.max(array_grid[:,c-1:c]) + nums_max
        c = c - 1

print(deleteGreatestValue([[1,2,4],[3,3,1]]))
#8

print(deleteGreatestValue([[10]]))
#10












#####################################################################################
#          1374. Generate a String With Characters That Have Odd Counts
#####################################################################################


"""
Given an integer n, return a string with n characters
    such that each character in such string occurs an odd number of times.

The returned string must contain only lowercase
    English letters. If there are multiples valid strings, return any of them.



Example 1:
Input: n = 4
Output: "pppz"
Explanation: "pppz" is a valid string since the character 'p'
    occurs three times and the character 'z' occurs once.
    Note that there are many other valid strings such as "ohhh" and "love".

Example 2:
Input: n = 2
Output: "xy"
Explanation: "xy" is a valid string since the characters 'x'
    and 'y' occur once. Note that there are many other valid strings such as "ag" and "ur".


Example 3:
Input: n = 7
Output: "holasss"

"""

def generateTheString(n: int) -> str:
    if n % 2 == 0:
        return "h"*(n-1)+"b"
    else:
        return "h"*n


##############################################

def generateTheString(n: int) -> str:

    return sum(n.count(x) for x in set(n) if n.count(x) % 2 !=0)

print(generateTheString("pppz"))

































#####################################################################################
#            746. Min Cost Climbing Stairs
#####################################################################################

"""
You are given an integer array cost where cost[i]
    is the cost of ith step on a staircase.
    Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.



Example 1:
Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.

Example 2:
Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.


"""

def minCostClimbingStairs(cost: list[int]) -> int:

    cost.append(0)
    reverse_cost = cost[::-1]

    n = 0

    while n < len(reverse_cost) - 3:
        print(reverse_cost[::-1])
        reverse_cost[n+3] = min(reverse_cost[n + 1],reverse_cost[n + 2]) + reverse_cost[n+3]
        n = n + 1

    return min(reverse_cost[-1],reverse_cost[-2])



print(minCostClimbingStairs([20, 1, 2, 20, 1, 5, 1, 30]))
#5

print(minCostClimbingStairs([10, 15, 20]))
#15


























#####################################################################################
#            2496. Maximum Value of a String in an Array
#####################################################################################

"""
The value of an alphanumeric string can be defined as:

The numeric representation of the string in base 10, if it comprises of digits only.
The length of the string, otherwise.
Given an array strs of alphanumeric strings, return the maximum value of any string in strs.



Example 1:
Input: strs = ["alic3","bob","3","4","00000"]
Output: 5
Explanation:
- "alic3" consists of both letters and digits, so its value is its length, i.e. 5.
- "bob" consists only of letters, so its value is also its length, i.e. 3.
- "3" consists only of digits, so its value is its numeric equivalent, i.e. 3.
- "4" also consists only of digits, so its value is 4.
- "00000" consists only of digits, so its value is 0.
Hence, the maximum value is 5, of "alic3".

Example 2:
Input: strs = ["1","01","001","0001"]
Output: 1
Explanation:
Each string in the array has value 1. Hence, we return 1.

"""


def maximumValue(strs: list[str]) -> int:

    q = 0
    for n in strs:
        try:
            n = int(n)
            if n > q:
                q = n

        except ValueError:
            n = len(n)
            if n > q:
                q = n

    return q

print(maximumValue(["alic3","bob","3","4","00000"]))
#5













#####################################################################################
#            2843. Count Symmetric Integers
#####################################################################################


"""
You are given two positive integers low and high.

An integer x consisting of 2 * n digits is symmetric if the sum
    of the first n digits of x is equal to the sum of the last
    n digits of x. Numbers with an odd number of digits are never symmetric.

Return the number of symmetric integers in the range [low, high].



Example 1:
Input: low = 1, high = 100
Output: 9
Explanation: There are 9 symmetric integers between 1 and 100: 11, 22, 33, 44, 55, 66, 77, 88, and 99.

Example 2:
Input: low = 1200, high = 1230
Output: 4
Explanation: There are 4 symmetric integers between 1200 and 1230: 1203, 1212, 1221, and 1230.
"""

import numpy as np

def countSymmetricIntegers(low: int, high: int) -> int:

    number_array = np.arange(low,high+1).tolist()
    even_len_array = [x for x in number_array if len(str(x)) % 2 == 0]

    return sum(1 for x in even_len_array
                if sum(int(t) for t in (str(x)[:int(len(str(x))/2)])) == sum(int(t) for t in (str(x)[int(len(str(x))/2):])))


print(countSymmetricIntegers(low = 1, high = 1200))
#14



















#####################################################################################
#            3174. Clear Digits
#####################################################################################


"""
You are given a string s.

Your task is to remove all digits by doing this operation repeatedly:

Delete the first digit and the closest non-digit character to its left.
Return the resulting string after removing all digits.



Example 1:
Input: s = "abc"
Output: "abc"
Explanation:
There is no digit in the string.

Example 2:
Input: s = "cb34"
Output: ""
Explanation:
First, we apply the operation on s[2], and s becomes "c4".
Then we apply the operation on s[1], and s becomes "".

"""

def clearDigits(s: str) -> str:
    list1 = []
    for n in s:
        if n.isalpha():
            list1.append(n)
        else:
            list1.pop()
    return "".join(list1)



print(clearDigits("cb34"))
















#####################################################################################
#            160. Find Words That Can Be Formed by Characters
#####################################################################################


"""
You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.



Example 1:

Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
Example 2:

Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.


"""
#if letter in chars and (word.count(letter) >= chars.count(letter)):

def countCharacters(words: list[str], chars: str) -> int:
    n = 0
    for word in words:
        if all(chars.count(letter) >= word.count(letter) for letter in word) and all(letter in chars for letter in word):
            n = len(word) + n
    return n

print(countCharacters(words = ["cat","bt","hat","tree"], chars = "atach"))
















#####################################################################################
#           2562. Find the Array Concatenation Value
#####################################################################################


"""
You are given a 0-indexed integer array nums.

The concatenation of two numbers is the number formed by concatenating their numerals.

For example, the concatenation of 15, 49 is 1549.

The concatenation value of nums is initially equal to 0.
    Perform this operation until nums becomes empty:

If there exists more than one number in nums, pick the
    first element and last element in nums respectively
     and add the value of their concatenation to the
     concatenation value of nums, then delete the first and last element from nums.

If one element exists, add its value to the
    concatenation value of nums, then delete it.

Return the concatenation value of the nums.



Example 1:
Input: nums = [7,52,2,4]
Output: 596
Explanation: Before performing any operation, nums is [7,52,2,4] and concatenation value is 0.
 - In the first operation:
We pick the first element, 7, and the last element, 4.
Their concatenation is 74, and we add it to the concatenation value, so it becomes equal to 74.
Then we delete them from nums, so nums becomes equal to [52,2].
 - In the second operation:
We pick the first element, 52, and the last element, 2.
Their concatenation is 522, and we add it to the concatenation value, so it becomes equal to 596.
Then we delete them from the nums, so nums becomes empty.
Since the concatenation value is 596 so the answer is 596.


Example 2:
Input: nums = [5,14,13,8,12]
Output: 673
Explanation: Before performing any operation, nums is [5,14,13,8,12] and concatenation value is 0.
 - In the first operation:
We pick the first element, 5, and the last element, 12.
Their concatenation is 512, and we add it to the concatenation value, so it becomes equal to 512.
Then we delete them from the nums, so nums becomes equal to [14,13,8].
 - In the second operation:
We pick the first element, 14, and the last element, 8.
Their concatenation is 148, and we add it to the concatenation value, so it becomes equal to 660.
Then we delete them from the nums, so nums becomes equal to [13].
 - In the third operation:
nums has only one element, so we pick 13 and add it to the concatenation value, so it becomes equal to 673.
Then we delete it from nums, so nums become empty.
Since the concatenation value is 673 so the answer is 673.


"""


def findTheArrayConcVal(nums: list[int]) -> int:

    list1 = []

    while len(nums) > 1:
        list1.append(int((str(nums.pop(0))+str(nums.pop()))))

    if len(nums) <= 1:
        if len(nums) == 1:
            list1.append(nums[0])
            return sum(list1)
        else:
            return sum(list1)

print(findTheArrayConcVal([7,52,2,4]))

print(findTheArrayConcVal([5,14,13,8,12]))














#####################################################################################
#           1619. Mean of Array After Removing Some Elements
#####################################################################################




"""
Given an integer array arr, return the mean of the
    remaining integers after removing the smallest 5% and the largest 5% of the elements.

Answers within 10-5 of the actual answer will be considered accepted.



Example 1:
Input: arr = [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3]
Output: 2.00000
Explanation: After erasing the minimum and the maximum
    values of this array, all elements are equal to 2, so the mean is 2.

Example 2:
Input: arr = [6,2,7,5,1,2,0,3,10,2,5,0,5,5,0,8,7,6,8,0]
Output: 4.00000

Example 3:
Input: arr = [6,0,7,0,7,5,7,8,3,4,0,7,8,1,6,8,1,1,2,4,8,1,9,5,4,3,8,5,10,8,6,6,1,0,6,10,8,2,3,4]
Output: 4.77778

"""


def trimMean(arr: list[int]) -> float:

    arr.sort()

    five_percent = len(arr)//20

    arr = arr[five_percent:-(five_percent)]

    return sum(arr)/len(arr)

print(trimMean([6,0,7,0,7,5,7,8,3,4,0,7,8,1,6,8,1,1,2,4,8,1,9,5,4,3,8,5,10,8,6,6,1,0,6,10,8,2,3,4]))
















#####################################################################################
#           2062. Count Vowel Substrings of a String
#####################################################################################


"""
A substring is a contiguous (non-empty) sequence of characters within a string.

A vowel substring is a substring that only consists of
    vowels ('a', 'e', 'i', 'o', and 'u') and has all five vowels present in it.

Given a string word, return the number of vowel substrings in word.



Example 1:
Input: word = "aeiouu"
Output: 2
Explanation: The vowel substrings of word are as follows (underlined):
- "aeiouu"
- "aeiouu"

Example 2:
Input: word = "unicornarihan"
Output: 0
Explanation: Not all 5 vowels are present, so there are no vowel substrings.

Example 3:
Input: word = "cuaieuouac"
Output: 7
Explanation: The vowel substrings of word are as follows (underlined):
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"

"""

#        if all(z in y for z in vowels):
#           t = max(y.count(z) for z in vowels) + t

import re

def countVowelSubstrings(word: str) -> int:

    vowels = ("a","e","o","u","i")
    list1 = [x if x in vowels else " " for x in word]
    list1 = (("".join(list1)).strip()).split(" ")
    p = 0
    for y in list1:
        q = [y[i:j] for i in range(len(y)) for j in range(i + 1, len(y) + 1)]
        for w in q:
            if all(z in w for z in vowels):
                p = p + 1

    return p

print(countVowelSubstrings("cuaieuoutac"))

















