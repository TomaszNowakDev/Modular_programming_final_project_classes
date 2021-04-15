# Tomasz Nowak
# 15 APR 2021

# Setting MAIN MENU as a constant
MAIN_MENU = "Running Contest \n=========================== \n1. Show the results for a race" \
            + "\n2. Add results for a race \n3. Show all competitors by county \n4. Show the winner of each race" \
            + "\n5. Show all the race times for one competitor \n6. Show all competitors who have won a race" \
            + "\n7. Quit"


class Runner:
    def __init__(self, n, c):
        self.name = n
        self.code = c

    def __str__(self):
        return f"{self.name} {self.code}"


class Venue:
    def __init__(self, code_run, times):
        self.code_run = code_run
        self.time = times

    def __str__(self):
        return f"{self.code_run} {self.time}"


def display(items):
    for item in range(len(items)):
        print(f"{item+1}. {items[item]}")


def reading_races():
    with open("Races.txt") as file:
        lines = file.readlines()
        return [race.strip() for race in lines]


def validation_for_choice(rac, prompt):
    display(rac)
    while True:
        try:
            cho = int(input(prompt))
            if 0 <= cho <= len(rac):
                break
            else:
                print("Choose one of the options please.")
        except ValueError:
            print("Numbers only please!")
    return cho


with open("Runners.txt") as file_runners:
    lines_runners = file_runners.readlines()
    runners = []
    for line in lines_runners:
        split_line_runners = line.split(",")
        name = split_line_runners[0]
        id_runner = split_line_runners[1].strip()
        runner = Runner(name, id_runner)
        runners.append(runner)


def reading_venues(races, choice1):
    with open(f"{races[choice1 - 1]}.txt") as file_races:
        lines_race_details = file_races.readlines()
        races_details = []
        for lin in lines_race_details:
            split_line_race = lin.split(",")
            code = split_line_race[0]
            time = int(split_line_race[1])
            race_det = Venue(code, time)
            races_details.append(race_det)


def main():
    print(MAIN_MENU)
    try:
        choice_main = int(input("==>"))
        while True:
            races = reading_races()
            if choice_main == 1:
                print("(1) Show the results for a race \n===============================")
                display(races)
                choice1 = validation_for_choice(races, "Choice ==> ")
                reading_venues(races, choice1)
                print(f"Results for {races[choice1 - 1]}\n=======================")

            elif choice_main == 2:
                print("(2) Add results for a race \n===============================")
            elif choice_main == 3:
                print("(3) Show all competitors by county \n===============================")
            elif choice_main == 4:
                print("(4) Show the winner of each race \n===============================")
            elif choice_main == 5:
                print("(5) Show all the race times for one competitor \n===============================")
            elif choice_main == 6:
                print("(6) Show all competitors who have won a race \n===============================")
            elif choice_main == 7:
                print("Thank you, Goodbye.")
                break
            else:
                print("Choose one of the options from 1 to 7.")
            print(MAIN_MENU)
            choice_main = int(input("==>"))
    except ValueError:
        print("Please choose one of the options from main menu.")


if __name__ == '__main__':
    main()
