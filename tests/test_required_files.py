#!/usr/bin/env python3
import sys
from pathlib import Path

def check_files(base_dir: Path, required_files: list[str]) -> bool:
    missing = []
    for filename in required_files:
        target = base_dir / filename
        if not target.exists():
            missing.append(filename)
    if missing:
        print("ERROR: Missing required file(s) in", str(base_dir))
        for fn in missing:
            print(f"  - {fn}")
        return False
    return True

def main():
    # The directory containing this script
    script_path = Path(__file__).resolve()
    repo_root = script_path.parent.parent  # base directory where files should reside

    # List required filenames relative to this directory
    required = [
        "README.md",
        "LICENSE",
        ".gitignore",
    #    "setup.py",
        # add others you need
    ]

    ok = check_files(repo_root, required)
    if not ok:
        sys.exit(1)

    print("All required files are present in", repo_root)
    sys.exit(0)

if __name__ == "__main__":
    main()