"""
Export the measured (UTM), assumed (COMSOL) and computed (COMSOL solution)
values without changing original numerical data. Creates Excel-compatible CSV
files and a Word-readable browser table appendix with citations to local files.
"""
from pathlib import Path
import csv,json,html,math
from datetime import date
R=Path(__file__).resolve().parent.parent
DATA=R/'04_TABLES_AND_PROVENANCE'
RAW=DATA/'COMSOL_RAW_AND_VALIDATION'
READ=R/'00_READ_FIRST'
OUT=DATA/'MANUSCRIPT_READY_TABLES'
OUT.mkdir(exist_ok=True)
def readcsv(p):
 with Path(p).open('r',encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
def writecsv(name,fieldnames,rows):
 p=OUT/name
 with p.open('w',encoding='utf-8-sig',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fieldnames,extrasaction='ignore');w.writeheader();w.writerows(rows)
 return p
def fld(raw,key):
 return float(raw[key])
qa=json.loads((RAW/'CORRECTED_QA.json').read_text(encoding='utf8'))
v=qa['coordinate']
source_input=readcsv(RAW/'PARAMETERS_EN_CN.csv')
PARAM=[]
def param(family,key,value,unit,evidence,source,note=''):
 PARAM.append(dict(model_family=family,parameter=key,value=str(value),unit=unit,evidence_status=evidence,source_file=source,interpretation_and_caveat=note))
core='PARAMETERS_EN_CN.csv; METHODS_AND_INTERPRETATION_EN_CN.md; A_STATIC_FINAL.mph/O_STATIC_FINAL.mph; A_COOLING_FINAL.mph/O_COOLING_FINAL.mph'
param('Geometry','Model A designation','Reference shell (existing curved configuration)','—','Model identity','S01_GEOMETRY.png; A_ALIGNED_WIDTH150_M.stl','NOT necessarily a thickness/coverage-matched closed-corner counterpart')
param('Geometry','Model O designation','Open-corner shell (repaired source STL)','—','Model identity','S01_GEOMETRY.png; OPEN_MASK_SOURCE_UNMODIFIED.stl','Distinct complete geometry, not only a cutout in the reference mask')
param('Geometry','Reference nominal width',150,'mm','Assumed normalization','PARAMETERS_EN_CN.csv','Both models normalized to nominal 150 mm; not an experimentally measured specimen width')
param('Geometry','Open-corner nominal width',150,'mm','Assumed normalization','PARAMETERS_EN_CN.csv','Does not imply matched volume or material thickness')
param('Geometry','Reference integrated material volume',v['A']['volume_m3']*1e6,'cm3','Numerical domain integration','CORRECTED_QA.json','Calculated on actual finite-element volume')
param('Geometry','Open-corner integrated material volume',v['0p2']['volume_m3']*1e6,'cm3','Numerical domain integration','CORRECTED_QA.json','Calculated on actual finite-element volume')
param('Geometry','Reference calculated mass',v['A']['volume_m3']*1400*1000,'g','Derived from assumed density','CORRECTED_QA.json; PARAMETERS_EN_CN.csv','Not actual weighed mass')
param('Geometry','Open-corner calculated mass',v['0p2']['volume_m3']*1400*1000,'g','Derived from assumed density','CORRECTED_QA.json; PARAMETERS_EN_CN.csv','Not actual weighed mass')
for key,value,unit in [
 ('Effective Young modulus',3.5,'GPa'),('Poisson ratio',.38,'1'),
 ('Density',1400,'kg/m3'),('Thermal conductivity',.25,'W/(m K)'),
 ('Specific heat capacity',1000,'J/(kg K)')]:
 param('Shared A/O homogeneous effective solid',key,value,unit,'Assumed NOT coupon-calibrated',core,'No explicit PLLA fibres, epoxy ply/interface, fracture, anisotropy or viscoelastic dissipation')
param('Shared A/O solid mechanics','Model equations','Linear elastic 3D solids','—','Native solid mechanics settings','METHODS_AND_INTERPRETATION_EN_CN.md; .mph','Small-strain idealized comparison, not impact test or damage simulation')
param('Shared A/O solid mechanics','Applied resultant force',2.70025832,'N','Prescribed equal-force scenario','T02_CORRECTED_MECHANICAL.csv; CORRECTED_QA.json','Same normalized Gaussian resultant on both configurations')
param('Shared A/O solid mechanics','Gaussian spatial radius',18,'mm','Assumed loading distribution','PARAMETERS_EN_CN.csv','Not a measured ball-contact pressure field')
param('Shared A/O solid mechanics','Restoring support traction','-K × gfix × (u,v,w)','N/m2','Specified mathematical idealization','METHODS_AND_INTERPRETATION_EN_CN.md','Not an exact clamped fixture or instrument-calibrated mounting condition')
param('Shared A/O solid mechanics','Support weighting gfix','0.5[1+tanh((abs(x)-xs)/0.25 mm)]','1','Specified analytical profile','METHODS_AND_INTERPRETATION_EN_CN.md','Physical boundary selection based on global x-coordinate')
param('Shared A/O solid mechanics','Baseline support coordinate threshold',65,'mm','Assumed','PARAMETERS_EN_CN.csv','Support sensitivity changed threshold to 60 mm')
param('Shared A/O solid mechanics','Support-region test threshold',60,'mm','Sensitivity only','PARAMETERS_EN_CN.csv','Changes the effective area and response')
param('Shared A/O solid mechanics','Support transition width',.25,'mm','Assumed tanh transition width','PARAMETERS_EN_CN.csv','Smooth transition')
param('Shared A/O solid mechanics','Baseline support stiffness',1e12,'N/m3','Assumed near-clamp penalty','PARAMETERS_EN_CN.csv','Stiffness sensitivity uses 1e13 N/m3')
param('Shared A/O solid mechanics','Support stiffness check',1e13,'N/m3','Sensitivity only','PARAMETERS_EN_CN.csv','Not a calibrated clamp')
param('Shared A/O cooling','Study','Time-dependent conduction, external convection','—','Model configuration','METHODS_AND_INTERPRETATION_EN_CN.md','No fluid flow, human skin or face-contact model')
param('Shared A/O cooling','Governing equation','ρ Cp ∂T/∂t = ∇·(k ∇T)','—','Documented PDE','METHODS_AND_INTERPRETATION_EN_CN.md','Homogeneous solid conduction')
param('Shared A/O cooling','Initial uniform temperature',318.15,'K','Prescribed','PARAMETERS_EN_CN.csv','Equivalent to 45°C')
param('Shared A/O cooling','Ambient temperature',293.15,'K','Prescribed','PARAMETERS_EN_CN.csv','Equivalent to 20°C')
param('Shared A/O cooling','Baseline convection coefficient',8,'W/(m2 K)','Prescribed','PARAMETERS_EN_CN.csv','Uniform on all exposed boundaries')
param('Shared A/O cooling','Boundary sensitivity coefficients','4;16','W/(m2 K)','Prescribed variants','PARAMETERS_EN_CN.csv','No measured ventilation rate or experimental calibration')
param('Shared A/O cooling','Radiation / heat generation','Not applied','—','Model omission','METHODS_AND_INTERPRETATION_EN_CN.md','No radiation or generated heat sources')
param('Shared A/O cooling','Simulation time interval','0 to 900','s','Time-dependent solution','A_COOLING_h8.csv; O_0p2_h8_TIGHT.csv','Dense CSV at 5-s intervals, 181 time points')
param('Shared A/O cooling','Open-corner time solver','BDF, maximum order 5, adaptive time stepping','—','Native solver setting','PARAMETERS_EN_CN.csv','Reference histories and tolerance checkpoints separately recorded')
param('Shared A/O cooling','Reference dense-solver tolerance',1e-5,'relative','Numerical solver setting','PARAMETERS_EN_CN.csv','Reference tight verification 1e-6; dense 300-s value differs from tight result by ~0.0052 K')
param('Shared A/O cooling','Reference strict verification tolerance',1e-6,'relative','Verification only','PARAMETERS_EN_CN.csv; A_COOLING_VERIFIED_BASE.csv','Not to be mixed into figure data from dense 1e-5 curve')
param('Shared A/O cooling','Open-corner dense-solver tolerance',1e-6,'relative','Numerical solver setting','PARAMETERS_EN_CN.csv','An independent check was performed at 1e-5')
param('Shared A/O cooling','Native spatial-field output times','0, 60, 300, 900','s','Native compact output','COMSOL_REPRODUCTION_EN_CN.md','Dense 181-point mean curves retained separately')
param('A/O mesh verification','Reference baseline tetrahedral elements',v['A']['tetrahedra'],'count','Numerically verified mesh','CORRECTED_QA.json','Bulk metrics mesh checked against finer mesh')
param('A/O mesh verification','Open-corner baseline tetrahedral elements',v['0p2']['tetrahedra'],'count','Numerically verified mesh','CORRECTED_QA.json','Bulk metrics mesh checked against finer mesh')
param('A/O mesh verification','Open-corner minimum mean-ratio quality','~0.000239','1','Reported mesh quality audit','RELEASE_AND_EXCLUSIONS_EN_CN.md','11 low-quality elements <0.001; ~2.09e-7 of volume; not proof of local stress-peak convergence')
param('A/O outputs','Reported stress','Volume mean von Mises stress','MPa','Computed FE solution','T02_CORRECTED_MECHANICAL.csv','Not maximum local stress or failure stress')
param('A/O outputs','Reported displacement','Maximum displacement magnitude','mm','Computed FE solution','T02_CORRECTED_MECHANICAL.csv','Support-region sensitivity remains important')
param('A/O outputs','Reported energy','Stored elastic strain energy in solid','mJ','Computed FE solution','T02_CORRECTED_MECHANICAL.csv','NOT dissipated impact energy')
param('Historical contact model','Native geometry family','H (distinct original-scale mask)','—','Model identity','Center_MESH3_SOLVED.mph; Orbital_MESH3_SOLVED.mph','Independent historical model, not same as normalized A/O')
param('Historical contact model','Rigid sphere size as reported','210','mm','Historical model documentation','METHODS_AND_INTERPRETATION_EN_CN.md','The historical methods call this a 210 mm sphere; do not assert radius/diameter without inspecting native geometry')
param('Historical contact model','Contact locations','Central; upper orbital','—','Prescribed model cases','D03_CONTACT_STABLE.csv','Equal imposed motion; unequal force')
param('Historical contact model','Prescribed sphere movement','1.5,2.0,2.5,3.0,3.5,4.0','mm','Released solved subset','D03_CONTACT_STABLE.csv','Original onset interval outside verified release')
param('Historical contact model','Regional sampling radius',150,'mm','Numerically defined ROI','METHODS_AND_INTERPRETATION_EN_CN.md','ROI intersection volume differs between central and orbital')
param('Historical contact model','Reaction / contact force','Per solved step in D03','N','Computed FE contact','D03_CONTACT_STABLE.csv','Not sensor-calibrated force')
param('Historical contact model','Regional stress','ROI mean','MPa','Computed FE solution','D03_CONTACT_STABLE.csv','Not full mask peak or tissue injury limit')
param('Historical contact model','Elastic energy','Stored (whole mask) and region-mean density','J; kJ/m3','Computed FE solution','D03_CONTACT_STABLE.csv','Energy storage not dissipation')
for missing in [
 ('Measured layer count and individual ply thickness','Unavailable in verified records','count/mm','Do not assume'),
 ('PLLA:epoxy constituent volume fractions','Unavailable in verified records','volume fraction','Do not assign mixture rule without evidence'),
 ('Anisotropic stiffness / fibre-matrix interface','Not measured / not assigned','—','Cannot claim experimentally calibrated fibre reinforcement'),
 ('Specimen-specific thickness/width of tensile coupons','Not verified in archived individual records','mm','Not used to calibrate current FE material'),
 ('Controlled geometry matched-only-corner comparison','Not carried out','—','A and O differ in multiple dimensions')]:
 param('Unverified experimental inputs: NOT in model',*missing,'Absent, do not invent','Thesis audit: THESIS_TENSILE_CLOSEOUT_EN_CN.md')
writecsv('TABLE_A_COMPLETE_MODEL_PARAMETERS.csv',['model_family','parameter','value','unit','evidence_status','source_file','interpretation_and_caveat'],PARAM)
# A/O accepted all mechanical cases with traceable native model names and response values.
native={'A':'A_STATIC_FINAL.mph','0p2':'O_STATIC_FINAL.mph'}
KEYS={'A':'Reference shell','0p2':'Open-corner shell'}
mechanical=[]
for key in ('A','0p2','A_fine','0p2_fine','alt','A_wide','0p2_wide','A_stiff','0p2_stiff'):
 item=v[key];nm=KEYS.get(key,('Reference shell' if key.startswith('A') else 'Open-corner shell'))
 role='baseline' if key in ('A','0p2') else ('mesh verification' if key.endswith('_fine') else 'support region test' if key.endswith('_wide') else 'support stiffness test' if key.endswith('_stiff') else 'alternate repair test')
 mechanical.append(dict(geometry=nm,internal_case_ID=key,study_role=role,
 mean_vonMises_stress_MPa=item['mean_vm_Pa']/1e6,max_displacement_mm=item['max_disp_m']*1000,
 stored_elastic_energy_mJ=item['energy_J']*1000,support_spring_energy_mJ=item['spring_energy_J']*1000,
 integrated_volume_cm3=item['volume_m3']*1e6,calculated_mass_g=item['volume_m3']*1400*1000,
 applied_force_N=item['force_N'],support_reaction_N=item['reaction_N'],
 effective_support_area_mm2=item['effective_support_area_m2']*1e6,
 tetrahedra=item['tetrahedra'],force_balance_error_pct=item['force_balance_percent'],
 work_balance_error_pct=item['energy_work_error_percent'],source='CORRECTED_QA.json; COORD_*.csv'))
writecsv('TABLE_B_MECHANICAL_ALL_ACCEPTED_CASES.csv',list(mechanical[0].keys()),mechanical)
# Exact dense plot data and strict tolerance separate from plotted A dense values
thermal=[];check=[]
for h in (4,8,16):
 for nm,n in [('Reference shell',f'A_COOLING_h{h}.csv'),('Open-corner shell',f'O_0p2_h{h}_TIGHT.csv')]:
  ary=readcsv(RAW/n)
  assert len(ary)==181,(n,len(ary))
  for o in ary:
   thermal.append(dict(geometry=nm,h_W_m2K=h,time_s=float(o['time_s']),mean_T_K=float(o['mean_T_K']),
    mean_temperature_C=float(o['mean_T_K'])-273.15,curve_file=n,
    data_status='Solved 5-s dense numerical output'))
  for t in (0,60,300,900):
   val=min(ary,key=lambda o:abs(float(o['time_s'])-t))
   check.append(dict(geometry=nm,h_W_m2K=h,time_s=t,mean_T_K=float(val['mean_T_K']),
    mean_temperature_C=float(val['mean_T_K'])-273.15,record_type='DENSE CURVE; plotted',source=n))
writecsv('TABLE_C_COOLING_FULL_181POINT_CURVES.csv',list(thermal[0].keys()),thermal)
tight=readcsv(RAW/'A_COOLING_VERIFIED_BASE.csv')
at=min(tight,key=lambda o:abs(float(o['time_s'])-300))
check.append(dict(geometry='Reference shell',h_W_m2K=8,time_s=300,
                  mean_T_K=float(at['mean_T_K']),mean_temperature_C=float(at['mean_T_K'])-273.15,
                  record_type='TIGHT 1e-6 VERIFICATION; not inserted into 1e-5 curve',source='A_COOLING_VERIFIED_BASE.csv'))
writecsv('TABLE_D_COOLING_MANUSCRIPT_CHECKPOINTS.csv',list(check[0].keys()),check)
# Contact source is complete 12 points, no new interpolated results
contact=[]
for r in readcsv(RAW/'D03_CONTACT_STABLE.csv'):
 contact.append(dict(region=r['case'],sphere_movement_mm=r['displacement_mm'],computed_contact_force_N=r['contact_force_N'],
   fixed_reaction_N=r['fixed_reaction_N'],reaction_imbalance_pct=r['force_imbalance_percent'],
   ROI_mean_stress_MPa=r['ROI_mean_stress_MPa'],ROI_mean_elastic_energy_density_kJ_m3=r['ROI_mean_energy_density_kJ_m3'],
   ROI_intersection_volume_cm3=float(r['ROI_volume_m3'])*1e6,whole_mask_stored_elastic_energy_J=r['whole_mask_stored_energy_J'],
   source='D03_CONTACT_STABLE.csv',released_window=r['release_status']))
assert len(contact)==12
writecsv('TABLE_E_HISTORICAL_SPHERE_CONTACT_12_SOLUTIONS.csv',list(contact[0].keys()),contact)
# Every sensitivity value used by the paper's visible graph in one table.
co=qa['comparisons']
sensitivity=[]
def sens(label,kind,metric,value,unit,internal,notes):
 sensitivity.append(dict(plot_panel=label,test_type=kind,metric=metric,displayed_value=value,unit=unit,
 source_case=internal,interpretation=notes))
for caption,key in [
 ('Time-step','O_0p2_h8_TOLERANCE.csv'),('Mesh','O_fine_h8_TIGHT.csv'),('Repair','O_alt_h8_TIGHT.csv')]:
 sens('S04a',caption,'max mean temperature difference',co[key]['max_mean_difference_K'],'K',key,'Open-corner; deterministic solver/mesh/repair comparison')
for caption,key in [
 ('Reference mesh','COORD_A_fine'),('Open-corner mesh','COORD_0p2_fine'),('Open-corner repair','COORD_repair')]:
 sens('S04b',caption,'ABS(mean stress %)',abs(co[key]['mean_vm_Pa_difference_percent']),'%',key,'Absolute numerical deviation; signed source in CORRECTED_QA')
for label,suffix,panel in [('Support-region sensitivity','wide','S04c'),('Support-stiffness sensitivity','stiff','S04d')]:
 for caption,key in [('Reference','COORD_A_'+suffix),('Open-corner','COORD_0p2_'+suffix)]:
  sens(panel,caption,'ABS(max displacement %)',abs(co[key]['max_disp_m_difference_percent']),'%',key,
       'Absolute numerical deviation; not experimental sample variability')
writecsv('TABLE_F_FIGURE_SENSITIVITY_VALUES.csv',list(sensitivity[0].keys()),sensitivity)
# Experimental tensile data and Table G are maintained exclusively in ../UTS.
# Plot-to-source index includes exact case names, and where figures reside.
figs=[
('M01','Historical contact, combined + M01_a-d','01_RECOMMENDED_FIGURES/M01_HISTORICAL_CONTACT.pdf','TABLE_E; D03_CONTACT_STABLE.csv','Central vs orbital at equal imposed sphere movement','Distinct historical model scale; no collision energy absorbed'),
('S01','Geometry representation','02_SUPPLEMENTAL_FIGURES/S01_GEOMETRY.png','A_ALIGNED_WIDTH150_M.stl; OPEN_MASK_SOURCE_UNMODIFIED.stl','Reference shell vs corrected open-corner shell','Not a matched-only-corners geometry pair'),
('S02','Cooling, combined + S02_a-d','02_SUPPLEMENTAL_FIGURES/S02_COOLING.pdf','TABLE_C; TABLE_D','h 8, 4, 16; 300s checkpoint shown from same dense curves','Strict A checkpoint tabulated separately, 0.0052K discrepancy disclosed'),
('S03','Mechanical, combined + S03_a-d','02_SUPPLEMENTAL_FIGURES/S03_MECHANICAL.pdf','TABLE_B; T02_CORRECTED_MECHANICAL.csv','Equal 2.70025832N, 2 geometries; stored elastic energy','Support selection/geometry confounded, no injury claims'),
('S04','Numerical sensitivity, combined + S04_a-d','02_SUPPLEMENTAL_FIGURES/S04_SENSITIVITY.pdf','TABLE_F; CORRECTED_QA.json; T03_VALIDATION_EN_CN.csv','Absolute deviations only','Do not treat deterministic sensitivity as statistical uncertainty'),
('CFI','Original thesis c/f/i corrections','01_RECOMMENDED_FIGURES/ORIGINAL_C_F_I_VERIFIED/C_F_I_VERIFIED_COMBINED.pdf','TABLE_I; D03_CONTACT_STABLE.csv','Regional mean values at 3/4mm and 1.5-4mm','NOT the unverified 30/40mm global peak results')
]
writecsv('TABLE_H_COMPLETE_FIGURE_SOURCE_INDEX.csv',['figure','kind','combined_figure','data_source','numerical_case','interpretation_limit'],
 [dict(zip(['figure','kind','combined_figure','data_source','numerical_case','interpretation_limit'],x)) for x in figs])
# Reader-facing visual tables. All exact values retained in source Excel-compatible CSV files.
def format_number(x):
 if isinstance(x,float):
  if abs(x)>10000 or 0<abs(x)<1e-4:return f'{x:.6g}'
  return f'{x:.6f}'.rstrip('0').rstrip('.')
 return str(x)
def htmltable(title,headers,rows):
 a=[f'<h2>{html.escape(title)}</h2><div class="tbl"><table><thead><tr>']
 a += ['<th>'+html.escape(t)+'</th>' for t in headers]
 a+=['</tr></thead><tbody>']
 for row in rows:
  a.append('<tr>')
  a.extend('<td>'+html.escape(format_number(v))+'</td>' for v in row)
  a.append('</tr>')
 a.append('</tbody></table></div>')
 return ''.join(a)
intro='''**Recommended designation:** Reference shell (the original A geometry) and open-corner shell (repaired O STL); not "closed-corner" because only corner openness was not controlled. The A/O internal file names remain unchanged for reproducibility.

**Status:** ASSUMED = prescribed numerical input, SOLVED = actual calculated model output, DOCUMENTED = specified in methods/native file, UNKNOWN = not measured/calibrated. No material claims should be reverse-engineered from these simulations.

**Experimental tensile tests:** See the separate UTS folder. No UTS results or calculations are presented as COMSOL model validation.

**Thermal record distinction:** A 300-s value from dense (relative tolerance 1e-5) was 300.626231875 K; strict 1e-6 300-s value was 300.631398640 K (difference ~0.00517 K). O h8 300-s value was 306.215044717 K. The S02 graphic uses the **same plotted dense curve** for panel d. No silent mixing of numerical versions.

**Materials:** Do not call the 3.5 GPa input an experimentally determined Young modulus for PLLA, DP420n or Medissa; it is a single isotropic assumed shell property.

**Historical sphere:** Original-scale central/orbital model uses a prescribed movement series and unequal contact forces; it is not force-matched with the 150-mm Reference/Open-corner screen.
'''
title='COMSOL model inputs, derived results and source data (journal handoff)'
blocks=['<!doctype html><html lang="en"><meta charset="utf-8"><title>'+title+'</title><style>body{font:14px/1.48 Arial,"Microsoft YaHei",sans-serif;max-width:1100px;margin:24px auto;padding:0 22px;color:#222}h1{font-size:25px;color:#16405d}h2{font-size:17px;margin-top:29px;border-bottom:1px solid #ccc;padding-bottom:6px}p{margin:8px 0}table{border-collapse:collapse;font-size:11px;width:100%;table-layout:auto}th,td{border:1px solid #d5d9dd;text-align:left;padding:7px;overflow-wrap:anywhere;vertical-align:top}th{background:#eef2f5}tr:nth-child(even){background:#fafafa}.tbl{overflow:auto}em{color:#444}@media print{body{font-size:10pt;max-width:none}table{font-size:8pt}h2{break-after:avoid}tr{break-inside:avoid}}</style><body><h1>'+title+'</h1>']
for para in intro.split('\n\n'):
 para=para.strip()
 if para:blocks.append('<p>'+html.escape(para).replace('**','')+'</p>')
fields=['Model','Parameter','Value','Unit','Evidence classification','Exact source','Scientific limit']
blocks.append(htmltable('Table A. Full recorded/assumed/derived model parameters',fields,
 [(r['model_family'],r['parameter'],r['value'],r['unit'],r['evidence_status'],r['source_file'],r['interpretation_and_caveat']) for r in PARAM]))
blocks.append(htmltable('Table B. Mechanical results and sensitivity',[
 'Configuration','Model check','Mean von Mises (MPa)','Maximum deflection (mm)','Stored strain energy (mJ)',
 'Volume (cm3)','Load (N)','Reaction (N)','Support area (mm2)','Tet. elements'],
 [(r['geometry'],r['study_role'],r['mean_vonMises_stress_MPa'],r['max_displacement_mm'],
   r['stored_elastic_energy_mJ'],r['integrated_volume_cm3'],r['applied_force_N'],r['support_reaction_N'],
   r['effective_support_area_mm2'],r['tetrahedra']) for r in mechanical]))
blocks.append(htmltable('Table C. Cooling checkpoint data (strict A verification separated)',[
 'Shell','h (W/m2K)','Time (s)','Mean K','Mean °C','Case','Source CSV'],
 [(r['geometry'],r['h_W_m2K'],r['time_s'],r['mean_T_K'],r['mean_temperature_C'],r['record_type'],r['source']) for r in check]))
blocks.append(htmltable('Table D. Historical sphere-contact simulation (released 12 records)',[
 'Position','Motion (mm)','Force (N)','ROI stress (MPa)','ROI mean energy density (kJ/m3)','Whole stored energy (J)','Force imbalance (%)'],
 [(r['region'],r['sphere_movement_mm'],r['computed_contact_force_N'],r['ROI_mean_stress_MPa'],
 r['ROI_mean_elastic_energy_density_kJ_m3'],r['whole_mask_stored_elastic_energy_J'],
 r['reaction_imbalance_pct']) for r in contact]))
blocks.append(htmltable('Table E. Figure S04 verified sensitivity values',[
 'Panel','Sensitivity','Metric','Absolute change','Unit','QA case'],
 [(r['plot_panel'],r['test_type'],r['metric'],r['displayed_value'],r['unit'],r['source_case']) for r in sensitivity]))
blocks.append(htmltable('Figure and graph data source index',[
 'Figure','Role','Figure path','Data file(s)','Scenario','Interpretation limits'],
 figs))
blocks.append('<p><b>Reproduction:</b> Original dense thermal curves and COMSOL solved models are delivered as CSV and native .mph in COMSOL. See TABLE_A through TABLE_F, TABLE_H and TABLE_I for Excel-ready exact values; experimental UTS material is in ../UTS.</p>')
blocks.append('</body></html>')
hfile=READ/'COMSOL_PARAMETERS_AND_RESULTS_EN_CN.html'
hfile.write_text('\n'.join(blocks),encoding='utf8')
# Word-readable RTF quick parameter/summary memo, exact csv index is the authoritative tabular record.
s=['{\\rtf1\\ansi\\deff0{\\fonttbl{\\f0 Arial;}{\\f1 Microsoft YaHei;}}\\uc1\\f0\\fs22']
def rtxt(x):
 ans=''
 for c in str(x):
  k=ord(c)
  if c in '\\{}':ans+='\\'+c
  elif k>127:ans+=f'\\u{k if k<32768 else k-65536}?'
  else:ans+=c
 return ans
for title,data in [
 ('Model parameters',[(r['model_family']+' | '+r['parameter'],r['value']+' '+r['unit']+' | '+r['evidence_status']) for r in PARAM]),
 ('Baseline mechanical values',[(r['geometry']+' '+r['study_role'],f"{r['mean_vonMises_stress_MPa']:.7g} MPa | {r['max_displacement_mm']:.7g} mm | {r['stored_elastic_energy_mJ']:.7g} mJ") for r in mechanical if r['study_role']=='baseline']),
 ('Thermal 300s checkpoints',[(r['geometry']+' h='+str(r['h_W_m2K'])+' '+r['record_type'],str(r['mean_T_K'])+' K') for r in check if r['time_s']==300]),
 ('Historical contact',[(r['region']+' '+r['sphere_movement_mm']+' mm',r['computed_contact_force_N']+' N; '+r['ROI_mean_stress_MPa']+' MPa') for r in contact])
 ]:
 s.append('\\par\\b '+rtxt(title)+'\\b0\\par ')
 for l,v2 in data:s.append(rtxt(l)+' : '+rtxt(v2)+'\\par\n')
s.append('}')
(READ/'COMSOL_PARAMETERS_AND_RESULTS_EN_CN.rtf').write_text(''.join(s),encoding='utf8')
print('PASS_COMSOL_TABLES',len(PARAM),'parameters',len(mechanical),'mechanical runs',
len(thermal),'dense thermal rows',len(check),'checkpoints',
len(contact),'contact states',len(sensitivity),'validation bar points')
print('PASS_COMSOL_CSV_TABLES_AND_HTML_WORD_READABLE')
