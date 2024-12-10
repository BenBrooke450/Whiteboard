


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










