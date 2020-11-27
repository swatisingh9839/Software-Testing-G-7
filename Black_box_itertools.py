import unittest
from itertools import *
import operator
import random


def is_even(self):
    return self % 2 == 0


def takewhile_even_check(self):
    while (self % 2 == 0):
        return self


class TestIslice(unittest.TestCase):
    def setUp(self):
        self.iterable = "abdbndhanfhf"
        self.args= 4
        
        self.start=1
        self.step=4
        self.loops = 20
        
        
        self.posList = [7,8,9]
        self.negList = [-1,-2,-3,-4]
        self.floatList = [10.15,1.5,8.5]
        self.mixfloat = [-1.0,-2.5,99.99,100.1,5599,777] #Decimal with Negative, Positive and Non decimal samples
        self.strList= ['Hello'] 
        self.emptyList= []
        self.multiList=[8.9,-8,(1,4),"Welcome!",5,'',-20]
        self.intValue= 12
        self.strValue = "Hi"
        
        self.strValue1 = ['A','B','C','D']
        self.intList1 = [0,1,2,3]
        self.StrList1 = ['smith','Jones','Justin']
      


        self.value_Integers = [0, 8, 2, 6, 4, 5, 3, 7, 1, 9]
        self.value_Float = [0.0, 4.0, 2.0, 6.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
        self.value_Continuous_Float = [5.0, 5.4, 5.2, 5.3, 5.4, 5.5]
        self.value_Continuous_Negative_Float = [-5.0, -5.6, -5.2, -5.3, -5.4, -5.5]
        self.negative_Integer = [4, 2, 1, 0, -1, -2, -3, -4]
        self.negative_Float = [2.0, 4.0, -10, 0.0, -0.5, -1.0, -2.0]







    def test_islice_1(self):
        #sliciing the string with index 2
        self.assertEqual(list(islice(self.iterable, 2)), list('ab'))
        self.assertEqual(list(islice(self.iterable, 2, 4)), list('db'))
        self.assertEqual(list(islice(self.iterable, 2, None)), list('dbndhanfhf'))
        self.assertEqual(list(islice(self.iterable, 4, None)), list('ndhanfhf'))
       

    def test_islice_2(self):

        #checking the ranges
        self.assertEqual(list(islice(range(5), None)), list(range(5)))
        self.assertEqual(list(islice(range(10), None, None)), list(range(10)))
        self.assertEqual(list(islice(range(10), None, None, None)), list(range(10)))
        self.assertEqual(list(islice(range(10), 2, None)), list(range(2, 10)))
        

    def test_islice_3(self):

        self.assertEqual(list(islice('ABCDEFG', 2)), list('AB'))
        self.assertEqual(list(islice('ABCDEFG', 2, 4)), list('CD'))
        self.assertEqual(list(islice('ABCDEFG', 2, None)), list('CDEFG'))
        self.assertEqual(list(islice('ABCDEFG', 0, None, 2)), list('ACEG'))

        # Test items consumed.
        it = iter(range(10))
        self.assertEqual(list(islice(it, 3)), list(range(3)))
        self.assertEqual(list(it), list(range(3, 10)))
        it = iter(range(10))
        self.assertEqual(list(islice(it, 3, 3)), [])
        self.assertEqual(list(it), list(range(3, 10)))
        



    def test_default(self):
        c = count()
        for i in range(self.loops):
            self.assertEqual(i, next(c))

    def test_start(self):
        start = random.randint(-10, 10)
        c = count(start=start)
        for i in range(start, start + self.loops):
            self.assertEqual(i, next(c))
    
    def test_step_pos(self):
        step = random.randint(1, 5)
        c = count(step=step)
        for i in range(0, self.loops, step):
            self.assertEqual(i, next(c))
    
    def test_count_islice(self):
        self.assertEqual(list(islice(count(10), 5)), [10, 11, 12, 13, 14])

    def test_step_neg(self):
        step = random.randint(-5, -1)
        c = count(step=step)
        for i in range(0, -self.loops, step):
            self.assertEqual(i, next(c))






    def test_for_product(self):

        result = list(product(self.posList))
        self.assertEqual(result,([(7,),(8,),(9,)])) #Testing list of positive values without repeat argument           

        result = list(product(self.negList,self.emptyList))
        self.assertEqual(result,([])) #Testing list of negative values with empty list and without repeat argument       

        result = list(product(self.floatList,self.strList,repeat=1))
        self.assertEqual(result,([(10.15, 'Hello'), (1.5, 'Hello'), (8.5, 'Hello')])) #Testing list of float and string values with repaet argument
       
        result = list(product(self.mixfloat,self.strList,self.emptyList,repeat=1))
        self.assertEqual(result,([])) #Testing multiple iterable list with empty list 
        
        result = list(product(self.strValue,repeat=2))
        self.assertEqual(result,([('H', 'H'), ('H', 'i'), ('i', 'H'), ('i', 'i')])) #Testing string value with repeat argument
        
        result = list(product())
        self.assertEqual(result,([()])) #Testing without aruguments          

        result = list(product(self.multiList,repeat=1))
        self.assertEqual(result,([(8.9,), (-8,), ((1, 4),), ('Welcome!',), (5,), ('',), (-20,)])) #Testing polymorphic list
       
        result = list(product(*self.strList))
        self.assertEqual(result,([('H',), ('e',), ('l',), ('l',), ('o',)])) #Testing list of positive values without repeat argument
        
        range1 = list(product(range(5)))
        self.assertEqual(range1,([(0,), (1,), (2,),(3,),(4,)])) #Testing for range of positive value         


    def test_for_combination(self):
        result = list(combinations(self.strValue1,2)) # Testing combinations of list of letters
        self.assertEqual(result, [('A', 'B'),('A', 'C'),('A', 'D'),('B', 'C'),('B', 'D'),('C', 'D')])
         
        result = list(combinations(self.intList1,2))
        self.assertEqual(result, ([(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]))
         
        result = list(combinations(self.StrList1,2))
        self.assertEqual(result, ([('smith', 'Jones'),('smith', 'Justin'),('Jones', 'Justin')]))



    def test_permutations(self):
        self.assertEqual(list(permutations('ABCD', 2)),list(map(tuple, 'AB AC AD BA BC BD CA CB CD DA DB DC'.split())))
        self.assertEqual(list(permutations(range(3))),[(0,1,2), (0,2,1), (1,0,2), (1,2,0), (2,0,1), (2,1,0)])
       

    def test_permutations_tuple_reuse(self):
        self.assertEqual(len(set(map(id, permutations('abcde', 3)))), 1)

if __name__ == '__main__':
    unittest.main()
