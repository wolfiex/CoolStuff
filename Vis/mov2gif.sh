ffmpeg -y -ss 30 -t 3 -i $@ \
-vf fps=10,scale=320:-1:flags=lanczos,palettegen palette.png\
 &&  \
ffmpeg -ss 30 -t 3 -i $@ -i palette.png -filter_complex \
 "fps=10,scale=320:-1:flags=lanczos[x];[x][1:v]paletteuse" output.gif


#$@ is the movie file, ss is the skip at the start time, t is the duration, scale is the pixels
