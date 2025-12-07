import random
import sys

HEARTS = chr(9827)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)
BACKSIDE = 'backside'
'''
black jack - классическая карточ игра
измевстаня как 21. В Этой версии нет
страхования и разбиения очков
'''


def main():
    print('''
    Правила игры: \n
    Постаратейсь набрать макс близкое \n
    к 21 число, не привышая его. \n
    Короли, дамы, валеты приносят по 10 очков. \n
    Тузы приносят 1 или 11 очков. \n
    Карты от 2 до 10 приносят свой номинал. \n
    (H)it, чтоб взять карту. \n
    (S)stand, чтоб прекратить брать карты. \n
    (D)abell, чтоб удвоить вставку при первой игре. \n
    В случае нечьи ставка возвращается к игроку \n
    Диллер прекращает тратить карты на 17 очках \n
    ''')
    money = 5000
    while True:
        if money <= 0:
            print('''
            Ты проиграл, у тебя закончились кредиты.
            ''')
            sys.exit()
        print(f"Кредиты: {money}")
        bet = get_bet(money)
        deck = get_deck()
        dealer_hand = [deck.pop(), deck.pop()]
        player_hand = [deck.pop(), deck.pop()]
        print(f"Ставка: {bet}")
        while True:
            display_hands(player_hand, dealer_hand, False)
            print()
            if get_hand_value(player_hand) > 21:
                break
            move = get_move(player_hand, money - bet)
            if move == 'D':
                additional_bet = get_bet(min(bet, (money - bet)))
                bet += additional_bet
                print(f"Ставка изменилась => {bet}")
            if move in ("H", "D"):
                new_card = deck.pop()
                rank, suit = new_card
                print(f"выпала карта {rank} номиналом {suit}")
                player_hand.append(new_card)
                if get_hand_value(player_hand) > 21:
                    continue
            if move in ("S", "N", "D"):
                break
        if get_hand_value(player_hand) <= 21:
            while get_hand_value(dealer_hand) < 17:
                print("Диллер берет карту")
                dealer_hand.append(deck.pop())
                display_hands(player_hand, dealer_hand, False)
                if get_hand_value(dealer_hand) > 21:
                    break
                input("для продолжения нажмите enter...")
                print("\n\n")
        display_hands(player_hand, dealer_hand, True)
        player_value = get_hand_value(player_hand)
        dealer_value = get_hand_value(dealer_hand)
        if dealer_value > 21:
            print(f"Диллер перебрал, выйграл ставку {bet}")
            money += bet
        elif player_value > 21 or player_value < dealer_value:
            print("Ты проиграл!")
            money -= bet
        elif player_value > dealer_value:
            print("Ты победил")
            money += bet
        elif player_value == dealer_value:
            print("Ничья, победителя нету")
        input("для продолжения нажмите enter...")


def get_bet(max_bet):
    while True:
        bet = input(f"Сколько хотите поставить от 1-{max_bet} \n"
                    "Ваш выбор").upper().strip()
        if bet == "QUIT":
            print("Выход")
            sys.exit()
        if not bet.isdecimal():
            continue
        bet = int(bet)
        if 1 <= bet <= max_bet:
            return bet


def get_deck():
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit))
            for rankd in "JQKA":
                deck.append((rankd, suit))
    random.shuffle(deck)
    return deck


def display_hands(player_hand, dealer_hand, show_dealer_hand):
    print()
    if show_dealer_hand:
        print(f"Диллер: {get_hand_value(dealer_hand)}")
        display_cards(dealer_hand)
    else:
        print("Диллер: ????")
        display_cards([BACKSIDE] + dealer_hand[1:])
    print(f"Игрок: {get_hand_value(player_hand)}")
    display_cards(player_hand)


def get_hand_value(cards):
    value = 0
    number_of_access = 0
    for card in cards:
        rank = card[0]
        if rank == "A":
            number_of_access += 1
        elif rank in "KQJ":
            value += 10
        else:
            value += int(rank)
    value += number_of_access
    for i in range(number_of_access):
        if value + 10 <= 21:
            value += 10
    return value


def display_cards(cards):
    rows = ['', '', '', '', '']
    for i, card in enumerate(cards):
        rows[0] += " ___ "
        if card == BACKSIDE:
            rows[1] += ' |## | '
            rows[2] += ' |###| '
            rows[3] += ' |_##| '
        else:
            rank, suit = card
            rows[1] += ' |{} | '.format(rank.ljust(2))
            rows[2] += ' | {} | '.format(suit)
            rows[3] += ' |_{}| '.format(rank.rjust(2, "_"))
    for row in rows:
        print(row)


def get_move(player_hand, money):
    while True:
        moves = ['(H)it', '(S)tand']
        if len(player_hand) == 2 and money > 0:
            moves.append('(D)ouble down')
        move_prompt = ", ".join(moves) + "> "
        move = input(move_prompt).upper()
        if move in "HS":
            return move
        if move == "D" and "(D)ouble down" in moves:
            return move


if __name__ == "__main__":
    main()


'''
1.  Строка 30: money = 5000 — начальная сумма денег игрока.
2.  Строка 38: bet = get_bet(money) — передача текущего баланса как максимальной ставки.
    Строка 98: if 1 <= bet <= max_bet: — проверка, что ставка не превышает баланс.
3.  Строка 38: deck.append((str(rank), suit)) и 
    строка 39: deck.append((rankd, suit)) — карта создается как кортеж (номинал, масть).
4.  Строка 32: dealer_hand = [deck.pop(), deck.pop()] и player_hand = [deck.pop(), deck.pop()] — рука представлена как список карт.
5.  Строка 89: rows = ['', '', '', '', ''] — rows[0] - верх, rows[1] - верх тела, rows[2] - центр, rows[3] - низ тела, rows[4] - низ.
6.  Строка 40: random.shuffle(deck) — перемешивание колоды. Без этого колода не будет случайной.
7.  Строка 66: money -= bet — уменьшение денег при проигрыше. Замена на += приведет к увеличению денег при проигрыше.
8.  Строка 35: display_hands(player_hand, dealer_hand, False) — False скрывает карту диллера.
    Строка 61: display_hands(player_hand, dealer_hand, True) — True показывает все карты диллера.
'''