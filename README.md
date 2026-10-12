# PLLA-Epoxy Facial Mask - COMSOL Numerical Data

This repository contains exported numerical data, validation tables, publication figures, and data-to-figure Python scripts for the COMSOL component of the PLLA-epoxy facial-mask manuscript.

PUBLIC DATA-ONLY RELEASE: Native COMSOL MPH files and geometry STL files are intentionally not included. This repository is meant to expose the numerical results, validation, figures, and reproducible post-processing without publishing the large native model files. Model fingerprints are retained for provenance, and native models can be supplied privately if required for peer review or editorial verification.

COMSOL version for the accepted native models: COMSOL Multiphysics 6.3.

## Study family 1 - Historical quasi-static sphere contact

A separate original-scale facial-shell model was evaluated under central and upper-orbital rigid-sphere displacement control.

Accepted released interval:
- prescribed sphere movement: 1.5 to 4.0 mm
- six solved states per loading location
- equal movement does not imply equal contact force
- corrected manuscript comparisons use regional mask-domain volume means and recoverable elastic strain energy

Primary data:
- 04_TABLES_AND_PROVENANCE/COMSOL_RAW_AND_VALIDATION/D03_CONTACT_STABLE.csv
- 04_TABLES_AND_PROVENANCE/MANUSCRIPT_READY_TABLES/TABLE_E_HISTORICAL_SPHERE_CONTACT_12_SOLUTIONS.csv
- 04_TABLES_AND_PROVENANCE/MANUSCRIPT_READY_TABLES/TABLE_I_ORIGINAL_C_F_I_VERIFIED_PLOT_DATA.csv

Primary figures:
- 01_RECOMMENDED_FIGURES/M01_HISTORICAL_CONTACT
- 01_RECOMMENDED_FIGURES/ORIGINAL_C_F_I_VERIFIED
- selected existing 4 mm native field exports in 02_SUPPLEMENTAL_FIGURES/CONTOURS_SELECTED_FROM_DESKTOP

The corrected original-style manuscript panels c, f and i use accepted regional-mean solution data. They do not reuse the older unresolved 30/40-mm all-domain peak-stress workbook values.

## Study family 2 - Reference-shell / open-corner-shell screening

Two complete 150-mm nominal-width shell geometries were evaluated as numerical screening cases.

Presentation names:
- Reference shell - internal historical code A
- Open-corner shell - internal historical code O

These are not a controlled one-variable comparison of corner openings. The geometries differ in volume, coverage, thickness distribution, and effective support region.

Accepted analyses include:
- prescribed-convection cooling
- equal-resultant linear-elastic mechanical screening
- mesh, geometry-repair, solver, support-region, and support-stiffness sensitivity checks

Primary tables:
- TABLE_A_COMPLETE_MODEL_PARAMETERS.csv
- TABLE_B_MECHANICAL_ALL_ACCEPTED_CASES.csv
- TABLE_C_COOLING_FULL_181POINT_CURVES.csv
- TABLE_D_COOLING_MANUSCRIPT_CHECKPOINTS.csv
- TABLE_F_FIGURE_SENSITIVITY_VALUES.csv

Primary figures:
- S01_GEOMETRY
- S02_COOLING
- S03_MECHANICAL
- S04_SENSITIVITY

## Main assumed effective material properties

The screening models use a single homogeneous isotropic effective solid, not a resolved fibre/resin laminate.

Young modulus: 3.5 GPa
Poisson ratio: 0.38
Density: 1400 kg/m3
Thermal conductivity: 0.25 W/(m K)
Specific heat capacity: 1000 J/(kg K)

These values were not calibrated from the archived UTS coupon tests and should not be described as direct measurements of the electrospun PLLA-epoxy composite.

## Repository structure

00_READ_FIRST - methods, interpretation limits, caption and figure indexes
01_RECOMMENDED_FIGURES - historical-contact publication candidates
02_SUPPLEMENTAL_FIGURES - geometry, cooling, mechanics, sensitivity, selected native contours
03_BACKUP_AND_INDEPENDENT - optional field views
04_TABLES_AND_PROVENANCE/COMSOL_RAW_AND_VALIDATION - exported numerical values and QA
04_TABLES_AND_PROVENANCE/MANUSCRIPT_READY_TABLES - consolidated author-facing tables
05_ADDITIONAL_FIGURES_AND_ARCHIVAL_DATA - later ball/mask setup figures, impact overviews, and clearly marked review-only historical thermomechanical endpoint material
06_REPRODUCIBLE_SOURCES - Python scripts for rebuilding exported-data figures and tables
NATIVE_MODELS_NOT_PUBLIC.md - native-model distribution policy and model-family list
MANIFEST_SHA256.csv - integrity hashes

## Important interpretation limits

- Sphere-contact studies are quasi-static displacement-controlled simulations, not dynamic impact experiments.
- Stored elastic strain energy is not dissipated impact energy.
- Local contact/support stress extrema may be mesh sensitive; corrected contact comparisons use regional or volume-mean values.
- The historical contact model is a different scale/model family from the normalized reference/open-corner study.
- The reference/open-corner calculations cannot isolate the effect of corner openings alone.
- Cooling studies solve homogeneous solid conduction with prescribed external convection; they do not resolve airflow, skin contact, or human thermal comfort.
- Older thesis thermomechanical histories with questionable heat capacity and starting-temperature behavior are not part of the accepted thermal conclusions. A small subset is retained only under `05_ADDITIONAL_FIGURES_AND_ARCHIVAL_DATA/THERMOMECHANICAL_REVIEW_ONLY` because it was shared as later archival visual material; its README and audit tables explicitly restrict interpretation.
- Experimental UTS data are maintained separately and are not included here.

## Reproduction from exported data

The Python scripts in 06_REPRODUCIBLE_SOURCES rebuild accepted graphs and tables using included CSV and JSON values. They do not recreate finite-element solutions.

Native finite-element reproduction requires the original COMSOL model files, which are intentionally not distributed through this public data repository.

## Status

This repository is intended for manuscript collaboration and numerical-data traceability. It preserves accepted exported results without silently replacing unresolved experimental or model assumptions.
