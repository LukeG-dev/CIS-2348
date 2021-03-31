#  Luke Gilin 1216992

class Team:
    def __init__(self, name='none'):
        self.name = name
        self.teamwins = 0
        self.team_losses = 0

    def get_win_percentage(self, team_wins, team_losses):
        percentage = team_wins / (team_wins + team_losses)
        if percentage > .50:
            print('Congratulations, Team {team} has a winning average!'.format(team=self.name))
        else:
            print('Team {name} has a losing average.'.format(name=self.name))


if __name__ == '__main__':
    #  Get input from user
    TeamName = input()
    TeamWins = int(input())
    TeamLosses = int(input())

    MyTeam = Team(TeamName)
    MyTeam.get_win_percentage(TeamWins, TeamLosses)



