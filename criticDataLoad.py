from games.models import CriticProfile, CriticReview, Game
import csv


CriticProfile.objects.all().delete()
CriticReview.objects.all().delete()

file = open("criticProfs.csv", "r")
file.readline()
for line in file:
    
    line = line.strip().split(",")
    cp = CriticProfile(critic_name=line[0], critic_src=line[1])
    
    cp.save()

print("Profiles done")

file = open("criticScores.csv", "r")
file.readline()
for line in file:
    line = [ '"{}"'.format(x) for x in list(csv.reader([line], delimiter=',', quotechar='"'))[0]]
    
    cp = CriticProfile.objects.get(critic_name=line[2].strip('\"'))
    gameName = line[0].strip('\"')
    crit_score = line[3].strip('\"')
    plat = line[4].strip('\"')
    
    platKeys = {
        'pc':'PC',
        'playstation-2':'PlayStation 2',
        'playstation-4':'PlayStation 4',
        'xbox-one':'Xbox One',
        'nintendo-64':'Nintendo 64',
        'gamecube':'GameCube',
        'psp':'PSP',
        'xbox-series-x':'Xbox Series X',
        'xbox-360':'Xbox 360',
        'playstation':'PlayStation',
        'switch':'Switch',
        'wii':'Wii',
        'playstation-3':'PlayStation 3',
        'game-boy-advance':'Game Boy Advance',
        'wii-u':'Wii U',
        '3ds':'3DS',
        'dreamcast':'Dreamcast',
        'playstation-5':'PlayStation 5',
        'stadia':'Stadia',
        'ds':'DS',
        'xbox':'Xbox',
        'playstation-vita':'PlayStation Vita',
    }
    plat = platKeys[plat]
    
    if Game.objects.filter(platform=plat).filter(game_name=gameName).exists():
        game = Game.objects.filter(platform=plat).get(game_name=gameName)
    else:
        continue
    
    if CriticReview.objects.filter(game=game).filter(critic=cp).exists():
        continue
        
    cr = CriticReview(game=game, critic=cp, critic_score=crit_score)
    
    cr.save()