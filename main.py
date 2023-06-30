from src.enum.common import Card as CardEnum, Suit as SuitEnum, Combination as CombinationEnum
from random import randint
from copy import deepcopy


class Player:
    def __init__(self):
        self.name = None
        self.hand = []
        self.hand_info = None
        self.combination = None

    def take_a_card(self, deck):
        """Взять карту из колоды"""
        random_card_index = randint(0, len(deck) - 1)
        card = deck.pop(random_card_index)
        self.hand.append(card)

    def get_hand_info(self):
        info = [
            0,  # card.value
            0,  # amount
            False,  # DIAMONDS
            False,  # CLUBS
            False,  # HEARTS
            False,  # SPADES
        ]
        self.hand_info = [deepcopy(info) for _ in range(len(CardEnum.name_list()))]

        for i in range(len(self.hand_info)):
            self.hand_info[i][0] = CardEnum.value_list()[i]  # Устанавливаем card.value
            for card in self.hand:
                if card.value == self.hand_info[i][0]:
                    self.hand_info[i][1] += 1  # Увеличиваем amount
                    self.hand_info[i][card.suit_value + 1] = True  # Устанавливаем флаг масти

    def add_wheel_ace_into_full_hand_info(self):
        self.hand_info.insert(0, deepcopy(self.hand_info[-1]))
        self.hand_info[0][0] = 1

    def remove_wheel_ace_from_full_hand_info(self):
        del self.hand_info[0]

    def check_for_straight(self):
        self.add_wheel_ace_into_full_hand_info()
        cnt = 0
        highest_card_value = False
        for i in range(len(self.hand_info) - 1, -1, -1):
            if self.hand_info[i][1] == 0:
                highest_card_value = False
                cnt = 0
            elif self.hand_info[i][1] > 0:
                cnt += 1
                if cnt == 1:
                    highest_card_value = self.hand_info[i][0]
            if cnt == 5:
                for card_enum in CardEnum:
                    if card_enum.value == highest_card_value:
                        highest_card_name = card_enum.name
                        self.combination = Combination(
                            name=CombinationEnum.STRAIGHT.name,
                            value=CombinationEnum.STRAIGHT.value,
                            highest_card_name=highest_card_name,
                            highest_card_value=highest_card_value
                        )
                (print(f"{self.name} - {self.combination.name}, {self.combination.highest_card_name}!"))
                self.remove_wheel_ace_from_full_hand_info()
                break
        self.remove_wheel_ace_from_full_hand_info()

    def check_for_flush(self):
        suit_counter = {SuitEnum.value_list()[i]: 0 for i in range(len(SuitEnum.value_list()))}
        for card in self.hand:
            suit_counter[card.suit_value] += 1
        print(suit_counter)

        for value in suit_counter.values():
            if value >= 5:
                # self.combination = Combination(
                #     name=CombinationName.FLUSH.value,
                #     value=CombinationValue.FLUSH.value,
                #     highest_card_value=None  # ДОДЕЛАТЬ!
                # )
                # (print(f"{self.name} - {CombinationName.FLUSH.value}!"))
                (print(f"{self.name} - Flush!"))


class Card:
    def __init__(self, name, value, suit_name, suit_value):
        self.name = name
        self.value = value
        self.suit_name = suit_name
        self.suit_value = suit_value


class Deck:
    def __init__(self):
        self.cards = []
        self.prepare()

    def prepare(self):
        """Подготавливаем полную колоду"""
        for card_enum in CardEnum:
            for suit_enum in SuitEnum:
                card = Card(
                    name=card_enum.name,
                    value=card_enum.value,
                    suit_name=suit_enum.name,
                    suit_value=suit_enum.value
                )
                self.cards.append(card)  # Добавляем карту в колоду


class Combination:
    def __init__(self, name, value, highest_card_name, highest_card_value):
        self.name = name
        self.value = value
        self.highest_card_name = highest_card_name
        self.highest_card_value = highest_card_value


list_of_names = ["player_1", "player_2", "player_3", "player_4", "player_5", "player_6", "player_7"]


if __name__ == "__main__":
    # TO_DO:
    # - написать метод перемешивания колоды

    num_of_players = 3
    list_of_players = [Player() for _ in range(num_of_players)]  # Создаем список игроков
    discards = Player()  # Создаем "отбой"
    board = Player()  # Создаем доску
    deck = Deck()  # Создаем и наполняем колоду

    # Выдаем по очереди по 1 карте игрокам 2 раза
    cnt = 0
    while cnt < 2:
        for player in list_of_players:
            player.take_a_card(deck.cards)
        cnt += 1

    for player in list_of_players:
        player.name = list_of_names[list_of_players.index(player)]  # Присваиваем игрокам имя
        print("***********************************")
        print(f"{player.name} hand:")
        for card in player.hand:
            print(f"{card.name=} {card.suit_name=}")

    # Флоп
    print("***********************************")
    print("The board - the flop:")
    discards.take_a_card(deck.cards)  # 1 карта в отбой
    board.take_a_card(deck.cards)
    board.take_a_card(deck.cards)
    board.take_a_card(deck.cards)
    for card in board.hand:
        print(f"{card.name=} {card.suit_name=}")

    # Терн
    print("***********************************")
    print("The board - the turn:")
    discards.take_a_card(deck.cards)  # 1 карта в отбой
    board.take_a_card(deck.cards)
    for card in board.hand:
        print(f"{card.name=} {card.suit_name=}")

    # Ривер
    print("***********************************")
    print("The board - the river:")
    discards.take_a_card(deck.cards)  # 1 карта в отбой
    board.take_a_card(deck.cards)
    for card in board.hand:
        print(f"{card.name=} {card.suit_name=}")

    # Добавляем карты с борда в руки игрокам для установки комбинации
    for player in list_of_players:
        for card in board.hand:
            player.hand.append(card)
        print("***********************************")
        print(f"{player.name} hand:")
        for card in player.hand:
            print(f"{card.name=} {card.suit_name=}")
        # Проверяем комбинации игроков
        # player.search_combination()
        player.get_hand_info()
        # player.check_for_flush()
        player.check_for_straight()
