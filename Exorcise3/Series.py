from Player import Player
from Equipment import Equipment


class Series:
    def __init__(self):
        self.equipment_list = [
            Equipment(13, 5, 10, [Player("Juan", 12, 5, 3, 6, 2, 1),
                                  Player("Carlos", 56, 7, 8, 2, 5, 3),
                                  Player("Pablo", 10, 9, 1, 11, 23, 8)]),

            Equipment(15, 7, 20, [Player("ronaldo", 4, 7, 8, 2, 1, 0),
                                  Player("Carl", 76, 20, 12, 45, 85, 8),
                                  Player("franco", 1, 49, 11, 71, 23, 58)])
        ]

    def name_player_more_batted(self):
        num_batted = 0
        name_player = ""
        for equipment in self.equipment_list:
            for player in equipment.player_list:
                if num_batted < player.batted:
                    num_batted = player.batted
                    name_player = player.name
        return name_player

    def data_the_player_highest_average(self):
        max_average = 0
        data_player = ""
        for equipment in self.equipment_list:
            for player in equipment.player_list:
                if max_average < player.average:
                    max_average = player.average
                    data_player = player
        return data_player

    def list_of_players_of_the_winning_team(self):
        list_name_player = []
        limit_winner = 0
        for equipment in self.equipment_list:
            if limit_winner < equipment.cant_game_winner:
                list_name_player = equipment.player_list
        return list_name_player
