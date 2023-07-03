from src.enum.common import Card as CardEnum, Suit as SuitEnum, Combination as CombinationEnum
from src.model.combination import Combination
from random import randint
from copy import deepcopy


class Player:
    def __init__(self):
        self.name = None
        self.hand = []
        self.hand_info = None
        self.combination = None

    def get_name(self):
        self.name = list_of_names[list_of_players.index(self)]

    def sort_a_hand_by_card_value_reversed(self):
        """Сортировка руки по значению карт в обратном порядке"""
        self.hand = list(sorted(self.hand, key=lambda x: x.value, reverse=True))

    def take_a_card(self, deck):
        """Взять карту из колоды"""
        random_card_index = randint(0, len(deck) - 1)
        card = deck.pop(random_card_index)
        self.hand.append(card)
        if len(self.hand) > 1:
            self.sort_a_hand_by_card_value_reversed()

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
                # for card_enum in CardEnum:
                #     if card_enum.value == highest_card_value:
                #         highest_card_name = card_enum.name
                #         self.combination = Combination(
                #             name=CombinationEnum.STRAIGHT.name,
                #             value=CombinationEnum.STRAIGHT.value,
                #             highest_card_name=highest_card_name,
                #             highest_card_value=highest_card_value
                #         )
                self.remove_wheel_ace_from_full_hand_info()
                break
        self.remove_wheel_ace_from_full_hand_info()

    def check_for_flush(self):
        suit_counter = {SuitEnum.value_list()[i]: 0 for i in range(len(SuitEnum.value_list()))}
        for card in self.hand:
            suit_counter[card.suit_value] += 1
        for key, value in suit_counter.items():
            if value >= 5:
                self.combination = Combination(
                    name=CombinationEnum.FLUSH.name,
                    value=CombinationEnum.FLUSH.value
                )
                for card in self.hand:
                    if card.suit_value == key:
                        self.combination.cards.append(card)

    def check_for_combinations(self):
        self.get_hand_info()
        if self.combination is None:
            print(f"{self.name} wanted to check the STRAIGHT_FLUSH")  # Нужна логика флеш-рояля
            if self.combination is None:
                print(f"{self.name} wanted to check the FOUR_OF_A_KIND")
                if self.combination is None:
                    print(f"{self.name} wanted to check the FULL_HOUSE")
                    if self.combination is None:
                        self.check_for_flush()
                        if self.combination is None:
                            print(f"{self.name} wanted to check the STRAIGHT")
                            # self.check_for_straight()  # Доделать метод
                            if self.combination is None:
                                print(f"{self.name} wanted to check the THREE_OF_A_KIND")
                                if self.combination is None:
                                    print(f"{self.name} wanted to check the TWO_PAIR")
                                    if self.combination is None:
                                        print(f"{self.name} wanted to check the PAIR")
                                        if self.combination is None:
                                            print(f"{self.name} wanted to check the HIGH_CART")

        if self.combination:
            print(f"{self.name} - {self.combination.name}!")
            for card in self.combination.cards:
                print(card.name, card.suit_name)


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


list_of_names = ["player_1", "player_2", "player_3", "player_4", "player_5", "player_6", "player_7"]


# # ПЕРЕМЕСТИТЬ В CONFIG ???
# def get_name(list_of_players):
#     """Присваиваем игрокам имя"""
#     for player in list_of_players:
#         player.name = list_of_names[list_of_players.index(player)]


def take_cards():
    """"""


if __name__ == "__main__":
    # TO_DO:
    # - сравнение комбинаций (перегрузка операторов)
    # - метод перемешивания колоды после её генерации

    num_of_players = 3
    list_of_players = [Player() for _ in range(num_of_players)]  # Создаем список игроков
    for player in list_of_players:
        player.get_name()  # Присваиваем игрокам имена
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
        # player.name = list_of_names[list_of_players.index(player)]  # Присваиваем игрокам имя
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
        player.sort_a_hand_by_card_value_reversed()
        print(f"{player.name} hand:")
        for card in player.hand:
            print(f"{card.name=} {card.suit_name=}")
        # Проверяем комбинации игроков
        player.check_for_combinations()
