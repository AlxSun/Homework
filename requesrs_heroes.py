import requests
response = requests.get("https://akabab.github.io/superhero-api/api/all.json")
json_response = response.json()

lst_hero = ["Hulk", "Captain America", "Thanos"]
def the_cleverest(heroes, powerstat):
    dct_heroes = {}
    for hero in heroes:
       for i in range(len(json_response)):
           if json_response[i]['name'] == hero:
               dct_heroes[hero] = json_response[i]["powerstats"][powerstat]
    print(max(dct_heroes.items())[0])

the_cleverest(lst_hero, 'intelligence')