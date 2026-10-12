# Replotting and reproduction / 重绘与复算
All paths below are relative to the extracted COMSOL_FINAL_CORRECTED_20261006 folder. Extract every native archive into the same parent directory.
所有压缩包解压到同一父目录；相对路径以本包根目录为准。

1. Open START_HERE.html. CSVs in 04_TABLES_AND_RAW_DATA are the exact graph data. Edit vector SVGs or regenerate using Node.js: node 09_EDITABLE_SOURCES/build_corrected_figures.cjs . Compile RasterCharts.java with a compatible JDK and run its class with the package root as argument to regenerate PNG/TIFF. The .draw files are the raster drawing instructions.
2. In COMSOL 6.3 open A_STATIC_FINAL.mph, O_STATIC_FINAL.mph, A_COOLING_FINAL.mph or O_COOLING_FINAL.mph from 08_NATIVE_MODELS. These files contain solutions and configured plot groups. Change plots without rerunning the solver. O native cooling archives save 0,60,300,900 s; the full 181-point curve CSVs remain in 04. Compact output equivalence is checked in T03. The compact native files do not contain all 181 full spatial fields.
3. To recalculate released models in an isolated output directory, compile RecomputeReleased.java with comsolcompile and invoke COMSOL batch with -inputfile RecomputeReleased.class -appargs <absolute package root> <new output folder>. The script loads the delivered solved models, runs the solver attached to the plotted dataset and writes new copies only. Material, loads, support variables, meshing and solvers are editable in those native files. Recalculation requires a licensed COMSOL 6.3 installation.
4. Other Java/Python audit scripts retain the original execution paths as provenance; they are not a portable one-click pipeline. Configure their paths before use. Blender repair scripts preserve the original STL and write derived geometry. Geometry inputs and repair-deviation records are supplied.
5. Historical Center/Orbital models are a separate scale and study family. Do not substitute their geometry, loads or ROIs into the A/O comparison. Baseline A cooling is the audited pre-existing model; its dense CSVs and tight checkpoint model are explicitly distinguished.

原生模型已含解，可直接调整视角和色标。O精简热模型仅保存四个空间场检查点；181点曲线CSV完整保留。需要复算时写入新文件夹，不覆盖原研究文件。其余历史脚本保留当时路径，先配置再使用。

The portable recomputation helper was compiled against COMSOL 6.3; it was not used to rerun every already-verified released solution. The executed numerical scripts and logs are preserved separately.
复算助手已通过COMSOL 6.3编译；未为测试助手而重复求解全部已验证模型。实际执行的数值脚本与日志另有保留。
