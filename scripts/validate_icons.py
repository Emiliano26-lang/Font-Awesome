#!/usr/bin/env python3
import sys
import yaml
from pathlib import Path

def main():
    if len(sys.argv) < 2:
        print("Usage: validate_icons.py <icon_requests.yml>")
        sys.exit(1)

    file_path = Path(sys.argv[1])
    if not file_path.exists():
        print(f"Error: {file_path} does not exist.")
        sys.exit(1)

    with open(file_path, "r", encoding="utf-8") as f:
        try:
            data = yaml.safe_load(f)
        except yaml.YAMLError as e:
            print(f"YAML parsing error: {e}")
            sys.exit(1)

    # Basic validation: ensure it's a list of requests
    if not isinstance(data, list):
        print("Validation failed: icon requests must be a list.")
        sys.exit(1)

    for i, req in enumerate(data, start=1):
        if "name" not in req or "category" not in req:
            print(f"Validation failed: request #{i} missing 'name' or 'category'.")
            sys.exit(1)

    print("Validation passed: all icon requests are valid.")

if __name__ == "__main__":
    main()
