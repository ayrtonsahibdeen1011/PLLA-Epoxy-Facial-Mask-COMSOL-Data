from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
import csv
R=Path(__file__).resolve().parent.parent
SOURCE=Path(r'C:\Users\ASUS\.codex\.chatgpt-projects\g-p-6aac0950585881919455cd2e85bfa9f1\COMSOL_FINAL_CORRECTED_20261006')
DEST=R/'03_BACKUP_AND_INDEPENDENT/COMSOL_FIELD_VIEWS'
DEST.mkdir(parents=True,exist_ok=True)
items=[
 ('A','STATIC_0','REFERENCE','DISPLACEMENT','Displacement magnitude (mm), stationary patch load','solid.disp','mm',0,.02),
 ('A','STATIC_1','REFERENCE','VON_MISES','von Mises stress (MPa), stationary patch load','solid.mises','MPa',0,.2),
 ('A','COOLING_0','REFERENCE','TEMPERATURE_300S','Temperature (K), 300 s, imposed convection','T','K',293.15,318.15),
 ('O','STATIC_0','OPEN_CORNER','DISPLACEMENT','Displacement magnitude (mm), stationary patch load','solid.disp','mm',0,.02),
 ('O','STATIC_1','OPEN_CORNER','VON_MISES','von Mises stress (MPa), stationary patch load','solid.mises','MPa',0,.2),
 ('O','COOLING_0','OPEN_CORNER','TEMPERATURE_300S','Temperature (K), 300 s, imposed convection','T','K',293.15,318.15)
]
font=ImageFont.truetype(r'C:\Windows\Fonts\arial.ttf',15)
out=[]
for code,case,short,label,title,expr,unit,lo,hi in items:
 original=f'FINAL_FIELD_{code}_{case}.png'
 inp=SOURCE/'03_SEPARATE_PANELS'/original
 assert inp.exists(),inp
 im=Image.open(inp).convert('RGB')
 width,height=im.size
 assert width==800 and height==600
 dr=ImageDraw.Draw(im)
 dr.rectangle((0,0,width,42),fill=(255,255,255))
 full='Reference shell' if code=='A' else 'Open-corner shell'
 dr.text((width/2,21),full+' | '+title,anchor='mm',font=font,fill='#111111')
 name=f'FIELD_{short}_{label}.png'
 im.save(DEST/name,optimize=True)
 assert (DEST/name).stat().st_size>10000
 out.append(dict(figure=name,source_original=original,public_shell_label=full,native_model=f'{code}_{"COOLING" if "COOLING" in case else "STATIC"}_FINAL.mph',
  dataset=('dset3' if code=='A' and 'COOLING' in case else 'dset1'),
  expression=expr,unit=unit,shared_color_min=lo,shared_color_max=hi,
  validity='Visualized solved COMSOL field with shared scale. Clipping is possible; NOT verified local stress peak.'))
 for f in DEST.glob(f'FINAL_FIELD_{code}_{case}.png'):
  f.unlink()
for f in DEST.glob('FINAL_FIELD_*.png'):
 f.unlink()
with (DEST/'FIELD_VIEW_SOURCE_AND_SCALES.csv').open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(out[0]));w.writeheader();w.writerows(out)
print('PASS 6 selected COMSOL backup fields relabeled + source map + retained shared color scales')
