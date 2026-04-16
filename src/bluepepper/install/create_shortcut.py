"""Create Windows shortcuts programmatically."""

import argparse
import logging
from pathlib import Path
from typing import Optional

from win32com.client import Dispatch


def create_shortcut(
    path: str,
    target: str,
    icon: str,
    args: Optional[str] = None,
) -> None:
    """Create a Windows shortcut.

    Args:
        path: Path where the shortcut will be created.
        target: Path to the executable the shortcut points to.
        icon: Path to the icon file (.ico).
        args: Optional command-line arguments for the target executable.
    """
    logging.info(f"Creating shortcut: {path}")
    shell = Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(path)
    shortcut.Targetpath = target
    shortcut.IconLocation = icon
    if args:
        shortcut.Arguments = args
    shortcut.save()


def main() -> None:
    """Parse arguments and create shortcut."""
    parser = argparse.ArgumentParser(
        description="Create a Windows shortcut.",
    )
    parser.add_argument(
        "-p",
        "--path",
        required=True,
        help="Path to shortcut to create",
    )
    parser.add_argument(
        "-t",
        "--target",
        required=True,
        help="Path to the executable",
    )
    parser.add_argument(
        "-i",
        "--icon",
        required=True,
        help="Path to the .ico file",
    )
    parser.add_argument(
        "-a",
        "--arguments",
        help="Arguments separated by spaces",
    )
    parsed_args = parser.parse_args()

    create_shortcut(
        path=str(Path(parsed_args.path)),
        target=str(Path(parsed_args.target)),
        icon=str(Path(parsed_args.icon)),
        args=parsed_args.arguments,
    )


if __name__ == "__main__":
    main()
