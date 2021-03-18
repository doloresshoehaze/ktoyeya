from dictionary import dictionary

articles = ['le', 'la', 'les', 'un', 'une', 'des', 'du', 'de']
keyWord = 'pièce'


def function(sent):
    for wordInputSent in sent:
        for _, (key1, value1) in enumerate(dictionary.items()):

            keyWordIndex = sent.index(keyWord)
            descriptionWordIndex = sent.index(wordInputSent)

            for _, (key2, value2) in enumerate(value1.items()):

                if ((value2['pos'] == descriptionWordIndex - keyWordIndex) & (key2 == wordInputSent)):
                    print('The word "' + keyWord +
                          '" is used in the meaning:', key1)
                    return

    print('Nothing found...')


sent = ''


while sent != '*':
    sent = input('enter: a sentence with ' + keyWord + '\n').lower()
    if sent == '*':
        break
    sent = sent.replace('.', '').replace(
        ',', '').replace(keyWord + 's', keyWord).split(' ')

    for article in sent:
        if article in articles:
            articleIndex = sent.index(article)
            sent.pop(articleIndex)

    if keyWord not in sent:
        print('there is no word ' + keyWord + '!!!')
        continue

    function(sent)
