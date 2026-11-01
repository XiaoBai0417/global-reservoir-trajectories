# Supplementary source methods

These four files were copied from the Reservoirwatch source folder supplied by the authors:

- MNDWI.js: example Sentinel-2 MNDWI water mask in Google Earth Engine.
- SDWI.js: example Sentinel-1 SDWI water mask in Google Earth Engine.
- contour_detection.py: contour/point demonstration using synthetic shapes.
- get_pois.py: POI retrieval and coordinate-conversion example using the AMap API.

These files are included as supplementary source material. They are not imported by the five global case-figure scripts, and their outputs are not used to calculate the bundled 100-case sample.

MNDWI.js and SDWI.js refer to a specific Earth Engine reservoir asset; replace that asset with one you can access before running them. get_pois.py contains a placeholder API-key string and requires the user to supply a valid AMap key. The sample figure requirements do not install the optional dependencies for these scripts; see requirements-source-methods.txt.

The supplied source folder contained no LICENSE or COPYING file. No licence is asserted here for these four files; confirm redistribution rights and preserve any upstream notices before public GitHub release.
