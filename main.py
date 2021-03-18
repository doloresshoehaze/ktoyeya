meaning1 = 'l"éléments d"un ensemble / элемент общности, деталь'
meaning2 = 'morceau de métal façonné servant de monnaie / кусок обработанного металла, служащий валютой, монета'
meaning3 = 'œuvre dramatique / драматическое произведение'
meaning4 = 'la chambre / комната'


dictionary = {
    meaning1: {
        'attachée': {
            'pos': -3,
        },
        'défectueuse': {
            'pos': 1,
        },
        'puzzle': {
            'pos': 2,
        },
        'plastique': {
            'pos': 2,
        },
        'machine': {
            'pos': 3,
        },
        'colle': {
            'pos': 3,
        },
        'complexe': {
            'pos': 4,
        }
    },
    meaning2: {
        'valeur': {
            'pos': -4,

        },
        'fouilles': {
            'pos': -2,
        },

        'rare': {
            'pos': 1,
        },
        'argent': {
            'pos': 2,
        },
        'frappée': {
            'pos': 3,
        },
        'époques': {
            'pos': 3,
        },
        'dénominations': {
            'pos': 5,
        }
    },
    meaning3: {
        'jouer': {
            'pos': -2,
        },
        'écrire': {
            'pos': -2,
        },
        'nouvelle': {
            'pos': -1,
        },
        'vocales': {
            'pos': 1,
        },
        'propos': {
            'pos': 2,
        },
        'fantastique': {
            'pos': 1,
        },
        'théatre': {
            'pos': 2,
        }
    },
    meaning4: {
        'belle': {
            'pos': -1,
        },
        'petite': {
            'pos': -1,
        },
        'vitrée': {
            'pos': 1,
        },
        'nettoyer': {
            'pos': 2,
        },
        'maison': {
            'pos': 3,
        },
        'garage': {
            'pos': 3,
        },
        'prendre': {
            'pos': 4,
        }
    }
}


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
