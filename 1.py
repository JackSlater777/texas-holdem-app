from src.enum.common import CardValue, CardSuit
from random import randint


class Player:
    def __init__(self, hand):
        self.hand = hand
        self.combination = None

    def get_name(self):
        for k, v in globals().items():
            if v is self:
                return k

    # def find_combination(self):
    #     for card in self.hand:
    #         pass

    def find_flush(self):
        suit_counter = {CardSuit.list()[i]: 0 for i in range(len(CardSuit.list()))}
        for card in self.hand:
            suit_counter[card.suit] += 1
        print(suit_counter)
        for value in suit_counter.values():
            if value >= 5:
                # self.combination = Combination(
                #     name=
                # )
                (print(f"{self.get_name()} has a flush!"))


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit  # Масть


class CardDeck:
    def __init__(self, cards):
        self.cards = cards

    def prepare(self):
        """Подготавливаем полную колоду"""
        for card_value in CardValue.list():
            for card_suit in CardSuit.list():
                card = Card(
                    value=card_value,
                    suit=card_suit
                )
                self.cards.append(card)  # Добавляем карту в колоду


class Board:
    def __init__(self, cards):
        self.cards = cards


class Combination:
    def __init__(self, name, highest_card):
        self.name = name
        self.highest_card = highest_card


def give_cards(num_of_cards, receiver, deck):
    cnt = 0
    while cnt < num_of_cards:
        random_card_index = randint(0, len(deck)-1)
        card = deck.pop(random_card_index)
        receiver.append(card)
        yield
        cnt += 1


if __name__ == "__main__":
    # num_of_players = 3

    card_deck = CardDeck(cards=[])  # Создаем колоду
    card_deck.prepare()  # Наполняем колоду

    # list_of_players = []
    # for _ in range(num_of_players):
    #     pass

    player_one = Player(hand=[])  # Создаем 1 игрока
    player_two = Player(hand=[])  # Создаем 2 игрока
    # Создаем генераторы для игроков
    give_cards_player_one = give_cards(2, player_one.hand, card_deck.cards)
    give_cards_player_two = give_cards(2, player_two.hand, card_deck.cards)
    # Выдаем по очереди по 2 карты игрокам
    next(give_cards_player_one)
    next(give_cards_player_two)
    next(give_cards_player_one)
    next(give_cards_player_two)

    print("First player's hand:")
    for card in player_one.hand:
        print(f"{card.value=} {card.suit=}")
    print("***********************************")
    print("Second player's hand:")
    for card in player_two.hand:
        print(f"{card.value=} {card.suit=}")

    board = Board(cards=[])  # Создаем доску
    # Создаем генератор для борда
    give_cards_desc = give_cards(5, board.cards, card_deck.cards)
    # Выложим флоп
    print("***********************************")
    print("The board - the flop:")
    next(give_cards_desc)
    next(give_cards_desc)
    next(give_cards_desc)
    for card in board.cards:
        print(f"{card.value=} {card.suit=}")
    # Выложим терн
    print("***********************************")
    print("The Desk - the turn:")
    next(give_cards_desc)
    for card in board.cards:
        print(f"{card.value=} {card.suit=}")
    # Выложим ривер
    print("***********************************")
    print("The Desk - the river:")
    next(give_cards_desc)
    for card in board.cards:
        print(f"{card.value=} {card.suit=}")

    # Добавляем карты с борда в руки игрокам для установки комбинации
    for card in board.cards:
        player_one.hand.append(card)
        player_two.hand.append(card)
    print("***********************************")
    print("First player's hand:")
    for card in player_one.hand:
        print(f"{card.value=} {card.suit=}")
    print("***********************************")
    print("Second player's hand:")
    for card in player_two.hand:
        print(f"{card.value=} {card.suit=}")


    player_one.find_flush()
    player_two.find_flush()
