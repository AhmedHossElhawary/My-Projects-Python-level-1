import random
import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def hangman_stages():
    return [  """
            +-------+
                    |
                    |
                    | 
                    |
                    |
         ==============
        """,
        """
            +-------+
            |       |
            0       |
                    |       
                    |
                    |
         ==============
        """,
        """
            +-------+
            |       |
            0       |
            |       |
                    |
                    |
         ==============
        """,
        """
            +-------+
            |       |
            0       |
           -|       |
                    |
                    |
         ==============
        """,
        """
            +-------+
            |       |
            0       |      
           -|-      |
                    |
                    |
         ==============
        """,
        """
            +-------+
            |       |
            0       |
           -|-      |
           /        |
                    |
         ==============
        """,
        """
            +-------+
            |       |
            0       |
           -|-      |
           / \      |
                    |
         ==============
        """]

def random_word():
    words = ["cat", "dog", "bird", "fish", "sun", "moon", "torch", "tree", "flower", "car", "house", "computer", "phone", "book", "pen", "pencil", "paper", "chair", "table", "bed", "sofa", "couch", "lamp", "clock", "mirror", "window", "door", "wall", "floor", "ceiling", "roof", "garden",\
              "park", "beach", "mountain", "river", "lake", "ocean", "sky", "cloud", "rain", "snow", "wind", "storm", "thunder", "lightning", "sunrise", "sunset", "day", "night", "week", "month", "year", "time", "calendar", "season", "spring", "summer", "autumn", "winter", "holiday", "vacation",\
                  "travel", "adventure", "explore", "discover", "learn", "teach", "friend", "family", "love", "happiness", "sadness", "anger", "fear", "surprise", "joy", "hope", "dream", "goal", "success", "failure", "challenge", "opportunity", "change", "growth", "health", "fitness", "nutrition", \
                    "exercise", "yoga", "meditation", "relaxation", "stress", "anxiety", "depression", "mindfulness", "selfcare", "wellness", "hobby", "music", "art", "dance", "sports", "game", "fun", "entertainment", "movie", "book", "tv", "show", "comedy", "drama", "action", "adventure", "romance", "sci-fi", "fantasy", "horror", "mystery", "thriller", "crime", "detective", "spy", "war", "history", "politics", "economy", "technology", "science", "space", "universe", "galaxy", "planet", "star", "blackhole", "wormhole", "time travel", "parallel universe", "multiverse", "alien", "extraterrestrial", "ufo", "abduction", "conspiracy", "myth", "legend", "folklore", "superstition", "magic", "witchcraft", "wizardry", "sorcery", "alchemy", "mythology", "religion", "philosophy", "psychology", "sociology", "anthropology", "history", "geography", "biology", "chemistry", "physics", "mathematics"]
    return random.choice(words)

def display_word(word, slice_of_word):
    return " ".join(slice_of_word)

def play():
    word = random_word()
    slice_of_word = ["_" for _ in range(len(word))]
    lives = 6
    stages = hangman_stages()
    print("Welcome to Hangman!")
    print(stages[6 - lives])
    while lives > 0:
        
        print(display_word(word, slice_of_word))
        guess = input("Guess a letter: ").lower()
        if guess in slice_of_word:
            print("You've already guessed that letter! Try again.")
            continue
        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    slice_of_word[i] = guess
            print("Good guess! Keep going!")
            if "_" not in slice_of_word:
                print(f"Congratulations! You've guessed the word: {word}")
                break
        else:
            lives -= 1
            print(stages[6 - lives])
            print(f"Wrong guess! You have {lives} lives left.")
    else:
        print(f"Game Over! The word was: {word}")

while True:
    play()
    me = input("Do you want to play Hangman? (yes/no): ").lower()
    me = me.strip()
    clear_screen()
    if me in ["no", "n"]:
        print("Thanks for playing! Goodbye!")
        break
        