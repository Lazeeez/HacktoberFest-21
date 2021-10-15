import itertools
import numpy as np


class FuzzySet:
    def __init__(self, size, data, degree):
        self.size = size
        self.data = data
        self.memb_degree = degree

    def display(self):
        for (a, b) in zip(self.data, self.memb_degree):
            print("(" + str(a) + ", " + str("%.3f" % b) + ")")

    def equality(self, obj):
        if isinstance(obj, FuzzySet) and self.size == obj.size:
            for i in range(self.size):
                if self.memb_degree != obj.memb_degree:
                    return "Given fuzzy sets are not equal"
        else:
            print("error")

        print("First set is:")
        self.display()
        print("Second set is:")
        obj.display()

    def complement(self):
        c = []
        for i in range(self.size):
            c.append(1 - self.memb_degree[i])
        compl = FuzzySet(self.size, self.data, c)
        print("Complemented set:")
        compl.display()

    def union(self, obj):
        if isinstance(obj, FuzzySet) and self.size == obj.size:
            union_memb = []
            union_deg = []

            for i in range(self.size):
                if self.memb_degree[i] > obj.memb_degree[i]:
                    union_deg.append(self.data[i])
                    union_memb.append(self.memb_degree[i])
                else:
                    union_deg.append(obj.data[i])
                    union_memb.append(obj.memb_degree[i])

            result = FuzzySet(self.size, union_deg, union_memb)
            result.display()
        else:
            print("error")

    def intersection(self, obj):
        if isinstance(obj, FuzzySet) and self.size == obj.size:
            inter_memb = []
            inter_deg = []

            for i in range(self.size):
                if self.memb_degree[i] < obj.memb_degree[i]:
                    inter_deg.append(self.data[i])
                    inter_memb.append(self.memb_degree[i])
                else:
                    inter_deg.append(obj.data[i])
                    inter_memb.append(obj.memb_degree[i])

            result = FuzzySet(self.size, inter_deg, inter_memb)
            result.display()
        else:
            print("error")

    def algb_product(self, obj):
        if isinstance(obj, FuzzySet) and self.size == obj.size:
            mul = []
            for (a, b) in zip(self.memb_degree, obj.memb_degree):
                mul.append(a * b)

            result = FuzzySet(self.size, self.data, mul)
            result.display()
        else:
            print("error")

    def crisp_product(self, crisp):
        mul = []
        for i in self.memb_degree:
            mul.append(i * crisp)

        result = FuzzySet(self.size, self.data, mul)
        result.display()

    def power(self, power):
        mul = []
        for i in self.memb_degree:
            mul.append(i ** power)

        result = FuzzySet(self.size, self.data, mul)
        result.display()

    def algb_sum(self, obj):
        if isinstance(obj, FuzzySet) and self.size == obj.size:
            sum = []
            for (a, b) in zip(self.memb_degree, obj.memb_degree):
                sum.append(a + b - a * b)

            result = FuzzySet(self.size, self.data, sum)
            result.display()
        else:
            print("error")

    def algb_diff(self, obj):
        if isinstance(obj, FuzzySet) and self.size == obj.size:
            diff = []
            c = [1 - i for i in obj.memb_degree]
            for (a, b) in zip(self.memb_degree, c):
                if a < b:
                    diff.append(a)
                else:
                    diff.append(b)

            result = FuzzySet(self.size, self.data, diff)
            result.display()
        else:
            print("error")

    def bound_sum(self, obj):
        if isinstance(obj, FuzzySet) and self.size == obj.size:
            sum = []
            for (a, b) in zip(self.memb_degree, obj.memb_degree):
                if 1 > a + b:
                    sum.append(a + b)
                else:
                    sum.append(1)

            result = FuzzySet(self.size, self.data, sum)
            result.display()
        else:
            print("error")

    def bound_diff(self, obj):
        if isinstance(obj, FuzzySet) and self.size == obj.size:
            diff = []
            for (a, b) in zip(self.memb_degree, obj.memb_degree):
                c = a + b - 1
                if 0 > c:
                    diff.append(0)
                else:
                    diff.append(c)

            result = FuzzySet(self.size, self.data, diff)
            result.display()
        else:
            print("error")

    def cartesian(self, obj):
        cart = []
        for i in self.memb_degree:
            for j in obj.memb_degree:
                if i < j:
                    cart.append(i)
                else:
                    cart.append(j)
        print(np.array(cart).reshape(self.size, obj.size))


if __name__ == "__main__":

    data = ["mango", "orange", "guava", "apple"]
    memb = [0.9, 0.75, 0.5, 0.8]

    fruit_sweetness = FuzzySet(4, data, memb)
    print("sweetness of fruit")
    fruit_sweetness.display()
    print("sourness of fruit")
    fruit_sweetness.complement()

    data = ["Kalakad", "Rosogolla", "Kamalbhog", "Ladoo"]
    memb = [0.8, 0.95, 0.85, 0.78]

    dessert_sweetness = FuzzySet(4, data, memb)
    print("sweetness of dessert")
    dessert_sweetness.display()
    print("sourness of dessert")
    dessert_sweetness.complement()

    print(
        "The sweetness of food items after fuzzy union operation between fruits and desserts"
    )
    fruit_sweetness.union(dessert_sweetness)
    print(
        "The sweetness of food items after fuzzy intersection operation between fruits and desserts"
    )
    fruit_sweetness.intersection(dessert_sweetness)

    data1 = ["x1", "x2", "x3", "x4"]
    memb1 = [0.25, 0.8, 0.1, 0.45]
    data2 = ["x1", "x2", "x3", "x4"]
    memb2 = [0.8, 0.95, 0.85, 0.78]

    set1 = FuzzySet(4, data1, memb1)
    set2 = FuzzySet(4, data2, memb2)

    print("The algebraic product of fuzzy set 1 and 2 is:")
    set1.algb_product(set2)

    print("The algebraic sum of fuzzy set 1 and 2 is:")
    set1.algb_sum(set2)

    print("The crisp product of fuzzy set 1 is:")
    set1.crisp_product(4)

    print("The power of dessert_sweetness set is:")
    dessert_sweetness.power(2)

    print("The algebraic difference of fuzzy set 1 and 2 is:")
    set1.algb_diff(set2)

    print("The bounded sum of fuzzy set 1 and 2 is:")
    set1.bound_sum(set2)

    print("The bounded difference of fuzzy set 1 and 2 is:")
    set1.bound_diff(set2)

    print("The cartesian product of fuzzy set 1 and 2 is:")
    set1.cartesian(set2)
