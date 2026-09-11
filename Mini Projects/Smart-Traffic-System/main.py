from database import init_db, get_violations
from cameras import SpeedCamera

def main():
    print("Starting Smart Traffic Management System...\n")
    init_db()

    radar = SpeedCamera(resolution="4K", fps=60, speed_limit=120)
    radar.check_multiple_speeds(110, 145, 95, 160)
    print("\n-------------------------------------------")

    print("Fetching Traffic Violations from SQLite Database:")
    violations = get_violations()

    if violations:
        for v in violations:
            print(f" [Violation ID: {v[0]}]  Speed: {v[1]} km/h | Road Limit: {v[2]} km/h")
    else:
        print("No violations recorded.")
if __name__ == "__main__":
    main()
