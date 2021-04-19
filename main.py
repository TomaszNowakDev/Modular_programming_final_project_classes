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


class ResultOfRace:
    def __init__(self, code_run, times):
        self.code_run = code_run
        self.time = times

    def __str__(self):
        return f"{self.code_run} {self.time_formatted()}"

    def time_formatted(self):
        minutes = self.time // 60
        seconds = self.time % 60
        tf = f"{minutes:>5} min {seconds:>2} sec"
        return tf


def display_numbered(items):
    for item in range(len(items)):
        print(f"{item+1}. {items[item]}")


def display(items):
    for i in range(len(items)):
        print(items[i])


def reading_races():
    with open("Races.txt") as file:
        lines = file.readlines()
        return [race.strip() for race in lines]


def validation_for_choice(minimum, maximum, prompt):
    while True:
        try:
            cho = int(input(prompt))
            if minimum < cho <= maximum:
                break
            else:
                print("Choose one of the following options please.")
        except ValueError:
            print("Numbers only please!")
    return cho


def reading_runners():
    with open("Runners.txt") as file_runners:
        lines_runners = file_runners.readlines()
        runners = []
        for line in lines_runners:
            split_line_runners = line.split(",")
            name = split_line_runners[0]
            id_runner = split_line_runners[1].strip()
            runner = Runner(name, id_runner)
            runners.append(runner)
    return runners


def reading_venues(race, choice1):
    with open(f"{race[choice1 - 1]}.txt") as file_races:
        lines_race_details = file_races.readlines()
        races_details = []
        for lin in lines_race_details:
            split_line_race = lin.split(",")
            code = split_line_race[0]
            time = int(split_line_race[1])
            race_det = ResultOfRace(code, time)
            races_details.append(race_det)
    return races_details


def main():
    print(MAIN_MENU)
    choice_main = validation_for_choice(0, 7, "==>")
    while True:
        races = reading_races()
        runners = reading_runners()

        if choice_main == 1:
            print("(1) Show the results for a race \n===============================")
            display_numbered(races)
            choice1 = validation_for_choice(0, len(races), "Choice ==> ")
            race_details = reading_venues(races, choice1)
            print(f"Results for {races[choice1 - 1]}\n=======================")
            for racer in race_details:
                print(racer)
            years = [race_details[i].time for i in range(len(race_details))]
            fastest = min(years)
            winner = [runner.code_run+" won the race." for runner in race_details if runner.time == fastest]
            print()
            display(winner)
        elif choice_main == 2:
            print("(2) Add results for a race \n===============================")
            new_race = input("Name of new race location ==> ").capitalize()
            while True:
                if new_race not in races:
                    with open("Races.txt", "a") as file_option2:
                        print(new_race, file=file_option2)
                else:
                    print(f"Data for {new_race} already exists, please enter a different name.")
                    new_race = input("Name of new race location ==> ").capitalize()
                with open(new_race.lower() + ".txt", "w") as file_race:
                    for racer1 in runners:
                        while True:
                            try:
                                time_from_race = int(input(f"What time {racer1.code} got in {new_race} race? ==>"))
                                if time_from_race > 0:
                                    print(f"{racer1.code},{time_from_race}", file=file_race)
                                    break
                                elif time_from_race == 0:
                                    print(f"{racer1.code} did not participate or did not finish the {new_race} race.")
                                    break
                                else:
                                    print("Positive numbers only, or number zero if the runner did not participate or"
                                          + " did not finish the race.")
                            except ValueError:
                                print("Numbers only please!")
                    break

        elif choice_main == 3:
            print("(3) Show all competitors by county \n===============================")
            print("Cork runners \n---------------------")
            for r in runners:
                if r.code.startswith("CK"):
                    print(f"\t{r.name:15}{r.code}")
            print("Kerry runners \n---------------------")
            for r in runners:
                if r.code.startswith("KY"):
                    print(f"\t{r.name:15}{r.code}")
        elif choice_main == 4:
            print("(4) Show the winner of each race \n===============================")

        elif choice_main == 5:
            print("(5) Show all the race times for one competitor \n===============================")
        elif choice_main == 6:
            print("(6) Show all competitors who have won a race \n===============================")
        elif choice_main == 7:
            print("Thank you, Goodbye.")
            break
        print(MAIN_MENU)
        choice_main = validation_for_choice(0, 7, "==>")


if __name__ == '__main__':
    main()
