import math

import data
import project1
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
# Part 1
    def test_vowels_count_1(self):
        num_vowels = project1.vowels_count('Pricequote')
        self.assertEqual(num_vowels, 5)

    def test_vowels_count_2(self):
        num_vowels = project1.vowels_count(' what Are wEto   Him')
        self.assertEqual(num_vowels, 6)

# Part 2
    def test_short_lists_1(self):
        List = project1.short_lists([[3, 4], [1, 0], [2, 8, 3], [4, 5]])
        self.assertEqual(List, [[3, 4], [1, 0], [4, 5]])

    def test_short_lists_2(self):
        List = project1.short_lists([[3, 4, 9], [1, 93, 0], [22, 18, 36], [44, 53]])
        self.assertEqual(List, [[44, 53]])


# Part 3
    def test_ascending_pairs_1(self):
        List = project1.ascending_pairs([[3, 4], [1, 0], [4.5, 4.5]])
        self.assertEqual(List, [[3, 4], [0, 1], [4.5, 4.5]])

    def test_ascending_pairs_2(self):
        List = project1.ascending_pairs([[3, 9, 4], [93, 34], [], [22, 18, 36], [4, 78]])
        self.assertEqual(List, [[3, 9, 4], [34, 93], [], [22, 18, 36], [4, 78]])

    def test_ascending_pairs_3(self):
        List = project1.ascending_pairs([[], [93, 34, 1], [0, 0], [22, 18, 36], []])
        self.assertEqual(List, [[], [93, 34, 1], [0, 0], [22, 18, 36], []])

# Part 4
    def test_add_prices_1(self):
        price1 = data.Price(1, 20)
        price2 = data.Price(7, 39)
        t_price = project1.add_prices(price1, price2)
        self.assertEqual(t_price.dollars, 8)
        self.assertEqual(t_price.cents, 59)

    def test_add_prices_2(self):
        price1 = data.Price(9, 80)
        price2 = data.Price(34, 40)
        t_price = project1.add_prices(price1, price2)
        self.assertEqual(t_price.dollars, 44)
        self.assertEqual(t_price.cents, 20)

    def test_add_prices_3(self):
        price1 = data.Price(0, 99)
        price2 = data.Price(0, 99)
        t_price = project1.add_prices(price1, price2)
        self.assertEqual(t_price.dollars, 1)
        self.assertEqual(t_price.cents, 98)

# Part 5
    def test_rectangle_area_1(self):
        p1 = data.Point(0,12)
        p2 = data.Point(6, 3)
        area = project1.rectangle_area(p1, p2)
        self.assertEqual(area, 54)

    def test_rectangle_area_2(self):
        p1 = data.Point(-20, 45)
        p2 = data.Point(-11, 36)
        area = project1.rectangle_area(p1, p2)
        self.assertEqual(area, 81)

# Part 6
    def test_books_by_author_1(self):
        book1 = data.Book(["jrr tolkien", "Ben"], "Book1")
        book2 = data.Book(["JK simmons"], "Book1")
        book3 = data.Book(["jrr tolkien", "Bob"], "Book1")
        books = [book1, book2, book3]
        result = project1.books_by_author("jrr tolkien", books)
        expected_result = [book1, book3]
        self.assertEqual(result, expected_result)

    def test_books_by_author_2(self):
        book1 = data.Book(["jrr tolkien", "Ben"], "Book1")
        book2 = data.Book(["JK simmons"], "Book1")
        book3 = data.Book(["jrr tolkien", "Bob"], "Book1")
        books = [book1, book2, book3]
        result = project1.books_by_author("JK simmons", books)
        expected_result = [book2]
        self.assertEqual(result, expected_result)


# Part 7
    def test_circle_bound_1(self):
        rect = data.Rectangle(data.Point(0, 0), data.Point(5, 5))
        bounding_circle = project1.circle_bound(rect)
        assert bounding_circle.center == data.Point(2.5, 2.5)
        assert bounding_circle.radius == 3.5355339059327378

    def test_circle_bound_2(self):
        rect = data.Rectangle(data.Point(0, 0), data.Point(5, 5))
        bounding_circle = project1.circle_bound(rect)
        assert bounding_circle.center == data.Point(2.5, 2.5)
        assert bounding_circle.radius == 3.5355339059327378

# Part 8
    def test_below_pay_average_1(self):
        employee_list = [data.Employee("Chris", 10), data.Employee("Madonna", 20), data.Employee("Jim", 15)]
        result = project1.below_pay_average(employee_list)
        assert result == ["Chris"], f"Expected ['Chris'], but got {result}"

    def test_below_pay_average_2(self):
        employee_list = [data.Employee("Fran", 1250), data.Employee("Elizabeth", 2550), data.Employee("Rosa", 2099)]
        result = project1.below_pay_average(employee_list)
        assert result == ["Fran"], f"Expected ['Fran'], but got {result}"





if __name__ == '__main__':
    unittest.main()