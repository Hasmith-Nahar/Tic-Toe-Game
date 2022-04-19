winning_plays = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]
PLAYER_1 = 'O'
PLAYER_2 = 'X'
 
 
def main():
    turn = PLAYER_1
    playing = True
    plays = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    while playing:
        render_grid(plays)
        plays = get_play(turn, plays)
        if check_if_game_is_over(plays, turn):
            player_win(plays, turn)
            playing = False
            continue
        if check_if_game_is_tied(plays):
            tie(plays)
            playing = False
            continue
        turn = change_turn(turn)
        clear_console()
 
 
def render_grid(plays):
    print(f"     |     |     ")
    print(f"  {plays[0]}  |  {plays[1]}  |  {plays[2]}  ")
    print(f"-----|-----|-----")
    print(f"  {plays[3]}  |  {plays[4]}  |  {plays[5]}  ")
    print(f"     |     |     ")
    print(f"-----|-----|-----")
    print(f"  {plays[6]}  |  {plays[7]}  |  {plays[8]}  ")
    print(f"     |     |     ")
 
 
def get_play(turn, plays):
    player = '1' if turn == PLAYER_1 else '2'
    try:
        play = int(input(f"Player {player} input where you want to place an {turn}: "))
        if not play_is_valid(play, plays):
            clear_console()
            print("Invalid play, please try again!")
            render_grid(plays)
            return get_play(turn, plays)
        plays[play - 1] = turn
        return plays
    except ValueError:
        return get_play(turn, plays)
 
 
def clear_console():
    print()
    print()
    print()
    print()
    print()
    print()
 
 
def play_is_valid(play, plays):
    try:
        return plays[play - 1] == play
    except IndexError:
        return False
 
 
def change_turn(turn):
    return PLAYER_1 if turn == PLAYER_2 else PLAYER_2
 
 
def check_if_game_is_over(plays, turn):
    player_plays = [index for index, play in enumerate(plays) if play == turn]
    for winning_play in winning_plays:
        if all(x in player_plays for x in winning_play):
            return True
    return False
 
 
def check_if_game_is_tied(plays):
    player_1_plays = [index for index, play in enumerate(plays) if play == PLAYER_1]
    player_2_plays = [index for index, play in enumerate(plays) if play == PLAYER_2]
    return len(player_1_plays) + len(player_2_plays) == 9
 
 
def player_win(plays, turn):
    clear_console()
    render_grid(plays)
    player = '1' if turn == PLAYER_1 else '2'
    print(f"Congratulations Player {player}!. You Won")
 
 
def tie(plays):
    clear_console()
    render_grid(plays)
    print(f"WOW! YOU TIED!")
 
 
main()
