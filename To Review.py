


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










