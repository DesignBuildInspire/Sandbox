import pandas as pd
from PIL import Image, ImageDraw, ImageFont


data=pd.read_csv("./information.csv")
datadict = data.to_dict(orient='records')
# index = 20

for index in range (0,50):

    resolution = 200            # resolutiuon of 200 pixels per inch ( ppi )
    w = int(2.5 * resolution)  
    h = int(3.5 * resolution)

    img = Image.new ("RGB", (w,h))
    titlef= ImageFont.truetype("./font/Roboto-Black.ttf", size=30)
    capitalf= ImageFont.truetype("./font/Roboto-Black.ttf", size=20)

    flagw = 2 * resolution
    flagh = 1 * resolution

    canvas = ImageDraw.Draw(img)
    canvas.rectangle([(0,0),(w,h)],fill="white")

    StateData = datadict[index]

    Statealias = str(StateData['Alias']).lower()

    flagname = f"./us-w550/{Statealias}.png"

    flag = Image.open(flagname).resize((flagw,flagh))
    img.paste(flag,(50, 100, 50+flagw, 100+flagh))


    Statename = str(StateData['Name'])
    Statecapital = str(StateData['Capital'])
    Stateid = str(StateData['ID'])
    StatePopulation = str(StateData['Population'])
    StateArea = str(StateData['Area'])
    StateMedianHouseholdIncome = str(StateData['Median Household Income'])
    StateTallestmountain = str(StateData['tallest mountain'])
    StateHighestPoint = str(StateData['Highest Point'])
    StateNeighboringStates = str(StateData['Neighboring States'])

    canvas.text((30,10),Statename, font=titlef, fill="Black")
    canvas.text((30,50),Statecapital, font=capitalf, fill="Black")

    canvas.ellipse((420,20,470,70),fill="grey")
    canvas.text((435,30),Stateid, font=titlef, fill="Black")

    canvas.text((30,350),"Population", font=capitalf, fill="Black")
    canvas.text((30,400),"Area", font=capitalf, fill="Black")
    canvas.text((30,450),"Median Household Income", font=capitalf, fill="Black")
    canvas.text((30,500),"Tallest Mountain", font=capitalf, fill="Black")
    canvas.text((30,550),"Highest Point", font=capitalf, fill="Black")
    canvas.text((30,600),"Neighboring States", font=capitalf, fill="Black")

    canvas.text((300,350),StatePopulation, font=capitalf, fill="Black")
    canvas.text((300,400),StateArea, font=capitalf, fill="Black")
    canvas.text((300,450),StateMedianHouseholdIncome, font=capitalf, fill="Black")
    canvas.text((300,500),StateTallestmountain, font=capitalf, fill="Black")
    canvas.text((300,550),StateHighestPoint, font=capitalf, fill="Black")
    canvas.text((300,600),StateNeighboringStates, font=capitalf, fill="Black")


    img.show()
    img.save("card.png")