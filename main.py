def get_direction(head, low, high):
    print("\n--- SCAN (Elevator) Direction Guide ---")
    print(f"Current Head Position: {head}")
    print(f"  'up'   -> Moves toward higher cylinders ({head} -> {high}), then reverses.")
    print(f"  'down' -> Moves toward lower cylinders  ({head} -> {low}), then reverses.\n")
    
    direction = input("Initial SCAN Direction (up/down): ").strip().lower()
    while direction not in ("up", "down"):
        direction = input("Invalid input. Please type 'up' or 'down': ").strip().lower()
    return direction

def scan(head, requests, low, high, direction):
    # Elevator: go one way to the disk END, then reverse
    smaller = sorted([r for r in requests if r < head])
    bigger = sorted([r for r in requests if r >= head])

    if direction == "up":
        order = bigger
        if len(smaller) > 0:
            order.append(high)               # touch the max boundary
            order += smaller[::-1]           # then go down (largest first)
    else:
        order = smaller[::-1]
        if len(bigger) > 0:
            order.append(low)                # touch the min boundary
            order += bigger                  # then go up
    return order


# ---------- OUTPUT ----------
def total_movement(head, order):
    total = 0
    current = head
    for cylinder in order:
        total += abs(cylinder - current)
        current = cylinder
    return total


def show_result(name, head, requests, order):
    print("\nDISK SCHEDULING -", name)
    print("\nInitial Head  :", head)
    print("Request Queue :", *requests)

    print("\nService Sequence:")
    print(head, end="")
    for cylinder in order:
        print(" ->", cylinder, end="")
    print("\n")

    print(f"{'Step':<6}{'From':<7}{'To':<6}Movement")
    current = head
    total = 0
    step = 1
    for cylinder in order:
        move = abs(cylinder - current)
        total += move
        note = "" if cylinder in requests else "  (disk boundary)"
        print(f"{step:<6}{current:<7}{cylinder:<6}{move:<4} = |{cylinder} - {current}|{note}")
        current = cylinder
        step += 1

    print("\nTotal Head Movement:", total, "cylinders")
    return total

while True:
    print("\n========================================")
    print("        DISK SCHEDULING SIMULATOR")
    print("========================================\n")
    print("1. FCFS")
    print("2. SSTF")
    print("3. SCAN (Elevator)")
    print("4. Compare Algorithms")
    print("5. Exit\n")
    print("=========================================")
    choice = input("Enter your selected Algorithm (1-5): ")
    print("=========================================\n")
    
    if choice == 5:
        print("Exiting the program...")
        break
    
    if choice < 1 or choice > 5:
        print("Invalid choice. Please select a valid option (1-5).")
        continue

     low, high, head, requests = get_inputs()

        if choice == 1:
        show_result("FCFS", head, requests, fcfs(head, requests))
    elif choice == 2:
        show_result("SSTF", head, requests, sstf(head, requests))
    elif choice == 3:
        direction = get_direction(head, low, high)
        show_result("SCAN", head, requests, scan(head, requests, low, high, direction))
    else:
