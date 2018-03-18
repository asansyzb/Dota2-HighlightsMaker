import matplotlib.pyplot as plt
from moviepy.editor import VideoFileClip, concatenate_videoclips, concatenate_audioclips

window = 30
step = 10
highlight_time = 500
clip_time = 4165 

def find_entry(lst, str) :
	for x in lst:
		if (x.startswith(str) == True):
			return x

f = open('damage.txt', 'r')
damage_time_value = []
count = 0
for line in f:
	r = line.split(" ")
	timestamp = find_entry(r, "timestamp")
	timestamp = timestamp.split(":")[1]
	value = find_entry(r, "value")
	value = value.split(":")[1]
	x = float(timestamp)
	x -= 160 - 144
	if (line.find('"target":"npc_dota_hero') != -1) and (line.find('"attacker":npc_dota_hero') != -1): 
		damage_time_value.append([x, int(value)])
	

damages = []
timestamps = []
for cur_time in range(0, clip_time, step):
	cumulative_damage = 0
	for timestamp, value in damage_time_value:
		#print (timestamp)
		if (timestamp >= cur_time and timestamp <= cur_time + window) :
			cumulative_damage += value
	#print(cumulative_damage)
	damages.append(cumulative_damage)
	timestamps.append(cur_time)

plt.plot(timestamps, damages)
plt.ylabel('damages')
#plt.ylabel('damage')
plt.xlabel('time')
plt.show()	

