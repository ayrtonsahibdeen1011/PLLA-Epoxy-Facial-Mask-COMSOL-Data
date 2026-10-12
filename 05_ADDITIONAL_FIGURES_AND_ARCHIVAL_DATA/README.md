# Additional figures and archival endpoint data

This folder preserves the **additional visual package shared after the main COMSOL handoff**. The image files were recovered from the original October 5 journal-review archive and copied without redrawing or regenerating the COMSOL figures.

## Recommended additional impact visuals

### IMPACT_SETUP
- `01_CENTER_BALL_MASK_0MM` — full sphere + mask assembly for central loading at 0 mm.
- `02_ORBITAL_BALL_MASK_0MM` — full sphere + mask assembly for upper-orbital loading at 0 mm.

These are the clearest geometry/context images for showing where the spherical loading is applied. They are setup views, not 4 mm stress maps.

### IMPACT_OVERVIEW
- `03_NINE_PANEL_CONTACT_OVERVIEW` — archived multi-panel contact overview.
- `04_CENTER_EXTENDED_FIELDS` — central 0/4 mm volumetric-strain, principal-stress and stored-energy fields.
- `05_ORBITAL_EXTENDED_FIELDS` — upper-orbital matching fields.

The nine-panel overview is an **alternative visual layout**, not a replacement for the corrected manuscript C/F/I figures in `01_RECOMMENDED_FIGURES/ORIGINAL_C_F_I_VERIFIED`. In particular, its panel (c) is a contact-reaction curve, whereas the corrected original-style manuscript panel (c) uses regional mean-stress data.

The accepted contact calculations are stationary, displacement-controlled sphere-to-mask simulations. Equal 4 mm movement does not imply equal force. Use the accepted data in `SOURCE_DATA/ACCEPTED_CONTACT_D03_STABLE.csv` and the main manuscript-ready contact tables for quantitative statements.

## Thermomechanical review-only material

The two files in `THERMOMECHANICAL_REVIEW_ONLY` are retained because they were part of the later supplemental package, **not because they establish a validated time-dependent thermal result**.

- `06_24H_ENDPOINT_OVERVIEW` — archived prescribed-temperature endpoint overview.
- `07_EPOXY_ENERGY_DENSITY_ENDPOINT` — archived E2/E3/E4 stored elastic-energy-density comparison.

These older cases are homogeneous single-material numerical templates. They used a prescribed 336.15 K boundary, a 293.15 K structural reference, and saved specific-heat inputs of approximately 1.0 J/(kg K) for the epoxy-labelled cases and 1.5 J/(kg K) for PLLA. The saved earliest temperatures do not match the old workbook's claimed 293.15 K starting state. Moisture diffusion was not solved.

Therefore these figures **must not be presented as**:
- a validated 0–24 h heating history;
- a calibrated wearer thermal-comfort result;
- a resolved electrospun PLLA–epoxy laminate simulation;
- evidence that conductivity or material choice caused a measured transient cooling benefit.

The accepted thermal study for the current paper is the separate Reference/Open-corner prescribed-convection screening in the main repository (`S02_COOLING`, Tables C/D and the associated validation files).

## Included source data

- `ACCEPTED_CONTACT_D03_STABLE.csv` — duplicate of the accepted contact source table for this folder to remain self-contained.
- `THERMAL_ASSUMED_PARAMETERS.csv` — parameters of the archived endpoint cases.
- `THERMAL_ENDPOINT_RESULTS.csv` — four checked endpoint outputs.
- `THERMAL_START_TEMPERATURE_AUDIT.csv` — documents the unreconciled initial-temperature problem.
- `SANITIZED_NATIVE_MODEL_HASH_INDEX.csv` — model fingerprints only; local computer paths have been removed.

## Native models

Native COMSOL `.mph` files are **not distributed in this public data repository**. Model fingerprints are retained for provenance, and native files can be supplied privately if required for peer review or editorial verification.
