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


if len(sys.argv) > 1:
    files = sys.argv[1:]
else:
    files=glob.glob('*.svg')

os.system('mkdir svgfiles; rm ./svgfiles/*')

files.sort()
files = [k.replace('.svg','') for k in files]

for i in files:
    cmd = "rsvg-convert -f pdf -o svgfiles/"+ i.replace(' ','') +".pdf " + i.replace(' ','\ ')+'.svg'
    print i
    os.system(cmd)






def pdf(files, columns = 2,ext='pdf'):

    split = np.split(np.array(files),[columns,])

    width = 1.0/columns

    string = ''
    counter = 0
    for i in split:
        if len(i)>1:
            for j in i:
                string += r'''\includegraphics[width=%.2f\textwidth]{%s.ext} & '''%(width,j.replace(' ',''))
            string = string[:-1] + ' \cr '

            for k in i:
                string += '(' + ascii_lowercase[counter] + ') ' + k.replace(' ','') + '  & '
                counter +=1

            string = string[:-1] + '\\\\[6pt] \n'
        else:
            string += r'''\multicolumn{%d}{c}{\includegraphics[width=%.2f\textwidth]{%s.ext} } \cr    \multicolumn{%d}{c}{(%s) %s}'''%(columns,width,i[0].replace(' ',''),columns,ascii_lowercase[counter],i[0].replace(' ',''))
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


    with open('svgfiles/result.tex','w') as f:
        f.write(latexdata)

    os.system('cd svgfiles/ && pdflatex result.tex && cp result.pdf ../')

    print 'written'
