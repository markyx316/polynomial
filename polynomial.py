class X:
    def __init__(self):
        pass

    def __repr__(self):
        return "X"
    
    def evaluate(self, value):
        return value

class Int:
    def __init__(self, i):
        self.i = i

    def __repr__(self):
        return str(self.i)
    
    def evaluate(self, value):
        return self.i

class Add:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return repr(self.p1) + " + " + repr(self.p2)
    
    def evaluate(self, value):
        return self.p1.evaluate(value) + self.p2.evaluate(value)

class Mul:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        p1_repr = f"( {repr(self.p1)} )" if isinstance(self.p1, (Add, Sub, Div)) else repr(self.p1)
        p2_repr = f"( {repr(self.p2)} )" if isinstance(self.p2, (Add, Sub, Div)) else repr(self.p2)
        return f"{p1_repr} * {p2_repr}"
    
    def evaluate(self, value):
        return self.p1.evaluate(value) * self.p2.evaluate(value)

class Div:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        p1_repr = f"( {repr(self.p1)} )" if isinstance(self.p1, (Add, Sub, Mul)) else repr(self.p1)
        p2_repr = f"( {repr(self.p2)} )" if isinstance(self.p2, (Add, Sub, Mul)) else repr(self.p2)
        return f"( {p1_repr} / {p2_repr} )"
    
    def evaluate(self, value):
        numerator = self.p1.evaluate(value)
        denominator = self.p2.evaluate(value)
        if denominator == 0:
            raise ValueError("Division by zero is not allowed.")
        return numerator / denominator

class Sub:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        p1_repr = repr(self.p1)
        p2_repr = repr(self.p2)
        return f"{p1_repr} - {p2_repr}"
    
    def evaluate(self, value):
        return self.p1.evaluate(value) - self.p2.evaluate(value)

# Test cases

# This will represent a polynomial that looks like: 4 + 3 + X + 1 * ( X * X + 1 )
poly1 = Add( Add( Int(4), Int(3)), Add( X(), Mul( Int(1), Add( Mul(X(), X()), Int(1)))))
print(f"Poly1: {poly1}")

# This will represent a polynomial that looks like: 7 - 3 + ( X / ( 2 * ( X + 1 ) ) )
poly2 = Add(Sub(Int(7), Int(3)), Div(X(), Mul(Int(2), Add(X(), Int(1)))))
print(f"Poly2: {poly2}")

# This will represent a polynomial that looks like: ( X + 5 ) * ( ( X / 2 ) - 3 * X )
poly3 = Mul(Add(X(), Int(5)), Sub(Div(X(), Int(2)), Mul(Int(3), X())))
print(f"Poly3: {poly3}")

# Evaluate the polynomials at different values of X (test cases for the exercise part c)
print(f"Poly1 evaluated at X = -1: {poly1.evaluate(-1)}")
print(f"Poly2 evaluated at X = 2: {poly2.evaluate(2)}")
print(f"Poly3 evaluated at X = 3: {poly3.evaluate(3)}")