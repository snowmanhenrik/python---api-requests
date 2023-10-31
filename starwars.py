def newRecruits(movieNum:int):

    totalscore = 0
    freqcount = 0
    winner = ""
    
    infile = open("starWars.csv","r")
    header = infile.readline()
    data = infile.readlines()

    infile.close()

    for line in data:
        line = line.strip()
        line = line.split(",")
        if int(line[3]) == movieNum:
            totalscore += int(line[1])
            freqcount += 1

    if freqcount == 0:
        winner = "No new recruits!"
    else:
        if totalscore > 0:
            winner = "The Jedis have won by {} points!".format(totalscore)
        else:
            winner = "Oh no, the Siths are better!"
    return winner

def orgByType(minChlorian:float,maxChlorian:float):

    infile = open("starWars.csv","r")
    header = infile.readline()
    data = infile.readlines()
    organizedDict = {}
    for line in data:
        line = line.strip()
        line = line.split(",")
        if int(line[1]) >= minChlorian and int(line[1]) <= maxChlorian:
            if line[2] in organizedDict:
                organizedDict[line[2]].append(line[0])
                organizedDict[line[2]].sort()
            else:
                organizedDict[line[2]] = [line[0]]
    infile.close()
    return organizedDict
            
def possiblePlanets(favPlanets:list):
    destinationDict = {}
    for planet in favPlanets:
        try:
            url = "https://swapi.dev/api/planets/?search=" + planet
            response = requests.get(url)
            data = response.json()
            if "temperate" in data["results"][0]["climate"]:
                destinationDict[planet] = data["results"][0]["climate"]
        except:
            continue
    return destinationDict
        
def residentHeights(planet:str):
    heights = []
    try:
        url = "https://swapi.dev/api/planets/?search=" + planet
        response = requests.get(url)
        data = response.json()
        for resident in data["results"][0]["residents"]:
            response2 = requests.get(resident)
            data2 = response2.json()
            datatuple = (int(data2["height"]),data2["name"])
            heights.append(datatuple)
    except:
        heights = []

    heights.sort()

def starshipInfo(starships:list):
    infile = open("starships.csv","w")
    infile.write("Starship Name,Model,Starship Class,Passengers")
    for i,starship in enumerate(starships):
        try:
            url = "https://swapi.dev/api/starships/?search=" + starship
            response = requests.get(url)
            data = response.json()
            name = str(data["results"][0]["name"])
            model = str(data["results"][0]["model"])
            starshipclass = str(data["results"][0]["starship_class"])
            passengers = str(data["results"][0]["passengers"])
            if i == (len(starships))-1:
                string = "\n" + name + "," + model + "," + starshipclass + "," + passengers
            else:
                string = "\n" + name + "," + model + "," + starshipclass + "," + passengers
            infile.write(string)
        except:
            continue
    infile.close()


