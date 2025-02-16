def get_word_count(file):
    split_file = file.split()
    return len(split_file)

def main():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()
    print(file_contents)
    print(get_word_count(file_contents))

main()