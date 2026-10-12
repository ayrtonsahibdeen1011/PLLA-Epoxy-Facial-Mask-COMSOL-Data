# COMSOL native contact contours — vetted existing exports
# COMSOL原生接触云图 — 经过来源核实的旧文件

**These are exact unchanged files from the 5 October Desktop archive, not regenerated images.** Binary image checksums match their source originals. The two associated native COMSOL meshes and solved model hashes match the accepted Center_MESH3_SOLVED.mph and Orbital_MESH3_SOLVED.mph in our final package. The archived exporter explicitly used dset1, mask solid domain 1, solnum 9 at 4 mm prescribed sphere displacement, native Rainbow color scale, same orthographic view and white background.

**Preferred supplement:** Pair center and orbital von Mises stress (CONTACT_4mm_Center_VonMises and CONTACT_4mm_Orbital_VonMises), followed by their paired elastic strain energy-density fields. **Optional** is the pair of displacement fields. PDF, PNG and high-resolution TIFF copies are supplied for each. No new composite montage or simulations were created.

Fixed scales for BOTH loading sites:
- solid.disp: displacement magnitude, 0 to 5 mm, linear
- solid.mises: von Mises stress, 0.001 to 80 MPa, logarithmic
- solid.Ws: stored elastic energy density, 0.00001 to 2.5 MJ/m3, logarithmic

**Scientific limits:** These are illustrative native local fields, not the regional volume means shown in M01 and corrected C/F/I. The 4 mm imposed movement gives unequal central and orbital reaction forces. Local maxima at constraint/contact hot spots are mesh-sensitive and may saturate the fixed color scale: do not infer converged failure stress, actual protection, clinical performance or dissipated impact energy. The original-scale COMSOL shell geometry (approximately 43 cm width) and homogeneous assumed E=3.5 GPa were not experimentally calibrated to the approximately 15 cm fabricated mask or individual UTS coupons. These historical sphere-contact images are SEPARATE from the normalized Reference shell/Open-corner shell mechanical and cooling screening. Do not mix their results.

**Suggested manuscript caption:** Spatial displacement magnitude (mm), von Mises stress (MPa) and recoverable elastic strain-energy density (MJ/m3) in the historical idealized facial-shell model at 4 mm prescribed rigid sphere displacement. Each response is shown separately for central and upper-orbital quasi-static loading using the same variable-dependent color limits and camera orientation. The location-dependent reaction forces are unequal, and local mesh-sensitive peaks are not used to assess fracture or in-vivo injury protection.

**中文说明：** 从10月5日已核查COMSOL导出文件中原样复制中心与眶部4毫米接触工况的三类云图（位移、等效应力、弹性能密度），不重新计算、不改色标。两组色标相同。位移控制不等于等力试验；约束边缘处局部峰值对网格敏感，不可代表真实断裂强度、受伤风险或冲击能量耗散。此历史尺度球压模型与另一个参考/开角壳体150毫米仿真不是同一研究场景。

**Desktop archive screening:** Earlier comparative mechanical/thermal A-B exports used a different B volume (~11.47 cm3) versus the accepted O model (~86.92 cm3), so they are excluded. Old 24-hour thermomechanical contour packages use questionable Cp and thermal histories and are excluded. Accepted existing Reference/Open-corner shell field maps remain in COMSOL/03_BACKUP_AND_INDEPENDENT/COMSOL_FIELD_VIEWS, unchanged.

The exact source filenames and SHA256 checksums, model hashes, expression, solver and 4mm color scales appear in SELECTED_CONTOURS_PROVENANCE_AND_SCALES.csv.
