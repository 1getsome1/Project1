import math

import data

# Write your functions for each part in the space below.

# Part 1
# design Recipe:
# 1) Count how many vowels, either upper or lower case, are in the string
# 2) def vowel_count(string) -> int:
# 3) template of function
#     - make a string that contains both upper and lower case vowels
#     - set a variable, count, equal to zero
#     - for loop for each character in the string
#     - if the character is one of the vowels in my "vowels" string add one to count
# 4) test case:    def test_vowels_count_1(self):
#                      num_vowels = project1.vowels_count('Pricequote')
#                      self.assertEqual(num_vowels, 5)
# 5)
def vowels_count(string)->int:
    vowels = "AEIOUaeiou"
    count = 0
    for x in string:
        if x in vowels:
            count +=1
    return count

# Part 2
# design Recipe:
# 1) make a new list that contains lists that have a length of two
# 2) def short_lists(F_L: list[list[int]])->list:
# 3) template of function
#     - make an empty list
#     - cycle through the list containing lists
#     - for loop for each character in the string
#     - if the length of the list is equal to two then it gets appended to the empty list
# 4) test case:        def test_short_lists_1(self):
#                          List = project1.short_lists([[3, 4], [1, 0], [2, 8, 3], [4, 5]])
#                          self.assertEqual(List, [[3, 4], [1, 0], [4, 5]])
# 5)

def short_lists(F_L: list[list[int]])->list:
    S_L = []
    for x in F_L:
        if len(x) == 2:
            S_L.append(x)
    return S_L

# Part 3
# design Recipe:
# 1) repeat the inputted list but if length of the nested lists is 2 then it would rearrange them into ascending order
# 2) def ascending_pairs(pairs: list[list[int]])->list:
# 3) template of function
#     - make an empty list
#     - cycle through the list containing lists
#     - if length of the nested list is 2
#     - then check if index 0 is less than or equal to index 1
#     - else append the nested list and switch the two items
#     - But always at the end add the nested list into empty list
# 4) test case:  def test_ascending_pairs_2(self):
#                    List = project1.ascending_pairs([[3, 9, 4], [93, 34], [], [22, 18, 36], [4, 78]])
#                           self.assertEqual(List, [[3, 9, 4], [34, 93], [], [22, 18, 36], [4, 78]])
# 5)

def ascending_pairs(pairs: list[list[int]])->list:
    elements = []
    for x in pairs:
        if len(x) == 2:
            if x[0] <= x[1]:
                elements.append(x)
            else:
                elements.append([x[1], x[0]])
        else:
            elements.append(x)
    return elements

# Part 4
# design Recipe:
# 1) take two prices, get the dollars of each price and add them together and do the same for cents
# 2) def add_prices(Price1:data.Price, Price2:data.Price)->data.Price:
# 3) template of function
#     - get values for both prices
#     - add the dollars of both prices together
#     - add the cents of both prices together
#     - check if the total amount of cents is equal or greater than 100
#     - if so add to the total dollars based on the remainder of cents after dividing by 100
#     - return price(dollars, cents)
# 4) test case:      def test_add_prices_3(self):
#                        price1 = data.Price(0, 99)
#                        price2 = data.Price(0, 99)
#                        t_price = project1.add_prices(price1, price2)
#                        self.assertEqual(t_price.dollars, 1)
#                        self.assertEqual(t_price.cents, 98)
# 5)

def add_prices(Price1:data.Price, Price2:data.Price)->data.Price:
    t_dollars = Price1.dollars + Price2.dollars
    t_cents = Price1.cents + Price2.cents
    if t_cents >= 100:
        t_dollars += t_cents // 100
        t_cents = t_cents % 100
    return data.Price(t_dollars, t_cents)


# Part 5
# design Recipe:
# 1) take two points, top left and bottom right, with both calculated the area of the rectangle
# 2) def rectangle_area(R:data.Rectangle):
# 3) template of function
#     - access two points make one top left and the other bottom right
#     - get the absolute differences between the two x coordinates
#     - get the absolute differences between the two y coordinates
#     - return the two values times each other to get area
# 4) test case:          def test_rectangle_area_1(self):
#                            p1 = data.Point(0,12)
#                            p2 = data.Point(6, 3)
#                            area = project1.rectangle_area(p1, p2)
#                            self.assertEqual(area, 54)
# 5)

def rectangle_area(top_left, bottom_right):
    width = abs(top_left.x - bottom_right.x)
    height = abs(top_left.y - bottom_right.y)
    return width * height

# Part 6
# design Recipe:
# 1) takes all books that have the same author as the input and puts them in a list
# 2) def books_by_author(author, books_L):
# 3) template of function
#     - take a book from the list and check if its author is the same
# 4) test case:    def test_books_by_author_1(self):
#                      book1 = data.Book(["jrr tolkien", "Ben"], "Book1")
#                      book2 = data.Book(["JK simmons"], "Book1")
#                      book3 = data.Book(["jrr tolkien", "Bob"], "Book1")
#                      books = [book1, book2, book3]
#                      result = project1.books_by_author("jrr tolkien", books)
#                      expected_result = [book1, book3]
#                      self.assertEqual(result, expected_result)
# 5)

def books_by_author(author_name: str, books: list[data.Book])->list[data.Book]:
    return [book for book in books if author_name in book.authors]



# Part 7
# design Recipe:
# 1) make a circle that would be bounding a rectangle
# 2) def circle_bound(rect):
# 3) template of function
#     - get the center point of the rectangle, both x and y coordinates
#     - calculate the radius of the circle
#     - return the two values times each other to get area
# 4) test case:    def test_circle_bound_1(self):
#         rect = data.Rectangle(data.Point(0, 0), data.Point(5, 5))
#         bounding_circle = project1.circle_bound(rect)
#         assert bounding_circle.center == data.Point(2.5, 2.5)
#         assert bounding_circle.radius == 3.5355339059327378
# 5)

def circle_bound(rectangle):
    x1, y1 = rectangle.top_left.x, rectangle.top_left.y
    x2, y2 = rectangle.bottom_right.x, rectangle.bottom_right.y
    center = data.Point((x1 + x2) / 2, (y1 + y2) / 2)
    radius = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) / 2

    return data.Circle(center, radius)

# Part 8
# design Recipe:
# 1) make a list for below average pay employees
# 2) def below_pay_average(employee_list: list[data.Employee]) -> list[str]:
# 3) template of function
#     - if list is empty return an empty list
#     - get the average for the employees
#     - check which employee has below average pay
# 4) test case:        def test_below_pay_average_1(self):
#         employee_list = [data.Employee("Chris", 10), data.Employee("Madonna", 20), data.Employee("Jim", 15)]
#         result = project1.below_pay_average(employee_list)
#         assert result == ["Chris"], f"Expected ['Chris'], but got {result}"
# 5)

def below_pay_average(employee_list: list[data.Employee]) -> list[str]:
    total_pay = 0
    num_employees = len(employee_list)
    if num_employees == 0:
        return []
    for employee in employee_list:
        total_pay += employee.pay_rate
    average_pay = total_pay / num_employees
    below_average = []
    for employee in employee_list:
        if employee.pay_rate < average_pay:
            below_average.append(employee.name)
    return below_average

