import unittest


# Class implements the functions of a calculus with storage
class Calculus:
    # Name of the file, where the __calculation_results should be stored in and where they should be refound
    CALCULUS_STORAGE_FILE_NAME = "calculus_output.txt"
    # A list of all calculation results that the calculator had calculated
    __calculation_results = []

    # defines the getter for __calculation_results  !!!ATTENTION Read more about @property in python!!!
    @property
    def calculation_results(self):
        """I'm the 'calculation_results' property."""
        print("getter of calculation_results called")
        return self.__calculation_results

    # def __init__(self):
    #    self.__calculation_results = self.restore_calculation_results()

    # ______________________ methods for calculation ______________________

    # Adds to values and append it on __calculation_results
    def add(self, x, y):
        self.__calculation_results.append(x + y)
        return x + y

    def sub(self, x, y):
        self.__calculation_results.append(x - y)
        return x - y

    def div(self, x, y):
        if y != 0:
            self.__calculation_results.append(x / y)
            return x / y
        else:
            # division by 0
            return "division by zero is not defined"

    def mul(self, x, y):
        self.__calculation_results.append(x * y)
        return x * y

    def mod(self, x, y):
        self.__calculation_results.append(x % y)
        return x % y

    # saves the calculation_results as a string in an output text file
    # TODO Restore calculation results and then store them | so storage of multiple sessions is possible
    def save_calculation_results_in_file(self):
        TextFileStorage.write_string_in_file(
            MyConverter.convert_list_of_numbers_into_string(self.__calculation_results),
            self.CALCULUS_STORAGE_FILE_NAME)

    # restore the calculation_results
    def restore_calculation_results(self):
        context_of_text_file = TextFileStorage.read_lines_from_text_file(self.CALCULUS_STORAGE_FILE_NAME)
        if context_of_text_file is not None:
            list_of_string_values_of_calculation_results = MyConverter.replace_an_array_of_characters_from_a_string(
                context_of_text_file[0].rstrip('\n'), ['[', ',', ']']).split()
            return MyConverter.convert_list_with_strings_into_list_with_numbers(
                list_of_string_values_of_calculation_results)
        else:
            return []


class MyConverter:
    # converts a list of numbers into a string
    @staticmethod
    def convert_list_of_numbers_into_string(list_of_numbers):
        result_string = ""
        for number in list_of_numbers:
            if number == list_of_numbers[0]:
                result_string += ("[" + str(number) + ", ")
            elif number == list_of_numbers[len(list_of_numbers) - 1]:
                result_string += (str(number) + "]")
            else:
                result_string += (str(number) + ", ")
        return result_string

    # replaces all characters in a string that are given in an array
    # so at the end there will be no character intersection between the string and the array
    @staticmethod
    def replace_an_array_of_characters_from_a_string(string_to_replace_characters="", array_with_characters=['']):
        if string_to_replace_characters != "" and array_with_characters != ['']:
            for char in array_with_characters:
                string_to_replace_characters = string_to_replace_characters.replace(char, '')
        return string_to_replace_characters

    # converts a list of strings into either int or float values and returns the result list
    @staticmethod
    def convert_list_with_strings_into_list_with_numbers(list_with_strings=[""]):
        list_with_numbers = []
        for string in list_with_strings:
            if '.' in string:
                list_with_numbers.append(float(string))
            elif '-' in string:
                list_with_numbers.append((2 * int(string)) - int(string))
            else:
                list_with_numbers.append(int(string))
        return list_with_numbers


class TextFileStorage:
    # writes a string in a text file
    @staticmethod
    def write_string_in_file(string, file_name):
        with open(file_name, "w") as text_file:
            print("{}".format(string), file=text_file)

    # read the lines of a text file
    @staticmethod
    def read_lines_from_text_file(file_name):
        try:
            with open(file_name) as text_file:
                return text_file.readlines()
        except FileNotFoundError:
            return None


# TestClass of MyConverter
class TestMyConverter(unittest.TestCase):
    def test_convert_list_of_numbers_into_string(self):
        self.assertEqual(MyConverter.convert_list_of_numbers_into_string([12, -33, 0, 12341234, 124.435]),
                         "[12, -33, 0, 12341234, 124.435]")

    def test_replace_an_array_of_characters_from_a_string(self):
        self.assertEqual(
            MyConverter.replace_an_array_of_characters_from_a_string(
                "[]This ///is a@@ really?? gr??eat S@tr@@ing!",
                ['/', '[', ']', '@', '?']),
            "This is a really great String!")

    # TODO check what happens when you enter a not valid number
    def test_convert_list_with_strings_into_list_with_numbers(self):
        self.assertEqual(
            MyConverter.convert_list_with_strings_into_list_with_numbers(["213", "-21312312124", "321.1232"]),
            [213, 21312312124, 321.1232])


# TestClass of TextFileStorage
class TestTextFileStorage(unittest.TestCase):
    def test_write_and_read_string_in_file(self):
        TextFileStorage.write_string_in_file("Is this string now in a text file?", "test_file.txt")
        context_of_text_file = TextFileStorage.read_lines_from_text_file("test_file.txt")
        self.assertEqual(context_of_text_file[0], "Is this string now in a text file?\n")


# TestClass of Calculus
class TestCalculus(unittest.TestCase):
    test_calculus = Calculus()

    def test_add(self):
        self.assertEqual(self.test_calculus.add(12, 98), 110)

    def test_subtraction_with_positive_result(self):
        self.assertEqual(self.test_calculus.sub(99, 33), 66)

    def test_subtraction_with_negative_result(self):
        self.assertEqual(self.test_calculus.sub(44, 88), -44)

    def test_division_by_zero(self):
        self.assertEqual(self.test_calculus.div(1, 0), "division by zero is not defined")

    def test_division_result_integer(self):
        self.assertEqual(self.test_calculus.div(30, 10), 3)

    def test_division_by_float(self):
        self.assertEqual(self.test_calculus.div(5, 2), 2.5)

    def test_multiplication_of_integer_values(self):
        self.assertEqual(self.test_calculus.mul(10, 66), 660)

    def test_multiplication_of_integer_and_float_values(self):
        self.assertEqual(self.test_calculus.mul(0.5, 100), 50)

    def test_mod(self):
        self.assertEqual(self.test_calculus.mod(9, 2), 1)

    def test_save_and_restore_calculation_results_in_file(self):
        self.test_calculus.add(12, 98)
        self.test_calculus.sub(44, 88)
        self.test_calculus.div(10, 0)
        self.test_calculus.mul(10, 66)
        self.test_calculus.mod(9, 2)
        self.test_calculus.save_calculation_results_in_file()
        TextFileStorage.write_string_in_file(
            MyConverter.convert_list_of_numbers_into_string(self.test_calculus.calculation_results), "test.txt")
        self.assertEqual(self.test_calculus.restore_calculation_results(), self.test_calculus.calculation_results)
