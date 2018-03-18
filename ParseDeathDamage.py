import matplotlib.pyplot as plt
from moviepy.editor import VideoFileClip, concatenate_videoclips, concatenate_audioclips
cnt = 0
#print(1)

death_time = []
window = 20
step = 10
highlight_time = 500
clip_time = 5000 
time_from_beginning = 0

def check (x, mp):
	cur_time = 0
	ans = 0
	#print (x)
	while (cur_time < clip_time) :
		if mp[cur_time] >= x:
			ans += window
			cur_time += window
			while cur_time < clip_time and mp[cur_time] > 0  :
				cur_time += step
				ans += step
		else :
			cur_time += step 

	if (ans >= highlight_time):
		return True
	return False

f = open('output.txt', 'r')
for line in f:
	r = line.split(" ")

	if (r[2] == "type:DOTA_COMBATLOG_GAME_STATE") :
		timestamp = r[4]
		timestamp = timestamp.split(":")[1]
		time_from_beginning = float(timestamp) 
		
	if (r[2] == "type:DOTA_COMBATLOG_DEATH" and line.find("assist_players") != -1):
		cnt = cnt + 1
		#print (r[15], r[16])
		timestamp = r[15]
		if (timestamp.startswith("timestamp") == False):
			timestamp = r[16]
		timestamp = timestamp.split(":")[1]
		#print (timestamp)
		x = float(timestamp)
		x -= time_from_beginning
		
		death_time.append(x)
		m = 0
		while (x > 60):
			m += 1
			x -= 60
#print(death_time)
kills = []
kill_times = []
print(death_time)
mp = {}
for cur_time in range(0, clip_time, step):
	death_count = 0
	for dead_time in death_time:
		if (dead_time >= cur_time and dead_time <= cur_time + window) :
			death_count += 1
	kill_times.append(cur_time)
	kills.append(death_count)
	mp[cur_time] = death_count

print (mp[110])

#plt.plot(timestamps, damages) #--> for damage plot uncomment it when using it

l = 0
r = 20
ans = 0
for i in range(10) :
	m = (l + r) / 2
	#print (l, r, m)
	if (check (m, mp) == True) :
		l = m + 1
		ans = m
	else :
		r = m - 1







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
	x -= time_from_beginning
	if (line.find('"target":"npc_dota_hero') != -1) and (line.find('"attacker":npc_dota_hero') != -1): 
		damage_time_value.append([x, int(value)])
	

damages = []
timestamps = []

mp_damage = {}
for cur_time in range(0, clip_time, 5):
	cumulative_damage = 0
	for timestamp, value in damage_time_value:
		#print (timestamp)
		if (timestamp >= cur_time and timestamp <= cur_time + 3) :
			cumulative_damage += value
	#print(cumulative_damage)
	mp_damage[cur_time] = cumulative_damage
	damages.append(cumulative_damage)
	timestamps.append(cur_time)

cur_time = 0
cut_frames = []
threshold = 300
while (cur_time < clip_time) :
	if mp[cur_time] >= ans:
		beg_time = cur_time
		cur_time += window
		while (cur_time < clip_time) and (mp[cur_time] > 0 or mp_damage[cur_time] > threshold):
				cur_time += step
		cut_frames.append([beg_time, cur_time])
	else :
		cur_time += step 

print(ans)
print(cut_frames)

fig, ax1 = plt.subplots()
ax1.plot(kill_times, kills, 'b', label = "cumulative kills")
ax1.set_ylabel('kills', color='b')
ax1.tick_params('y', colors='b')
ax1.set_xlabel('time(s)')
ax1.legend(loc="upper left")
ax2 = ax1.twinx()
ax2.plot (timestamps, damages, 'g', label = "cumulative damage")
ax2.set_ylabel('damages', color='g')
ax2.tick_params('y', colors='g')
ax2.legend(loc="upper right")

font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 16,
        }
plt.title('highlights are red regions', fontdict=font)
fig.tight_layout()

#for l, r in cut_frames:
#	plt.axvspan(l, r, color='red', alpha=0.1)
#plt.show()

#print(ans)
for x, y in cut_frames:
	print x, y
#print(cut_frames)

#video = VideoFileClip("VP vs Liquid en.mp4")
#video_1 = video.subclip(cut_frames[0][0], cut_frames[0][1]) 
#video_2 = video.subclip(cut_frames[1][0], cut_frames[1][1]) #

#final_video = concatenate_videoclips([video_1, video_2])
#for i in range(2, len(cut_frames)):
#	video_i = video.subclip(cut_frames[i][0], cut_frames[i][1])  
#	final_video = concatenate_videoclips([final_video, video_i])
#
#final_video.write_videofile("highlight_final__damage_eng.mp4")