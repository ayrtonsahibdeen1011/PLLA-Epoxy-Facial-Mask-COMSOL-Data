from pathlib import Path
import csv,hashlib
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
R=Path(__file__).resolve().parent.parent
SRC=R/'04_TABLES_AND_PROVENANCE/COMSOL_RAW_AND_VALIDATION/D03_CONTACT_STABLE.csv'
D=R/'01_RECOMMENDED_FIGURES/ORIGINAL_C_F_I_VERIFIED'
T=R/'04_TABLES_AND_PROVENANCE/MANUSCRIPT_READY_TABLES'
D.mkdir(exist_ok=True);T.mkdir(exist_ok=True)
with SRC.open(encoding='utf-8-sig',newline='') as f:raw=list(csv.DictReader(f))
assert len(raw)==12
C={}
for location in ['Center','Orbital']:
 C[location]=sorted((r for r in raw if r['case']==location),key=lambda r:float(r['displacement_mm']))
 assert [float(r['displacement_mm']) for r in C[location]]==[1.5,2.,2.5,3.,3.5,4.]
 assert all(r['release_status']=='RELEASE_1p5_TO_4' for r in C[location])
def value(w,x,key):
 return float(next(r[key] for r in C[w] if float(r['displacement_mm'])==x))
def ratio(key):return value('Orbital',4.,key)/value('Center',4.,key)
B='#245579';O='#be5f47'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'axes.linewidth':.9,
 'svg.fonttype':'none','pdf.fonttype':42,'axes.facecolor':'white','figure.facecolor':'white'})
def clean(ax):
 ax.grid(False);ax.spines['top'].set_visible(False);ax.spines['right'].set_visible(False)
 ax.tick_params(direction='out')
def bars(ax,xx,ys,colors,w):
 objects=ax.bar(xx,ys,width=w,color=colors)
 for obj,y in zip(objects,ys):
  ax.annotate(f'{y:.2f}',(obj.get_x()+obj.get_width()/2,y),
   textcoords='offset points',xytext=(0,4),ha='center',va='bottom',fontsize=9)
def chart_c(ax):
 locs=np.array([3.,4.])
 bars(ax,list(locs-.17)+list(locs+.17),
  [value('Center',float(x),'ROI_mean_stress_MPa') for x in locs]+
  [value('Orbital',float(x),'ROI_mean_stress_MPa') for x in locs],
  [B,B,O,O],.34)
 ax.set_xticks([3,4],['3.0','4.0']);ax.set_xlim(2.55,4.45);ax.set_ylim(0,5.7)
 ax.set_ylabel('Regional mean von Mises stress (MPa)')
 ax.set_xlabel('Prescribed sphere movement (mm)')
 clean(ax)
def chart_f(ax):
 for case,col,mark in [('Center',B,'o'),('Orbital',O,'s')]:
  x=[float(r['displacement_mm']) for r in C[case]]
  y=[float(r['ROI_mean_stress_MPa']) for r in C[case]]
  ax.plot(x,y,color=col,lw=1.7,marker=mark,markersize=5)
 ax.set_xlim(1.4,4.1);ax.set_ylim(0,5.35)
 ax.set_xticks([1.5,2,2.5,3,3.5,4])
 ax.set_ylabel('Regional mean von Mises stress (MPa)')
 ax.set_xlabel('Prescribed sphere movement (mm)')
 clean(ax)
def chart_i(ax):
 bars(ax,[-.17,.83,.17,1.17],
  [1.,1.,ratio('ROI_mean_stress_MPa'),ratio('ROI_mean_energy_density_kJ_m3')],
  [B,B,O,O],.34)
 ax.set_xticks([0,1],['Regional mean\nstress','Regional mean\nelastic energy density'])
 ax.set_ylim(0,1.27);ax.set_xlim(-.55,1.55)
 ax.set_ylabel('Ratio to center (center = 1)')
 clean(ax)
def save(fig,p):
 fig.savefig(str(p)+'.pdf',bbox_inches='tight',pad_inches=.15)
 fig.savefig(str(p)+'.svg',bbox_inches='tight',pad_inches=.15)
 fig.savefig(str(p)+'.png',dpi=320,bbox_inches='tight',pad_inches=.15)
 fig.savefig(str(p)+'.tiff',dpi=600,bbox_inches='tight',pad_inches=.15,pil_kwargs={'compression':'tiff_lzw'})
 plt.close(fig)
legend=[Patch(color=B,label='Center'),Patch(color=O,label='Upper orbital')]
parts=[('C_REGIONAL_STRESS_3_AND_4_MM',chart_c),('F_REGIONAL_STRESS_1P5_TO_4_MM',chart_f),
 ('I_REGIONAL_MEAN_RATIOS_AT_4_MM',chart_i)]
for nm,draw in parts:
 fig,ax=plt.subplots(figsize=(5.6,4.5))
 fig.subplots_adjust(left=.15,right=.97,bottom=.22,top=.79)
 draw(ax)
 fig.legend(handles=legend,loc='upper center',frameon=False,ncol=2,bbox_to_anchor=(.5,.982),fontsize=9.5)
 save(fig,D/nm)
fig,axes=plt.subplots(1,3,figsize=(16.8,5))
fig.subplots_adjust(left=.065,right=.989,bottom=.225,top=.78,wspace=.39)
for tag,(_,draw),ax in zip(('c','f','i'),parts,axes):
 draw(ax);ax.set_title('('+tag+')',loc='left',weight='bold',pad=11)
