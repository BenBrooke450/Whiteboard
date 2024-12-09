
"""
Given a string s, check if it can be
    constructed by taking a substring of it
    and appending multiple copies of the substring together.



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

def repeatedSubstringPattern(s: str) -> bool:

    n = len(s) # Loop through possible lengths for the substring

    for i in range(1, n):
        # Check if the length divides the total length of the string

        if n % i == 0:
            # Form the repeating string
            substring = s[:i]

            repeated_string = substring * (n // i)
            # Check if the repeated string matches the original string

            if repeated_string == s:
                return True
        return False


"""
So what´s really going on here

"""


# Example usage
print(repeatedSubstringPattern("abab"))
# Output: True
print(repeatedSubstringPattern("aba"))
# Output: False
print(repeatedSubstringPattern("abcabcabcabc"))
# Output: True
























