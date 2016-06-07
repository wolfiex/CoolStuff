from pandas import *
import glob
import numpy as np
from matplotlib.pyplot import * 

folders = glob.glob('/Users/dna/Desktop/Proc/*') #get files


unstable = []
stable = []

for i in folders[:-1]: 
    #read for the 15th
	opn = glob.glob('%s/*15.csv'%i)
	stab = read_csv(opn[0])
	#read for the 14th
	opn = glob.glob('%s/*14.csv'%i)
	unstab = read_csv(opn[0])

    #manually select period i want (lazy)
	stab = stab.ix[1:60]
	unstab= unstab.ix[781:840]

    #update column headers to ones easier to use	
	columns = ['time','u','v','t','rh']
	stab.columns = columns
	unstab.columns = columns

    #wind speed
	stab['ws'] = [ np.sqrt(i[1].v**2 + i[1].u**2) for i in stab.iterrows()]
	unstab['ws'] = [ np.sqrt(i[1].v**2 + i[1].u**2) for i in unstab.iterrows()]

    #add to the empty lists from the start
	stable.append(stab)
	unstable.append(unstab)



offset = .15
height = np.array([1.32,1.85,2.69,4.04,6.08,8.95])+  offset
height = np.vectorize(lambda x : np.log(x))(height)

dummy_u, dummy_s= [], []
sd_u=[]
sd_s=[]
#make lists with data
for i in xrange(len(stable)):
	dummy_s.append(stable[i].ws.mean())
	dummy_u.append(unstable[i].ws.mean())			
	sd_s.append(stable[i].ws.max())
	sd_u.append(unstable[i].ws.max())


for i in folders: 
    #read files
	opn = glob.glob('%s/*11.csv'%i)
	try: 
		df = read_csv(opn[0])

		df.DateTime.map(lambda x: x.split(' ')[1].replace(':',''))#seperate by space, and remove colons

		df.columns = ['time','u','v','t','rh']

		df['ws'] = [ np.sqrt(j[1].v**2 + j[1].u**2) for j in df.iterrows()] #windspeed 

		plot( df.t,  label = i)#plot temp vs index for each file 


	except: None #if error incurred, do nothing

legend(loc='UL')#legend in upper left
show()
