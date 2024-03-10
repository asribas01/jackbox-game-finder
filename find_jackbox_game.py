from difflib import get_close_matches

def find_game_in_jackbox_packs(game_name, jackbox_packs):
    for pack_number, pack_games in jackbox_packs.items():
        if game_name in pack_games:
            return game_name, pack_number
    similar_games = get_close_matches(game_name, [game for pack_games in jackbox_packs.values() for game in pack_games], n=3, cutoff=0.6)
    if similar_games:
        print("Game not found. Did you mean:")
        for i, game in enumerate(similar_games, start=1):
            print(f"{i}. {game}")
        print("Warning: any invalid response will reset the search")  # Warning message
        while True:
            selection = input("Select a game by entering its number, or enter '0' to input again: ")
            if selection.isdigit():
                selection = int(selection)
                if 0 < selection <= len(similar_games):
                    game_to_find = similar_games[selection - 1]
                    return find_game_in_jackbox_packs(game_to_find, jackbox_packs)
                else:
                    return None  # Treat any invalid choice as if '0' was entered
    return None

jackbox_packs = {
    1: ["You Don't Know Jack", "Fibbage XL", "Drawful", "Word Spud", "Lie Swatter"],
    2: ["Fibbage 2", "Earwax", "Bidiots", "Quiplash XL", "Bomb Corp."],
    3: ["Quiplash 2", "Trivia Murder Party", "Guesspionage", "Tee K.O.", "Fakin' It"],
    4: ["Fibbage 3", "Survive the Internet", "Monster Seeking Monster", "Bracketeering", "Civic Doodle"],
    5: ["You Don't Know Jack: Full Stream", "Split the Room", "Mad Verse City", "Zeeple Dome", "Patently Stupid"],
    6: ["Trivia Murder Party 2", "Dictionarium", "Push The Button", "Joke Boat", "Role Models"],
    7: ["Quiplash 3", "The Devils and the Details", "Champ'd Up", "Talking Points", "Blather 'Round"],
    8: ["Job Job", "Weapons Drawn", "Drawful Animate", "The Poll Mine", "The Wheel of Enormous Proportions"],
    9: ["Junktopia", "Quixort", "Roomerang", "Nonsensory", "Fibbage 4"],
    10: ["Fixy Text", "Tee K.O. 2", "Dodo Re Mi", "Time Jinx", "Hypnotorious"]
}

while True:
    game_to_find = input("Enter the name of the game you want to find: ").lower()
    found_game = find_game_in_jackbox_packs(game_to_find, jackbox_packs)
    if found_game:
        game_name, pack_number = found_game
        print(f"Found {game_name} in Jackbox Party Pack {pack_number}.")
    else:
        print("Game not found.")
