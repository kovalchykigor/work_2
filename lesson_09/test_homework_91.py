import unittest
from work_2.lesson_09.homework_91 import count_unique_characters
from work_2.lesson_09.homework_91 import count_uppercase_starting_words
from work_2.lesson_09.homework_91 import extract_strings


class TestCountUniqueCharacters(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(count_unique_characters(''), (0, False))

    def test_string_with_less_than_10_unique_chars(self):
        self.assertEqual(count_unique_characters('abcabc'), (3, False))

    def test_string_with_exactly_10_unique_chars(self):
        self.assertEqual(count_unique_characters('abcdefghij'), (10, False))

    def test_string_with_more_than_10_unique_chars(self):
        self.assertEqual(count_unique_characters('abcdefghijk'), (11, True))

    def test_string_with_special_chars(self):
        # Виправлений очікуваний результат з 9 на 8
        self.assertEqual(count_unique_characters('a!@#a!@#b$%^&'), (9, False))


class TestCountUppercaseStartingWords(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(count_uppercase_starting_words(''), 0)

    def test_all_lowercase(self):
        self.assertEqual(count_uppercase_starting_words('this is a test'), 0)

    def test_all_uppercase_starting(self):
        self.assertEqual(count_uppercase_starting_words('This Is A Test'), 4)

    def test_mixed_case(self):
        self.assertEqual(count_uppercase_starting_words('This is A Test'), 3)

    def test_special_characters(self):
        self.assertEqual(count_uppercase_starting_words('This is a Test, and This is another Test!'), 4)


class TestExtractStrings(unittest.TestCase):
    def test_mixed_list(self):
        self.assertEqual(extract_strings(['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']),
                         ['1', '2', 'False', '6', 'Python', 'Lorem Ipsum'])

    def test_all_strings(self):
        self.assertEqual(extract_strings(['hello', 'world', 'test']), ['hello', 'world', 'test'])

    def test_no_strings(self):
        self.assertEqual(extract_strings([1, 2, 3, True, False, 5, 6, 7, 8, 9, 0]), [])

    def test_empty_list(self):
        self.assertEqual(extract_strings([]), [])

    def test_mixed_types(self):
        self.assertEqual(extract_strings(['a', 1, 'b', 2.0, 'c', False, 'd', None]), ['a', 'b', 'c', 'd'])


if __name__ == '__main__':
    unittest.main()
