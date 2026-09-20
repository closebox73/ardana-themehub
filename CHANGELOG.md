## [1.5] Delphinus - 2026-09-19

### Added

- Added automatic UpdateCard asset refresh after a successful update.
- Added automatic refresh of the Ardana application icon cache after an update.
- Added **Stop All** button to the Dashboard for stopping all currently running Ardana theme configurations.
- Added **Autostart** settings to the Settings page.

### Changed

- UpdateCard now reloads `assets/logo.png` after the update has been installed.
- UpdateCard now refreshes the displayed version information after installation.
- GTK icon cache is rebuilt after updated Ardana icons are installed.
- Desktop application metadata is refreshed after an update.
- Moved the **Autostart** toggle from the Dashboard to the Settings page.
- Autostart settings are now managed from the Settings page while preserving the existing autostart mechanism.
- Dashboard header now uses **Stop All** instead of the Autostart toggle.
- Stop All only stops currently running Ardana theme configurations and does not remove their saved autostart entries.
- Aligned the Settings page header and spacing with the existing About page layout.

### Fixed

- Fixed UpdateCard artwork not changing immediately after an update.
- Fixed the new Ardana logo requiring ThemeHub to be restarted before it appeared.
- Fixed the application icon cache not immediately reflecting updated Ardana icons.
- Improved the Dashboard header layout by placing **Stop All** alongside the theme search control.

### Build

- Build: `20260919`
