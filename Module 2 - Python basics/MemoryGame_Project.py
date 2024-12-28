from random import shuffle

def reset_cards_state(cards):
    return {
        card: {"flipped": False, "matched": False} for card in cards
    }

def shuffle_cards():
    card_list = ["A1", "A2", "B1", "B2", "C1", "C2", "D1", "D2", "E1", "E2", "F1", "F2"]
    shuffle(card_list)
    return card_list

def check_win(cards_state):
    return all(cards_state[card]["matched"] for card in cards_state)

def flip_card(index, cards_deck, cards_state):
    index -= 1
    if index < 0 or index >= len(cards_deck):
        print("Invalid card index. Please choose a number between 1-12.")
        return None
    card = cards_deck[index]
    if cards_state[card]["matched"]:
        print("This card is already matched. Please choose another.")
        return None
    if cards_state[card]["flipped"]:
        print("This card is already flipped. Please choose another.")
        return None
    cards_state[card]["flipped"] = True
    return cards_state

def check_match(cards_state):
    flipped_cards = [card for card in cards_state if cards_state[card]["flipped"]]
    if len(flipped_cards) != 2:
        print("Two cards must be flipped to check for a match.")
        return
    card1, card2 = flipped_cards
    if card1[0] == card2[0]:
        print(f"Match found! ({card1}, {card2})")
        cards_state[card1]["matched"] = True
        cards_state[card2]["matched"] = True
    else:
        print(f"No match. ({card1}, {card2})")
        cards_state[card1]["flipped"] = False
        cards_state[card2]["flipped"] = False

def display_cards(cards, cards_state):
    cards_display = ""
    for card in cards:
        if cards_state[card]["flipped"] or cards_state[card]["matched"]:
            cards_display += f"[{card[0]}] "
        else:
            cards_display += "[#] "
    rows = [cards_display[i:i + 16] for i in range(0, len(cards_display), 16)]
    return "\n".join(rows).strip()

def game_init():
    print("Welcome to the memory game!")
    cards_deck = shuffle_cards()
    current_cards_state = reset_cards_state(cards_deck)
    while True:
        print(display_cards(cards_deck, current_cards_state))
        if check_win(current_cards_state):
            print("You Won!")
            break
        for num in ["first", "second"]:
            while True:
                try:
                    index = int(input(f"Choose {num} card (1-12): "))
                    updated_state = flip_card(index, cards_deck, current_cards_state)
                    if updated_state:
                        current_cards_state = updated_state
                        break
                except ValueError:
                    print("Invalid input. Please enter a number between 1 and 12.")
            print(display_cards(cards_deck, current_cards_state))
        check_match(current_cards_state)

while True:
    game_init()
    if input("Play again? (yes/no): ").strip().lower() not in ["yes", "y"]:
        print("Goodbye!")
        break