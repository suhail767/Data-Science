import csv
from datetime import datetime
from matplotlib import pyplot as plt

# Get date, low and high temperature from file
filename = "san_francisco.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%m/%d/%Y")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
    # Plot data
    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(dates, highs, c='red', alpha=0.5)
    plt.plot(dates, lows, c='blue', alpha=0.5)
    plt.fill_between(dates, highs, lows, facecolor='grey', alpha=0.2)

    # Format Plot
    plt.title("Daily high and low temperatures in San Francisco, 2014",
              fontsize=18)
    fig.autofmt_xdate()
    plt.xlabel('', fontsize=16)
    plt.ylabel('Temperature(F)', fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=10)
    plt.show()
