def count_sequence_repeats(sequence, history):
    count = 0
    seq_length = len(sequence)
    history_length = len(history)

    for i in range(history_length - seq_length + 1):
        if history[i:i+seq_length] == sequence:
            count += 1

    return count

# Example opponent history
opponent_history = ["R", "P", "R", "P", "S", "R", "R", "P", "P", "S"]

# Sequence to count
quincy_choices = ["R", "R", "P", "P", "S"]

repeats_count = count_sequence_repeats(quincy_choices, opponent_history)
print("Number of times Quincy's sequence repeats:", repeats_count)
