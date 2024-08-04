def is_anagram(left, right):
    left_letters = sorted(left)
    right_letters = sorted(right)
    print(left_letters)
    print(right_letters)
    return left_letters == right_letters

print(is_anagram("listen", "silent"))
