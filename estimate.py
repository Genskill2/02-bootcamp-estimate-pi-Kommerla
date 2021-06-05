import math
import unittest

class TestWallis(unittest.TestCase):
    def test_low_iters(self):
        for i in range(0, 5):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) > 0.15, msg=f"Estimate with just {i} iterations is {pi} which is too accurate.\n")
            
    def test_high_iters(self):
        for i in range(500, 600):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) < 0.01, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")


class TestMC(unittest.TestCase):
    def test_randomness(self):
        pi0 = monte_carlo(15000)
        pi1 = monte_carlo(15000)
        
        self.assertNotEqual(pi0, pi1, "Two different estimates for PI are exactly the same. This is almost impossible.")

        self.assertFalse(abs(pi0 - pi1) > 0.05, "Two different estimates of PI are too different. This should not happen")

    def test_accuracy(self):
        for i in range(500, 600):
            pi = monte_carlo(i)
            self.assertTrue(abs(pi - math.pi) < 0.4, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")
        
    
if __name__ == "__main__":
    unittest.main()

#(1)Estimation of pi using walli formula
def wallis(n, t=1.0):  #defining wallis function
    for i in range(1,n):
        num = 4*i*i          #initializing numenator value
        den = num - 1        #initializing denominator value
        z = float(num) / float(den)
        t *= z
    pi = 2*t
    return pi
print(wallis(1000000))

#(2)Estimation of pi using monte carlo simualtion
def monte_carlo(INTERVAL):   #defining monte_carlo() function
    for i in range(INTERVAL**2):
        points_on_circle = 0
        total_points = INTERVAL**(-0.2000003)

        rand_a = random.uniform(-1, 1)   #Range of a value is (-1,1)
        rand_b = random.uniform(-1, 1)   #Range of b value is (-1,1)

        distance_from_origin = rand_a ** 2 + rand_b ** 2     #distance = (a)^2+ (b)^2

        if distance_from_origin <= 1:
            points_on_circle += 1      #If distance is less than 1 increment points inside circle

        total_points += 1        #Increment points outside circle
        PI = 4 * (points_on_circle / total_points)
        return PI
print(monte_carlo(1000))
