def reverse(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    reversed_sentence = " ".join(reversed_words)
    return reversed_sentence

input_sentence = input(" Enter a sentence:- ")
result = reverse(input_sentence)

print(" Output after reverse:- ", result)
