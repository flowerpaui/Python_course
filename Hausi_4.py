import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import ttest_ind

df = pd.read_csv('./assignment_4/parking_data_small.csv')
df.head() #kurzer Ueberblcik über Variablen und Art der Daten

###hier habe ich einfach ein bisschen rumprobiert
df.sort_values(by=['Issue Date']) #geordnet nach wann vergeben
df.groupby('RP State Plate').mean()

plt.hist(df['Fine amount'])
plt.show() #welche Strafhöhen wie oft

df['Issue time'].describe() #verstehen wie aufgebaut --> wie tausenderzahlen -> 1145.00--> 11.45h
#sinnvoll machen aufwendig --> durch 100 und dann nur Stunden nehmen o.ä?

##Untersuchen: verschiedene Strafhöhen nach Tageszeit?
#erst mal einfache Fragestellung: tagsüber (6-22h) anders als nachts(22-6)?
day=df['Fine amount'][df['Issue time'].isin(range(600,2200))]  #tags

night=df['Fine amount'][~df['Issue time'].isin(range(600,2200))] #nachts

ttest_ind(day.dropna(), night.dropna()) #sign Unterschied
#aber welche richtung?
day.mean()
night.mean() #nachts geringer


######PLOTTING

#versuche####
df.groupby('Agency')   
fine_array=np.array(df.groupby('Agency')['Fine amount'])
fine_list=list(df.groupby('Agency')['Fine amount'])
agcy=list(set(df['Agency'].values)) #nummern aller agencies (set damit alle nur einmal)

ls1=[]
for i in range(0, (len(agcy))):
    ls1.append(list(fine_list[i][1]))


plt.hist(ls1, bins=20, histtype='bar') #eher wirr da so untrschiedliche anzahl an vergebene
##versuche ende



###tag vs nacht
fig=plt.figure()
ax1=fig.add_subplot(1,2,1)
ax1.hist(day, color='yellow')
ax1.set_ylim([0,700])
ax1.set_title("Fines during the day")
ax1.set(xlabel='Amount of fine', ylabel="Number of fines issued")
ax1.set_ylim([0,700])
ax2=fig.add_subplot(1,2,2)
ax2.hist(night, color='black')
ax2.set_ylim([0,700])
ax2.set_title("Fines during the night")
ax2.set(xlabel='Amount of fine')
plt.savefig('./daynighthist.pdf')
plt.show()



#day times 
hrs=list(df['Issue time']/100) #hour fits, minutes as decimals
map(int, hrs)
df['hrs']=df['Issue time']/100

for i in range(0,len(df)):
    if df['hrs'][i]>0:
        df['hrs'][i]=int(df['hrs'][i]) #etwas kompliziert, aber hat wegen der nan sonst iwie nicht geklappt
#'cuts' decimals
#nur noch die Stunde angegeben, in der fine vergeben wurde

df.groupby('hrs')

hrfines=list(df.groupby('hrs')['Fine amount'].mean()) #liste mit den 24 MW der fines in den 24 des tages

hrfines.append(hrfines[0]) #an stellle 24 nochmal den wert von 0, damit plot netter ;)
plt.plot(hrfines, marker='.', color='white', markeredgecolor='red', markersize=10, linewidth=5) 
plt.xlim([0,24]) #zeit soll nur 0-24 gehen, automatisch die 25 noch, macht keinen sinn
plt.xticks(np.arange(0, 25, step=2)) #alle 2h strich an x
plt.title('Fines issued for parking')
plt.xlabel('Hour of the day')
plt.ylabel('Average cost of fine [$]')
plt.axvspan(0,24,facecolor='black') #hintergrund nachts (22-6) schwarz
plt.axvspan(6,22, facecolor='yellow') #und tags gelb
plt.savefig('./daynightplt.pdf')



