from bs4 import BeautifulSoup

def get_pairs(paragraphs):

    #create pairs dict
    pairs = {"default" : "default response"}

    for index, p in enumerate(paragraphs):
        # key dialogue
        dialogue1 = p.get_text()

        # check for out of boundsd
        if index + 1 < len(paragraphs):
            dialogue2 = paragraphs[index + 1].get_text()    # set value dialogue (response)
        else:
            continue
        
        # checks for quotatios and max length
        if dialogue1.count("\"") == 2 and len(dialogue1) < 300 and dialogue2.count("\"") == 2 and len(dialogue2) < 300:
            pairs.update({dialogue1 : dialogue2})

    return pairs


def main():
    # define target novel
    filename = "sources/Victoria _ Project Gutenberg.html";

    with open(filename, 'r') as file:
        content = file.read()

    soup = BeautifulSoup(content, 'html.parser')

    paragraphs = soup.find_all('p')

    pairs = get_pairs(paragraphs)

    for key in pairs:
        print(key, pairs[key])

main()