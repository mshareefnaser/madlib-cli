import re  


def read_template(path):
    ''' a function that read file from specific path'''
    with open(path) as file:
        content = file.read()
        return content


def parse_template(content):
    '''
    a function that extract the words between curly braces '{}' inside a string , 
    it returns two arguments:
    srtipped: the string after removing the words
    parts: the words taken from the string
    '''

    pattern = r"\{([^}]+)\}"
    stripped = re.sub(pattern, "{}", content)
    parts = re.findall(pattern, content)
    return stripped, tuple(parts)


def merge(stripped, parts):
    '''
    Merges the given parts into the stripped string by replacing any
    curly-braced placeholders with the corresponding part.
    '''
    return stripped.format(*parts)

def write_file(path,content):
    ''' a function that write a file in a specific path'''
    with open(path,'w') as file:
        file.write(content)

def main():
    print("Welcome to Madlib Game")
    print("You will be asked to enter some words to complete the game")
    print("after you finish, the game will be generated in a new file")
    # path = "./assets/dark_and_stormy_night_template.txt"
    path = "./assets/make_me_a_video_game_template.txt"
    template_file = read_template(path)
    stripped, parts = parse_template(template_file)
    user_inputs = []
    for part in parts:
        user_input = input(f"Give me a {part}: ")
        user_inputs.append(user_input)

    game_output = merge(stripped, tuple(user_inputs))
    write_file("assets/res.txt", game_output)
    print(game_output)



if __name__ == "__main__":
    main()
