'''
A script to iteratively download a website, and its dependant files.

D. Ellis May 2016

If running manually add module and run using:
from from_source_download import*  
url= 'http://.....'
get_dependancies(get_url(url))          
            
'''            
            
import sys,re
import urllib2

def get_url(url):
    ##function ot read source code, get the file name and download it
    response = urllib2.urlopen(url)
    html = response.read()
    filename= url.split('/')[-1]
    f= open(filename,'w')
    f.write(html)
    f.close()
    print filename, 'written'
    return html




def get_dependancies(html): 

    #get html code for links, js scripts and images
    links = re.findall(r'<\s{0,5}link*[^>]*>',html) #read in all hyperlinks
    scripts = re.findall(r'<\s{0,5}script\s{0,5}src*[^>]*>',html) 
    img = re.findall(r'<\s{0,5}img\s{0,5}src*[^>]*>',html)

    mined = scripts+links+img #combine found scripts

    #read all items within '' and ""
    strings = [re.findall(r'\"(.+?)\"',qt.replace(' ','')) for qt in mined] + [re.findall(r"\'(.+?)\'",qt.replace(' ','')) for qt in mined]


    for j in strings:
            for k in j: 
                newurl= '/'.join(url.split('/')[:-1])
                if (k[:2] == './'): k=k[2:]
                
                #try for full urls
                if '//' in k or 'http' in k or k[0]=='#': continue #not needed
                #recursivley go back a folder 
                while k[:3] == '../': 
                    newurl = '/'.join(newurl.split('/')[:-1])
                    k = k[3:]
                
                try:
                    html2 = get_url(newurl+'/'+k)
                    if k[-5:]--'.html': get_dependancies(html2) #call fn recursively
                    break
                except:None
                
 
 
 
if __name__ == "__main__":
    # read urls from cmd arguments
    for url in sys.argv[1:]: get_dependancies(get_url(url))
 
                
                
                
                
                
print 'remember to remove the path names of links in source code.'             


            
