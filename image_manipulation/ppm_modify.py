"""
    CS051P Lab Assignments: PPM Image Modifier

    Name: Dylan O'Connor

    Date: October 19th, 2022

    The goal of this assignment is to give you practice working with lists
    by writing a program that manipulates image files in various ways.
"""
from math import sqrt


def decode(in_filename, out_filename):
    """
    Takes an input ppm file and creates a new ppm file that contains the same header, with all elements
    in the body converted to 0, 153, or 255 depending on the remainder of each element
    :param in_filename: a ppm file containing an image
    :param out_filename: a blank ppm file
    :return: the converted ppm file
    """
    # initializes variable to open input file and read it
    reading = open(in_filename, "r")

    # initializes variable to open output file and write on it
    writing = open(out_filename, "w")

    # initializes a variable to keep track of lines
    count = 0

    # for loop that splits each line of file into lists or a header
    for line in reading:

        # if statement to separate header and body
        if count > 2:

            # splits given line into a list
            num_list = line.split()

            # variable to keep track of written string
            final_str = ""

            # for loop that adds 0, 153, or 255 (based on elem remainder) to string to then be written in final file
            for elem in num_list:
                if int(elem) % 3 == 0:
                    final_str = final_str + "0 "
                if int(elem) % 3 == 1:
                    final_str = final_str + "153 "
                if int(elem) % 3 == 2:
                    final_str = final_str + "255 "

            # writes converted line into new file
            writing.write(final_str + "\n")

        # else statement to separate header from body
        else:

            # checks if first line, copies line in input file to output file
            if count == 0:
                writing.write(line)

            # checks if second line, copies line in input file to output file
            if count == 1:
                writing.write(line)

            # checks if third line, copies line in input file to output file
            if count == 2:
                writing.write(line)

            # keeps track of line count
            count = count + 1

    # closes files
    writing.close()
    reading.close()

    # returns the final header + body ppm file
    return writing


def main_part1():
    """
    Takes an input ppm file that contains an image and creates a new ppm file with simplified RGB values
    """
    # runs decode function to decode file and create new one
    decode("part1.ppm", "new.ppm")

    pass


def negate(line):
    """
    Negates a string of values between 0 and 255
    :param line: (str) a string of values that are between 0 and 255
    :return: (str) a string of negated values
    """
    # splits given string into a list
    num_list = line.split()

    # initializes a variable to represent an empty list
    result = []

    # for loop that takes each integer in list and makes a new list of their negated values
    for elem in num_list:
        new_elem = 255 - int(elem)
        result.append(str(new_elem))

    # returns a string the represents the new list
    return " ".join(result)


def grey_scale(line):
    """
    Takes a string that contains values between 0 and 255 and converts them to greyscale values
    :param line: (str) a string that contains values between 0 and 255
    :return: (str) a string that contains a list of grey-scaled values between 0 and 255
    """
    # splits string into a list
    num_list = line.split()

    # initializes a variable to represent an empty list
    result = []

    # for loop that goes through every third element in list
    for i in range(0, len(num_list), 3):

        # checks if num_list can be indexed
        if len(num_list) * 3 + 1 > i:

            # initializes three variables to represent the values of the element and the two sequential elements
            r, g, b = int(num_list[i]), int(num_list[i + 1]), int(num_list[i + 2])

            # calculates the grey scale value of the pixel based on its RGB values
            grey = int(sqrt(r ** 2 + g ** 2 + b ** 2))

            # if statement to keep grey scale value below or equal to 255
            if grey > 255:
                grey = '255'
            else:
                grey = str(grey)

            # makes new list of grey scaled values, 1 for each r, g, b, value replaced
            result.append(grey)
            result.append(grey)
            result.append(grey)

    # returns a string that represents the final list
    return " ".join(result)


