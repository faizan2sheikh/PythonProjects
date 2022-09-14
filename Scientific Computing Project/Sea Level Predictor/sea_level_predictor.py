import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(12,6))
    sns.scatterplot(x=df['Year'],y=df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    fit = linregress(y=df['CSIRO Adjusted Sea Level'], x=df['Year'])
    fig, ax = plt.subplots(figsize=(12,6))
    plt.scatter(x=df['Year'],y=df['CSIRO Adjusted Sea Level'])
    x_p1 = pd.Series([i for i in range(1880,2051)])
    y_p1 = (fit.slope*x_p1) + fit.intercept
    plt.plot(x_p1,y_p1, color='g')
  
    # Create second line of best fit
    mod_data = df[df['Year']>=2000]
    new_fit = linregress(y=mod_data['CSIRO Adjusted Sea Level'], x=mod_data['Year'])
    x_p2 = pd.Series([j for j in range(2000,2051)])
    y_p2 = (new_fit.slope*x_p2) + new_fit.intercept
    plt.plot(x_p2,y_p2, color='r')

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()