Exercise 9: Recursion
=======

Introduction
------------
Remember when you used to point a video camera at the screen that was displaying the video feed, or tried to put two mirrors face-to-face and peer into infinity? Yeah, recursion is kind of like that.

Take the following function:

    def func_a():
        print "Function a is the haps right now."
        func_b()

So far, nothing out of the ordinary. It is perfectly permissible to call func_b from func_a. But, in an M. Night Shyamalan-worthy twist, look at the definition of func_b --

    def func_b():
        print "FUNCTION B IN THE HIZOUSE."
        func_a()

Uh-oh.

Running this beastly combination of functions together produces the following output (assuming we start from func_a)

Function a is the haps right now.
FUNCTION B IN THE HIZOUSE.
Function a is the haps right now.
FUNCTION B IN THE HIZOUSE.
Function a is the haps right now.
FUNCTION B IN THE HIZOUSE.
Function a is the haps right now.
FUNCTION B IN THE HIZOUSE.
Function a is the haps right now.
FUNCTION B IN THE HIZOUSE.

... forever.

Actually, eventually the computer explodes in a fiery blaze. Better stop your program.

Let's take the idea one step further. If func_a can call func_b which just ends up calling func_a, what happens if we eliminate the middle man?

    def func_c():
        print "OH MY GOD I DON'T UNDERSTAND WHAT'S HAPPENING"
        func_c()

This is a recursive call. Any function that calls itself is said to be recursive. For the full definition of recursion, look up recursion in a dictionary, but the important part here is that the function calls itself. While you were busy panicking, trying to stop the computer from exploding, you may have noticed that a side effect of recursion is that it causes a chunk of code to repeat. As it stands, func_c is effectively an infinite loop. With slight changes, we can harness the power of recursion for evil. I mean good. We can harness it for good. I mean loops.

Consider the following scenario. I have two functions, func_d, and func_e.

    def func_d():
        func_e()
        print "I'm done."

    def func_e():
        print "Sup." 

Neither function is recursive. At this point, it's helpful to imagine that the call to func_e is _nested_ inside func_d. If we call func_d, the text "I'm done" won't print until after func_e has been called and completed. The same idea applies to our recursive function:

    def func_c():
        print "OH MY GOD I DON'T UNDERSTAND WHAT'S HAPPENING"
        func_c()

If we call func_c, it won't complete until after it calls and completes.. func_c, which never completes until it calls func_c and.. arrrrgh. Func_c is nested inside func_c which is nested inside func_c and it never stops. Okay, let's try a different tack. What if we randomly forced func_c to end?

    def func_c():
        if random.choice([True, False]):
            return
        print "OH MY GOD I DON'T UNDERSTAND WHAT'S HAPPENING"
        func_c()

In this case, each call to func_c might randomly end, allowing the enclosing call to func_c to end, allowing the enclosing one to end, until we finally reach the outer enclosure. Now we're getting somewhere. Let's make one more change. Instead of randomly ending, let's control when we end. In this case, we'll end when the argument to func_c is 0.

    def func_c(n):
        if n == 0:
            return
        print "OH MY GOD I DON'T UNDERSTAND WHAT'S HAPPENING"
        func_c(n)

So now func_c takes an argument, n. And if n is 0, it stops. If it's not 0, it repeats. So far, things are still not better. We have some control, the function either repeats forever, or doesn't. Let's look at the last line. If the function repeats while n is 0, what if, when we called func_c, we inched n towards 0, like so.

    def func_c(n):
        if n == 0:
            return
        print n
        func_c(n-1)

If you run this, you'll find that this function counts down from n to 1, printing each number, then stopping. This is a (semi) useful recursive function. Without looping, we can repeat a piece of code and we can control how many times it repeats. There are three rules to writing a recursive function:

    1. The recursive function must have a base case where it decides to end, here, it's when n reaches 0.
    2. The function must accept some argument that can be moved _towards_ the base case, here, it's our argument n.
    3. The function must call itself. This happens on the last line.

One note about base cases, consider the base case to be the most degenerate input your function can take and still be considered to do it's job. If your function is going to print the numbers from n to 0, the simplest version of that is to just print 0. If your function manipulates a list or a string in some way, say, to count the length, the easiest length string to count is 0.

If you need some extra reading, refer to this link:

    * http://interactivepython.org/runestone/static/pythonds/Recursion/recursionsimple.html

Description
-------
Here, you'll find a series of tasks you can already do. But as in the demo, a wizard has taken away your powers of iteration and you're left to accomplish them recursively.
