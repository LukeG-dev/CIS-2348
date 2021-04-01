#  Luke Gilin 1216992

class Team:
    def __init__(self):
        self.team_name = 'none'
        self.team_wins = 0
        self.team_losses = 0

    def get_win_percentage(self):

        win_percentage = self.team_wins / (self.team_wins + self.team_losses)
        return win_percentage


if __name__ == '__main__':
    #  Get input from user
    TeamName = input()
    TeamWins = int(input())
    TeamLosses = int(input())

    Myteam = Team()
    Myteam.team_name = TeamName
    Myteam.team_losses = TeamLosses
    Myteam.team_wins = TeamWins
    percentage = Myteam.get_win_percentage()

    if percentage > .50:
        print('Congratulations, Team {team} has a winning average!'.format(team=TeamName))
    else:
        print('Team {name} has a losing average.'.format(name=TeamName))