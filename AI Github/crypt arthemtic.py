import itertools

def solve_cryptarithmetic():
    # Define the letters in the puzzle
    letters = 'SENDMORY'
    
    # Create all possible permutations of digits 0-9 for these 8 letters
    for perm in itertools.permutations(range(10), len(letters)):
        # Map each letter to a digit
        s, e, n, d, m, o, r, y = perm
        
        # Make sure leading letters (S and M) are not zero
        if s == 0 or m == 0:
            continue
        
        # Convert the letters to numbers
        send = s * 1000 + e * 100 + n * 10 + d
        more = m * 1000 + o * 100 + r * 10 + e
        money = m * 10000 + o * 1000 + n * 100 + e * 10 + y
        
        # Check if the equation SEND + MORE = MONEY holds
        if send + more == money:
            print("Solution found!")
            print(f"SEND = {send}")
            print(f"MORE = {more}")
            print(f"MONEY = {money}")
            return
        
    print("No solution found.")

# Call the function to solve the problem
solve_cryptarithmetic()
