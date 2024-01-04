def count_words(sentence):
    """Count the number of words in a given sentence."""
    words = sentence.split()
    return len(words)

def main():
    try:
        # Prompt user for input
        user_input = input("Enter a sentence or paragraph: ")

        # Check for empty input
        if not user_input:
            raise ValueError("Input cannot be empty.")

        # Count words and display output
        word_count = count_words(user_input)
        print(f"Word count: {word_count}")

    except ValueError as ve:
        print(f"Error: {ve}")

if __name__== "__main__":
    main()
