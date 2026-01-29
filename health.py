# main.py
from health import Health
from file_manager import save_health_data, read_health_data

def menu():
    print("\n🌿 SMART HEALTH TRACKER")
    print("1. Add Today’s Health Data")
    print("2. View Health History")
    print("3. Exit")

while True:
    menu()
    choice = input("Choose option: ")

    if choice == "1":
        water = float(input("💧 Water intake (liters): "))
        steps = int(input("🚶 Steps walked: "))
        sleep = float(input("😴 Sleep hours: "))

        health = Health(water, steps, sleep)
        save_health_data(health)

        print(f"✅ Health data saved | ❤️ Health Score: {health.health_score()}/100")

    elif choice == "2":
        records = read_health_data()
        if not records:
            print("⚠️ No records found. Add data first!")
        else:
            print("\n--- Health History ---")
            for r in records:
                water, steps, sleep, score = r.strip().split(",")
                print(
                    f"💧 Water: {water}L | 🚶 Steps: {steps} | 😴 Sleep: {sleep}h | ❤️ Score: {score}"
                )

    elif choice == "3":
        print("👋 Stay healthy, stay happy 💚")
        break

    else:
        print("❌ Invalid option. Please choose 1, 2, or 3.")
