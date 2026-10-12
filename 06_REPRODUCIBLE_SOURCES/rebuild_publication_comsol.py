"""
Rebuild data-driven COMSOL figures for the collaborator.
Uses only archived, solved COMSOL numerical CSVs and validated QA data;
the original numerical models, COMSOL source results and dense histories are untouched.
Reference shell = original A configuration. Open-corner shell = repaired O geometry.
Do not interpret the differences as an isolated corner-opening effect.
"""
from pathlib import Path
import csv,json,math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from PIL import Image,ImageDraw,ImageFont
ROOT=Path(__file__).resolve().parent.parent
RAW=ROOT/'04_TABLES_AND_PROVENANCE'/'COMSOL_RAW_AND_VALIDATION'
SPLIT=ROOT/'02_SUPPLEMENTAL_FIGURES'/'INDIVIDUAL_PANELS'
MAIN=ROOT/'02_SUPPLEMENTAL_FIGURES'
MAINSP=ROOT/'01_RECOMMENDED_FIGURES'/'INDIVIDUAL_PANELS'
SPLIT.mkdir(parents=True,exist_ok=True)
MAINSP.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':9.4,'axes.linewidth':.8,'axes.facecolor':'white',
 'figure.facecolor':'white','svg.fonttype':'none','pdf.fonttype':42,'axes.edgecolor':'#242424',
 'xtick.direction':'out','ytick.direction':'out','savefig.facecolor':'white'})
CLR={'Reference shell':'#205579','Open-corner shell':'#BC533E'}
NAMES=['Reference shell','Open-corner shell']
def data(name):
 with (RAW/name).open('r',encoding='utf-8-sig',newline='') as f:
  return list(csv.DictReader(f))
def export(fig,stem,folder,hi=False):
 for ext in ('pdf','svg'):
  fig.savefig(folder/(stem+'.'+ext),bbox_inches='tight',pad_inches=.12)
 fig.savefig(folder/(stem+'.png'),dpi=320,bbox_inches='tight',pad_inches=.12)
 if hi: fig.savefig(folder/(stem+'.tiff'),dpi=550,bbox_inches='tight',pad_inches=.12,pil_kwargs={'compression':'tiff_lzw'})
 plt.close(fig)
def decorate(ax,metric,title,panel=None):
 ax.grid(False)
 ax.spines['top'].set_visible(False);ax.spines['right'].set_visible(False)
 ax.tick_params(labelsize=9,pad=4)
 ax.set_ylabel(metric,fontsize=9.5,labelpad=6)
 ax.set_title((f'({panel})  ' if panel else '')+title,fontsize=10.2,loc='left',pad=13)
def cooling_curve(ax,h,letters=None):
 aa=data(f'A_COOLING_h{h}.csv')
 oo=data(f'O_0p2_h{h}_TIGHT.csv')
 assert len(aa)>=150 and len(oo)>=150
 for nm,rr in [('Reference shell',aa),('Open-corner shell',oo)]:
  tt=np.asarray([float(x['time_s']) for x in rr],dtype=float)
  cc=np.asarray([float(x['mean_T_K'])-273.15 for x in rr],dtype=float)
  assert abs(tt[0])<1e-6 and tt[-1]>899 and abs(cc[0]-45)<.1
  ax.plot(tt,cc,lw=1.85,c=CLR[nm],label=nm,zorder=3)
 decorate(ax,'Mean solid temperature (°C)',f'Cooling, h = {h} W/(m²·K)',letters)
 ax.set_xlim(0,900);ax.set_ylim(19.5,45.5);ax.set_xticks([0,300,600,900])
 ax.set_xlabel('Time (s)')
 return aa,oo
def plotbars(ax,items,title,ylabel,letter=None,ymin=0,ylim=None,sci=False):
 xx=np.arange(len(items),dtype=float)
 vals=[float(t[1]) for t in items]
 cols=[t[2] for t in items]
 bars=ax.bar(xx,vals,color=cols,width=.55,zorder=3)
 ax.set_xticks(xx,[t[0] for t in items],fontsize=8.8)
 ax.tick_params(axis='x',length=0)
 ax.set_ylim(ymin,ylim if ylim else max(vals)*1.32)
 if sci: ax.ticklabel_format(axis='y',style='sci',scilimits=(-2,2))
 decorate(ax,ylabel,title,letter)
 for b,v in zip(bars,vals):
  sval=f'{v:.4g}' if abs(v)<.1 else f'{v:.3f}' if abs(v)<1 else f'{v:.2f}'
  ax.annotate(sval,(b.get_x()+b.get_width()/2,b.get_height()),
              xytext=(0,4),textcoords='offset points',ha='center',va='bottom',fontsize=8.5)
 ax.margins(x=.12)
def composition(stem,render):
 fig,axs=plt.subplots(2,2,figsize=(10.8,7.9))
 fig.subplots_adjust(left=.088,right=.963,bottom=.105,top=.885,wspace=.3,hspace=.4)
 for i,ax in enumerate(axs.flat):render(i,ax,chr(97+i))
 legend=[Line2D([0],[0],lw=2,c=CLR[nm],label=nm) for nm in NAMES] if stem=='S02_COOLING' else None
 if legend:
  fig.legend(handles=legend,loc='upper center',ncol=2,frameon=False,bbox_to_anchor=(.5,.977),fontsize=10)
 export(fig,stem,MAIN,True)
 for i in range(4):
  fig,ax=plt.subplots(figsize=(5.45,4.18))
  fig.subplots_adjust(left=.15,right=.96,bottom=.19,top=.81)
  render(i,ax,chr(97+i))
  if legend and i<3:
   fig.legend(handles=legend,loc='upper center',ncol=2,frameon=False,bbox_to_anchor=(.5,.983),fontsize=9)
  export(fig,f'{stem}_{chr(97+i)}',SPLIT,True)
