def process_file(filename):
    # Easter Egg check
    if filename.lower() == "na na boo boo":
        print("NA NA BOO BOO TO YOU - You have been punk'd!")
        return
    
    # Normal file processing
    try:
        with open(filename, 'r') as file:
            count = 0
            for line in file:
                if line.startswith('Subject:'):
                    count += 1
            print(f"There were {count} subject lines in {filename}")
    except FileNotFoundError:
        print(f"File cannot be opened: {filename}")

# Get filename from user
filename = input("Enter the file name: ")
process_file(filename)