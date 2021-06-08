import requests
import json

# APIkey = 'RGAPI-5052849a-7542-4271-a055-c392ed5cad13'
# Version 11.11.1

# Get a list of champion names
allChampsURL = 'http://ddragon.leagueoflegends.com/cdn/11.11.1/data/en_US/champion.json'
allChampsJson = requests.get(allChampsURL).json()
data = allChampsJson['data']
allChamps = data.keys()

print("Total champions:", len(allChamps))

# Build a list of abilities for every champion
champInfoURL = 'http://ddragon.leagueoflegends.com/cdn/11.11.1/data/en_US/champion/'
champ_abilities_list = []
for champ in allChamps:
    detailedInfo = f'{champInfoURL}{champ}.json'
    champInfoJson = requests.get(detailedInfo).json()
    abilities = []
    
    spells = champInfoJson['data'][champ]['spells']
    print(f"Retrieving {champ}'s spells...")
    for spell in spells:
        abilities.append(spell['name'])
        
    champion = {
        "name": champ,
        "abilities": abilities
    }
    champ_abilities_list.append(champion)
    
print(f"Finished retrieving {len(champ_abilities_list)} champions' spells!")

# print(champ_abilities_list)

choice = input("Press the Enter key to write downloaded data to 'league.json' file, anything else to abort: ")

if choice == "":
    champ_obj = json.dumps(champ_abilities_list, indent=4)
    with open('league.json', 'w') as f:
        f.write(champ_obj)
        f.close()
    print("Write to 'league.json' successfully!")
else:
    print("Aborted")
    exit()