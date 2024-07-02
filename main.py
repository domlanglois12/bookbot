def main():
    book_path = "bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    character_counts = count_characters(text)
    
    print(f"{num_words} words found in the document.")
    
    # Sort character counts by frequency (descending)
    sorted_char_counts = sorted(character_counts.items(), key=lambda x: x[1], reverse=True)

    print("Character counts (sorted by frequency):")
    for char, count in sorted_char_counts:
        print(f"{char}: {count}")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_characters(text):
    lowercase = text.lower()
    char_count = {}

    for char in lowercase:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    
    return char_count


main()


  

