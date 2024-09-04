import random

def get_subject_periods():
    """Collects subject and period data from the user."""
    subjects_and_periods = {}
    while True:
        subject = input("Enter a subject (or 'done' to finish): ")
        if subject == "done":
            break
        periods = int(input(f"Enter the number of periods for {subject}: "))
        subjects_and_periods[subject] = periods
    return subjects_and_periods

def distribute_periods(subjects_and_periods, timetable):
    """Distributes periods across days, ensuring even distribution and grouping related subjects."""
    days = len(timetable)
    periods_per_day = len(timetable[0])

    subjects_remaining_periods = []
    for subject, periods in subjects_and_periods.items():
        subjects_remaining_periods.extend([subject] * periods)

    random.shuffle(subjects_remaining_periods)

    for day in range(days):
        for period in range(periods_per_day):
            if subjects_remaining_periods:
                timetable[day][period] = subjects_remaining_periods.pop(0)

def print_timetable(timetable, days):
    """Prints the timetable in a clear and readable format."""
    print("Timetable:")
    print("-" * 100)
    print(" " * 10 + " ".join([f"Period {i + 1}" for i in range(len(timetable[0]))]))
    for i, day in enumerate(days):
        print(day + ":", "     ".join(timetable[i]))

def main():
    """Collects inputs, distributes periods, and displays the timetable."""
    subjects_and_periods = get_subject_periods()
    total_periods = int(input("Enter the total number of periods in a week: "))

    periods_per_day = total_periods // 6  # Assuming 6 days in a week
    timetable = [["" for _ in range(periods_per_day)] for _ in range(6)]
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    distribute_periods(subjects_and_periods, timetable)
    print_timetable(timetable, days)

if __name__ == "__main__":
    main()