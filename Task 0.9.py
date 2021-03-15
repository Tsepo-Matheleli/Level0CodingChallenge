def vowels(word):
    new_word_list = list(word)
    vowel_list = ('a', 'e', 'i', 'o', 'u')
    common_vowels = ''
    for character in new_word_list:
        if character in vowel_list:
            common_vowels += character + ', '
    print('Vowels: ' + common_vowels)


vowels('Umuzi')
