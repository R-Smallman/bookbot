def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def get_book_length(filepath):
    file_contents = get_book_text(filepath)
    num_words = len(file_contents.split())
    return (f"Found {num_words} total words")

def get_book_characters(filepath):
    file_characters = list(get_book_text(filepath).lower())
    character_dict = {}
    for character in file_characters:
        if character in character_dict:
            character_dict[character] += 1
        else:
            character_dict[character] = 1
    return character_dict



def get_book_sorted_characters(filepath):
    characters = get_book_characters(filepath)

    sorted_characters = []

    for character in characters:
        # if alpha ; append to list
        if character.isalpha():
            char = character
            num = characters.get(character)
            sorted_characters.append({"char": char, "num": num})
    
    def sort_by_num(character):
        return character["num"]

    sorted_characters.sort(key=sort_by_num, reverse=True)

    lines = []

    for item in sorted_characters:
        lines.append(f"{item["char"]}: {item["num"]}")
    
    return "\n".join(lines)

def prepare_report(filepath):

    get_book_text(filepath)
    book_length = get_book_length(filepath)
    
    get_book_characters(filepath)
    book_characters = get_book_sorted_characters(filepath)


    print(f"""============ BOOKBOT ============
Analyzing book found at {filepath}...
----------- Word Count ----------
{book_length}
--------- Character Count -------
{book_characters}
============= END ===============
""")