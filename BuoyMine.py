'''
A rudementary program to that mines lon and lat of the buoy data. 
Dan Ellis, May 2016
'''
 
import urllib2, re 
from pandas import * 
import multiprocessing as mp 
import numpy as np 

a = re.compile('<a *[^>]*>') #read in all hyperlinks
e = re.compile('<b *[^>]*>.*</b><br') #read in block text


main = urllib2.urlopen('http://www.ndbc.noaa.gov/to_station.shtml').read() #read source

def mine (i): #gets text from link source. 
    try: 
        ur = i.split('"')[1]
        st= urllib2.urlopen('http://www.ndbc.noaa.gov/%s'%ur).read()
        return e.findall(st)      
    except: return []



n = mp.Pool(16).map(mine, a.findall(main))
np.save('temp.noaa',n)
#n=np.load('temp.noaa.npy')



def save(j): #check if coords contained, if so datamong & correct. 
        if 'N' in j: 
                
            if 'W' in j:
				k= j.split('(')[0].replace('<b>','')
				try:
					lon = (float(k.split(' N ')[0]))
					lat =(-1*float(k.split(' N ')[1].replace('W','').replace(' ','')))
					return [lat,lon]
				except:None


            if 'E' in j:
				k= j.split('(')[0].replace('<b>','')
				try:
					lon = (float(k.split(' N ')[0]))
					lat = (float(k.split(' N ')[1].replace('E','').replace(' ','')))
					return [lat,lon]
				except:None
				
        if 'S' in j: 
        
            if 'W' in j:
				k= j.split('(')[0].replace('<b>','')
				try:
					lon = (-1*float(k.split(' S ')[0]))
					lat =(-1*float(k.split(' S ')[1].replace('W','').replace(' ','')))
					return [lat,lon]
				except:None


            if 'E' in j:
				k= j.split('(')[0].replace('<b>','')
				try:
					lon = (-1*float(k.split(' S ')[0]))
					lat = (float(k.split(' S ')[1].replace('E','').replace(' ','')))
					return [lat,lon]
				except:None				
				
        return []



full=[]


def entries (k): #sep for mp
    coord=[]
    for j in k:  
        coord.extend(save(j))
    return coord


full.extend(mp.Pool(16).map(entries, n))
    
df= DataFrame(full).dropna(axis=0) # turn results into something useful. 
df['3'] = 1
df.columns= ['Longitude','Latitude','Altitude']
df.to_csv('buoydata.csv') #save







    
