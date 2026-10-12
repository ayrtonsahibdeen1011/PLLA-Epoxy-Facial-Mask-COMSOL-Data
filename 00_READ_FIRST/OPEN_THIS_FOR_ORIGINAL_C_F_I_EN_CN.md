# Original thesis panels C, F and I — corrected numerical replacements
# 原论文 C/F/I 推荐替代图

**If the collaborator only asks for C, F and I, use this directory.** Its combined graph and 3 independent panels are ready in PDF, editable SVG, PNG and 600-dpi TIFF.

Files:
- C_F_I_VERIFIED_COMBINED.pdf/svg/png/tiff — the 3-panel combined comparison.
- C_REGIONAL_STRESS_3_AND_4_MM.* — corrected panel (c), regional mean stress at 3 and 4 mm.
- F_REGIONAL_STRESS_1P5_TO_4_MM.* — corrected panel (f), solved 1.5–4 mm regional mean stress.
- I_REGIONAL_MEAN_RATIOS_AT_4_MM.* — corrected panel (i), normalized orbital/center mean stress and mean elastic energy density at 4 mm.

**Exact underlying numerical data:** 04_TABLES_AND_PROVENANCE/COMSOL_RAW_AND_VALIDATION/D03_CONTACT_STABLE.csv. Source solved COMSOL 6.3 models: 07_COMSOL_EDITABLE_NATIVE_MODELS/Center_MESH3_SOLVED.mph and Orbital_MESH3_SOLVED.mph in the full backup. TABLE_I_ORIGINAL_C_F_I_VERIFIED_PLOT_DATA.csv in MANUSCRIPT_READY_TABLES records all exact plotted values, case name, units, and transformations. TABLE_E provides the full source contact state. Each source was checked against released mesh-3 data. Source SHA256 is given beside the figures.

**Crucial scientific change:** The old thesis panel (c) used unverified 30/40 mm center/global peak values. The corrected 3/4 mm graph is NOT the same experiment relabeled. The original (f) and (i) were based on unvalidated all-domain maxima; the new figures use consistent 0.150 m ROI volume means from the repaired stationary-contact model. Use the new captions and change the surrounding manuscript descriptions accordingly. Same prescribed displacement does NOT mean same contact force. No claim about dissipated impact energy or injury protection is justified.

中文提示：如果只需要原论文的(c)、(f)、(i)三图，使用本文件夹的整图或拆图。图(c)改为经确认的3、4 mm，不能再写旧图的30、40 mm。图(f)是1.5到4 mm的六个计算结果，图(i)是4 mm的区域平均应力和平均弹性能密度归一化值。数据来自 D03_CONTACT_STABLE.csv；不是旧版全域应力最大值，也不代表实际吸收冲击能量。