fig.legend(handles=legend,loc='upper center',frameon=False,ncol=2,bbox_to_anchor=(.5,.955))
save(fig,D/'C_F_I_VERIFIED_COMBINED')
records=[]
for row in raw:
 records.append(dict(panel='f',loading_location=row['case'],
  displacement_mm=row['displacement_mm'],regional_mean_stress_MPa=row['ROI_mean_stress_MPa'],
  regional_mean_energy_density_kJ_m3=row['ROI_mean_energy_density_kJ_m3'],
  source='D03_CONTACT_STABLE.csv',interpretation='Solved regional mask-domain mean (not global peak)'))
for x in (3.,4.):
 for label in ('Center','Orbital'):
  records.append(dict(panel='c',loading_location=label,displacement_mm=x,
   regional_mean_stress_MPa=value(label,x,'ROI_mean_stress_MPa'),
   regional_mean_energy_density_kJ_m3=value(label,x,'ROI_mean_energy_density_kJ_m3'),
   source='D03_CONTACT_STABLE.csv',interpretation='Selected 3 and 4 mm solved values; NOT the old 30/40 mm workbook'))
for label in ('Center','Orbital'):
 records.append(dict(panel='i',loading_location=label,displacement_mm=4.,
  regional_mean_stress_MPa=value(label,4.,'ROI_mean_stress_MPa')/value('Center',4.,'ROI_mean_stress_MPa'),
  regional_mean_energy_density_kJ_m3=value(label,4.,'ROI_mean_energy_density_kJ_m3')/value('Center',4.,'ROI_mean_energy_density_kJ_m3'),
  source='D03_CONTACT_STABLE.csv',interpretation='Normalized ratio, center=1, dimensionless'))
with (T/'TABLE_I_ORIGINAL_C_F_I_VERIFIED_PLOT_DATA.csv').open('w',newline='',encoding='utf-8-sig') as f:
 w=csv.DictWriter(f,fieldnames=list(records[0]));w.writeheader();w.writerows(records)
text="""# Corrected original-style panels (c), (f), (i)
# 最初图 c/f/i 的可靠数据替代图

These three panels deliberately reproduce the FORM of the old montage, not the invalid old global peak data.

**Source:** the delivered 12-record file at 04_TABLES_AND_PROVENANCE/COMSOL_RAW_AND_VALIDATION/D03_CONTACT_STABLE.csv, taken from COMSOL 6.3 fully solved Center_MESH3_SOLVED.mph and Orbital_MESH3_SOLVED.mph, found in 07_COMSOL_EDITABLE_NATIVE_MODELS in the full archive. Exact copied values, normalized derived ratios and source references are all in 04_TABLES_AND_PROVENANCE/MANUSCRIPT_READY_TABLES/TABLE_I_ORIGINAL_C_F_I_VERIFIED_PLOT_DATA.csv; the same raw model response is listed in TABLE_E_HISTORICAL_SPHERE_CONTACT_12_SOLUTIONS.csv.

**(c):** Center and upper orbital regional mask-domain mean von Mises stress at prescribed movement 3.0 and 4.0 mm. The OLD panel (c) used unresolved 30/40 mm workbook loading and an all-domain maximum, which cannot honestly be re-labelled or reused. This revised panel uses verified mesh-3 regional quantities and 3/4 mm instead.

**(f):** Center and orbital regional mean von Mises stress for the six verified solved movements 1.5, 2, 2.5, 3, 3.5 and 4 mm. Do not use the old 20/40 global maxima, and do not extrapolate the unverified initial contact/onset interval.

**(i):** At 4 mm, each location's mean stress and mean elastic energy density normalized by the respective center value. Orbital/center stress ratio = 0.6650 and energy density ratio = 0.4531. This is NOT total dissipated energy or physical impact protection.

**Numerical limitations:** Models are stationary nonlinear contact, separate original historical geometry scale, a sphere with numerically prescribed movement and non-identical resulting contact force, approximate ROI 0.150 m radius intersected with mask-domain material (volumes differ between positions). Effective homogeneous material E=3.5 GPa, v=0.38 is an assumption, not a measured PLLA-epoxy laminate. Retain the documented idealized supports and initial-clearance sensitivity limitations. No transient impact, crash absorption or injury reduction is established. Detailed methods and sensitivity records are supplied in the main handoff. The original archived global maxima failed provenance/domain and convergence checks; this regional-mean correction is a scientifically DIFFERENT set of quantities.

**建议图注：** (c) 在3和4 mm的球体指定位移下，中间与眶部区域体积平均von Mises应力；(f) 1.5到4 mm的六个已计算位移点的区域平均应力响应；(i) 4 mm时区域平均应力及平均弹性能量密度的眶部/中央归一化比率。注意原版30/40 mm图及旧全局最大值不可作为已验证结果；位移相等不代表作用力相等，弹性能量密度亦不等于吸收冲击能。
"""
(D/'READ_FIRST_C_F_I_DATA_SOURCES_AND_CAPTIONS_EN_CN.md').write_text(text,encoding='utf-8')
digest=hashlib.sha256(SRC.read_bytes()).hexdigest()
(D/'D03_SOURCE_SHA256.txt').write_text('Source file: 04_TABLES_AND_PROVENANCE/COMSOL_RAW_AND_VALIDATION/D03_CONTACT_STABLE.csv\nSHA256: '+digest+'\n')
print('PASS combined and 3 individual panels, PDF/SVG/PNG/TIFF')
print('PASS plot data rows',len(records),'source D03 SHA256',digest)
print('PASS c 3/4mm; f 1.5-4mm; i normalized ratios',
      ratio('ROI_mean_stress_MPa'),ratio('ROI_mean_energy_density_kJ_m3'))
