from src.enum.common import CardValue, CardSuit
from random import randint


class Player:
    def __init__(self):
        self.name = None
        self.hand = []
        self.combination = None

    def take_a_card(self, deck):
        """Взять карту из колоды"""
        random_card_index = randint(0, len(deck) - 1)
        card = deck.pop(random_card_index)
        self.hand.append(card)

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
                (print(f"{self.name} has a flush!"))


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit  # Масть


class CardDeck:
    def __init__(self):
        self.cards = []
        self.prepare()

    def prepare(self):
        """Подготавливаем полную колоду"""
        for card_value in CardValue.list():
            for card_suit in CardSuit.list():
                card = Card(
                    value=card_value,
                    suit=card_suit
                )
                self.cards.append(card)  # Добавляем карту в колоду


class Combination:
    def __init__(self, name, highest_card):
        self.name = name
        self.highest_card = highest_card


list_of_names = ["player_1", "player_2", "player_3", "player_4", "player_5", "player_6", "player_7"]


if __name__ == "__main__":
    num_of_players = 3
    list_of_players = [Player() for _ in range(num_of_players)]  # Создаем список игроков
    discards = Player()  # Создаем "отбой"
    board = Player()  # Создаем доску
    card_deck = CardDeck()  # Создаем и наполняем колоду

    # Выдаем по очереди по 1 карте игрокам 2 круга
    cnt = 0
    while cnt < 2:
        for player in list_of_players:
            player.take_a_card(card_deck.cards)
        cnt += 1

    for player in list_of_players:
        player.name = list_of_names[list_of_players.index(player)]  # Присваиваем игрокам имя
        print("***********************************")
        print(f"{player.name} hand:")
        for card in player.hand:
            print(f"{card.value=} {card.suit=}")

    # Флоп
    print("***********************************")
    print("The board - the flop:")
    discards.take_a_card(card_deck.cards)  # 1 карта в отбой
    board.take_a_card(card_deck.cards)
    board.take_a_card(card_deck.cards)
    board.take_a_card(card_deck.cards)
    for card in board.hand:
        print(f"{card.value=} {card.suit=}")

    # Терн
    print("***********************************")
    print("The board - the turn:")
    discards.take_a_card(card_deck.cards)  # 1 карта в отбой
    board.take_a_card(card_deck.cards)
    for card in board.hand:
        print(f"{card.value=} {card.suit=}")

    # Ривер
    print("***********************************")
    print("The board - the river:")
    discards.take_a_card(card_deck.cards)  # 1 карта в отбой
    board.take_a_card(card_deck.cards)
    for card in board.hand:
        print(f"{card.value=} {card.suit=}")

    # Добавляем карты с борда в руки игрокам для установки комбинации
    for player in list_of_players:
        for card in board.hand:
            player.hand.append(card)
        print("***********************************")
        print(f"{player.name} hand:")
        for card in player.hand:
            print(f"{card.value=} {card.suit=}")


    # player_one.find_flush()
    # player_two.find_flush()