def row_scaler(rows, scale):
    """
    Takes a list of lists and returns a scaled list of lists
    :param rows: (list) a list of lists containing integers
    :param scale: (int) an integer of any value
    :return: (list) a modified list of lists
    """
    # initializes an empty list
    result = []

    # if statement to check for 0 being entered, and returns nothing
    if scale == 0:
        return result

    # if statement to check if the scaling factor is greater than the number of lists, does not modify lists
    if scale >= len(rows):
        return rows

    # for loop to create a new list of scaled rows
    for row in range(0, len(rows)):

        # if statement that checks that row number is evenly divisible by scaling factor, then adds to new list
        if row % scale == 0:
            result.append(rows[row])

    # returns the new list of rows
    return result


def col_scaler(rows, scale):
    """
    Takes a list of lists and scales each list within the list based on a scaling factor
    :param rows: (list) a list of lists of rgb values
    :param scale: (int) a scaling factor
    :return: (list) a new list of altered lists
    """
    # initializes a variable to represent an empty list of rows
    new_rows = []

    # if statement to account for 0 being entered, returns nothing
    if scale == 0:
        return new_rows

    # if statement to account for scaling factor being larger than number triplets in one row
    if scale >= (len(rows[0]) / 3):
        return rows

    # for loop that runs through each list within the row list
    for row in rows:

        # initializes variable to count number of groups of three in list
        count = 0

        # initializes variable to represent an empty list
        new_row = []

        # for loop that runs on every third element in list
        for i in range(0, len(row), 3):

            # if statement that runs when indexed element is evenly divisible by scaling factor and within range
            if count % scale == 0 and count * 3 < len(row) - 3:

                # appends element as well as the next two to a new list
                new_row.append(row[i])
                new_row.append(row[i + 1])
                new_row.append(row[i + 2])

            # updates every third element count
            count += 1

        # appends newly created list to list of rows
        new_rows.append(new_row)

    # returns the new list of rows
    return new_rows


def scale(image, row_scale, col_scale):
    """
    Takes an image body (a list of lists) and two scaling factors and returns a scaled list of lists
    :param image: (list) a list of lists of rgb values
    :param row_scale: (int) a scaling factor for image height
    :param col_scale: (int) a scaling factor for image width
    :return: (list) a scaled list of lists
    """
    # initializes variable to represent the list of lists created by running the function row_scaler on image
    row_list = row_scaler(image, row_scale)

    # initializes variable to represent the list of lists created by running the function col_scaler on row_list
    new_image = col_scaler(row_list, col_scale)

    # returns the new image based on the list of lists that new_image represents
    return new_image


def file_reader(in_file):
    """
    Reads a ppm file and returns a list of lists based off of file
    :param in_file: (file) a ppm file
    :return: (list) a list of lists based on ppm file body
    """
    # initializes a variable to read file
    reading = open(in_file, "r")

    # initializes a variable to represent beginning of ppm header
    type_ppm = reading.readline()

    # initializes variables to represent dimensions of ppm header
    w, h = reading.readline().split()

    # initializes variable to represent end of ppm header
    max_val = reading.readline()

    # converts type of height and width of ppm dimensions to integers
    w = int(w)
    h = int(h)

    # initializes variables that represent empty lists
    image_body = []
    formatted_rows = []
    new_row = []

    # for loop that splits each line into a list and consolidates them to one list
    for line in reading:
        image_body += line.split()

    # calculates proper number of rows based on width
    row_count = 3 * w

    # asserts that first value of list is being entered
    first = True

    # for loop that creates an index for all rgb values in ppm file
    for num in range(3 * (h + 1) * w):

        # if statement that activates when num is evenly divisible by the proper number of rows based on width
        if num % row_count == 0:

            # if statement that checks if new list is empty
            if len(new_row) != 0:

                # appends a newly created list that is row_count length to the final row list
                formatted_rows.append(new_row)

                # asserts that first value of list will be entered next
                first = True

                # empties list
                new_row = []

            # checks if first value of list is being entered and if num can be indexed
            if first and num < 3 * h * w:
                new_row.append(image_body[num])
                first = False

        # creates a new list by appending values from image_body list only if num can be indexed
        elif num < 3 * h * w:
            new_row.append(image_body[num])

    # closes file
    reading.close()

    # returns the newly formatted list of lists
    return formatted_rows


