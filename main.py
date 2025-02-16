def get_word_count(file):
    split_file = file.split()
    return len(split_file)

def get_char_count(file):
    char_count_dict = {}

    for char in file.lower():
        try:
            char_count_dict[char] += 1
        except KeyError:
            char_count_dict[char] = 1
    
    return char_count_dict

def sort_on(dict):
    return dict["count"]

def main():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()
    
    print(f"--- Begin report of {path_to_file} ---")
    word_count = get_word_count(file_contents)
    print(f"{word_count} words found in the document")
    print()
    print()

    char_count = get_char_count(file_contents)
    char_count_list = []

    for key in char_count.keys():
        if key.isalpha():
            char_count_list.append({"character": key, "count": char_count[key]})
    
    char_count_list.sort(reverse=True, key=sort_on)

    for entry in char_count_list:
        print(f"The '{entry["character"]}' character was found {entry["count"]} times")





    

main()