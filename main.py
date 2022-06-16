from sportsipy.nhl.teams import Teams
from sportsipy.nhl.roster import Player

def test():
    current_season = '2021-22'
    teams = Teams()
    for team in teams:
        print(team.name)
        roster = team.roster
        for player in roster.players:
            adjusted_point_shares = round(player(current_season).point_shares * (82 / player(current_season).
                                                                                 games_played), 2)
            print(player(current_season).name, player(current_season).point_shares, adjusted_point_shares)


# TODO:  Iterate through rosters of all teams
#       If FWD or DEF, get the point shares (PS), standardize to a per-82 to account for injuries
#       ie, if player played 52 games, calculate (PS) * (82/GP)
#       if GOALIE, get the GSAA


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test()