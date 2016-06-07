import numpy as np 
from pandas import * 
import tephi  
import matplotlib.pyplot as plt


''' functions to plot tephigrams- use the sond function for the sond data''' 



def dew(T,RH):
    a, b = 17.271, 237.7 
    return (b * gamma(T,RH)) / (a - gamma(T,RH))

def gamma(T,RH):
    a, b = 17.271, 237.7 
    return (a * T / (b + T)) + np.log(RH/100.0)


def pt(filee='Tfaffdata.csv',col='blue'):
	df = read_csv(filee) #read file
	df['dews']= [ dew( i[1]['Dry Bulb Temperature (K) (Whirling Hygrometer)'] -273,
		 i[1]['Derived RH (%) (Whirling Hygrometer and Table)']) for i in df.iterrows() ]
	df = df.drop(df.index[-1]) #drop last column 

	tpg = tephi.Tephigram()
	#tpg.plot(dews, label='Dew-point temperature', color='blue', linewidth=2, linestyle='--', marker='s')
	profile = tpg.plot(zip(df['Pressure (mb)'],df.dews), linewidth=2, color=col )
	tpg.plot( zip(df['Pressure (mb)'],df['Dry Bulb Temperature (K) (Whirling Hygrometer)']-273),linewidth=2, color='grey')
	df.fillna(0, inplace=True)
	barbs = zip(df['Wind Speed (m/s)']*1.94384, df['Wind Direction (m/s)'],df['Pressure (mb)'])
	profile.barbs(np.array(barbs)[[range(0,len(barbs),2)]])
	plt.show()



def sond(col='magenta',bar=10):
	df = read_csv('sonddata.csv')
	df.columns = [i.replace(' ','') for i in df.columns]
	tpg = tephi.Tephigram()#tpg.plot(dews, label='Dew-point temperature', color='blue', linewidth=2, linestyle='--', marker='s')
	df=df[ df['P']>700 ]
	profile = tpg.plot(zip(df['P'],df['Dewp']), linewidth=2, color=col )
    
	tpg.plot( zip(df['P'],df['Temp']),linewidth=2, color='grey')
	barbs = zip(df['Speed']*1.94384, df['Dir'],df['P'])
	profile.barbs(np.array(barbs)[[range(0,len(barbs),bar)]])
	plt.show()

df = read_csv('sonddata.csv')
df.columns = [i.replace(' ','') for i in df.columns]
df = df[df.GpsHeightMSL<900]



#plt.show()
