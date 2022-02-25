from Player import Player
from Equipment import Equipment


class Series:
    def __init__(self):
        self.player_list = [
            Player("Juan", 12, 5, 3, 6, 2, 1),
            Player("Carlos", 56, 7, 8, 2, 5, 3),
            Player("Pablo", 10, 9, 1, 11, 23, 8)

        ]

    def name_player_more_batted(self):
        num_batted = 999999
        name_player = ""
        for player in self.player_list:
            if num_batted > player.batted:
                num_batted = player.batted
                name_player = player.name
        return name_player

    def data_the_player_highest_average(self):
        data_player = ""
        for player in self.player_list:
            average = player.hits + player.double + player.triple + player.homeruns / 4
            data_player = player
        return data_player

    def list_of_players_of_the_winning_team(self):
        pass
