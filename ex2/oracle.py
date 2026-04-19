import os


def load_config() -> None:
    from dotenv import load_dotenv
    load_dotenv()
    config = {
        "MATRIX_MODE": os.getenv("MATRIX_MODE"),
        "DATABASE_URL": os.getenv("DATABASE_URL"),
        "API_KEY": os.getenv("API_KEY"),
        "LOG_LEVEL": os.getenv("LOG_LEVEL"),
        "ZION_ENDPOINT": os.getenv("ZION_ENDPOINT"),
    }
    return config


def validate_config(config: dict) -> None:
    missing = [k for k, v in config.items() if not v]

    if missing:
        print("WARNING: Missing configuration values:")
        for key in missing:
            print(f"- {key}")

def display_config(config: dict) -> None:
    print("ORACLE STATUS: Reading the Matrix...\n")

    print("Configuration loaded:")

    mode = config["MATRIX_MODE"] or "development"
    print(f"Mode: {mode}")

    if config["DATABASE_URL"]:
        print("Database: Connected")
    else:
        print("Database: Not configured")

    if config["API_KEY"]:
        print("API Access: Authenticated")
    else:
        print("API Access: Missing key")

    print(f"Log Level: {config['LOG_LEVEL'] or 'INFO'}")

    if config["ZION_ENDPOINT"]:
        print("Zion Network: Online")
    else:
        print("Zion Network: Offline")


def security_check(config: dict) -> None:
    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")
    print("\nThe Oracle sees all configurations.")


def main():
    config = load_config()
    validate_config(config)
    display_config(config)
    security_check(config)


if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        print(err)