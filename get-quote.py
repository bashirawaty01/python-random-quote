import random


def primary():
    # print("Keep it logically awesome.")

    f = open("quotes.txt")
    quotes = f.readlines()
    f.close()

    last = len(quotes) - 1

    # If you want to add or remove quotes from your text file, you could change the last variable to update automatically:
    # last = len(quotes) - 1

    rnd = random.randint(0, last)  # 0 is the lowest-possible number

    print(quotes[rnd])

    # print out more than one quote
    # rnd = random.randint(0, last)  # 0 is the lowest-possible number
    # rnd1 = random.randint(0, last)  # 0 is the lowest-possible number
    # print(quotes[rnd])
    # print(quotes[rnd1])


if __name__ == "__main__":
    primary()
