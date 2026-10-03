import sys
from pathlib import Path
from PIL import Image
d=Path(sys.argv[1]); cols=int(sys.argv[2]) if len(sys.argv)>2 else 5; tw=int(sys.argv[3]) if len(sys.argv)>3 else 360
pat=sys.argv[4] if len(sys.argv)>4 else "[0-9]*.png"
fs=sorted(d.glob(pat))
ims=[Image.open(f) for f in fs]
w,h=ims[0].size; th=int(h*tw/w)
rows=(len(ims)+cols-1)//cols
S=Image.new("RGB",(cols*(tw+6),rows*(th+6)),(255,0,80))
for k,im in enumerate(ims):
    S.paste(im.convert("RGB").resize((tw,th)),((k%cols)*(tw+6),(k//cols)*(th+6)))
o=d/("sheet-"+pat.replace('*','x').replace('[','').replace(']','').replace('?','q')+".png"); S.save(o); print(o, len(ims))
