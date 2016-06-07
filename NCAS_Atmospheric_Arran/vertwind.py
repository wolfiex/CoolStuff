import numpy as np 
from pandas import * 
import tephi  
import matplotlib.pyplot as plt
from bng import * 
import re
r = re.compile("([a-zA-Z]+)([0-9]+)") # search for letters and numbers only 

for i in ['Tfaffdata.csv', 'fitz.csv','eckman.csv']:


	a= read_csv(i)
	a= a[:-1] #remove last column 
	
	a['time']= a['GPS UTC Time'].map(lambda x: (str(x).replace(':',''))) #time
	H = a['Wind Speed (m/s)']  #wind speed
	theta = a['Wind Direction (m/s)'] #wind direction
	a['u'] = H / theta.map(lambda o: np.sin(float(o)) ) #u component
	a['v'] = H / theta.map(lambda o: np.cos(float(o)) ) #v component
	
	e,n=[],[]
	for j in a['GPS Location    (NS 04472 32358)']:
		
		try:
			cd = j.split(' ') #seperate coordinates 
			inp= cd[0].upper() # capitalise letters
			E=int(cd[1]) #east component    
			N=int(cd[2]) #north component
		
		except Exception as z:  
            ''' having failed the above try this - there were two formats used, this deals with both'''
			cd = j.split(' ')
			m = r.match(str(cd[0]))  #take only the letters and numbers (see regex in line 7)
			inp= m.group(1).upper() 
			E=m.group(2) # get from regex match
			N=cd[1] 


		if inp == 'NR': E -= 100000	 	
	 	e.append(int(E)*100)
	 	n.append(int(N)*100)
    
    #add as columns to the initial dataframe
	a['n']=n
	a['e']=e	

	w,t=[],[]
	
	
	for i in xrange(1,len(a)-2): 
        #for each index in dataframe (ie each row)
		ucomp = a.ix[i].u*a.ix[i+1]['GPS Altitude (m)']- a.ix[i-1]['GPS Altitude (m)']
		vcomp = a.ix[i].v*a.ix[i+1]['GPS Altitude (m)']- a.ix[i-1]['GPS Altitude (m)']
        
        #add w component to w list
		w.append(ucomp /(2*abs(a.ix[i+1].e - a.ix[i-1].e)) + vcomp/(2*abs(a.ix[i+1].n - a.ix[i-1].n)) )
		t.append(a.ix[i].time) #and time to time list 
	 

	plt.plot(t, Series(w).fillna(0), label= i ) #plot time and w, where any nans are equated to 0.  

#plot labels etc. 
plt.ylabel('Vert Windspeed')
plt.xlabel('Time (HHMM)')
plt.legend(loc='UL')
plt.show()	





