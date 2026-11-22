def get_number(explanation, prompt, minimum=None, maximum=None, rule=""):
    if explanation != "":
        print("\n" + explanation)
    while True:
        text = input(prompt)

        # Error handling: Is it a whole number?
        try:
            number = int(text)
        except ValueError:
            print(f"  ERROR: '{text}' is not a whole number.")
            print("  Letters, symbols, decimals, and blank entries are not accepted.")
            print("  Please enter digits only (example: 25).")
            continue

        # Error handling 2: Is it inside the allowed range?
        if (minimum is not None and number < minimum) or \
           (maximum is not None and number > maximum):
            print(f"  ERROR: {number} is invalid. {rule}")
            continue

        return number
        
def get_inputs():
    low = get_number(
        "Please enter a whole number for the MINIMUM disk cylinder (usually 0).",
        "Minimum Disk Cylinder: ",
        minimum = 0,
        rule = "Cylinder numbers cannot be negative. Enter 0 or higher.")

    high = get_number(
        "Please enter a whole number for the MAXIMUM disk cylinder (example: 199).\n"
        "It must be greater than the minimum cylinder.",
        "Maximum Disk Cylinder: ",
        minimum = low + 1,
        rule=f"The maximum must be GREATER than the minimum ({low}), "
             "so the disk range is invalid.")

    head = get_number(
        f"Please enter a whole number for the INITIAL HEAD position.\n"
        f"It must be inside the disk range ({low} to {high}).",
        "Initial Head Position: ",
        minimum = low, maximum = high,
        rule = f"The head must be inside the disk range ({low} to {high}).")

    n = get_number(
        "Please enter how many requests are in the queue (a whole number, at least 1).",
        "Number of Requests: ",
        minimum = 1,
        rule = "There must be at least 1 request to schedule.")

    print(f"\nNow enter each request as a whole number from {low} to {high}.")
    print("Requests outside this range are rejected and asked for again.")
    requests = []
    for i in range(n):
        r = get_number("", f"Request {i + 1}: ", minimum=low, maximum=high,
                       rule=f"A request must be inside the disk range ({low} to {high}).")
        requests.append(r)

    return low, high, head, requests

def scan(head, requests, low, high, direction):
    # Elevator: go one way to the disk END, then it will reverse
    smaller = sorted([r for r in requests if r < head])
    bigger = sorted([r for r in requests if r >= head])

    if direction == "up":
        order = bigger
        if len(smaller) > 0:
            order.append(high)       # It will go to the maximum boundary
            order += smaller[::-1]   # Then it will go down from largest
    else:
        order = smaller[::-1]
        if len(bigger) > 0:
            order.append(low)        # It will go to the minimum boundary
            order += bigger          # Then it will go up from smallest
    return order


while True:
    print("\n========================================")
    print("        DISK SCHEDULING SIMULATOR")
    print("========================================\n")
    print("1. FCFS")
    print("2. SSTF")
    print("3. SCAN (Elevator)")
    print("4. Compare Algorithms")
    print("5. Exit")

    choice = get_number(
        "\nPlease enter the number of your choice (a whole number from 1 to 5).",
        "Select Algorithm: ",
        minimum=1, maximum=5,
        rule="That is not on the menu. Choose a number from 1 to 5.")

    if choice == 5:
        print("Goodbye!")
        break

    low, high, head, requests = get_inputs()

    if choice == 1:
        show_result("FCFS", head, requests, fcfs(head, requests))
    elif choice == 2:
        show_result("SSTF", head, requests, sstf(head, requests))
    elif choice == 3:
        direction = get_direction()
        show_result("SCAN", head, requests, scan(head, requests, low, high, direction))
    else:
        direction = get_direction()
        compare(head, requests, low, high, direction)
