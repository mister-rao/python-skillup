games = ["PUBG", "AC: Odyssey", "Foriza Horizon 4", "FIFA 21", "Call of Duty: Modern Warfare"]
rented_games = {}

def display_available_games():
    print("List of available games:")
    for game in games:
        print("- " + game)

def rent_game(person, game, due_date):
    if game in games:
        games.remove(game)
        rented_games[game] = (person, due_date)
        print("Game successfully rented to " + person + " until " + due_date)
    else:
        print("The game is not available.")

def return_game(game):
    if game in rented_games:
        person, due_date = rented_games.pop(game)
        games.append(game)
        print(game + " has been returned by " + person)
    else:
        print("This game has not been rented out.")

# Example usage
display_available_games()
rent_game("Jilan", "PUBG", "2023-02-20")
display_available_games()
return_game("PUBG")
display_available_games()

rent_game("kohli","FIFA 21","2023-02-24")
display_available_games()
