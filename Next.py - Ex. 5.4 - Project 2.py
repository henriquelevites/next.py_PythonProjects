class IDNotInteger(Exception):
    """
    A class used to represent custom exception in case ID number is not integer
    """

    def __init__(self, id_number):
        """Sets the initial value for the attribute of ID number
        :param id_number: citizen's ID number
        :type id_number: int
        :return: None
        """
        self._id_number = id_number

    def __str__(self):
        """ Overriding the __str__ method in BaseException.
            When the exception is thrown, the string returned from this method is printed to the screen.
        :return: custom exception message
        :rtype: string
        """
        return "'" + str(self._id_number) + "' is not an integer number" + "\n"


class IDTooShort(Exception):
    """
    A class used to represent custom exception in case ID number has less than 9 digits.
    """

    def __init__(self, id_number):
        """Sets the initial value for the attribute of ID number
        :param id_number: citizen's ID number
        :type id_number: int
        :return: None
        """
        self._id_number = id_number

    def __str__(self):
        """ Overriding the __str__ method in BaseException.
            When the exception is thrown, the string returned from this method is printed to the screen.
        :return: custom exception message
        :rtype: string
        """
        return "ID '" + str(int(self._id_number)) + "' has less than 9 digits" + "\n"


class IDTooLong(Exception):
    """
    A class used to represent custom exception in case ID number has more than 9 digits.
    """

    def __init__(self, id_number):
        """Sets the initial value for the attribute of ID number
        :param id_number: citizen's ID number
        :type id_number: int
        :return: None
        """
        self._id_number = id_number

    def __str__(self):
        """ Overriding the __str__ method in BaseException.
            When the exception is thrown, the string returned from this method is printed to the screen.
        :return: custom exception message
        :rtype: string
        """
        return "ID '" + str(int(self._id_number)) + "' has more than 9 digits" + "\n"


class NumberOfValidIDsToPrintNotInteger(Exception):
    """
    A class used to represent custom exception in case the number of valid IDs numbers to print is not integer
    """

    def __init__(self, number_of_next_valid_ids):
        """Sets the initial value for the attribute of number of valid ID numbers to print
        :param number_of_next_valid_ids: valid ID number
        :type number_of_next_valid_ids: int
        :return: None
        """
        self._number_of_next_valid_ids = number_of_next_valid_ids

    def __str__(self):
        """ Overriding the __str__ method in BaseException.
            When the exception is thrown, the string returned from this method is printed to the screen.
        :return: custom exception message
        :rtype: string
        """
        return "'" + str(self._number_of_next_valid_ids) + "' is not an integer number" + "\n"


class NumberOfValidIDsToPrintTooLong(Exception):
    """
    A class used to represent custom exception in case the number of valid IDs numbers to print has more than 9 digits.
    """

    def __init__(self, number_of_next_valid_ids):
        """Sets the initial value for the attribute of number of valid ID numbers to print
        :param number_of_next_valid_ids: valid ID number
        :type number_of_next_valid_ids: int
        :return: None
        """
        self._number_of_next_valid_ids = number_of_next_valid_ids

    def __str__(self):
        """ Overriding the __str__ method in BaseException.
            When the exception is thrown, the string returned from this method is printed to the screen.
        :return: custom exception message
        :rtype: string
        """
        return "Number of valid IDs to print '" + str(int(self._number_of_next_valid_ids)) + "' is too long" + "\n"


class NumberOfValidIDsToPrintZero(Exception):
    """
    A class used to represent custom exception in case the number of valid IDs numbers to print has more than 9 digits.
    """

    def __init__(self, number_of_next_valid_ids):
        """Sets the initial value for the attribute of number of valid ID numbers to print
        :param number_of_next_valid_ids: valid ID number
        :type number_of_next_valid_ids: int
        :return: None
        """
        self._number_of_next_valid_ids = number_of_next_valid_ids

    def __str__(self):
        """ Overriding the __str__ method in BaseException.
            When the exception is thrown, the string returned from this method is printed to the screen.
        :return: custom exception message
        :rtype: string
        """
        return "No valid IDs to print." + "\n"


