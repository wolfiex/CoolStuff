'''
A simple program to convert svg to png, and then use latex to create a grid of n plots across  for a page.
brew install Caskroom/cask/inkscape
brew install librsvg
etc...

inkscape t.svg --export-pdf=t.pdf
rsvg-convert -f pdf -o foo.pdf foo.svg


D.Ellis 2017
'''

import glob,sys,os
import numpy as np
from string import ascii_lowercase

ext = 'eps'
#ext {eps,pdf}



if len(sys.argv) > 1:
    files = sys.argv[1:]
else:
    files=glob.glob('*.svg')

os.system('mkdir svgfiles; rm ./svgfiles/*')

files.sort()
files = [k.replace('.svg','') for k in files]

cwd = os.getcwd()

for i in files:
    if ext=='pdf': cmd = "rsvg-convert -f pdf -o svgfiles/"+ i.replace(' ','') +".pdf " + i.replace(' ','\ ')+'.svg'
    #if ext=='pdf': cmd = "inkscape -z  --export-pdf="+ cwd+"/svgfiles/"+ i.replace(' ','\ ')+".pdf " + cwd+"/"+ i.replace(' ','\ ')+'.svg'
    elif ext=='eps': cmd = "inkscape -z --export-area-drawing " + cwd+"/"+ i.replace(' ','\ ')+".svg -E "+   cwd+"/svgfiles/"+ i.replace(' ','\ ')+".eps --export-ps-level=3"#--export-ignore-filters
    print i
    os.system(cmd)






def pdf(files, columns = 3,ext=ext, folder = 'svgfiles'):

    split =  np.split(np.array(files),xrange(0,len(files),columns))

    width = 1.0/columns

    string = ''
    counter = 0
    for i in split:
        print i , len(i)
        if len(i)>0:
            if (len(i)==columns):
                for j in i:
                    string += r'''\includegraphics[width=%.2f\textwidth]{%s} &'''%(width,j.replace(' ','')+'.'+ext)
                string = string[:-1] + '\\\\[6pt] \n'

                for k in i:
                    string += '(' + ascii_lowercase[counter] + ') ' + k.replace(' ','') + '  &'
                    counter +=1

                string = string[:-1] + '\\\\[6pt] \n'
            else:
                print i ,counter
                string += r'''\multicolumn{%d}{c}{\includegraphics[width=%.2f\textwidth]{%s} } \\\\[6pt] \n    \multicolumn{%d}{c}{(%s) %s}'''%(columns-1,width,i[0].replace(' ','')+'.'+ext,columns,ascii_lowercase[counter],i[0].replace(' ',''))+ '\\\\[6pt] \n'
                counter +=1


    latexdata =r'''
    \documentclass{article}
    \usepackage{geometry}
     \geometry{
     a4paper,
     total={170mm,257mm},
     left=10mm,
     right=10mm,
     top=10mm,
     bottom=12mm,
     }
    \usepackage{graphicx}
    \usepackage{subfig}

    \begin{document}

    \begin{figure}
    \begin{tabular}{%s}
    %s
    \end{tabular}
    \caption{caption}
    \end{figure}
    \end{document}

    ''' % ('c'*columns,string)




    with open(folder+'/result.tex','w') as f:
        f.write(latexdata)

    os.system('cd '+folder+'/ && pdflatex result.tex && cp result.pdf ../')

    print 'written'

pdf(files)
