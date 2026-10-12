# Figure captions and use guide
# 图注及使用指南
## M01 Historical sphere contact
Idealized quasi-static central and orbital contact in the repaired historical-scale model. Panels show contact force, regional mean von Mises stress, regional mean elastic energy density and whole-mask stored elastic energy as functions of prescribed sphere movement over the verified 1.5–4 mm subset. Lines connect computed points. Comparisons are at equal movement, not equal contact force. This geometry is not the normalized A/O comparison. The results do not establish impact energy absorption or injury thresholds.
历史尺度模型中，中心及眶部准静态接触的合力、区域平均应力、区域平均弹性能密度及整体弹性储能。仅显示已验证位移段，线段连接计算点。该图不是150 mm A/O方案对照，也不代表冲击耗能或伤害阈值。
## S01 Geometry identity
Orthographic projections of the existing curved configuration A and the corrected open-corner configuration O at common nominal width. The scale bars represent 50 mm. Equal width does not imply matched thickness, volume, coverage or fixture area. O is derived from Untitled面具完成.stl; the prior flat 3MF is excluded from this identity.
相同名义宽度下A与O的正投影，标尺50 mm。宽度相同不代表厚度、体积、覆盖或支承面积相同。O来源于本次确认的STL。
## S02 Cooling comparison
Free cooling with shared conductivity, density, heat capacity, initial temperature and ambient temperature. The baseline coefficient is 8 W/(m2 K); boundary sensitivity uses 4 and 16 W/(m2 K). A dense curves use 1e-5 tolerance with independent 1e-6 verification; O dense curves use 1e-6. The tabulated A 300 s verification value differs from its dense-curve value by approximately 0.0052 K. Temperature differences compare complete configurations, not the isolated effect of openings or solved ventilation.
相同热学假设下的自由冷却及对流边界敏感性。A的密集曲线与严格检查点容差不同，差异已核查。不能把温度差解释为单独开口效应或流动通风结果。
## S03 Stationary mechanical comparison
Volume-mean von Mises stress, maximum displacement, stored elastic energy and integrated solid volume for A and O under a common normalized Gaussian resultant and coordinate-defined elastic supports. Stored energy is recoverable elastic energy. It is not dissipated impact energy. Local stress peaks and failure strength are not compared.
同等高斯合力和坐标定义弹性支承下的体积平均应力、最大位移、弹性储能及实体体积。储能不是冲击耗散能，未比较局部峰值或失效强度。
## S04 Numerical sensitivity
Changes in accepted bulk responses when the volume mesh, O surface repair, support stiffness or support-region threshold is changed. These are deterministic sensitivity calculations, not experimental replicates or statistical uncertainty bars. The earlier face-centroid support method is diagnostic only and is not used in S03.
网格、O表面修复、支承刚度及范围变化的确定性敏感性检查，不是实验重复或统计误差条。旧整面选支承结果只作诊断，不用于S03。
## Optional field views
Every FINAL_FIELD file is an undeformed-geometry COMSOL view from the stated solved model, with a fixed range shared by A and O for the same quantity. Units are on the legend. Mechanical views use the baseline coordinate-defined supports. Thermal views are at 300 s. Geometry size is documented in S01. Color clipping, when present, must not be interpreted as a bound on the true local maximum. Use the native model to change view, range or expression without solving again.
备选云图均来自标明的已求解模型。同一变量在A和O间采用相同色标范围，单位见图例。图像未放大变形；热图时间为300秒。色标截断不是实际极值界限，可在原生模型中改视角或色标，无需重新求解。