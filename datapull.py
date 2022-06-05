import requests
import numpy as np
import pandas as pd
import statistics as st

mergedData=pd.read_csv('mergedData.csv')
def getEstimates(currentLevel):  
    returnDF = pd.DataFrame(columns=['daysInTable','medianValue'])  
    def getMedianValue(outcomesDF):
        medianValue=st.median(outcomesDF["X2"])
        return medianValue
    samples=9999
    daysInTable = [1,7,31,93,365,365*2]
    for y in daysInTable:
        outcomes=[]
        for i in range(samples):
            outcomes.append(sum(mergedData['waterUsage'][np.random.randint(0,len(mergedData),size=y)])+currentLevel)
        outcomesPercentFull=outcomes/mergedData['conservation_capacity'][0]
        X2 = np.sort(outcomesPercentFull)
        F2 = np.array(range(outcomesPercentFull.size))/float(outcomesPercentFull.size-1)
        outcomesDF = pd.DataFrame({"X2":X2,"F2":F2})  
        medianValue=getMedianValue(outcomesDF)
        returnDF=returnDF.append({"medianValue":("%.3g%%" %(medianValue*100))},ignore_index=True)
    returnDF["daysInTable"]=("Tomorrow","One week","One month","Three months","One year","Two years")
    return(returnDF)



pastData = pd.read_csv('https://waterdatafortexas.org/reservoirs/individual/medina-30day.csv',header=53)

rateDaily = (pastData['reservoir_storage'][0]-pastData['reservoir_storage'][30])/30
daysUntilGone = pastData['reservoir_storage'][30]/rateDaily
timeUpdated=[pastData['date'][30]]
dataTable = pd.DataFrame({"timeUpdated":timeUpdated,"percentFull":pastData['percent_full'][30],"rateDaily":rateDaily,"daysUntil":daysUntilGone})
dataTable=getEstimates(pastData['reservoir_storage'][30])
Func = open("/Users/josephcano/Desktop/LightArtGallery/medinalakelevel/index.html","w")
displayTable = "<table><tr><th>Time in future</th><th>Probabalistic lake level</th></tr>"
for i in range(len(dataTable)):
    displayTable+="<tr><td>"+str(dataTable['daysInTable'][i])+"</td><td>"+str(dataTable['medianValue'][i])+"</td></tr>"
Func.write('<head> <meta charset="utf-8"> <meta name="viewport" content="width=device-width, initial-scale=1"> <title>Home</title> <link rel="stylesheet" href="css.css"> <script src="script.js"></script></head><body> <div class="header"> <h1 id="logo">Medina lake is %s%% full</h1> <h2 id="subtitle">Over the past 30 days it has lost %s acre-ft/day</h2> </div> </div></body>' % (pastData['percent_full'][30],int(rateDaily))+displayTable+"</table>"+'<h2 id="subtitle">On any given day, there is only a 17%% chance that the Medina Lake level will increase </h2><h2 id="subtitle">Last updated on: %s</h2>' % timeUpdated[0]+'<a id="subtitle" href="about.html" style="text-align: center;margin: 0 auto; display:block;">About</a>')
Func.close()

Func = open("/Users/josephcano/Desktop/LightArtGallery/medinalakelevel/css.css","w")
css = """
body{background:linear-gradient(180deg,#fdefc6 %s%%,#b6d1dc %s%%)}#logo{font-family:Arial,Helvetica,sans-serif;color:black;font-size:50px;text-align:center;margin-top:30px}#subtitle{text-decoration:none;font-family:Arial,Helvetica,sans-serif;color:black;font-size:30px;text-align:center;margin-top:30px} table { border-spacing: 1; border-collapse: collapse; background: #b6d1dc; font-family: Arial, Helvetica, sans-serif; border-radius: 6px; overflow: hidden; max-width: 800px; width: 100%%; margin: 0 auto; position: relative; text-align: center; font-size:30px;}
""" % (100-pastData['percent_full'][30],pastData['percent_full'][30])
Func.write(css)



