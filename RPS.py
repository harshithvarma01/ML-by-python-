import random
def player(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)
    if not opponent_history:
        return random.choice(["R", "P", "S"])
    # Count occurrences of each move
    move_counts = {"R": 0, "P": 0, "S": 0}
    for move in opponent_history:
        move_counts[move] += 1
    # Predict opponent's next move 
    predicted_move = max(move_counts, key=move_counts.get)
    # Counter the predicted move
    counter_moves = {"R": "P", "P": "S", "S": "R"}
    return counter_moves[predicted_move]
print(player("R"))