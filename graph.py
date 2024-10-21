import os
import csv
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Define the filename for storing data
FILENAME = 'elo_data.csv'

def initialize_csv(filename):
    """Initialize the CSV file with headers if it doesn't exist."""
    if not os.path.exists(filename):
        with open(filename, mode='w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Datetime', 'ELO'])

def read_data(filename):
    """Read data from the CSV file."""
    datetimes = []
    elos = []
    with open(filename, mode='r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            datetimes.append(datetime.strptime(row['Datetime'], '%Y-%m-%d %H:%M:%S'))
            elos.append(float(row['ELO']))
    return datetimes, elos

def write_data(filename, dt, elo):
    """Write a new entry to the CSV file."""
    with open(filename, mode='a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([dt.strftime('%Y-%m-%d %H:%M:%S'), elo])

def plot_graph_with_time(datetimes, elos):
    """Plot the ELO progression graph with time on the x-axis."""
    if not datetimes:
        print("No data to display.")
        return

    plt.figure(figsize=(12, 6))
    plt.plot(datetimes, elos, marker='o', linestyle='-')
    plt.title('ELO Progression Over Time')
    plt.xlabel('Date and Time')
    plt.ylabel('ELO Rating')
    plt.grid(True)
    plt.tight_layout()

    # Format the x-axis for better readability
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))
    plt.gcf().autofmt_xdate()  # Rotate date labels for readability

    plt.show()

def plot_graph_with_game_number(elos):
    """Plot the ELO progression graph with game number on the x-axis."""
    if not elos:
        print("No data to display.")
        return

    game_numbers = list(range(1, len(elos) + 1))

    plt.figure(figsize=(12, 6))
    plt.plot(game_numbers, elos, marker='o', linestyle='-')
    plt.title('ELO Progression by Number of Games')
    plt.xlabel('Game Number')
    plt.ylabel('ELO Rating')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def main():
    initialize_csv(FILENAME)
    datetimes, elos = read_data(FILENAME)

    while True:
        user_input = input("Enter '1' to add ELO, '2' to view graph with time, '3' to view graph with game number, or 'q' to quit: ")

        if user_input == '1':
            # Add a new ELO entry
            elo_input = input("Enter the ELO after your game: ")
            try:
                elo_value = float(elo_input)
                current_datetime = datetime.now()
                write_data(FILENAME, current_datetime, elo_value)
                datetimes.append(current_datetime)
                elos.append(elo_value)
            except ValueError:
                print("Invalid ELO value. Please enter a numeric value.")
        elif user_input == '2':
            # Display the graph with time on the x-axis
            plot_graph_with_time(datetimes, elos)
        elif user_input == '3':
            # Display the graph with game number on the x-axis
            plot_graph_with_game_number(elos)
        elif user_input == 'q':
            # Quit the program
            break
            break
        else:
            print("Invalid input. Please enter '1', '2', '3', or 'q'.")

if __name__ == '__main__':
    main()
