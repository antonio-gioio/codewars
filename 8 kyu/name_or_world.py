"""Define a method hello that returns "Hello, Name!" to a given name, or says Hello, World! if name is not given (or passed as an empty String).

Assuming that name is a String and it checks for user typos to return a name with a first capital letter (Xxxx).

Examples:

hello "john"   => "Hello, John!"
hello "aliCE"  => "Hello, Alice!"
hello          => "Hello, World!" # name not given
hello ''       => "Hello, World!" # name is an empty String
"""
import unittest

def hello(name = ""):
    return f"Hello, {name.title() or 'World'}!"

class mytestcase(unittest.TestCase):
    
    def test_steps(test):
        tests = (
    ("John", "Hello, John!"),
    ("aLIce", "Hello, Alice!"),
    ("", "Hello, World!"),
)

        for inp, exp in tests:
            test.assertEqual(hello(inp), exp)

        test.assertEqual(hello(), "Hello, World!")



if __name__ == '__main__':
    unittest.main()