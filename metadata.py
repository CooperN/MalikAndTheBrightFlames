import requests


player = 55996945

url = 'https://character-service.dndbeyond.com/character/v5/character/'

def main():
    getCharacters(player)



def getCharacters(id):
    r = requests.get(f'https://character-service.dndbeyond.com/character/v5/character/{player}')

    data = r.json()

    characters = data['data']
    characterss = characters['campaign']
    charactersss = characterss['characters']

    ids = []

    for character in charactersss:
        ids.append(character['userId'])
    
    print(ids)

class character():
    def __init__(self):
        self.id

if __name__ == '__main__':
    main()
