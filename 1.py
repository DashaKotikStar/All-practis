import random
import sys

# Символы для мастей
HEARTS = chr(9829)  # Черви
DIAMONDS = chr(9830)  # Бубны
SPADES = chr(9824)  # Пики
CLUBS = chr(9827)  # Трефы
BACKSIDE = 'backside'  # Рубашка карты

def main():
    print('''
Правила игры: 

    Постарайтесь набрать максимально близкое 
    к 21 число, не превышая его 

    Короли, дамы, валеты приносят по 10 очков.
    Тузы приносят 1 или 11 очков.
    Карты от 2 до 10 приносят свой номинал.
    (H)it, чтобы взять карту,
    (S)tand, чтобы прекратить брать карты.
    (D)ouble, чтобы удвоить ставку при первой игре.
    В случае ничьей ставка возвращается к игроку.
    Диллер прекращает брать карту на 17 очках.
    Хороших игр!!
''')
    money = 5000  # Начальный капитал

    while True:
        # Проверка, не закончились ли деньги
        if money <= 0:
            print("У тебя закончились деньги!")
            print("Спасибо за игру!")
            sys.exit()

        # Сделать ставку
        print(f'Ваш баланс: {money} монет')
        bet = getBet(money)

        # Раздать начальные карты
        deck = getDeck()
        dealerHand = [deck.pop(), deck.pop()]
        playerHand = [deck.pop(), deck.pop()]

        # Обработка действий игрока
        print(f'Ставка: {bet}')
        while True:
            displayHands(playerHand, dealerHand, False)
            print()

            # Проверка на перебор
            if getHandValue(playerHand) > 21:
                break

            # Получить ход игрока
            move = getMove(playerHand, money - bet)

            if move == 'D':
                # Удвоение ставки
                additionalBet = getBet(min(bet, (money - bet)))
                bet += additionalBet
                print(f'Ставка увеличена. Теперь она составляет: {bet}')

            if move in ('H', 'D'):
                # Игрок берёт карту
                newCard = deck.pop()
                rank, suit = newCard
                print(f'Вы вытянули {rank} {suit}.')
                playerHand.append(newCard)

                if getHandValue(playerHand) > 21:
                    # Перебор
                    displayHands(playerHand, dealerHand, False)
                    break

            if move in ('S', 'D'):
                # Игрок останавливается
                break

        # Обработка действий диллера
        if getHandValue(playerHand) <= 21:
            while getHandValue(dealerHand) < 17:
                print('Диллер берёт карту...')
                dealerHand.append(deck.pop())
                displayHands(playerHand, dealerHand, False)

                if getHandValue(dealerHand) > 21:
                    break  # Диллер перебрал
                input('Нажмите Enter, чтобы продолжить...')
                print('\n\n')

        # Отобразить финальные руки
        displayHands(playerHand, dealerHand, True)

        playerValue = getHandValue(playerHand)
        dealerValue = getHandValue(dealerHand)

        # Определить результат
        if dealerValue > 21:
            print(f'Диллер перебрал! Вы выиграли {bet} монет!')
            money += bet
        elif (playerValue > 21) or (playerValue < dealerValue):
            print('Вы проиграли!')
            money -= bet
        elif playerValue > dealerValue:
            print(f'Вы выиграли {bet} монет!')
            money += bet
        elif playerValue == dealerValue:
            print('Ничья, ставка возвращена к вам.')

        input('Нажмите Enter, чтобы продолжить...')
        print('\n\n')


def getBet(maxBet):
    """Спрашивает ставку у игрока."""
    while True:
        print(f'Сколько вы хотите поставить? (1-{maxBet}, или QUIT)')
        bet = input('> ').upper().strip()
        if bet == 'QUIT':
            print('Спасибо за игру!')
            sys.exit()

        if not bet.isdecimal():
            continue  # Повторить, если ввод не число

        bet = int(bet)
        if 1 <= bet <= maxBet:
            return bet


def getDeck():
    """Создаёт колоду карт (список кортежей (номинал, масть))."""
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit))  # Карты 2-10
        for rank in ('J', 'Q', 'K', 'A'):
            deck.append((rank, suit))  # Валет, Дама, Король, Туз
    random.shuffle(deck)
    return deck


def displayHands(playerHand, dealerHand, showDealerHand):
    """Отображает карты игрока и диллера. Если showDealerHand False, то скрывает первую карту диллера."""
    print()
    # Показать карты диллера
    if showDealerHand:
        print(f'ДИЛЛЕР: {getHandValue(dealerHand)}')
        displayCards(dealerHand)
    else:
        print('ДИЛЛЕР: ???')
        # Скрыть первую карту
        displayCards([BACKSIDE] + dealerHand[1:])

    # Показать карты игрока
    print(f'ИГРОК: {getHandValue(playerHand)}')
    displayCards(playerHand)


def getHandValue(cards):
    """Возвращает стоимость карт. Фигурные - 10, Туз - 11 или 1."""
    value = 0
    numberOfAces = 0

    # Добавить стоимость карт (кроме тузов)
    for card in cards:
        rank = card[0]
        if rank == 'A':
            numberOfAces += 1
        elif rank in ('K', 'Q', 'J'):  # Фигурные карты
            value += 10
        else:  # Карты 2-10
            value += int(rank)

    # Добавить стоимость тузов
    value += numberOfAces  # Сначала добавим 1 за каждый туз
    for i in range(numberOfAces):
        # Если можно, сделать туз 11 (не превысив 21)
        if value + 10 <= 21:
            value += 10

    return value


def displayCards(cards):
    """Отображает все карты из списка."""
    rows = ['', '', '', '', '']  # Строки для отображения карт

    for i, card in enumerate(cards):
        rows[0] += ' ___  '  # Верхняя строка
        if card == BACKSIDE:
            # Рубашка карты
            rows[1] += '|## | '
            rows[2] += '|###| '
            rows[3] += '|_##| '
        else:
            # Номинал и масть
            rank, suit = card[0], card[1]
            rows[1] += f'|{rank.ljust(2)} | '
            rows[2] += f'| {suit} | '
            rows[3] += f'|_{rank.rjust(2, "_")}| '

    # Вывести строки
    for row in rows:
        print(row)


def getMove(playerHand, money):
    """Спрашивает у игрока ход: взять карту (H), остановиться (S) или удвоить (D)."""
    while True:
        # Определяем возможные ходы
        moves = ['(H)it', '(S)tand']

        # Удвоение возможно только при первом ходе
        if len(playerHand) == 2 and money > 0:
            moves.append('(D)ouble down')

        # Спрашиваем ход
        movePrompt = ', '.join(moves) + '> '
        move = input(movePrompt).upper()
        if move in ('H', 'S'):
            return move
        if move == 'D' and '(D)ouble down' in moves:
            return move


# Запуск игры
if __name__ == '__main__':
    main()