import re

#represents a polynomial term, eg. 2x^2
class PolynomialTerm(object):
    def __init__ (self,coefficient,power):
        self.coefficient = coefficient
        self.power = power
    #calculates a deriative and returns the result polynomial term
    def calcDerivative(self):
        if self.power == 0:
            return PolynomialTerm(0,0)
        else:
            return PolynomialTerm(self.coefficient*self.power,self.power-1)
    #evaluates the term numerically at a given point (returns a float)
    def evaluate(self,x):
        return (x**self.power * self.coefficient)*1.0
    def __str__(self):
        if self.power == 1:
            return str(self.coefficient) + 'x'
        elif self.power == 0:
            return str(self.coefficient)
        else:
            return str(self.coefficient)+'x^'+str(self.power)

#represents an entire polynomial eg. 3x^3 + 4x^2 + 1
class Polynomial(object):
    def __init__(self,polynomialterms):
        self.polynomialterms = polynomialterms
    #calculates the derivative and returns the polynomial object
    def derivative(self):
        result = []
        for term in self.polynomialterms:
            derv = term.calcDerivative()
            if derv.coefficient != 0:
                result.append(derv)
        return Polynomial(result)
    #evalutes at a given point
    def evaluatePolynomial(self,x):
        result = 0.0
        for term in self.polynomialterms:
            result += term.evaluate(x)
        return result
    def __str__(self):
        result = ""
        if len(self.polynomialterms) == 0:
            return "0"
        result += str(self.polynomialterms[0])
        for term in self.polynomialterms[1:]:
            result += " + "
            result += str(term)
        return result

#parses a polynomial in text form and converts it into a polynomial object
def textToPolynomial (polynomialText):
    tokens = re.split("[ ]+",polynomialText)
    result = []
    sign = 1 #tracks whether we saw a + or - last
    for token in tokens:
        if token == '':
            continue
        if token == '+':
            sign = 1
            continue
        elif token == '-':
            sign = -1
            continue
        tokens2 = re.split("[ ]*[x][ ]*[\^][ ]*",token) #split on 'x^'
        if len(tokens2) == 1: #means it is just a constant or a linear term
            if 'x' in token: #linear
                if len(token) == 1: #just an 'x'
                    result.append(PolynomialTerm(sign,1))
                else: #a coefficient and x
                    result.append(PolynomialTerm(sign * int(token[0:-1]),1))
            else: #constant
                result.append(PolynomialTerm(sign * int(token),0))
        else:
            if tokens2[0] == '':
                result.append(PolynomialTerm(sign,int(tokens2[1])))
            else:
                result.append(PolynomialTerm(sign * int(tokens2[0]),int(tokens2[1])))
    return Polynomial(result)

'''
a = input('Enter your polynomial:\n')
poly = textToPolynomial(a)
print("Derivative:")
print(poly.derivative())
'''