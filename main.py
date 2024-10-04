import os
import csv
from bs4 import BeautifulSoup

def get_pairs(paragraphs):

    #create pairs dict
    pairs = {"default" : "default response"}

    for index, p in enumerate(paragraphs):
        # key dialogue
        dialogue1 = p.get_text()
        print(dialogue1)

        # check for out of boundsd
        if index + 1 < len(paragraphs):
            dialogue2 = paragraphs[index + 1].get_text()    # set value dialogue (response)
        else:
            continue
        
        # checks for quotations and max length
        #print("we are checking")
        if dialogue1.count("\"") == 2 and dialogue2.count("\"") == 2:
            pairs.update({dialogue1 : dialogue2})

    return pairs

def create_csv(filename, pairs):

    name = filename.split('/')[-1].split('.')[0]
    path = os.path.join('./dialogue-pairs', name + '.csv')

    with open(path, mode='w', newline='') as file:
        writer = csv.writer(file)

        for key, value in pairs.items():
            writer.writerow([key, value])


def main():
    # define target novel
    filename = "sources/Cosmos_Colliding.html";

    with open(filename, 'r') as file:
        content = file.read()

    soup = BeautifulSoup(content, 'html.parser')

    paragraphs = soup.find_all('p')

    pairs = get_pairs(paragraphs)

    for key in pairs:
        print(key, pairs[key])

    #create new csv
    create_csv(filename, pairs)

main()