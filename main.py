"""
main.py
Make a python script in the introductions folder to introduce yourself.
DO NOT WRITE IN THIS FILE. Pull Requests will be rejected and ignored.
"""
from pathlib import Path
import importlib.util
import sys
import time

if __name__ == "__main__":
    print("Welcome to micromouse! Let me introduce you to each other!")
    intro_dir = Path("introductions")
    for intro_file in intro_dir.glob("*.py"):
        
        if intro_file.name == "__init__.py":
            continue
        module_name = intro_file.stem
        spec = importlib.util.spec_from_file_location(module_name, intro_file)
        module = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = module
        spec.loader.exec_module(module)
        if hasattr(module, "introduce"):
            print(f"\n--- Introduction from {module_name} ---")
            module.introduce()
            time.sleep(1)
        else:
            print(f"\n--- {module_name} does not have an introduce() function ---")
    print("\n--- End of introductions ---")
    print("Atharv was here")


    antoehunsatohensuthasnoethuns