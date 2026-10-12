# COMSOL — Numerical figures, model definitions and data
# COMSOL — 数值模拟：全部图表、参数、数据和原生模型

This folder contains COMSOL studies only. UTS experimental traces are in the separate UTS folder.


## Best existing COMSOL contours (no new calculations)
**Supplementary field views at 4 mm, from the accepted original-scale historical sphere-contact models:** 02_SUPPLEMENTAL_FIGURES/CONTOURS_SELECTED_FROM_DESKTOP. Open OPEN_CONTOURS.html in that folder. Six existing native COMSOL fields (paired central/orbital displacement, von Mises stress and stored elastic energy density) are offered as intact PDF/PNG/TIFF archive exports with fixed, consistent scales and bilingual captions. They are NOT A/O geometry comparison contours. Source checksums, native model SHA256, dset1/solnum9, units and scale limits are supplied in SELECTED_CONTOURS_PROVENANCE_AND_SCALES.csv. Prefer stress and energy-density pairs; displacement pair is an optional backup. See the folder's READ_FIRST_SELECTED_CONTOURS_EN_CN.md for all scientific limitations.
**中文：** 已从以前保存的ZIP原图核对并精选4mm准静态球压模型的中央/眶部位移、等效应力、弹性能密度云图，全部原样复制，无重新计算或修图。不是新A/O结构对照研究；尺度、源模型及物性局限见文件夹说明。

## Recommended and supplementary graphs
- 01_RECOMMENDED_FIGURES/ORIGINAL_C_F_I_VERIFIED — The original requested (c), (f), (i) graph formats, recreated from verified mesh-3 regional contact data. Includes combined and three separate PDF, SVG, PNG, TIFF figures, exact source CSV references, bilingual explanation and model names.
- 01_RECOMMENDED_FIGURES/M01_HISTORICAL_CONTACT — Historical center/orbital stationary sphere contact, with (a-d) split panels under INDIVIDUAL_PANELS.
- 02_SUPPLEMENTAL_FIGURES — S01 geometry, S02 prescribed-convection cooling, S03 static mechanical screening, S04 numerical sensitivity. S02–S04 have their own individual a–d panels.
- 03_BACKUP_AND_INDEPENDENT/COMSOL_FIELD_VIEWS — Six illustrative field maps and scale/variable source index.

## Where parameters and every computed number live
- 00_READ_FIRST/COMSOL_PARAMETERS_AND_RESULTS_EN_CN.html and its RTF version: the full readable model parameter/result appendix.
- 04_TABLES_AND_PROVENANCE/MANUSCRIPT_READY_TABLES — Tables A–F, H and I (55 setup/material entries; 9 mechanical cases; 1,086 cooling rows; 25 checkpoints; 12 contact solutions; 10 sensitivity values; source indexes).
- 04_TABLES_AND_PROVENANCE/COMSOL_RAW_AND_VALIDATION — Original solved response CSVs and numerical verification JSON; D03_CONTACT_STABLE.csv is the actual corrected (c)/(f)/(i) source.
- 07_COMSOL_EDITABLE_NATIVE_MODELS — Six solved COMSOL 6.3 models in FULL ZIP, geometry STLs in both copies.
- 06_REPRODUCIBLE_SOURCES — Executable graph/table scripts. COMSOL_FIGURE_BUILDER stores older historical source scripts and should not overwrite the improved charts.

## Scientific distinctions
- Original figures (c)/(f)/(i) had unreliable 30/40 mm data and old global maxima. New panel (c) is regional mean stress at 3 and 4 mm; (f) shows six solved points from 1.5 to 4 mm; (i) shows center-normalized regional mean stress and energy density at 4 mm. New captions must replace old claims.
- The reference shell (internal A) and open-corner shell (internal O) have different entire geometries, thickness/volume/support; they are not a matched one-variable closed/open comparison.
- The A/O solid is one **assumed effective isotropic material**: E 3.5 GPa, Poisson ratio 0.38, density 1400 kg/m3, thermal conductivity 0.25 W/(m K), heat capacity 1000 J/(kg K). It is not an explicitly layered or experimentally calibrated electrospun PLLA–epoxy composite.
- Mechanical screens apply 2.70025832 N under idealized boundary supports; cooling assumes 45°C initial, 20°C ambient, external h=4/8/16 W/(m2 K), no airflow or skin physiology; historical sphere contact uses equal imposed movement, not equal force.
- Stored elastic energy is not dissipated collision energy. Old questionable thesis thermomechanical histories are excluded. The baseline reference dense cooling curve differs from a separate strict 300s checkpoint by ~0.00517 K, disclosed in Table D.

## 中文说明
此文件夹仅包含 **COMSOL 数值模拟**，有推荐整图、全部拆分子图、区域图、原始求解CSV、参数表、网格及边界检查、源代码和六个原生模型（大包）。最初的 (c)(f)(i) 图已按可靠的 Mesh-3 求解数据重绘；旧 30/40 mm 和全域最大值不应再按原说明用于期刊。参考壳体与开角壳体并非只改变角部开口的严格匹配试样。等效材料参数是模型假设，并未根据实验拉伸试样标定。实验 UTS 请打开另一个 UTS 文件夹。
