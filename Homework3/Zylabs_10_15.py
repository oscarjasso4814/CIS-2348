class Team:
    def __init__(self):
        self.name = 'none'
        self.wins = 0
        self.losses = 0

    def get_win_percentage(self):
        win_percent = self.wins / (self.wins + self.losses)
        return win_percent

    def print_standing(self):
        percent = team.get_win_percentage()
        if percent >= 0.5:
            print('Congratulations, Team', team.name, 'has a winning average!')
        else:
            print('Team', team.name, 'has a losing average.')


if __name__ == "__main__":
    team = Team()

    user_name = input()
    user_wins = int(input())
    user_losses = int(input())

    team.name = user_name
    team.wins = user_wins
    team.losses = user_losses

    team.print_standing()

