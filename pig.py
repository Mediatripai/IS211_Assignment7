import random
import argparse

class Player:
    """Represents a player in the game of Pig."""

    def __init__(self, name):
        """Initializes a new Player object with the given name."""
        self.name = name
        self.score = 0
        self.turn_score = 0

    def hold(self):
        """Adds the current turn score to the player's total score and resets the turn score."""
        self.score += self.turn_score
        self.turn_score = 0

    def reset_turn_score(self):
        """Resets the player's turn score to 0."""
        self.turn_score = 0

class Die:
    """Represents a six-sided die."""

    def __init__(self, sides=6):
        """Initializes a new Die object with the specified number of sides."""
        self.sides = sides

    def roll(self):
        """Rolls the die and returns a random number between 1 and the number of sides."""
        return random.randint(1, self.sides)

class Game:
    """Represents a game of Pig."""

    def __init__(self, player_names):
        """Initializes a new Game object with the specified player names."""
        self.die = Die()
        self.players = [Player(name) for name in player_names]
        self.current_player = 0  # Use index for current player

    def switch_turn(self):
        """Switches to the next player's turn."""
        self.current_player = (self.current_player + 1) % len(self.players)

    def play_turn(self):
        """Plays a single turn for the current player."""
        current_player = self.players[self.current_player]
        print(f"{current_player.name}'s turn. Current score: {current_player.turn_score}, Total score: {current_player.score}")
        while True:
            decision = input("Press 'r' to roll or 'h' to hold: ").strip().lower()
            if decision == 'r':
                roll = self.die.roll()
                print(f"{current_player.name} rolled a {roll}")
                if roll == 1:
                    print(f"{current_player.name} loses this turn's points!")
                    current_player.reset_turn_score()
                    break
                else:
                    current_player.turn_score += roll
                    # Update and display the scorecard
                    self.display_scorecard()
            elif decision == 'h':
                current_player.hold()
                # Update and display the scorecard
                self.display_scorecard()
                break
            else:
                print("Invalid input. Please choose 'r' to roll or 'h' to hold.")

    def display_scorecard(self):
        """Displays the current scores for all players."""
        print("\nCurrent Scores:")
        for player in self.players:
            print(f"{player.name}: {player.score}")
        print()

    def check_winner(self):
        """Checks if a player has won the game."""
        for player in self.players:
            if player.score >= 100:
                return player
        return None

    def play_game(self):
        """Plays the entire game of Pig."""
        while True:
            self.play_turn()
            winner = self.check_winner()
            if winner:
                print(f"{winner.name} wins with a score of {winner.score}!")
                break
            self.switch_turn()

def main():
    """Main function to start the game."""
    # Set up argparse to allow for a configurable number of players
    parser = argparse.ArgumentParser(description="Play a game of Pig!")
    parser.add_argument('--numPlayers', type=int, default=2, help='Number of players (default: 2)')
    args = parser.parse_args()

    # Collect player names
    player_names = []
    for i in range(1, args.numPlayers + 1):
        name = input(f"Enter the name for Player {i}: ")
        player_names.append(name)

    # Start the game
    game = Game(player_names)
    game.play_game()

if __name__ == "__main__":
    main()
    for i in range(1, args.numPlayers + 1):
        name = input(f"Enter the name for Player {i}: ")
        player_names.append(name)

    # Start the game
    game = Game(player_names)
    game.play_game()

if __name__ == "__main__":
    main()