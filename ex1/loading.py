import importlib
import sys
from typing import Any


def check_dep() -> tuple[dict[str, dict[str, str | Any | str]], list[str]]:
    deps = [
        {"name": "pandas", "info": "Data manipulation ready"},
        {"name": "numpy", "info": "Numerical computation ready"},
        {"name": "requests", "info": "Network access ready"},
        {"name": "matplotlib.pyplot", "info": "Visualization ready"},
    ]

    installed = {}
    errors = []

    for dep in deps:
        name = dep["name"]
        try:
            module = importlib.import_module(name)
            version = getattr(module, "__version__", "unknown")

            installed[name] = {
                "module": module,
                "version": version,
                "info": dep["info"],
            }
        except Exception:
            errors.append(name)

    return installed, errors


def analyze_matrix(packages) -> None:
    np = packages["numpy"]["module"]
    pd = packages["pandas"]["module"]
    plt = packages["matplotlib.pyplot"]["module"]
    print("Analyzing Matrix data...")
    data = np.random.rand(100, 10)

    print("Processing 1000 data points...")
    df = pd.DataFrame(data)
    stats = df.mean()

    print("Generating visualization...")
    plt.figure()
    stats.plot(kind="bar")
    plt.title("Average Values per Column")
    plt.xlabel("Column")
    plt.ylabel("Mean Values")

    filename = "matrix_analysis.png"
    plt.savefig(filename)
    plt.close()

    print("Analysis complete!")
    print(f"Results saved to: {filename}")


def main() -> None:
    installed, errors = check_dep()
    print("\nLOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")
    for err in errors:
        print(f"[ERROR] {err} - Not Installed")

    if len(errors) > 0:
        raise ValueError("Dependency issues!")

    for name, data in installed.items():
        print(f"[OK] {name} ({data['version']}) - {data['info']}")

    analyze_matrix(installed)
    if "poetry" in sys.executable.lower():
        print("running with poetry in environment")
    else:
        print("runinnig with pip in environment")


if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        print(f"ERROR: {err}")
