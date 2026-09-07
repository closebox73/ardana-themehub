#!/usr/bin/env python3

import json
import sys
import zipfile
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parent

THEMES_DIR = ROOT_DIR / "themes"
FONTS_DIR = ROOT_DIR / "fonts"
PREVIEWS_DIR = ROOT_DIR / "previews"
INDEX_FILE = ROOT_DIR / "index.json"


def load_metadata(zip_path):

    try:

        with zipfile.ZipFile(
            zip_path,
            "r",
        ) as archive:

            metadata_paths = [
                name
                for name in archive.namelist()
                if Path(name).name == "metadata.json"
            ]

            if not metadata_paths:

                print(
                    f"[ERROR] metadata.json not found: "
                    f"{zip_path.name}"
                )

                return None

            metadata_path = metadata_paths[0]

            with archive.open(
                metadata_path
            ) as file:

                return json.load(file)

    except zipfile.BadZipFile:

        print(
            f"[ERROR] Invalid ZIP file: "
            f"{zip_path.name}"
        )

    except json.JSONDecodeError as error:

        print(
            f"[ERROR] Invalid metadata.json: "
            f"{zip_path.name}"
        )

        print(
            f"        {error}"
        )

    except Exception as error:

        print(
            f"[ERROR] Failed to read: "
            f"{zip_path.name}"
        )

        print(
            f"        {error}"
        )

    return None


def validate_metadata(
    metadata,
    zip_path,
):

    required_fields = [
        "name",
        "version",
        "author",
        "fonts",
    ]

    missing = []

    for field in required_fields:

        if field not in metadata:

            missing.append(
                field
            )

    if missing:

        print(
            f"[ERROR] Missing metadata fields "
            f"in {zip_path.name}:"
        )

        for field in missing:

            print(
                f"        - {field}"
            )

        return False

    if not isinstance(
        metadata["fonts"],
        list,
    ):

        print(
            f"[ERROR] 'fonts' must be a list: "
            f"{zip_path.name}"
        )

        return False

    return True


def validate_fonts(
    fonts,
    theme_name,
):

    missing_fonts = []

    for font_name in fonts:

        font_path = (
            FONTS_DIR /
            font_name
        )

        if not font_path.exists():

            missing_fonts.append(
                font_name
            )

    if missing_fonts:

        print(
            f"[ERROR] Missing font dependencies "
            f"for {theme_name}:"
        )

        for font_name in missing_fonts:

            print(
                f"        - {font_name}"
            )

        return False

    return True


def find_preview(theme_name):

    preview_path = (
        PREVIEWS_DIR /
        f"{theme_name}.webp"
    )

    if preview_path.exists():

        return (
            f"previews/"
            f"{preview_path.name}"
        )

    return None


def build_theme_entry(
    metadata,
    zip_path,
):

    theme_name = metadata["name"]

    if not validate_fonts(
        metadata["fonts"],
        theme_name,
    ):

        return None

    preview = find_preview(
        theme_name
    )

    if not preview:

        print(
            f"[ERROR] Preview not found: "
            f"{theme_name}.webp"
        )

        return None

    return {
        "name": theme_name,
        "version": metadata["version"],
        "author": metadata["author"],
        "fonts": metadata["fonts"],
        "whats_new": False,
        "file": (
            f"themes/"
            f"{zip_path.name}"
        ),
        "preview": preview,
    }


def generate_index():

    required_dirs = [
        THEMES_DIR,
        FONTS_DIR,
        PREVIEWS_DIR,
    ]

    for directory in required_dirs:

        if not directory.exists():

            print(
                f"[ERROR] Directory not found: "
                f"{directory.name}/"
            )

            sys.exit(1)

    theme_entries = []

    zip_files = sorted(
        THEMES_DIR.glob("*.zip"),
        key=lambda item: item.name.lower(),
    )

    if not zip_files:

        print(
            "[WARNING] No theme ZIP files found."
        )

    for zip_path in zip_files:

        print()
        print(
            f"[READ] {zip_path.name}"
        )

        metadata = load_metadata(
            zip_path
        )

        if not metadata:
            continue

        if not validate_metadata(
            metadata,
            zip_path,
        ):
            continue

        entry = build_theme_entry(
            metadata,
            zip_path,
        )

        if not entry:
            continue

        theme_entries.append(
            entry
        )

        print(
            f"[OK] Indexed: "
            f"{entry['name']} "
            f"v{entry['version']}"
        )

    index = {
        "themes": theme_entries
    }

    with INDEX_FILE.open(
        "w",
        encoding="utf-8",
    ) as file:

        json.dump(
            index,
            file,
            indent=4,
            ensure_ascii=False,
        )

        file.write("\n")

    print()
    print(
        "[DONE] index.json generated"
    )

    print(
        f"[INFO] Total themes: "
        f"{len(theme_entries)}"
    )


if __name__ == "__main__":

    generate_index()
