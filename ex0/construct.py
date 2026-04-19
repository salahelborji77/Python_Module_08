import os
import sys
import site

def main() -> None:
    run_py = sys.executable
    if sys.prefix != sys.base_prefix:
        print("MATRIX STATUS: Welcome to the construct\n")
        print(f"Current Python {run_py}")
        print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
        print(f"Environment Path: {sys.prefix}\n")
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.")
        print("\nPackage installation path:")
        print(site.getsitepackages()[0])

    else:
        print("\nMATRIX STATUS: You're still plugged in\n")
        print(f"Current Python: {run_py}")
        print("Virtual Environment: None detected\n")
        print(
            "WARNING: You're in the global environment!",
            "The machines can see everything you install.\n"
            )
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\Scripts\\activate # On Windows\n")
        print("Then run this program again.")


main()