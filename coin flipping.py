import random

def flip_coin():
    return 'Heads' if random.randint(0, 1) == 0 else 'Tails'

def main():
    print("Coin Flip Simulator")
    flips = int(input("Enter the number of times you want to flip the coin: "))
    heads_count = 0
    tails_count = 0

    for _ in range(flips):
        result = flip_coin()
        print(result)
        if result == 'Heads':
            heads_count += 1
        else:
            tails_count += 1

    print("\nResults:")
    print(f"Heads: {heads_count}")
    print(f"Tails: {tails_count}")

if __name__ == "__main__":
    main()
