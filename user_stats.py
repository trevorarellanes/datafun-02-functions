"""
Trevor Arellanes
Fundamentals of Data Analytics
1/24/23

This example illustrates basic analytics
using just the built-in statistics module.

VS Code Menu / View / Command Palette / Python Interpretor
Must be 3.10 or greater to get the correlation and linear regression.

To update, try:
conda update pythnon -y
conda --version

Uses only Python Standard Library module:

- statistics - for basic descriptive and a bit of predictive stats

"""

import statistics

# define a variable with some univariant data 
# (one varabile, many readings)
heart_rate = [
    105,
    129,
    87,
    86,
    111,
    111,
    89,
    81,
    108,
    92,
    110,
    100,
    75,
    105,
    103,
    109,
    76,
    119,
    99,
    91,
    103,
    129,
    106,
    101,
    84,
    111,
    74,
    87,
    86,
    103,
    103,
    106,
    86,
    111,
    75,
    87,
    102,
    121,
    111,
    88,
    89,
    101,
    106,
    95,
    103,
    107,
    101,
    81,
    109,
    104,
]

# univariant time series data (one varabile over time)
# typically, x (or time) is independent and
# y is dependent on x (e.g. temperature vs hour of day)
x_times = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
y_temps = [2, 5, 8, 20, 21, 23, 24, 27, 30, 31, 31,32]

# Descriptive: Averages and measures of central tendency

mean = statistics.mean(heart_rate)
median = statistics.median(heart_rate)
mode = statistics.mode(heart_rate)
# Sharing results
print()
print(f'We are presented with the univariant data set heart_rate which contains data in BPM as follows: {heart_rate}')
print()
print('Below are measures of the average and central tendency for the data set')
print(f'The average is {mean} BPM, the median is {median} BPM, and the mode is {mode} BPM')
print()
if mean or median or mode > 100:
    print('That is an elevated resting heart rate!')
print()

# Descriptive: Measures of spread
print('Listed below are measures of how spread out the data is:')
var = statistics.variance(heart_rate)
stdev = statistics.stdev(heart_rate)
lowest = min(heart_rate)
highest = max(heart_rate)
print()
print(f'Variance: {var:.2f}')
print(f'Standard deviation: {stdev:.2f}')
print(f'Lowest heart rate: {lowest} BPM ')
print(f'Highest heart rate: {highest} BPM')
print()

# Descriptive: Univariant Timeseries Data.........................

# describe relationships
# univariant time series data (one varabile over time)
# x is time spent exercising daily
# y is resting heart rate
xexercise = [65, 45, 45, 50, 10, 0, 0, 15, 25, 60, 50, 65]
yheart_rate = [62, 85, 80, 71, 95, 101, 90, 88, 52, 75, 72, 68]
print()
xx_corr = statistics.correlation(xexercise, xexercise)
xy_corr = statistics.correlation(xexercise, yheart_rate)
print()
slope, intercept = statistics.linear_regression(xexercise, yheart_rate)

# Choose an x value off in the future (future x)
future_exercise = 100

# Extend the line out into the unknown future
# and read the value (of future y)
future_heart_rate = round(slope * future_exercise + intercept)
# share what we learned
print("=============================================================")
print()
print("Below is the data and results used for our statistical analysis:")
print()
print(f"xexercise:{xexercise}")
print()
print(f"yheart_rate:{yheart_rate}")
print()
print(f"The correlation between exercise and exercise = {xx_corr:.2f}")
print(f"The correlation between exercise and heart rate = { xy_corr:.2f}")
print()
print(f'The slope is: {slope:.2f}')
print(f'The intercept is: {intercept:.2f}')
print()
print(f'Below is the result of inputting the future exercise time of 100min and having our model predict the future heart rate for that value')
print(f'For the value {future_exercise} min of exercise, the predicted heartrate is {future_heart_rate} BPM')





