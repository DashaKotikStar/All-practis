import random, sys
HEART = chr(9827)
DIANONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)
BACKSIDE = 'backside'
'''
black jack - классическая карточная игра, известная как 21. В этой версии нет страхования или разбиения очков.
'''
def main():
    print('''
    Правила игры: \n
        Постарайтесь набрать максимальнго близкое 
        к 21 число не перивышая его \n
        Короли, дамы, валеты приносят по 10 очков.\n
        Тузы приносят 1 или 11 очков.\n
        Карты от 2 до 10 приносят свой наминал.\n
        (H)it, чтобы взять карту,\n
        (S)tand, чтобы прекратить брать карты.\n
        (D)abll, чтобы удвоить ставку при первой игре.\n
        В случае ничьи ставка возращается к игроку.\n
        Диллер прекращает брать карту на 17 очках.\n
        Хороших игр!!
    ''')
    money = 50
    while True:
        if money <= 0:
            print('''
            Ты проиграл. У тебя закончились деньги. Приходи ещё.
            ''')
            sys.exit()
        print(f"ДЕНЬГИ {money}")
        bet = getBet(money)
        deck = getDeck()
        dealerHand = [deck.pop(), deck.pop()]
        plaerHand = [deck.pop(), deck.pop()]
        #обработка действий игрока
        print(f"Ставка: {bet}")
        while True:
            displayHands(plaerHand, dealerHand, False)
            print()
            if getHandValue(plaerHand) > 21:
                break
            move = getMove(plaerHand, money - bet)
            if move == 'D':
                additionalBet = getBet(min(bet, (money-bet)))
                bet += additionalBet
                print(f"Ставка изменилась => {bet}")
            if move in ("H", "D"):
                newCard = deck.pop()
                rank, suit = newCard
                print(f"Выпала карта {rank}, номиналом: {suit}")
                plaerHand.append(newCard)
                if getHandValue(plaerHand) > 21:
                    continue
            if move in ("S", "D"):
                break
            #Обработка действий диллера
            if getHandValue(plaerHand) <= 21:
                while getHandValue(dealerHand) < 17:
                    print("Диллер берёт ещё одну карту...")
                    dealerHand.append(deck.pop())
                    displayHands(plaerHand, dealerHand, False)
                    if getHandValue(dealerHand) > 21:
                        break
                    input("Для продолжения, нажмите Enter...")
                    print("\n\n")
            #Финал
            displayHands(plaerHand, dealerHand, True)
            playerValue = getHandValue(plaerHand)
            dealerVakue = getHandValue(dealerHand)
            if dealerVakue > 21:
                print(f"Диллер перебрал! Ты выйграл ставку {bet}")
                money += bet
            elif playerValue > 21 or playerValue < dealerVakue:
                print("Ты проиграл!")
                money -= bet
            elif playerValue > dealerVakue:
                print("Ты победил!")
                money += bet
            elif playerValue == dealerVakue:
                print("Это ничья, победителя нет...")
            input("Нажмите Enter, тобы продолжить...")
            print("\n\n")

            def getBet(maxBet):
                if 1 <= bet <= maxBet:
                    return bet
            #Создание 52 игральных карт
            def getDeck():
                deck = []
                for suit in (HEARTS, DIANONDS, SPADES, CLUBS):
                    for rank in range(2, 11):
                        deck.append((str(rank), suit))
                        for rank in ("JQKA"):
                            deck.append((rank, suit))
                random.shuffle(deck)
            return deck
        
