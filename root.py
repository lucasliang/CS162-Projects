import derivative
from derivative import textToPolynomial

a = input('Enter your polynomial:\n')
poly = textToPolynomial(a)
guess = input('Enter a initial guess:\n')
current = int(guess)
n = 0
accuracy = 0.001
while abs(poly.evaluatePolynomial(current)) > accuracy and n < 1000:
    #to avoid divide by 0 errors, we just reset the guess to some random positive number
    #I used n so we have something that always changes and we never get 'stuck' on any number
    if poly.derivative().evaluatePolynomial(current) == 0:
        current = n
    else:
        current = current - (poly.evaluatePolynomial(current)) / (poly.derivative().evaluatePolynomial(current))
    n += 1
if abs(poly.evaluatePolynomial(current)) > accuracy:
    print("Unable to reach a root, try again with a different guess!")
else:
    print("Root = {}".format(current))