"""
Given a string, find the length of the longest substring in it with no more than K distinct characters.
"""


def longest_substring_with_k_distinct(str, k):
    longest_len = 0

    char_count = {}

    def add_to_count(char):
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    left, right = 0, 0
    while right < len(str):
        add_to_count(str[right])

        if len(char_count) == k:
            longest_len = max(longest_len, right-left+1)
        else:
            # decrease window from the left till we have <= k characters in the char_count
            while len(char_count) > k and left <= right:
                # remove from char count
                if char_count[str[left]] == 1:
                    char_count.pop(str[left])
                else:
                    char_count[str[left]] -= 1
                # move left part of window forward: make window smaller
                left += 1

        right += 1  # expand window

    return longest_len


def main():
    print("Length of the longest substr1ing: " +
          str(longest_substring_with_k_distinct("araaci", 2)))
    print("Length of the longest substr1ing: " +
          str(longest_substring_with_k_distinct("araaci", 1)))
    print("Length of the longest substr1ing: " +
          str(longest_substring_with_k_distinct("cbbebi", 3)))


main()

"""
SOLUTION:
First, we will insert characters from the beginning of the string until we have ‘K’ distinct characters in the HashMap.
These characters will constitute our sliding window. We are asked to find the longest such window having no more than ‘K’ distinct characters. We will remember the length of this window as the longest window so far.
After this, we will keep adding one character in the sliding window (i.e., slide the window ahead) in a stepwise fashion.
In each step, we will try to shrink the window from the beginning if the count of distinct characters in the HashMap is larger than ‘K.’ We will shrink the window until we have no more than ‘K’ distinct characters in the HashMap. This is needed as we intend to find the longest window.
While shrinking, we’ll decrement the character’s frequency going out of the window and remove it from the HashMap if its frequency becomes zero.
At the end of each step, we’ll check if the current window length is the longest so far, and if so, remember its length.
"""