def file_writer(list_lists, out_file):
    """
    Writes onto a file in ppm format based on a list of lists
    :param list_lists: (list) a list of lists that represents an image body
    :param out_file: (file) an empty file to write in
    """
    # initializes a variable to open file and write in it
    writing = open(out_file, "w")

    # writes P3 on top of new file
    writing.write("P3\n")

    # writes dimensions of file based on length and number of lists in list of lists
    writing.write(str(len(list_lists[0]) // 3))
    writing.write(" ")
    writing.write(str(len(list_lists)))

    # writes 255 below dimensions in file
    writing.write("\n")
    writing.write("255")
    writing.write("\n")

    # for loop that turns each row in list of lists into a string
    for row in list_lists:
        writing.write(" ".join(row) + "\n")

    # closes file
    writing.close()


def main():
    """
    1. Ask the user for an input file.
    2. Ask the user for an output file.
    3. List the possible image manipulation functions and ask the user to
       choose one of them. If they don't enter a valid choice, ask them again.
    4. Perform the requested manipulation on the input file and write the
       result to the output file in ppm format (don't forget to write out
       the header information!).
    """
    # initializes variables that ask for files to read and write in
    in_file = input("Please enter an input file\n")
    out_file = input("Please enter an output file\n")

    # initializes variables to read and write in files
    reading = open(in_file, "r")
    writing = open(out_file, "w")

    # prints possible image manipulation functions
    print("Possible image manipulation functions:\n Negate \n Greyscale \n Scale")

    # initializes valid inputs for choice
    choices = (1, 2, 3)

    # initializes a variable to represent the user's function choice
    choice = 0

    # while loop that continues until a valid choice has been selected
    while choice not in choices:

        # asks user to enter a 1, 2 or 3
        choice = int(input("Please choose a manipulation function, 1, 2 or 3\n"))

        # if statement that runs a print statement when an invalid choice is inputted
        if choice not in choices:
            print("Please enter a valid number")

    # if statement that runs when choice = 1
    if choice == 1:

        # initializes a variable to count number of lines
        lin_count = 0

        # for loop that goes through each line in file
        for line in reading:

            # adds 1 to count for each line in file
            lin_count += 1

            # if statement that runs when line count is below or equal to 3
            if lin_count <= 3:

                # copies first 3 lines onto file
                writing.write(line)

        # initializes an empty list
        new_list = []

        # for loop that indexes list of lists received from file_reader function
        for i in file_reader(in_file):

            # negates each list in list of lists and creates new list from it
            new_list.append(negate(" ".join(i)))

        # for each list in new_list, writes a line in file
        for string in new_list:
            writing.write(string + "\n")

    # if statement that runs when choice = 2
    if choice == 2:

        # initializes a variable to count number of lines
        lin_count = 0

        # for loop that goes through each line in file
        for line in reading:

            # adds 1 to count for each line in file
            lin_count += 1

            # if statement that runs when line count is below or equal to 3
            if lin_count <= 3:

                # copies first 3 lines onto file
                writing.write(line)

        # initializes an empty list
        new_list = []

        # for loop that indexes list of lists received from file_reader function
        for i in file_reader(in_file):

            # converts each list in list of lists to greyscale and creates new list from it
            new_list.append(grey_scale(" ".join(i)))

        # for each list in new_list, writes a line in file
        for string in new_list:
            writing.write(string + "\n")

    # if statement that checks if choice = 3
    if choice == 3:

        # initializes variables that represent inputted scaling factors
        height = int(input("Please enter a height scaling factor\n"))
        width = int(input("Please enter a width scaling factor\n"))

        # writes a ppm file based on file_writer function, list of lists from file_reader, and scaling factors
        file_writer(scale(file_reader(in_file), height, width), out_file)

    # closes files
    reading.close()
    writing.close()


if __name__ == '__main__':
    # main_part1()  # comment this out after you check in for part 1
    main()  # uncomment this after you check in for part 1
