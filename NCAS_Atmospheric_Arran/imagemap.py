import matplotlib.pyplot as plt
import numpy as np
import time,glob
from pandas import*

fahrenheit_to_kelvin = lambda (temp) :(temp -32.0)*5.0/9.0 + 273

#get files
files = glob.glob('*.csv')

df=[]

for f in files[2:]: #read 2nd element onwards
	x = read_csv(f,header=1) #make df
	x = x.dropna(axis=1)#clean na
	x.columns = ['%s_%s'%(i.split(' ')[0].strip(','), f.split('_')[0]) for i in x.columns] # parse header names
	x[x.columns[2]] = x[x.columns[2]].map(fahrenheit_to_kelvin)#apply function to column 2 
	df.append(x)#add dataframe as element in df list 



## davis weatherstation
davis = read_csv(files[0]).dropna(axis=0)
davis.columns = ['%s_%s'%(i.split(' ')[0].strip(','), f.split('_')[0]) for i in davis.columns]

cq = 2 #temp column (i'm being lazy)
m = 0 #max

for i in df: m+= i[i.columns[cq]].max() # add the max value for each file in df list
m=(m/len(df)) # get average of sum of maximums 

if (m < davis[davis.columns[1]].max()): 	m = davis[davis.columns[1]].max() #if davis max is greater use this instead

''' do the same for min'''
mi=0
for i in df: mi+= i[i.columns[cq]].min()
mi=(mi/len(df)) 
if (mi< davis[davis.columns[1]].min()):	mi= davis[davis.columns[1]].min()




npx=8
npy=8
cmap = plt.get_cmap('YlOrRd')#colourmap
#http://matplotlib.org/examples/images_contours_and_fields/interpolation_methods.html

plt.show(block=False) ## update live


#sorry constants and bad programming tecneque
#mi=0
mx=m
m=1


time.sleep(10)

# draw some data in loop
for i in range(0,len(x), len(x)/1000):
	#time.sleep(1) # if needed to update slower
  
	# - davis.loc[i, davis.columns[cq]]/m + mic


	a= np.zeros((npy,npx))
	a[:,:]= davis.loc[i, davis.columns[1]] #set background to davis value
	#a[:,:] = 0.13 #set bg to white
	
    '''update sensors at locations on the grid'''
	a[3,4] = df[1].loc[i, df[1].columns[cq]]  
	a[3,3] = df[2].loc[i, df[2].columns[cq]] 
	a[4,0] = df[3].loc[i, df[3].columns[cq]]
	a[6,4] = df[4].loc[i, df[4].columns[cq]]
	a[7,1] = df[5].loc[i, df[5].columns[cq]]
	a[0,5] = df[6].loc[i, df[6].columns[cq]]
	a[7,3] = df[7].loc[i, df[7].columns[cq]]
	a[4,6] =  df[8].loc[i, df[8].columns[cq]]
	#sensor 9 
	a[6,5] =  df[0].loc[i, df[0].columns[cq]]

 	a=(a)/(mx) 


 	if (df[0].loc[i,df[0].columns[1]].split()[1] == '00:00:00'):
 	    #make title red at midnight
		plt.title('##########' +df[0].loc[i,df[0].columns[1]]+ '##########' ,color= 'red') 
	else:
		plt.title(df[0].loc[i,df[0].columns[1]],color='black')


	im.set_array(a) #update image map
	plt.draw()# redraw the figure






