def get_num_words(string):
    return len(string.split())
    
def count_characters(text):
    char_dict = {}
    for char in text:
        lower_char = char.lower()
        if lower_char in char_dict:
            char_dict[lower_char] += 1
        else:
            char_dict[lower_char] = 1
    
    return char_dict

def sort_on(dict):
    return dict["num"]

def sort_dict(unsorted_dict):
    listyboi = []
    for key, value in unsorted_dict.items():
        listyboi.append({ "char": key, "num": value})
    listyboi.sort(reverse=True, key=sort_on)
    return listyboi