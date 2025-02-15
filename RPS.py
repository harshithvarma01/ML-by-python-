import random

def player(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)
    
    if not opponent_history:
        return random.choice(["R", "P", "S"])
    
    # Sometimes choose randomly, sometimes use the strategy
    if random.random() < 0.3:  # 30% chance of random move
        return random.choice(["R", "P", "S"])
    
    # Predict the opponent's next move based on the most frequent past move
    most_common = max(set(opponent_history), key=opponent_history.count)
    
    # Counter the predicted move
    counter_moves = {"R": "P", "P": "S", "S": "R"}
    
    return counter_moves[most_common]

# Simulate a series of moves between the player and the opponent
def simulate_game():
    opponent_moves = ["R", "P", "S", "R", "P", "P", "S"]  # Example opponent's moves
    player_moves = []
    prev_play = None

    for move in opponent_moves:
        player_move = player(prev_play, opponent_history=player_moves)
        player_moves.append(player_move)
        prev_play = move
        print(f"Opponent: {move} | Player: {player_move}")

simulate_game()
