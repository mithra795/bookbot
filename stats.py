def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        word_count = len(file_contents.split())
        return print(f"Found {word_count} total words")
    
def get_char_count(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        char_count = {}
        for i in file_contents:
            i = i.lower()
            if i in char_count:
                char_count[i] += 1
            else:
                char_count[i] = 1
        #list_of_chars = list(char_count)
        #list_of_chars.sort(reverse=True, key=)
        return char_count
    
def shitty(items):
    return items["num"]

def sort_on(chars):
    my_list = []
    for i in chars:
       char = {"char": i,
               "num": chars[i]}
       my_list.append(char)
       my_list.sort(reverse=True, key=shitty)
    return my_list



           

    
