import pandas as pd

import random, emailattachment
df = pd.read_csv('cdata.csv',)




df['id']=df.index
choices = ['Starter','Main','Dessert']

stats =''
for it in choices:
    stats += '\n\n %s\n'%it
    stat = df.groupby(it)[it].count()
    stat.sort(ascending=False)
    
    for s in range(len(stat)):
        stats += '''%s | %s\n''' %( stat[s]*'#',stat.index[s] )






while True:
    df['random']= [random.random() for i in df.index]
    df.sort('random',inplace=True)
    counter = 0
    for i in xrange(len(df)):
        if df.index[i] == df.id[i] : 
            counter +=1
    if counter ==0:   break


df.reset_index(inplace=True)



for i in xrange(len(df)):

    content = '' 
    
    user = df.ix[i].Name
    email = df.ix[i].email
    ss = df.ix[int(df.ix[i].id)].Name




    content += '''Hi %s, \n\nFor this years secret santa you shall be buying for :   %s. \n\nThis can be whatever you want (within reason of-course), but must lie between the \xA35-8 mark.  \nThe date of the meal is  Friday the 2nd of December, @7pm. \n\nYour meal choices are:\n'''%(user,ss)

    for c in choices:
        content += '%s : %s\n'%(c,df.ix[i][c])

    content+= '\nSee you there!\nThe second years. \n\n\nP.S. For those of you interested - Below are some stats about the meal choices.' +  stats 
    
  
    
    emailattachment.send(email, 'Secret Santa 2016',content,'daniel.ellis@york.ac.uk',attach='')
