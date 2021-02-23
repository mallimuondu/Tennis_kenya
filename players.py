import json as js
with open('Players.json','r') as s:
    players = js.load(s)
    for dub in players["players"]:
        print(dub['name'],dub['age'],dub['tournaments_won'])
with open('Matches.json','r') as i:
    Match = js.load(i)
    for dub in Match["Round1"]:
        print(dub['points'])