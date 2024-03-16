from anagram_checker import AnagramChecker

def main():
    checker = AnagramChecker()
    while True:
        print("\n1. Input a word")
        print("2. Exit")
        choice = input("Choose an option: ")
        if choice == '2':
            break
        elif choice == '1':
            word = input("Enter a word: ").strip()
            if not word.isalpha():
                print("Error: Only alphabetic characters are allowed.")
                continue
            if ' ' in word:
                print("Error: Only a single word is allowed.")
                continue
            if not checker.is_valid_word(word):
                print("Error: This is not a valid English word.")
                continue
            anagrams = checker.get_anagrams(word)
            print(f"\nYOUR WORD: \"{word.upper()}\"")
            print("This is a valid English word.")
            print(f"Anagrams for your word: {', '.join(anagrams)}.")

if __name__ == "__main__":
    main()
