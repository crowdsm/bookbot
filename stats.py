def get_num_words(book_contents):
    num_words = 0 
    words = book_contents.split()
    for word in words:
        num_words += 1
    return num_words

def get_num_chars(book_contents):
    num_chars = {}
    lower_book_contents = book_contents.lower()
    for i in range(0, len(book_contents)):
        if lower_book_contents[i] in num_chars:
            num_chars[lower_book_contents[i]] += 1
        else:
            num_chars[lower_book_contents[i]] = 1
    return num_chars

def sort_on(dict):
    return dict["count"]

def sort_chars(num_chars):
    char_and_count = []

    for char in num_chars:
        char_and_count.append({
            "char":char, 
            "count":num_chars[char]
        })

    char_and_count.sort(reverse=True, key=sort_on)
    return char_and_count
    