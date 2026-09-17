## [1.2] Delphinus - 2026-09-18

### Added

- Added Reset to Default support for theme configuration.
- Added automatic detection when the current configuration differs from the default configuration.
- Added default configuration support for colors, scale, and geometry.
- Added a descriptive note below the Reset to Default button.

### Changed

- Moved the Reset to Default section to the bottom of the scrollable Customize content.
- Apply now becomes active when valid configuration changes are detected.
- Reset to Default now becomes active when the current configuration differs from the default configuration.
- Reset restores colors, scale, and geometry from the theme's default configuration.
- Geometry restoration includes alignment, `gap_x`, `gap_y`, minimum dimensions, and maximum dimensions.
- Scale calculation now uses 1366px width as the 1.00 baseline.
- Corrected scaling so 1920px corresponds to a scale of 1.40.

### Fixed

- Fixed the Reset section not being properly included in the Customize dialog scroll area.
- Fixed the Apply button not reflecting pending configuration changes.
- Fixed the Reset button not reflecting differences between the current configuration and `default.json`.
- Fixed incorrect scale calculations for different display resolutions.

### Build

- Build: `20260918`
