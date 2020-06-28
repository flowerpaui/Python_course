import pandas as pd
import matplotlib.pyplot as plt
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