def check_id_valid(id_number):
    """Checks the validity of ID number
    :param id_number: citizen's ID number
    :type: int
    :return: True if ID number is valid, otherwise False
    :rtype: boolean
    """
    id_number_digits_list = list(map(int, str(id_number)))
    id_number_digits_list[1::2] = map(lambda x: x * 2, id_number_digits_list[1::2])
    id_number_digits_list = map(lambda x: (x % 10 + x // 10), id_number_digits_list)
    sum_to_check_validity = sum(id_number_digits_list)
    if sum_to_check_validity % 10 == 0:
        return True
    else:
        return False


class IDIterator:
    """
    A class used to represent iterator.
    """
    def __init__(self, id_number):
        """Sets the initial value for the attribute of ID number
        :param id_number: citizen's ID number
        :type id_number: int
        :return: None
        """
        self._id = id_number - 1

    def __iter__(self):
        """Used to return the iterator instance
        :return: None
        """
        return self

    def __next__(self):
        """Check if the given id number is valid (by calling the function
            check_id_valid),if so return the given id number,else increase
            the id number by one and check again and so on until find
            valid id.
        :return: valid id number.
        :rtype: int
        """
        self._id += 1

        while not check_id_valid(self._id):
            self._id += 1
            if self._id > 999999999:
                raise StopIteration()

        return self._id


def id_generator(id_number):
    """Checks if the given id number is valid (by calling the function
    check_id_valid),if so return the given id number,else increase
    the id number by one and check again and so on until he finds
    valid id.
    :param: citizen's ID number
    :type: int
    :return: valid id number.
    :rtype: int
    """
    for id_gen in range(id_number, 999999999):

        if not check_id_valid(id_gen):
            id_gen += 1

        else:
            yield id_gen


def main():
    """Main program function.
    """
    while True:
        try:
            id_number = input("Please enter ID number (9 digits integer number): ")

            if not str(id_number).isdigit():
                raise IDNotInteger(id_number)

            if len(str(int(id_number))) < 9:
                raise IDTooShort(id_number)

            if len(str(int(id_number))) > 9:
                raise IDTooLong(id_number)

            number_of_next_valid_ids = input("Please enter the number of next valid IDs to print (integer number): ")

            if not str(number_of_next_valid_ids).isdigit():
                raise NumberOfValidIDsToPrintNotInteger(number_of_next_valid_ids)

            if len(str(int(number_of_next_valid_ids))) > 9:
                raise NumberOfValidIDsToPrintTooLong(number_of_next_valid_ids)

            if int(number_of_next_valid_ids) == 0:
                raise NumberOfValidIDsToPrintZero(number_of_next_valid_ids)

        except IDNotInteger as e:
            print(e)

        except IDTooShort as e:
            print(e)

        except IDTooLong as e:
            print(e)

        except NumberOfValidIDsToPrintNotInteger as e:
            print(e)

        except NumberOfValidIDsToPrintTooLong as e:
            print(e)

        except NumberOfValidIDsToPrintZero as e:
            print(e)

        else:
            id_number = int(id_number)

            number_of_next_valid_ids = int(number_of_next_valid_ids)

            my_identity = iter(IDIterator(id_number))    # Create an iterator from class IDIterator

            print("\n", "Next %d valid IDs generated by ITERATOR CLASS (max checked ID = 999999999):" % number_of_next_valid_ids)

            count_valid_ids = 0

            for id_iter in my_identity:

                print(id_iter)
                count_valid_ids += 1

                if count_valid_ids == number_of_next_valid_ids:
                    break

            my_id_gen = id_generator(id_number)    # Create a generator from generator function id_generator

            print("\n", "Next %d valid IDs generated by GENERATOR FUNCTION (max checked ID = 999999999):" % number_of_next_valid_ids)

            count_valid_ids = 0

            for id_gen in my_id_gen:

                print(id_gen)
                count_valid_ids += 1
                if count_valid_ids == number_of_next_valid_ids:
                    break
            break


if __name__ == '__main__':
    main()