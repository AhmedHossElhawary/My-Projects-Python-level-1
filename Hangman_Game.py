import random

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
            |       0
            | 
            |
            |
         ==============
        """,
        """
            +-------+
            |       |
            |       0
            |       |
            |
            |
         ==============
        """,
        """
            +-------+
            |       |
            |       0
            |      -|
            |
            |
         ==============
        """,
        """
            +-------+
            |       |
            |       0
            |      -|-
            |
            |
         ==============
        """,
        """
            +-------+
            |       |
            |       0
            |      -|-
            |      /
            |
         ==============
        """,
        """
            +-------+
            |       |
            |       0
            |      -|-
            |      / \ 
            |
         ==============
        """]

def random_word():
    words = ["cat", "dog", "bird", "fish", "sun", "moon", "torch", "tree", "flower", "car", "house", "computer", "phone", "book", "pen", "pencil", "paper", "chair", "table", "bed", "sofa", "couch", "lamp", "clock", "mirror", "window", "door", "wall", "floor", "ceiling", "roof", "garden", "park", "beach", "mountain", "river", "lake", "ocean", "sky", "cloud", "rain", "snow", "wind", "storm", "thunder", "lightning", "sunrise", "sunset", "day", "night", "week", "month", "year", "time", "calendar", "season", "spring", "summer", "autumn", "winter", "holiday", "vacation", "travel", "adventure", "explore", "discover", "learn", "teach", "friend", "family", "love", "happiness", "sadness", "anger", "fear", "surprise"]
    return random.choice(words)

def display_word(word, slice_of_word):
    return " ".join(slice_of_word)

def play():
    word = random_word()
    slice_of_word = ["_" for _ in range(len(word))]
    wrong_count = 0
    stages = hangman_stages()
    max_wrong = len(stages) - 1
    
    while "_" in slice_of_word and wrong_count < max_wrong:
        print(stages[wrong_count])
        print("Word: " + display_word(word, slice_of_word))
        print(f"Wrong guesses: {wrong_count}/{max_wrong}")
        guess = input("Guess a letter: ").lower()
        
        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    slice_of_word[i] = guess
            print("Correct guess!")
        else:
            print("Wrong guess!")
            wrong_count += 1
    
    print(stages[wrong_count])
    print("Word: " + display_word(word, slice_of_word))
    
    if "_" not in slice_of_word:
        print("Congratulations! You won! The word was: " + word)
    else:
        print("Game over! You lost! The word was: " + word)

while True:
    play()
    me = input("Do you want to play Hangman? (yes/no): ").lower()
    me = me.strip()
    if me in ["no", "n"]:
        print("Thanks for playing! Goodbye!")
        break
        