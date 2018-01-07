

def reverse_string(string):

    return string[::-1]

# Write an algorithm that returns true/false if a word is a palindrome
# (i.e. reads the same forwards/backwards) racecar  dad mum


def is_palindrome(word):

    p0 = 0
    p1 = len(word) - 1

    is_palin = True

    while(p0 < p1):

        if word[p0].lower() != word[p1].lower():
            is_palin = False
            return is_palin

        p0 += 1
        p1 -= 1

    return is_palin
