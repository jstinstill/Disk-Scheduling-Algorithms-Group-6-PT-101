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
