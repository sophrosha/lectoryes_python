import random

# Константы
OBJECT_PRONOUNS = ['Her', 'Him', 'Them']
POSSESIVE_PRONOUMS = ['Her', 'His', 'Their']
PERSONAL_PRONOUMS = ['She', 'He', 'They']
STATE = ['PERM', 'MOSCOW', 'EKATERINBURG', 'ORENBURG',
         'KRANOKAMSK', 'SOLEKAMSK', 'SAMARA', 'SARATOV',
         'KAZAN', 'BEREZNIKI']

NOUNS = ['Clown', 'Cat', 'Dog', 'Avocado', 'Doctor', 'Parent',
         'Robot', 'Telegram', 'Youtube', 'VK', 'Video Game',
         'Telephone', 'Figma', 'Chicken']
PLACES = ['House', 'Attic', 'Bank', 'School', 'College',
          'Basement', 'Hospital']

WHEN = ['Soon', 'This Year', 'Later Today', 'RIGHT NOW', 'NEXT WEEK']
def main():
    headline = None
    while True:
        print("Enter the number of clickbait headlines to generate:")
        response = input(">>>: ")
        if not response.isdecimal():
            print("Please enter a number!")
        else:
            number_of_headlines = int(response)
            break
    for i in range(number_of_headlines):
        clickbait_type = random.randint(1, 8)
        if clickbait_type == 1:
            headline = generateAreMillenialsKillingHeadline()
        elif clickbait_type == 2:
            headline = generateWhatTouDontKnowHeadline()
        elif clickbait_type == 3:
            headline = generateBigCompaniesGateHerHeadline()
        elif clickbait_type == 4:
            headline = generateYouWantBelieveHeadline()
        elif clickbait_type == 5:
            headline = generateDownWantYouToKnowHeadline()
        elif clickbait_type == 6:
            headline = generateGiftIdeaHeadline()
        elif clickbait_type == 7:
            headline = generateReasonsWhyHeadline()
        elif clickbait_type == 8:
            headline = generateJobAutomatedHeadline()
        print(headline)
    print()
    website = random.choice(['wobsite', 'blag', 'facebuuk', 'Googles', 'VKF', 'Twedie', 'Pastagram'])
    when = random.choice(WHEN).lower()
    print("POST these to our", website, when, "or you\'re fired!")

def generateAreMillenialsKillingHeadline():
    noun = random.choice(NOUNS)
    return f'Are Millenials Killing the {noun} Industry?'
def generateWhatTouDontKnowHeadline():
    noun = random.choice(NOUNS)
    plural_noun = random.choice(NOUNS) + 's'
    when = random.choice(WHEN)
    return f'Without This {noun}, {plural_noun} Could kill You {when}'

def generateBigCompaniesGateHerHeadline():
    pronoun = random.choice(OBJECT_PRONOUNS)
    state = random.choice(STATE)
    noun1 = random.choice(NOUNS)
    noun2 = random.choice(NOUNS)
    return (f'Big Companies Hate {pronoun}! See how this {state} {noun1} Invented'
            f'a Cheaper {noun2}')

def generateYouWantBelieveHeadline():
    state = random.choice(STATE)
    noun = random.choice(NOUNS)
    pronoun = random.choice(OBJECT_PRONOUNS)
    place = random.choice(PLACES)
    return f'You Won\'t Believe what this {state} {noun} found in {pronoun} {place}'

def generateDownWantYouToKnowHeadline():
    plural_noun1 = random.choice(NOUNS) + 's'
    plural_noun2 = random.choice(NOUNS) + 's'
    return f'What {plural_noun1} Don\'t Want you to know about {plural_noun2}'

def generateGiftIdeaHeadline():
    number = random.randint(7, 15)
    noun = random.choice(NOUNS)
    state = random.choice(STATE)
    return f'{number} gift idead to give your {noun} from {state}'

def generateReasonsWhyHeadline():
    number1 = random.randint(3, 19)
    number2 = random.randint(1, number1)
    plural_noun = random.choice(NOUNS) + 's'
    return (f'{number1} reasons why {plural_noun} are morre interesting that you think'
            f'(Number {number2} will surprise you)')

def generateJobAutomatedHeadline():
    state = random.choice(STATE)
    noun = random.choice(NOUNS)
    i = random.randint(0, 2)
    pronoun1 = POSSESIVE_PRONOUMS[i]
    pronoun2 = POSSESIVE_PRONOUMS[i]
    if pronoun1 == 'Their':
        return (f'This {state} {noun} Didn\'t think robots take {pronoun1} job.'
                f'{pronoun2} Were Wrong.')
    else:
        return (f'This {state} {noun} Didn\'t think robots take {pronoun1} job.'
                f'{pronoun2} Was Wrong.')


if __name__ == "__main__":
    main()

'''
1. при создании итерации на 27 строке будет проверяться сама переменная, но так как ее нету то будет создаваться ошибка
2. Почти так же, но число будет считаться просто ввиде str, и по этому не будет проходить через range, который требует int а не str.
3. Так как на 48 строке кроме choice так же выбирается последняя буква насколько понимаю то ее попросту не будет и будет вылезать ошибка отсуствия списка.
'''