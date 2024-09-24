from bs4 import BeautifulSoup

def get_pairs(paragraphs):

    pairs = {
        "test" : "test response"
    }

    for index, p in enumerate(paragraphs):

        dialogue1 = p.get_text()
        dialogue2 = ""


        if "\"" in dialogue1 and len(dialogue1) < 300:
            pairs.update({p.get_text(): ""})

    return pairs


def main():

    filename = "sources/Victoria _ Project Gutenberg.html";

    with open(filename, 'r') as file:
        content = file.read()

    soup = BeautifulSoup(content, 'html.parser')

    paragraphs = soup.find_all('p')

    pairs = get_pairs(paragraphs)

    for key in pairs:
        print(key, pairs[key])

main()