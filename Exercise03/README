Exercise 03: Functions, Composition, and Documentation
======================================================

Introduction
------------
As in math, functions can be directly composed. That is, assume you have two functions, f and g:

    Function f takes as input an integer and outputs an integer.

    Function g takes as input an integer and outputs a string.

If you wanted to call function f, and use the results as an input to function g, you could do it like so:

    val = f(5)
    results = g(val) 

Using direct substitution, we can shortcut this behavior:

    results = g( f(5) )

The ability to compose functions together means we can construct complex behavior in terms of much simpler behaviors. Consider the following scenario:

    Imagine the owner of a movie theater who has complete freedom in setting
    ticket prices. The more he charges, the fewer the people who can afford
    tickets. In a recent experiment the owner determined a precise relationship
    between the price of a ticket and average attendance. At a price of $5.00
    per ticket, 120 people attend a performance. Decreasing the price by a dime
    ($.10) increases attendance by 15. Unfortunately, the increased attendance
    also comes at an increased cost. Every performance costs the owner $180.
    Each attendee costs another four cents ($0.04). The owner would like to
    know the exact relationship between profit and ticket price so that he can
    determine the price at which he can make the highest profit.

There are two ways we could solve this problem. One is to extract all the math into a single function:

    def profit(price):
        return (((5.0-price) * (15 / 0.1) + 120) * price) - (180 + (0.4 * (120 + ((15 / 0.1) * (5 - price)))))

Another way is to compose the function out of smaller, simpler, well-named functions.

    def profit(price):
        return revenue(price) - cost(price)

    def revenue(price):
        return attendees(price) * price)

    def cost(price):
        return 180 + (0.4 * attendees(price))

    def attendees(price):
        return 120 + (15/0.1) * (5.0 - price)

Both do the same thing, but one is much easier to read and modify after the fact.

Any time you require a value as part of an expression, you may always substitute a function that returns a value of that type. This is true in function calls, arithmetic expressions, conditionals, and so forth:

    Examples:

    if number_is_even(5):
        ...

    while mouse_is_moving():
        ...

    hypotenuse = math.sqrt(math.square(get_side_1()), math.square(get_side_2))


Knowine this, it becomes more important that we know as much as possible about our the signatures of the functions we use.

Python has a feature called a 'docstring' (documentation string) that helps us organize our code. If the first line in a function definition is a string, that string can later be automatically extracted to produce documentation for a project.

    def myfunction():
        "Here is my docstring"

You can also use the 'rare' triple-quote string:

    def myfunction():
        """Here is a triple-quote string"""

Writing a useful docstring is a habit best formed early. Here we present a convention for writing docstrings that ties into our formal problem-solving methodology.

    def myfunction(arg1, arg2):
        """
        A summary of the function, what it accomplishes, how it does so, and what it returns.

        Arguments:
        arg1 -- The expected argument type, and a description of the argument, possible values
        arg2 -- " " "

        Return:
        The type of the value the function returns, if at all. Possible ranges of values

        Examples:
        >>> myfunction(1, 2)
        35
        >>> myfunction(3, 5)
        10
        """

That's a lot of work before we even write the function, but it's necessary to help plan things out The description is mostly self-explanatory, but let's see an example.

    def hypotenuse(side_a, side_b):
        """
        Returns the length of the hypotenuse of a triangle as a real number. Accepts the other two sides as real numbers. Uses the pythagorean theorem.

        Arguments:
        side_a -- length of one side of a triangle as a real number
        side_b -- length of the other side of a triangle as a real number

        Return:
        A real number, guaranteed to be greater than side_a and side_b

        Examples:
        >>> hypotenuse(3, 4)
        5
        >>> hypotenuse(6, 8)
        10
        """

Description
-----------
You will be asked to write a series of small functions, and for each, write out a complete docstring describing the signature and functionality of the function. Put these functions in a file named ex05.py.  These examples come from a textbook and are kind of boring, but bear with it! It builds character.

1. The United States uses the English system of (length) measurements. The rest of the world uses the metric system. So, people who travel abroad and companies that trade with foreign partners often need to convert English measurements to metric ones and vice versa.

Here is a table that shows the six major units of length measurements of the English system:12

English
1 inch  =   2.54    cm
1 foot  =   12  in.
1 yard  =   3   ft.
1 rod   =   5(1/2)  yd.
1 furlong   =   40  rd.
1 mile  =   8   fl.

Develop the functions 'inches_to_cm', 'feet_to_inches', 'yards_to_feet', 'rods_to_yards', 'furlongs_to_rods', and 'miles_to_furlongs'.

Then develop the functions 'feet_to_cm', 'yards_to_cm', 'rods_to_inches', and 'miles_to_feet'.

2. Develop the function inside_circle, which consumes three numbers representing the x and y coordinates of a point and the radius r of a circle centered around the origin It returns true if the point is within or on the circle. It returns false otherwise. The distance of the point to the origin is the square root of x^2 + y^2.

3. A local discount store has a policy of putting labels with dates on all of its new merchandise. If an item has not sold within two weeks the store discounts the item by 25% for the third week, 50% for the fourth week, and 75% for the fifth week. After that no additional discounts are given.
Develop the function 'new_price', which takes the initial price of an item and the number of weeks since the item was dated and produces the selling price of the item.

4. A manufacturing company measured the productivity of its workers and found that between the hours of 6am and 10am they could produce 30 pieces/hour/worker; between 10am and 2pm they could produce 40 pieces/hour/worker; and between 2pm and 6pm they could produce 35 pieces/hour/worker.
Develop a function 'production' that takes an hour of the day between 6am and 6pm, in twenty-four hour format, along with the number of workers and computes the total number of pieces produced during that hour.

5. An Internet service provider charges a base rate per megabyte (MB) transferred depending on market conditions. In addition to the base, transfers between 100 and 500 MB are charged an additional $0.05/MB plus 33% of the base. Data transfers between 500 MB and 1500 MB are charged 1.44 times the base plus $0.08/MB. Above 1500 MB the rate is simply twice the base. All data in a transfer is charged the same rate. For example, if 1600 MB are transfered, then the charge for all 1600 MB is twice the base.
Develop the function 'bill_amount', which takes an amount of data transferred in megabytes and a base rate in dollars and computes the total charge.

Extra Credit:
Read the documentation on the 'turtle' python module: http://docs.python.org/library/turtle.html

Write a function 'flag' that draws a Japanese flag, given a center point in x,y coordinates and a width in pixels.

Write a function that takes in five arguments, top, left, x, y, and spacing, that draws a grid of flags x across and y down, with the spacing in pixels between each, using top and left as your starting coordinates. 
