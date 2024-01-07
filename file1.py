def add_player(stack):
    player_code = input("Enter player code: ")
    score = int(input("Enter player score: "))
    rank = int(input("Enter player rank: "))
    record = (player_code, score, rank)
    stack.append(record)
    print("Player record added successfully!")
def delete_player(stack):
    if not stack:
        print("Stack is empty. No player records to delete.")
        return
    deleted_player = stack.pop()
    print(f"Player record deleted:\nPlayer Code: {deleted_player[0]}\nScore:{deleted_player[1]}\nRank: {deleted_player[2]}")
def display_players(stack):
    if not stack:
        print("Stack is empty. No player records to display.")
        return
    print("Player Records:")
    for player in reversed(stack):
        print(f"Player Code: {player[0]}, Score: {player[1]}, Rank:{player[2]}")
def main():
    player_stack = []
    while True:
        print("\nMenu:")
        print("1. Add Player Record")
        print("2. Delete Player Record")
        print("3. Display Player Records")
        print("4. Quit")
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            add_player(player_stack)
        elif choice == "2":
            delete_player(player_stack)
        elif choice == "3":
            display_players(player_stack)
        elif choice == "4":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
if __name__ == "__main__":
    main()