# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 20:33:21 2023

@author: Shravani
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def plot_approve_votes(data, x_col, y_col, label_col):
    """
    This function plots the approve votes against the date and labels them according to the subject column.

    Args:
    data (DataFrame): The input DataFrame containing the data.
    x_col (str): The name of the column containing the x-axis values (date).
    y_col (str): The name of the column containing the y-axis values (approve adjusted votes).
    label_col (str): The name of the column containing the labels (subject).

    Returns:
    None
    """
    # Group the data by the label column
    grouped_data = data.groupby(label_col)
    plt.figure(figsize=(20,20))

    # Plot each group separately
    for label, group in grouped_data:
        
        plt.plot(group[x_col], group[y_col], label=label)
    # Add labels and legend
    
    plt.xlabel(x_col)
    plt.ylabel("Approved Votes ")
    plt.title('Approve Votes vs Date for each Party')
    plt.legend()

    # Show the plot
    plt.savefig("F1.png")

# Read the data from a CSV file
data = pd.read_csv('covid_approval_polls.csv')
data['Date'] = pd.to_datetime(data['end_date'])
# Call the function to plot the data
#plot_approve_votes(data, 'date', 'approve adjusted votes', 'subject')
plot_approve_votes(data, 'Date', 'approve', 'party')


def plot_sponsor_pie_chart(df, figsize=(10, 10), fontsize=14):
    """
    Plots a pie chart of the vote counts for each sponsor in the given DataFrame.

    Parameters:
    df (pandas.DataFrame): The input DataFrame with columns "sponsor" and "vote_counts".
    figsize (tuple, optional): The size of the plot in inches (width, height). Default is (8, 8).
    fontsize (int, optional): The font size of the labels. Default is 14.

    Returns:
    None.
    """
    # Group the data by sponsor and calculate the total vote counts
    data = df.groupby('subject')['sample_size'].sum()

    # Create a pie chart of the vote counts for each sponsor
    fig, ax = plt.subplots(figsize=figsize)
    ax.pie(data, labels=data.index, autopct='%1.1f%%', startangle=90, textprops={'fontsize': fontsize})
    ax.axis('equal')

    # Set the title
    ax.set_title('Sample Size total by Subject  ', fontsize=fontsize+2)

    # Show the plot
    plt.savefig("F2.png")

plot_sponsor_pie_chart(data)

def plot_top_disapproval_sponsors(df, figsize=(30, 30), fontsize=12):
    """
    Plots a bar chart of the top 10 sponsors with the highest average disapproval ratings in the given DataFrame.

    Parameters:
    df (pandas.DataFrame): The input DataFrame with columns "sponsor" and "disapproval_percent".
    figsize (tuple, optional): The size of the plot in inches (width, height). Default is (8, 6).
    fontsize (int, optional): The font size of the labels. Default is 12.

    Returns:
    None.
    """
    # Group the data by sponsor and calculate the average disapproval rating
    data = df.groupby('sponsor')['disapprove'].mean().sort_values(ascending=False)[:10]

    # Define a list of colors for the bars
    colors = plt.cm.tab10(np.arange(len(data)))

    # Create a bar chart of the top 10 sponsors with the highest average disapproval ratings
    fig, ax = plt.subplots(figsize=figsize)
    ax.bar(data.index, data.values, color=colors)

    # Set the title and axis labels
    ax.set_title('Top 10 Sponsors with Highest Average Disapproval Ratings', fontsize=fontsize+2)
    ax.set_xlabel('Sponsor', fontsize=fontsize)
    ax.set_ylabel('Average Disapproval Rating', fontsize=fontsize)

    # Set the font size of the axis tick labels
    ax.tick_params(axis='both', which='major', labelsize=fontsize)

    # Show the plot
    plt.savefig("F3.png")



plot_top_disapproval_sponsors(data)