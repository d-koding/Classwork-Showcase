"""
    CS051P Lab Assignments: PPM Image Tester

    Name: Dylan O'Connor

    Date: October 19th, 2022

    Test blackbox cases for image manipulation code
"""

from ppm_modify import *

def main():
    # test negate
    print("*** testing negate ***")
    assert type(negate("255 0 79")) == str  # check type is str
    assert negate("255 0 255 0 0 0 255 0 255") == "0 255 0 255 255 255 0 255 0"  # check negate works on min max values
    assert negate("   120 10 1 203 30 34 68 38 23 12") == "135 245 254 52 225 221 187 217 232 243"  # check negate works
    # on random values between 0 and 255
    assert negate("1 2  3  255 245   254 1 3 1") == "254 253 252 0 10 1 254 252 254"  # check negate works on values
    assert negate("245   243 234  245      231 231") == "10 12 21 10 24 24"  # check negate works on all large values
    assert negate("   2 3     4  2    ") == "253 252 251 253"  # check negate works on all small values and spaces
    assert negate("232") == "23"  # check negate works on one value
    print("negate passed")

    # test grey_scale
    print("*** testing grey_scale ***")
    assert type(grey_scale("1 2 3 255 4 6")) == str  # assert correct type
    assert grey_scale("1    3 2      239 23 12   ") == "3 3 3 240 240 240"  # check correct grey scale conversion
    assert grey_scale("90     12  12 255 23 1      12 2 2      ") == "91 91 91 255 255 255 12 12 12"  # check again
    assert grey_scale("255    245 245 234  255 255") == "255 255 255 255 255 255"  # check large values
    assert grey_scale("   1 2 1   1   4 5  5  3 2") == "2 2 2 6 6 6 6 6 6"  # check small values
    print("grey_scale passed")

    # test scale
    print("*** testing scale ***")
    assert type(scale([[1, 2, 6, 1, 255, 90, 98, 34, 12], [6, 45, 23, 12, 12, 244, 76, 34, 76]], 1, 3)) == list
    # check correct type
    assert scale([[1, 2, 6, 1, 255, 90, 98, 34, 12], [6, 45, 23, 12, 12, 244, 76, 34, 76]], 1, 3) == [[1, 2, 6, 1, 255, 90, 98, 34, 12], [6, 45, 23, 12, 12, 244, 76, 34, 76]]
    # check scale properly scales large lists
    assert scale([[1, 2, 3], [90, 65, 12]], 2, 2) == [[1, 2, 3], [90, 65, 12]]  # check scale scales small lists
    assert scale([[36, 1, 34, 67, 43, 100, 13, 56, 23], [76, 43, 12, 98, 45, 23, 100, 189, 23]], 3, 2) == [[36, 1, 34], [76, 43, 12]]
    # check scale on odd height even width
    assert scale([[6, 1, 244, 1, 43, 23, 1, 6, 23], [100, 43, 122, 9, 5, 233, 100, 18, 23]], 2, 3) == [[6, 1, 244, 1, 43, 23, 1, 6, 23], [100, 43, 122, 9, 5, 233, 100, 18, 23]]
    # check scale on even height odd width
    assert scale([[69, 20, 241, 1, 43, 32, 17, 63, 23], [103, 134, 1, 97, 5, 23, 90, 15, 231]], 3, 1) == [[69, 20, 241, 1, 43, 32], [103, 134, 1, 97, 5, 23]]
    # check scale on double odd
    assert scale([[69, 20, 241, 1, 43, 32, 17, 63, 23], [103, 134, 1, 97, 5, 23, 90, 15, 231], [1, 2, 4, 5, 2, 3, 4, 5, 6]], 3, 3) == [[69, 20, 241, 1, 43, 32], [103, 134, 1, 97, 5, 23]]
    # check scale on double odd again
    print("scale passed")


if __name__ == "__main__":
    main()
