def main():
    book_path = "./books/frankenstein.txt"
    book = read_book(book_path)
    print_report(book)


def read_book(path):
    with open(path) as f:
        return f.read()


def count_words(txt):
    words_arr = txt.split()
    word_count = len(words_arr)
    return word_count


def count_chars(txt):
    txt_to_lower = txt.lower()
    chars_count = {}
    for char in txt_to_lower:
        if char not in chars_count:
            chars_count[char] = 1
        else:
            chars_count[char] += 1
    return chars_count


def dict_to_list(dict):
    new_list = []
    for i in dict:
        new_list.append({"name": i, "count": dict[i]})
    new_list.sort(reverse=True, key=sort_on)
    return new_list


def sort_on(dict):
    return dict["count"]


def print_report(book):
    word_count = count_words(book)
    count_dict = count_chars(book)
    chars_count_list = dict_to_list(count_dict)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")

    for i in range(len(chars_count_list)):
        name = chars_count_list[i]["name"]
        count = chars_count_list[i]["count"]
        print(f"The '{name}' character was found {count} times")

    print("--- End report ---")


main()
