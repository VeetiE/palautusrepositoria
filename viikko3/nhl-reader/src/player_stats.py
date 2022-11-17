from player_reader import PlayerReader
from player import Player

class PlayerStats:
    def __init__(self, reader):
        self.reader=reader
        self.players=[]

    def top_scorers_by_nationality(self, nationality):
        for player_dict in self.reader.response:
            if player_dict['nationality']=='FIN':
                player = Player(
                    player_dict['name'],
                    player_dict['team'],
                    player_dict['goals'],
                    player_dict['assists'],
                    player_dict['nationality']
                )
                self.players.append(player)
        print(f"Players from {nationality}")
        self.players=sorted(self.players, key=lambda player:(player.sum()),reverse=True)
        return self.players
