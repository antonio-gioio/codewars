"""When it's spring Japanese cherries blossom, it's called "sakura" and it's admired a lot. The petals start to fall in late April.

Suppose that the falling speed of a petal is 5 centimeters per second (5 cm/s), and it takes 80 seconds for the petal to reach the ground from a certain branch.

Write a function that receives the speed (in cm/s) of a petal as input, and returns the time it takes for that petal to reach the ground from the same branch.

Notes:

The movement of the petal is quite complicated, so in this case we can see the velocity as a constant during its falling.
Pay attention to the data types.
If the initial velocity is non-positive, the return value should be 0
    """
import unittest
def sakura_fall(v):
    return 400/v if v > 0 else 0

class mytestcase(unittest.TestCase):
    def test_steps(test):
        test.assertAlmostEqual(sakura_fall(5), 80)
        test.assertAlmostEqual(sakura_fall(10), 40)
        test.assertAlmostEqual(sakura_fall(-1), 0)



if __name__ == '__main__':
    unittest.main()