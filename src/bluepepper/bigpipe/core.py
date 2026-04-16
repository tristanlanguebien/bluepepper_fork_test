import os

if not os.environ.get("BLUEPEPPER_ROOT"):
    raise RuntimeError(
        'The environment variable "BLUEPEPPER_ROOT" was not found. Please make sure to initialize bluepepper'
    )

from pathlib import Path

root_dir = Path(os.environ["BLUEPEPPER_ROOT"])
user_prefs_dir = root_dir.parent / f"{root_dir.name}_userprefs/{os.environ['USERNAME']}"
