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
import random       #import random library
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
