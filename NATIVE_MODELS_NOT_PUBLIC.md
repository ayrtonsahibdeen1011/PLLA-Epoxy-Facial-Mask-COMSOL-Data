# Native COMSOL models are not part of this public release

This repository is intentionally a **data/results release**. Native COMSOL `.mph` files and geometry-source `.stl` files are not published here.

The accepted native model families are:

## Historical sphere-contact
- `Center_MESH3_SOLVED.mph`
- `Orbital_MESH3_SOLVED.mph`

## Reference shell / Open-corner shell
- `A_STATIC_FINAL.mph` — Reference-shell static screening
- `O_STATIC_FINAL.mph` — Open-corner static screening
- `A_COOLING_FINAL.mph` — Reference-shell cooling
- `O_COOLING_FINAL.mph` — Open-corner cooling

Internal code `A` corresponds to **Reference shell** and internal code `O` to **Open-corner shell**.

Model SHA-256 fingerprints are retained in the repository's provenance/index files so the exact native files can be identified later. Native models may be supplied privately to editors or reviewers if needed.

The old thesis thermomechanical models with unresolved heat-capacity and saved-initial-temperature issues are not part of the accepted native-model set.
