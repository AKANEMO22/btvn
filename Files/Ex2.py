def process_spam_confidence(filename):
    try:
        total = 0
        count = 0
        
        with open(filename) as file:
            for line in file:
                if line.startswith('X-DSPAM-Confidence:'):
                    # Extract the number from the line
                    number = float(line.split(':')[1].strip())
                    total += number
                    count += 1
        
        if count > 0:
            average = total / count
            print(f"Average spam confidence: {average}")
        else:
            print("No spam confidence values found")
            
    except FileNotFoundError:
        print(f"File cannot be opened: {filename}")
    except ValueError:
        print("Error processing numbers in the file")

# Get filename from user and process it
filename = input("Enter the file name: ")
process_spam_confidence(filename)