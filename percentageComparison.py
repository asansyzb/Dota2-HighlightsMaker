import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
names = ["VP vs Liquid", "EG vs VP", "Navi vs EG", "Liquid vs Secret", "Navi vs Newbee"]
ocvrFile = ["VPvsLiquid(ocvr).txt", "EGvsVP(ocvr).txt", "NaviVSEG(ocvr).txt", "LiquidvsSecret(ocvr).txt", "NavivsNewbee(ocvr).txt"]
firstAlgo = ["VPvsLiquid(1stalgo).txt", "EGvsVP(2ndalgo).txt", "NaviVsEG(1stalgo).txt", "LiquidvsSecret(1stalgo).txt", "NavivsNewbee(1stalgo).txt"]
secondAlgo = ["VPvsLiquid(2ndalgo).txt","EGvsVP(1stalgo).txt", "NaviVsEG(2ndalgo).txt", "LiquidvsSecret(2ndalgo).txt", "NavivsNewbee(2ndalgo).txt"]

def secs(str):
	x, y = str.split(":")
	return int(x) * 60 + int(y)

for i in range(1):
	with open(ocvrFile[i]) as f:
		best = f.readlines()
	with open(firstAlgo[i]) as d:
		content1 = d.readlines()
	with open(secondAlgo[i]) as e:
		content2 = e.readlines()
	range1 = [0] * 5000
	range2 = [0] * 5000
	bestLength = 0
	content1Length = 0
	content2Length = 0
	data = []
	#print (i)
	for line in best:
		#print line
		x,y = line.split("-")
		z,w = secs(x), secs(y)
		bestLength += w-z + 1
		data.append([z, w + 1])

	for x, y in data:

		plt.axvspan(x, y, color='blue', alpha=0.5)
		for j in range(x, y):
			range1[j] = range2[j] = 1
	data = []
	for line in content1:
		x,y = line.split(" ")
		data.append([int(x), int(y) + 1])
	
	for x, y in data:
		plt.axvspan(x, y, color='red', alpha=0.5)
#		print (x, y, y-x)
		content1Length += y - x 
		for j in range(x, y):
			range1[j] = range1[j] + 1
    
	data = []
	for line in content2:
		x,y = line.split(" ")
		data.append([int(x), int(y) + 1])
	for x, y in data:
		content2Length += y-x
		for j in range(x, y):
			range2[j] = range2[j] + 1

   	r1count = 0
   	r2count = 0
   	for t in range(4999):
   		if (range1[t] == 2):
   			plt.axvspan(t, t, color='violet', alpha=1.0)
   			r1count = r1count + 1
		if (range2[t] == 2):
			r2count = r2count + 1
	font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 14,
    }
	plt.title("GAME: " + names[i] + "\n Comparison of the first algorithm and Youtube highlights", fontdict=font)
	#plt.savefig(names[i] + " 1.png")
	
	red_patch = mpatches.Patch(color='red', alpha=0.5, label='Not captured in the intersection Noobfromua data')
	blue_patch = mpatches.Patch(color='blue',  alpha=0.5, label='Not captured in the intersection the first algorithm data')
	orange_patch = mpatches.Patch(color='violet', alpha=0.8, label='Intersection of Noobfromua and the First algorithm data')
	plt.legend(handles=[red_patch, blue_patch, orange_patch])
	plt.show()

#	print (bestLength, content1Length, content2Length)
#	print (r1count, r2count)
	print (100-r1count*100/min(bestLength, content1Length), 100-r2count*100/min(bestLength, content2Length))

