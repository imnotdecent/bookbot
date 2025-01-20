def wordcount(text):
    words = text.split()
    return len(words)

def charactercount(text):
    lowercase_file_contents = text.lower()
    char_count = {}
    for c in lowercase_file_contents:
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1
    return char_count

def report(text):
    counts = {}
    for i in text:
        if i.isalpha():
            char = i.lower()
            counts[char] = counts.get(char, 0) + 1
    sorted_counts = sorted(counts.items(), key=lambda item:item[1], reverse=True)
    
    for char, count in sorted_counts:
        print(f"The '{char}' character was found {count} times")


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = wordcount(file_contents)
        character_count = charactercount(file_contents)
        print(f"{word_count} words found in the document.\n")
        report(file_contents)

if __name__ == "__main__":
    main()