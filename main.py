def get_word_count(file):
    split_file = file.split()
    return len(split_file)

def get_char_count(file):
    char_count = {}

    for char in file.lower():
        try:
            char_count[char] += 1
        except KeyError:
            char_count[char] = 1
    
    return char_count

def main():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()
    print(file_contents)
    print(get_word_count(file_contents))
    book_char_count = get_char_count(file_contents)
    print(book_char_count)

main()