# Ardana ThemeHub

Official theme repository for **Ardana ThemeHub**.

This repository provides themes, configuration files, metadata, previews, and font dependencies used by Ardana ThemeHub.

## Repository Structure

```text
ardana-themehub/
├── index.json
│
├── themes/
│   └── ThemeName/
│       ├── metadata.json
│       ├── ThemeName.conf
│       └── ...
│
├── fonts/
│   ├── FontName.ttf
│   └── FontName.otf
│
└── previews/
    └── ThemeName.jpg
```

## Themes

Each theme is stored in its own directory inside:

```text
themes/
```

The directory name represents the theme name.

Each theme contains a `metadata.json` file that defines information such as:

* Theme name
* Version
* Author
* Required fonts
* Available Conky configuration files
* Configuration geometry

Example:

```json
{
    "name": "Thuban",
    "version": "1.0",
    "author": "Closebox73",

    "fonts": [
        "Inter-Regular.otf",
        "Inter-Bold.otf"
    ]
}
```

## Font Dependencies

Some themes require additional fonts.

Required fonts are defined in each theme's metadata and are checked by Ardana ThemeHub before installation.

ThemeHub compares the required fonts with fonts already available in:

```text
~/.local/share/fonts
```

If a required font is already available locally, it will not be downloaded again.

Only missing fonts are installed.

## Index

The repository uses `index.json` as the ThemeHub market index.

The index provides information about available themes, including:

* Theme name
* Version
* Author
* Required fonts
* Theme path
* Preview

ThemeHub downloads the index to display available themes and compare them with locally installed themes.

## License

This repository is licensed under the **MIT License**.

The Ardana theme configurations, metadata, index files, and other original repository content are released under the MIT License.

## Third-Party Fonts

Fonts included in this repository are obtained from **Google Fonts** and are licensed under the **SIL Open Font License (OFL)**.

Each font remains subject to its original license and copyright terms.

## About Ardana ThemeHub

Ardana ThemeHub is the theme management and distribution system for Ardana, providing a centralized way to discover, install, update, and manage themes and their required dependencies.
