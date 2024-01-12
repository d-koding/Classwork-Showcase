"""
    CS051P Lab Assignments: Final Project

    Authors: Dylan O'Connor and Adrian Clement

    Date:   November 30th, 2022

    The goal of this assignment is to visualize the correlation between song popularity
    and a series of factors, being length, key, and genre
"""
import csv
from statistics import mean
import matplotlib.pyplot as plt


def parse_song_length(fname):
    """
    Makes a list of song lengths in ms
    :param fname: (file) csv file
    :return: (list) a list of song lengths
    """
    # opens file and reads it
    file1 = open(fname, "r")
    reading = csv.reader(file1)
    next(reading)

    # takes all song length info
    song_length_list = []
    for line in file1:
        count = 0
        duration = ""
        for i in range(len(line)):
            if line[i] == "," and line[i + 1] != " ":
                count += 1
            if count == 2 and line[i] != ",":
                duration += line[i]
        song_length_list.append(int(duration))

    # returns final list
    return song_length_list


def sort_lengths(list):
    """

    :param list:
    :return:
    """

    length_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for length in list:
        category = int(length) // 30000
        length_list[category - 1] += 1

    return length_list


def parse_genre(fname):
    """

    :param fname:
    :return:
    """
    file1 = open(fname, "r")
    reading = csv.reader(file1)
    next(reading)

    # takes all genre info
    genre_list = []
    for line in file1:
        genre_list.append(line[17])

    return genre_list


def song_length_analysis(song_length):
    """
    Takes a song dataset and returns a dictionary with the dates as keys and lengths as values
    :param fname: (str) a file name
    :return: (dict) a dictionary organized by dates and lengths
    """
    file1 = open(fname, "r")
    reading = csv.reader(file1)
    next(reading)

    dict1 = {}

    for line in reading:
        if int(line[2]) > 180000:
            dict1[line[4]] = ">3 minutes"

        if 120000 <= int(line[2]) <= 180000:
            dict1[line[4]] = ">2 minutes"

        if 60000 <= int(line[2]) < 120000:
            dict1[line[4]] = ">1 minute"

        if int(line[2]) < 60000:
            dict1[line[4]] = "<1 minute"


def length_year_analysis(fname, song_length):
    """

    :param song_length:
    :param year:
    :return:
    """
    file1 = open(fname, "r")
    reading = csv.reader(file1)
    next(reading)

    year_length_dict = {}
    for line in fname:  # creates new year key
        if line[4] not in year_length_dict:
                key = line[4]
                year_length_dict.setdefault(key, []).append(line[2])
        else:  # adds onto existing year key
                key = line[4]
                year_length_dict.setdefault(key, []).extend(line[2])

    # calculates average song length for corresponding year, and substitutes that value for each key
    for key in year_length_dict.keys():
        avg_length = mean(year_length_dict[key])
        year_length_dict[key] = avg_length

    return year_length_dict


def length_genre_analysis(length_info, genre_info):
    """

    :param length_info:
    :param genre_info:
    :return:
    """

    # creates dict with genre keys and list values of song lengths for the corresponding genre
    genre_length_dict = {}
    for elem in genre_info:
        for i in range(len(elem)):  # takes length of each individual list inside of genre_info_list
            if genre_info[i] == "set()":  # addresses bug in csv file
                if "other" not in genre_length_dict:  # creates new dict key
                    key = "other"
                    genre_length_dict.setdefault(key, []).append(length_info[elem[i]])
                else:  # adds onto existing dict key
                    key = "other"
                    genre_length_dict.setdefault(key, []).extend(length_info[elem[i]])
            elif genre_info[elem[i]] not in genre_length_dict:  # creates new dict key for non-bugged
                key = genre_info[elem[i]]
                genre_length_dict.setdefault(key, []).append(length_info[elem[i]])
            else:  # adds onto existing dict key for non-bugged
                key = genre_info[elem[i]]
                genre_length_dict.setdefault(key, []).extend(length_info[elem[i]])

    # calculates average song length for corresponding genre, and substitutes that value for each key
    for key in genre_length_dict.keys():
        avg_length = mean(genre_length_dict[key])
        genre_length_dict[key] = avg_length

    return genre_length_dict


def synthesize_data(dict):
    """
    Synthesizes dictionary into a list of lists
    :param dict: (dict) a dictionary
    :return: (list) a list of lists
    """
    new_list = []

    # takes each individual
    for key in dict.keys():
        entry = []
        entry.append(key)
        entry.append(dict[key])
        new_list.append(entry)

    return new_list


def plot_bar(data1, data2, labelx, labely):
    """
    Plots a dataset on a graph
    :param data1: (list) list used for x-axis
    :param data2: (list) list used for y-axis
    :param format: (str) specified format of graph
    :param name: (str) name of graph line
    """
    # establishes x and y axis
    x = data1
    y = data2

    # for each dataset, append to x and y
    for elem in data1:
        x.append(elem)
    for elem in data2:
        y.append(elem)

    # plots the x and y lists
    plt.bar(x, y)

    # plots legend, labels, titles, shows plot
    plt.legend()
    plt.xlabel(labelx)
    plt.ylabel(labely)
    plt.title("Song Length vs. Number of Songs")
    plt.show()


def main():
    """
    Creates 3 graphs representing...
    """
    song_lengths = parse_song_length("songs_normalize.csv")
    list_length = sort_lengths(song_lengths)

    # second intervals
    time_list = []
    time = 0
    for times in range(17):
        time_list.append(str(time) + "-" + str(time + 30) + " seconds")
        time += 30

    plot_bar(list_length, song_lengths, time_list, "times")


if __name__ == '__main__':
    main()
