import tkinter as tk
import random
from PIL import Image, ImageTk

class BearCowboyNinjaGame:
    def __init__(self, root):
        """
        Initialize the game window and widgets.
        :param root: The root window of the Tkinter application.
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        self.root = root
        self.root.title("Bear, Cowboy, Ninja Game")
        self.root.state('zoomed')  # Make the window fullscreen
        self.root.resizable(True, True)  # Allow window resizing

        # Load background image
        self.background_image = ImageTk.PhotoImage(Image.open("images/background.png"))
        self.background_label = tk.Label(self.root, image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1)  # Cover the entire window with the background

        # Initialize game stats
        self.user_wins = 0
        self.cpu_wins = 0
        self.draws = 0

        # Create the game widgets
        self.create_widgets()

    def create_widgets(self):
        """
        Create and place all the widgets in the game window.
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        # Introductory label
        self.intro_label = tk.Label(self.root, text="Welcome to Bear, Cowboy, Ninja!", font=("Helvetica", 24, "bold"), bg="#FFFFCC")
        self.intro_label.pack(pady=20)  # Padding for better spacing

        # Instructions label
        self.instructions = tk.Label(self.root, text="Choose your character:", font=("Helvetica", 18), bg="#FFFFCC")
        self.instructions.pack()

        # Frame for the buttons and captions
        self.button_frame = tk.Frame(self.root, bg="#FFFFCC")
        self.button_frame.pack(pady=20)

        # Load character images
        self.bear_image = ImageTk.PhotoImage(Image.open("images/bear.png").resize((150, 150)))
        self.cowboy_image = ImageTk.PhotoImage(Image.open("images/cowboy.png").resize((150, 150)))
        self.ninja_image = ImageTk.PhotoImage(Image.open("images/ninja.png").resize((150, 150)))

        # Create buttons with images and captions
        self.create_button_with_caption("Bear", self.bear_image, self.button_frame, 0)
        self.create_button_with_caption("Cowboy", self.cowboy_image, self.button_frame, 1)
        self.create_button_with_caption("Ninja", self.ninja_image, self.button_frame, 2)

        # Result and stats labels
        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 16), bg="#FFFFCC")
        self.result_label.pack(pady=20)

        self.stats_label = tk.Label(self.root, text="", font=("Helvetica", 16), bg="#FFFFCC")
        self.stats_label.pack(pady=20)

    def create_button_with_caption(self, caption, image, frame, column):
        """
        Create a button with a caption and place it in the specified frame.
        :param caption: The text caption for the button.
        :param image: The image to display on the button.
        :param frame: The frame in which to place the button.
        :param column: The column position for the button.
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        # Create the caption label and place it in the frame
        caption_label = tk.Label(frame, text=caption, font=("Helvetica", 14), bg="#FFFFCC")
        caption_label.grid(row=0, column=column, padx=20, pady=10)

        # Create the button with the image and place it in the frame
        button = tk.Button(frame, image=image, command=lambda: self.choose_character(caption), borderwidth=2, relief="solid")
        button.grid(row=1, column=column, padx=20, pady=10)

    def choose_character(self, player_choice):
        """
        Handle the event when the player chooses a character.
        :param player_choice: The character chosen by the player.
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        # Choose a character for the opponent
        opponent = self.opponent_choice()
        
        # Determine the result of the battle
        result = self.battle(player_choice, opponent)
        
        # Update the result label
        self.result_label.config(text=f"You chose: {player_choice}\nOpponent: {opponent}\n{result}")
        
        # Update game statistics
        self.update_stats(result)

    def opponent_choice(self):
        """
        Randomly choose a character for the opponent.
        :return: The character chosen for the opponent.
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        return random.choice(["Bear", "Cowboy", "Ninja"])

    def battle(self, player, opponent):
        """
        Determine the result of the battle between the player's choice and the opponent's choice.
        :param player: The character chosen by the player.
        :param opponent: The character chosen by the opponent.
        :return: The result of the battle.
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        # Define the outcomes of the battles between characters
        outcomes = {
            ("Bear", "Cowboy"): "Bear wins! The Cowboy is no match for the Bear's strength.",
            ("Bear", "Ninja"): "Ninja wins! The Bear is outmaneuvered by the Ninja's agility.",
            ("Cowboy", "Bear"): "Cowboy wins! The Bear is outsmarted by the Cowboy's quick draw.",
            ("Cowboy", "Ninja"): "Ninja wins! The Cowboy's gun skills can't keep up with the Ninja's speed.",
            ("Ninja", "Bear"): "Ninja wins! The Bear is outmaneuvered by the Ninja's agility.",
            ("Ninja", "Cowboy"): "Ninja wins! The Cowboy's gun skills can't keep up with the Ninja's speed.",
        }

        # Determine the result of the battle
        if player == opponent:
            result = f"It's a tie! Both {player}s are evenly matched."
            self.update_stats("draw")
        else:
            result = outcomes.get((player, opponent), "It's a tie!")
            if "wins" in result:
                if player in result:
                    self.update_stats("user wins")
                else:
                    self.update_stats("cpu wins")
        
        return result

    def update_stats(self, outcome=None):
        """
        Update the game statistics based on the outcome of the battle.
        :param outcome: The outcome of the battle.
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if outcome:
            if "draw" in outcome.lower():
                self.draws += 1
            elif "user wins" in outcome:
                self.user_wins += 1
            else:
                self.cpu_wins += 1

        # Calculate total games played
        total_games = self.user_wins + self.cpu_wins + self.draws
        
        # Calculate win percentages
        user_win_percentage = (self.user_wins / total_games * 100) if total_games > 0 else 0
        cpu_win_percentage = (self.cpu_wins / total_games * 100) if total_games > 0 else 0
        draw_percentage = (self.draws / total_games * 100) if total_games > 0 else 0

        # Update the statistics label
        stats_text = (f"User Wins: {self.user_wins}\n"
                      f"CPU Wins: {self.cpu_wins}\n"
                      f"Draws: {self.draws}\n"
                      f"User Win Percentage: {user_win_percentage:.2f}%\n"
                      f"CPU Win Percentage: {cpu_win_percentage:.2f}%\n"
                      f"Draw Percentage: {draw_percentage:.2f}%")
        
        self.stats_label.config(text=stats_text)

