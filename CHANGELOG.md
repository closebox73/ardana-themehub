## [1.7] Delphinus - 2026-09-30

### Added

- Added `whoami` to the System Provider to retrieve the current username.
- Added `distro` to the System Provider to retrieve the Linux distribution name from `/etc/os-release`.
- Added network connection status icons for Wi-Fi, wired, and disconnected states.

### Changed

- System Provider now exposes username and distribution information through `theme.providers.system.get()`.
- System identity information is loaded during provider initialization.

### Build

- Build: `20260930`
