def common_letters(first_word, second_word):
    first_word_list = list(first_word)
    second_word_list = list(second_word)
    common_words = ''
    for character in first_word_list:
        if character in second_word_list:
            common_words += character + ', '
    print('Common Letters: ' + common_words)