qa=json.loads((RAW/'CORRECTED_QA.json').read_text(encoding='utf8'))
co=qa['comparisons']
# Strict checkpoint is intentionally NOT inserted into a plot of A dense solver outputs.
# At 300s, the A reference curve is ~0.0052 K different from the tighter verification.
def rr_at_300(h):
 a,o=data(f'A_COOLING_h{h}.csv'),data(f'O_0p2_h{h}_TIGHT.csv')
 def near(r):return min(r,key=lambda x:abs(float(x['time_s'])-300))
 return float(near(a)['mean_T_K'])-273.15,float(near(o)['mean_T_K'])-273.15
def cool_plot(i,ax,letter):
 if i<3:
  cooling_curve(ax,[8,4,16][i],letter)
 else:
  ref,opn=rr_at_300(8)
  plotbars(ax,[('Reference\nshell',ref,CLR[NAMES[0]]),('Open-corner\nshell',opn,CLR[NAMES[1]])],
           'At 300 s, h = 8 W/(m²·K)','Mean temperature (°C)',letter,ylim=40)
composition('S02_COOLING',cool_plot)
coords=qa['coordinate']
def mech_plot(i,ax,letter):
 r,o=coords['A'],coords['0p2']
 info=[
  ('Mean von Mises stress','Stress (MPa)','mean_vm_Pa',1e-6,.05),
  ('Maximum displacement','Displacement (mm)','max_disp_m',1000,.021),
  ('Stored elastic energy','Energy (mJ)','energy_J',1000,.021),
  ('Integrated material volume','Volume (cm³)','volume_m3',1e6,100)
 ]
 title,y,key,scale,lim=info[i]
 plotbars(ax,[('Reference\nshell',r[key]*scale,CLR[NAMES[0]]),
              ('Open-corner\nshell',o[key]*scale,CLR[NAMES[1]])],title,y,letter,ylim=lim)
composition('S03_MECHANICAL',mech_plot)
def change(key,field):
 return abs(float(co[key][field]))
def sens_plot(i,ax,letter):
 C1=CLR['Reference shell'];C2=CLR['Open-corner shell']
 specs=[
  ('Thermal checks (open-corner)',
   'Max. mean-temperature difference (K)',
   [('Time-step',co['O_0p2_h8_TOLERANCE.csv']['max_mean_difference_K'],C2),
    ('Mesh',co['O_fine_h8_TIGHT.csv']['max_mean_difference_K'],C2),
    ('Repair',co['O_alt_h8_TIGHT.csv']['max_mean_difference_K'],C2)],.026),
  ('Mechanical numerical checks',
   'Absolute mean-stress change (%)',
   [('Ref. mesh',change('COORD_A_fine','mean_vm_Pa_difference_percent'),C1),
    ('Open mesh',change('COORD_0p2_fine','mean_vm_Pa_difference_percent'),C2),
    ('Open repair',change('COORD_repair','mean_vm_Pa_difference_percent'),C2)],.48),
  ('Support-region sensitivity',
   'Absolute displacement change (%)',
   [('Reference',change('COORD_A_wide','max_disp_m_difference_percent'),C1),
    ('Open-corner',change('COORD_0p2_wide','max_disp_m_difference_percent'),C2)],31),
  ('Support-stiffness sensitivity',
   'Absolute displacement change (%)',
   [('Reference',change('COORD_A_stiff','max_disp_m_difference_percent'),C1),
    ('Open-corner',change('COORD_0p2_stiff','max_disp_m_difference_percent'),C2)],5)
 ]
 title,yl,items,lim=specs[i]
 plotbars(ax,items,title,yl,letter,ylim=lim)
composition('S04_SENSITIVITY',sens_plot)
# Rewrite existing S01 bitmap's editorial LABEL BANDS ONLY, with no alterations to source mask outlines/scales.
geometry=MAIN/'S01_GEOMETRY.png'
im=Image.open(geometry).convert('RGB')
assert im.size==(2400,1500)
dr=ImageDraw.Draw(im)
# The original titles lie in whitespace above the drawings; black headings in old image start at x ~50.
# Preserve visual render, descriptions and scientific size; only typography/band text changes.
try:
 font=ImageFont.truetype(r'C:\Windows\Fonts\arialbd.ttf',37)
 small=ImageFont.truetype(r'C:\Windows\Fonts\arial.ttf',24)
except OSError:
 font=ImageFont.load_default()
 small=ImageFont.load_default()
dr.rectangle((22,12,1525,94),fill='white')
dr.rectangle((22,700,1800,790),fill='white')
dr.text((38,27),'Reference shell  |  original curved configuration',fill='#161616',font=font)
dr.text((38,719),'Open-corner shell  |  repaired source configuration',fill='#161616',font=font)
im.save(geometry,optimize=True)
# Mirrors: M01 user-facing figure already has central/orbital labels; copy split panels to discoverable place.
# Supplied M01 split panels were originally in BACKUP/COMSOL_SPLIT_PANELS.
source=ROOT/'03_BACKUP_AND_INDEPENDENT'/'COMSOL_SPLIT_PANELS'
for ch in 'abcd':
 for ext in ('pdf','svg','png'):
  from shutil import copy2
  src=source/f'M01_{ch}.{ext}'
  dest=MAINSP/f'M01_{ch}.{ext}'
  if src.exists():copy2(src,dest)
  else:assert dest.exists(),dest
print('PASS 3 COMSOL composites, 12 individual panels, S01 titles, M01 split panels')
print('S02 h8 dense 300s C',rr_at_300(8))
