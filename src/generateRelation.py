import json

dataPath = '../data/stereomood_data_traceable_haslyrics.json'

with open(dataPath) as f:
    database = json.load(f)

# calculate total labels
moods = set()
for key in database:
    for mood in database[key]['moods']:
        moods.add(str(mood))
moods = list(moods)
lenmoods = len(moods)
print moods
moodsDict = {}
for index, mood in enumerate(moods):
    moodsDict[mood] = index

# generate relation matrix
relationMatrix = [[0 for j in xrange(lenmoods)] for i in xrange(lenmoods)]
selfMoodsDict = [{'total': 0, 'self': 0, 'percentage': 0.0} for i in xrange(lenmoods)]
for key in database:
    currentMoodsList = database[key]['moods']
    for mood in currentMoodsList:
        mood = str(mood)
        index = moodsDict[mood]
        selfMoodsDict[index]['total'] += 1
        if len(currentMoodsList) == 1:
            selfMoodsDict[index]['self'] += 1
        for anotherMood in currentMoodsList:
            anotherMood = str(anotherMood)
            if anotherMood != mood:
                anotherIndex = moodsDict[anotherMood]
                relationMatrix[index][anotherIndex] += 1
print relationMatrix

# get self occurance percentage
selfOccurancePercent = []
for i in xrange(len(selfMoodsDict)):
    selfMoodsDict[i]['percentage'] = float(selfMoodsDict[i]['self'])/selfMoodsDict[i]['total']
    selfOccurancePercent.append("%.2f" % selfMoodsDict[i]['percentage'])
print selfOccurancePercent
