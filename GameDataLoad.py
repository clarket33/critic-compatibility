from games.models import Game, GameReview
import csv

Game.objects.all().delete()
GameReview.objects.all().delete()

file = open("gameData.csv", "r")
file.readline()
for line in file:
    
    line = [ '"{}"'.format(x) for x in list(csv.reader([line], delimiter=',', quotechar='"'))[0]]
    dateLine = line[1].replace(",","").strip('\"').split(" ")
    
    months = {
        "January": "01",
        "February": "02",
        "March": "03",
        "April": "04",
        "May": "05",
        "June": "06",
        "July": "07",
        "August": "08",
        "September": "09",
        "October": "10",
        "November": "11",
        "December": "12"
    }
    
    str = ""
    str += dateLine[2] + "-" + months[dateLine[0]] + "-"
    if len(dateLine[1]) < 2:
        str += "0" + dateLine[1]
    else:
        str += dateLine[1]
        
    
    gameName = line[0].strip('\"')
    releaseDate = str
    platfrm = line[3].strip('\"')
    criticScore = line[2].strip('\"')
    imageSrc = line[4].strip('\"')
    gameSrc = line[5].strip('\"')
    
    
    if Game.objects.filter(game_name=gameName).filter(platform=platfrm).filter(release_date=releaseDate).exists():
        continue    
    
    
    game = Game(game_name=gameName, release_date=releaseDate, platform=platfrm , 
                    critic_score=criticScore ,
                    image_src=imageSrc , game_src=gameSrc )
    game.save()    
    
    
    

