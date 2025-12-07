import random

#КОНСТАНТЫ
OBJECT_PRONOUNS = ['Her', 'Him', 'Them']
POSSESSIVE_PRONOUNS = ['Her', 'His', 'Their']
PERSONAL_PRONOUNS = ['She', 'He', 'They']
STATE = ['PERM', 'MOSCOW', 'EKAT', 'ORENBURG',
         'KRASNOKAMSK', 'SOLEKAMSK', 'SAMARA', 'SARATOV',
         'KAZAN', 'BEREZNики']
NOUNS = ["Clown", 'Cat', 'Dog', 'Avocado', 'Doctor', 'Parent',
         "Robot", 'Telegram', 'Youtube', 'VK', 'Video Game',
         'Telephone', 'Figma', 'Chicken']
PLACES = ['House', 'Attic', 'Bank', 'School', 'College',
          'Basement', 'Hospital']
WHEN = ['Soon', 'This Year', 'Later Today', 'RIGHT NOW', 'NEXT WEEK']
def main():
    while True:
        print("Enter the number of clickbait headlines to generate:")
        response = input(">>>")
        if not response.isdecimal():
            print("Please enter a number!")
        else:
            numberOfHeadlines = int(response)
            break

    for i in range(numberOfHeadlines):
        clickbaitType = random.randint(1, 8)
        if clickbaitType == 1:
            headline = generateAreMillennialsKillingHeadline()
        elif clickbaitType == 2:
            headline = generateWhatYouDontKnowHeadline()
        elif clickbaitType == 3:
            headline = generateBigCompaniesHateHerHeadline()
        elif clickbaitType == 4:
            headline = generateYouWontBelieveHeadline()
        elif clickbaitType == 5:
            headline = generateDontWantYouToKnowHeadline()
        elif clickbaitType == 6:
            headline = generateGiftIdeaHeadline()
        elif clickbaitType == 7:
            headline = generateReasonsWhyHeadline()
        elif clickbaitType == 8:
            headline = generateJobAutomatedHeadline()

        print(headline)
        print()

        website = random.choice(['wobsite', 'blag', 'facebuuk', 'Googles', 'VKF', 'Twedie', 'Pastagram'])
        when = random.choice(WHEN).lower()
        print("POST these to our", website, when, "or you're fired!")

def generateAreMillennialsKillingHeadline():
    noun = random.choice(NOUNS)
    return f"Are Millennials Killing the {noun} Industry?"

def generateWhatYouDontKnowHeadline():
    noun = random.choice(NOUNS)
    pluralNoun = random.choice(NOUNS) + "s"
    when = random.choice(WHEN)
    return f"Without This {noun}, {pluralNoun} Could kill You {when}"

def generateBigCompaniesHateHerHeadline():
    pronoun = random.choice(OBJECT_PRONOUNS)
    state = random.choice(STATE)
    noun1 = random.choice(NOUNS)
    noun2 = random.choice(NOUNS)
    return (f"Big Companies Hate {pronoun}! See How This {state} {noun1} Invented "
            f"a Cheaper {noun2}")

def generateYouWontBelieveHeadline():
    state = random.choice(STATE)
    noun = random.choice(NOUNS)
    pronoun = random.choice(OBJECT_PRONOUNS)
    place = random.choice(PLACES)
    return f"'You Won't Believe What This {state} {noun} Found in {pronoun} {place}'"

def generateDontWantYouToKnowHeadline():
    pluralNoun1 = random.choice(NOUNS) + "s"
    pluralNoun2 = random.choice(NOUNS) + "s"
    return f"What {pluralNoun1} Don 't Want You To Know About {pluralNoun2}"

def generateGiftIdeaHeadline():
    number = random.randint(7, 15)
    noun = random.choice(NOUNS)
    state = random.choice(STATE)
    return f"{number} Gift Ideas to Give Your {noun} From {state}"

def generateReasonsWhyHeadline():
    number1 = random.randint(3, 19)
    number2 = random.randint(1, number1)
    pluralNoun = random.choice(NOUNS) + "s"
    return (f"{number1} Reasons Why {pluralNoun} Are Morre Interesting That You Think "
            f"(Number {number2} Will Surprise You)")

def generateJobAutomatedHeadline():
    state = random.choice(STATE)
    noun = random.choice(NOUNS)
    i = random.randint(0, 2)
    pronoun1 = POSSESSIVE_PRONOUNS[i]
    pronoun2 = POSSESSIVE_PRONOUNS[i]
    if pronoun1 == "Their":
        return (f"This {state} {noun} Didn\\'t Think Robots Would Take {pronoun1} Job. "
                f"{pronoun2} Were Wrong.")
    else:
        return (f"This {state} {noun} Didn\\'t Think Robots Would Take {pronoun1} Job. "
                f"{pronoun2} Was Wrong.")
if __name__ == "__main__":
    main()