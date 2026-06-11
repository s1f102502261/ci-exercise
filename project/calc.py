def fact(n):
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def gcd(a, b):
    a = abs(a)
    b = abs(b)
    while b != 0:
        a, b = b, a % b
        
    return a
    def test_gcd_positive(self):
        self.assertEqual(gcd(7, 3), 1)
        self.assertEqual(gcd(56, 98), 14)

    def test_gcd_negative(self):
        self.assertEqual(gcd(-15, -25), 5)
        self.assertEqual(gcd(-24, 32), 8)

    def test_gcd_zero(self):
        self.assertEqual(gcd(5, 0), 5)
        self.assertEqual(gcd(0, 7), 7)
        self.assertEqual(gcd(0, 0), 0)
