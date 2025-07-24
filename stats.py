# get entire book text from file as string
def get_book_text(filepath):
    # open file
    with open(filepath) as f:
        # output
        return f.read()

# get book word count
def get_book_length(filepath):
    # input
    file_contents = get_book_text(filepath)
    # length
    num_words = len(file_contents.split())
    # output
    return (f"Found {num_words} total words")

# get book character count
def get_book_characters(filepath):
    # input
    file_characters = list(get_book_text(filepath).lower())
    # dict
    character_dict = {}
    # loop
    for character in file_characters:
        if character in character_dict:
            character_dict[character] += 1
        else:
            character_dict[character] = 1
    # output
    return character_dict

# sort character count by appearance value
def get_book_sorted_characters(filepath):
    # input
    characters = get_book_characters(filepath)
    # list
    sorted_characters = []
    # loop
    for character in characters:
        # if alpha ; append to list
        if character.isalpha():
            char = character
            num = characters.get(character)
            sorted_characters.append({"char": char, "num": num})
    # def
    def sort_by_num(character):
        return character["num"]
    # sorting
    sorted_characters.sort(key=sort_by_num, reverse=True)
    # list
    lines = []
    # append
    for item in sorted_characters:
        lines.append(f"{item["char"]}: {item["num"]}")
    # join
    return "\n".join(lines)

# report
def report(filepath):
    # call stat functions
    get_book_text(filepath)
    book_length = get_book_length(filepath)
    get_book_characters(filepath)
    book_characters = get_book_sorted_characters(filepath)
    # prepare report parts
    TITLE_HEADER = "============ BOOKBOT ============"
    FILEPATH = f"Analyzing book found at {filepath}"
    WORD_COUNT = "----------- Word Count ----------" + "\n" + f"{book_length}"
    CHARACTER_COUNT = "--------- Character Count -------" + "\n" + f"{book_characters}"
    END_FOOTER = "============= END ==============="
    # prepare report
    REPORT = TITLE_HEADER + "\n" + FILEPATH + "\n" + WORD_COUNT + "\n" + CHARACTER_COUNT + "\n" + END_FOOTER
    # output
    print(REPORT)