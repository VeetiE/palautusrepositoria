class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1_score = 0
        self.p2_score = 0
        


    def won_point(self, player_name):
        if player_name == "player1":
            self.p1_score = self.p1_score + 1
        else:
            self.p2_score = self.p2_score + 1
    
    def tie(self):
        score=''
        self.p1_score == self.p2_score
        if self.p1_score == 0:
            score = "Love-All"
        elif self.p1_score == 1:
            score = "Fifteen-All"
        elif self.p1_score == 2:
            score = "Thirty-All"
        elif self.p1_score == 3:
            score = "Forty-All"
        else:
                score = "Deuce"
        return score
    
    def advantage(self):
        score=''
        minus_result = self.p1_score - self. p2_score
        if minus_result == 1:
            score = "Advantage player1"
        elif minus_result == -1:
            score = "Advantage player2"
        elif minus_result >= 2:
            score = "Win for player1"
        else:
            score = "Win for player2"
        return score
    
    def print_score(self):
        score = ""
        temp_score = 0
        for player in range(1, 3):
            if player == 1:
                temp_score = self.p1_score
            else:
                score = score + "-"
                temp_score = self.p2_score
            if temp_score == 0:
                score = score + "Love"
            elif temp_score == 1:
                score = score + "Fifteen"
            elif temp_score == 2:
                score = score + "Thirty"
            elif temp_score == 3:
                score = score + "Forty"
        return score
    
    def get_score(self):
        score = ""
        if self.p1_score == self.p2_score:
            score=self.tie()
        elif self.p1_score >= 4 or self.p2_score >= 4:
            score=self.advantage()
        else:
            score=self.print_score()

        return score
