from games.models import Game
import csv

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
    
    
    
    game = Game(game_name=line[0].strip('\"') , release_date=str, platform=line[3].strip('\"') , 
                critic_score=line[2].strip('\"') ,
                image_src=line[4].strip('\"') , game_src=line[5].strip('\"') )
    game.save()
    
    

