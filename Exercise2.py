import sys
import json
import random


def main():
    if len(sys.argv) != 7:
        print("Please input 6 parameters.Ex. 1 2 3 4 5 6")
        return

    numbers = [int(num) for num in sys.argv[1:]]

    while True:
        print("\nChoose an option:")
        print("1. Perform subtraction and show output on screen")
        print("2. Perform multiplication and store result in a JSON file")
        print("3. Pick randomly a number and show it on screen")
        print("4. Print sorted (highest to lowest) array/list numbers")
        print("5. Print sorted (lowest to highest) array/list numbers")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            subtraction_result = numbers[0] - sum(numbers[1:])
            print("Subtraction result:", subtraction_result)
        elif choice == '2':
            multiplication_result = 1
            for num in numbers:
                multiplication_result = multiplication_result * num
            result_dict = {f"InputNumber{i + 1}": num for i, num in enumerate(numbers)}
            result_dict["Multiplication"] = multiplication_result
            with open("multiplication_result.json", "w") as f:
                json.dump(result_dict, f)
            print("Multiplication result stored in multiplication_result.json")
        elif choice == '3':
            print("Randomly picked number:", random.choice(numbers))
        elif choice == '4':
            sorted_numbers = sorted(numbers, reverse=True)
            print("Sorted (highest to lowest):", sorted_numbers)
        elif choice == '5':
            sorted_numbers = sorted(numbers)
            print("Sorted (lowest to highest):", sorted_numbers)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()