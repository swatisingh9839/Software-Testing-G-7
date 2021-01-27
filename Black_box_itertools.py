import operator
import unittest 

from decimal import Decimal
from fractions import Fraction
import itertools as it
import random
from itertools import *

'''
class TestIslice(unittest.TestCase):
    def setUp(self):
        self.iterable = "abdbndhanfhf"
        self.args= 4

    

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
    
    def test_islice_3(self):
     # Test invalid arguments
        ra = range(10)
        self.assertRaises(TypeError, islice, ra)
        self.assertRaises(TypeError, islice, ra, 2, 3, 4, 5) #too many argumnents
        self.assertRaises(ValueError, islice, ra, -5, 5, 2)  #negative arguments
        self.assertRaises(ValueError, islice, ra, 2, -4, -2)
        self.assertRaises(ValueError, islice, ra, 2, 5, -2)
        self.assertRaises(ValueError, islice, ra, 2, 10, 0) #invalid range
        self.assertRaises(ValueError, islice, ra, 'a')       #invalid argument
        self.assertRaises(ValueError, islice, ra, 'a', 1)
        self.assertRaises(ValueError, islice, ra, 1, 'a')
        self.assertRaises(ValueError, islice, ra, 'a', 1, 1)
        self.assertRaises(ValueError, islice, ra, 1, 'a', 1)

    def test_islice(self):
        for args in [          # islice(args) should agree with range(args)
                (10, 20, 3),
                (10, 3, 20),
                (10, 20),
                (10, 10),
                (10, 3),
                (20,)
                ]:
            self.assertEqual(list(islice(range(100), *args)),
                             list(range(*args)))

        
'''
class TestItertools(unittest.TestCase):
    def setUp(self):
        self.iterable = "abdbndhanfhf"
        self.args= 4

    

    def test_compress_1(self):
        self.assertEqual(list(compress(data='ABCDEF', selectors=[1,0,1,0,1,1])), list('ACEF'))
        self.assertEqual(list(compress('ABCDEF', [1,0,1,0,1,1])), list('ACEF'))
        self.assertEqual(list(compress('ABCDEF', [0,0,0,0,0,0])), list(''))
        self.assertEqual(list(compress('ABCDEF', [1,1,1,1,1,1])), list('ABCDEF'))
        self.assertEqual(list(compress('ABCDEF', [1,0,1])), list('AC'))
        self.assertEqual(list(compress('ABC', [0,1,1,1,1,1])), list('BC'))
        
        self.assertRaises(TypeError, compress, None, range(6))      # 1st arg not iterable
        self.assertRaises(TypeError, compress, range(6), None)      # 2nd arg not iterable
        self.assertRaises(TypeError, compress, range(6))            # too few args
        self.assertRaises(TypeError, compress, range(6), None)      # too many args
    
    
       
    

def iterator_to_list(iterator: it) -> list:
    if iterator is None:
        return None
    result = []
    for element in iterator:
        result.append(element)
    return result


class TestStarmap(unittest.TestCase):
    """Test class to test the `itertools.starmap` function."""

    def test_starmap_1(self):
        
        self.assertEqual(iterator_to_list(it.starmap(pow, [(2, 6)])), [64])
        self.assertEqual(iterator_to_list(it.starmap(pow, [(3, 3)])), [27])
        self.assertEqual(iterator_to_list(it.starmap(pow, [(10, 4)])), [10000])
        self.assertEqual(iterator_to_list(it.starmap(pow, [(2, 5), (3, 2), (10, 3)])), [32, 9, 1000])

    def test_more_arguments(self):
        """More arguments are passed than the given function uses."""
        self.assertRaises(TypeError, it.starmap(float, [(0, 0)]))
        self.assertRaises(TypeError, it.starmap(pow, [(0, False)]))
        self.assertRaises(TypeError, it.starmap(pow, [(0, 'a')]))

    def test_less_arguments(self):
        """Less arguments are passed than the given function uses."""
        self.assertRaises(TypeError, it.starmap(pow, [(5)]))
        self.assertRaises(TypeError, it.starmap(pow, [(2)]))
        self.assertRaises(TypeError, it.starmap(pow, [(3)]))
        self.assertRaises(TypeError, it.starmap(pow, [(5), (2), (3)]))

    def test_none_arguments(self):
        """Nones are passed as arguments."""
        self.assertRaises(TypeError, it.starmap(pow, [(None, 3)]))
        self.assertRaises(TypeError, it.starmap(pow, [(1, None)]))
        self.assertRaises(TypeError, it.starmap(pow, [(None, None)]))

    def test_exception_in_inner_function(self):
        """Launching an exception in the inner function."""
        def my_function(arg):
            raise Exception("Always launches exception")
        self.assertRaises(Exception, it.starmap(my_function, [1, 2, 3]))

    def test_functions_as_arguments(self):
        """Functions are passed as arguments to the main function."""
        def return1():
            return 1

        def return2():
            return 2

        def self_function(func1, func2):
            return func1() + func2()

        self.assertEqual(iterator_to_list(it.starmap(self_function, [(return1, return2), (return2, return1)])), [3, 3])


class Itertools_MyTest(unittest.TestCase):

    def setUp(self):
        
        self.posList = [7,8,9]
        self.negList = [-1,-2,-3,-4]
        self.floatList = [10.15,1.5,8.5]
        self.mixfloat = [-1.0,-2.5,99.99,100.1,5599,777] #Decimal with Negative, Positive and Non decimal samples
        self.strList= ['Hello'] 
        self.emptyList= []
        self.multiList=[8.9,-8,(1,4),"Welcome!",5,'',-20]
        self.intValue= 12
        self.strValue = "Hi"
        

    def test_for_product(self):
#Testing list of positive values without repeat argument           
        result = list(product(self.posList))
        
#Testing list of negative values with empty list and without repeat argument       
        self.assertEqual(result,([(7,),(8,),(9,)])) 
        result = list(product(self.negList,self.emptyList))
        self.assertEqual(result,([])) 

#Testing list of float and string values with repaet argument
        result = list(product(self.floatList,self.strList,repeat=1))
        self.assertEqual(result,([(10.15, 'Hello'), (1.5, 'Hello'), (8.5, 'Hello')]))
       
#Testing multiple iterable list with empty list 
        result = list(product(self.mixfloat,self.strList,self.emptyList,repeat=1))
        self.assertEqual(result,([]))

#Testing string value with repeat argument        
        result = list(product(self.strValue,repeat=2))
        self.assertEqual(result,([('H', 'H'), ('H', 'i'), ('i', 'H'), ('i', 'i')]))
        
#Testing without aruguments                  
        result = list(product())
        self.assertEqual(result,([()])) 

#Testing polymorphic list
        result = list(product(self.multiList,repeat=1))
        self.assertEqual(result,([(8.9,), (-8,), ((1, 4),), ('Welcome!',), (5,), ('',), (-20,)]))
       
#Testing list of positive values without repeat argument
        result = list(product(*self.strList))
        self.assertEqual(result,([('H',), ('e',), ('l',), ('l',), ('o',)]))
        
#Testing for range of positive value         
        range1 = list(product(range(5)))
        self.assertEqual(range1,([(0,), (1,), (2,),(3,),(4,)])) 

#testing TypeError: integer object is not an iterable
        self.assertRaises(TypeError,product,self.intValue,repeat=1) 

#Testing TypeError: integer argument expected, got float        
        self.assertRaises(TypeError,product,self.strValue,repeat=1.5) 
        
#Testing TypeError: 'string' object cannot be interpreted as an integer
        self.assertRaises(TypeError,product,self.strValue,repeat='12')  

#Testing OverflowError: Python int too large to convert to C ssize_t
        self.assertRaises(OverflowError,product,self.strList,repeat=8**60) 
 
'''
class Itertools_MyTest(unittest.TestCase):

    def setUp(self):
        
        self.posList1 = [12345,678,90]
        self.posList2 = [90,876,54321]

        self.negList1 = [-21,-143343,-12312000,-904]
        self.negList2= [-100,-123,-123]

        self.floatList1 = [10.15,1.5,8.5]
        self.floatList2 = [-1.0,-2.5,99.99,100.1,5599,777] 

        self.strList1= ['Hello this is my world'] 
        self.strList2 = ['This is testing messgage']

        self.emptyList1= []
        self.emptyList2= []

        self.multiList1=[8.9,-8,(1,4),"Welcome!",5,'',-20]

        self.intValue= 12
        self.strValue1 = "Hi"
        
    def test_for_chain(self):
       
        chainlist = list(chain(self.posList1,self.posList2))
        self.assertListEqual(chainlist, [12345,678,90,90,876,54321]) #Testing with list of positive values        

        chainlist = list(chain(self.negList1,self.negList2))
        self.assertListEqual(chainlist, [-21,-143343,-12312000,-904,-100,-123,-123]) #Testing with list of negative values        

        chainlist = list(chain(self.posList1,self.negList2)) #Testing with list of positive and negative values
        self.assertListEqual(chainlist,[12345,678,90,-100,-123,-123])          
        
        chainlist = list(chain(self.posList1,self.posList1)) #Testing for same list/single list
        self.assertListEqual(chainlist, [12345,678,90,12345,678,90])        

        chainlist = list(chain(self.posList1,self.floatList2)) #Testing with list of positive and decimal values
        self.assertListEqual(chainlist,[12345,678,90,-1.0,-2.5,99.99,100.1,5599,777])
        
        chainlist = list(chain(self.strList1,self.strList2)) #Testing for list of string values
        self.assertListEqual(chainlist,['Hello this is my world', 'This is testing messgage'])
        
        chainlist = list(chain())
        self.assertListEqual(chainlist,[]) #Testing without argument

        chainlist = list(chain(self.strList1,chain(self.negList2,chain(self.floatList1)))) #Testing for multiple chain()
        self.assertListEqual(chainlist,['Hello this is my world', -100,-123,-123, 10.15,1.5,8.5])
                
        chainMixedList = list(chain(self.strList1,self.negList1,self.posList2,self.floatList2)) #Testing with list of mixed values
        self.assertListEqual(chainMixedList,['Hello this is my world',-21,-143343,-12312000,-904,90,876,54321,-1.0,-2.5,99.99,100.1,5599,777])        

        emptyList = list(chain(self.emptyList1,self.emptyList2)) #Testing for empty list
        self.assertListEqual(emptyList, [])
        
        multiList = list(chain(self.multiList1,self.emptyList2))
        self.assertListEqual(multiList, [8.9,-8,(1, 4),'Welcome!',5,'',-20]) #Testing multi value list and empty list        

        stringValue = (list(chain(self.strValue1,self.strValue1)))
        self.assertListEqual(stringValue,['H','i','H','i']) #Testing for string value                 
        
        self.assertRaises(TypeError,chain(self.intValue,self.strValue1)) 
        self.assertRaises(TypeError,chain(self.intValue)) 
    
'''
'''
class Itertools_MyTest(unittest.TestCase):

    def setUp(self):
        
        self.posList = ['Test',0,-123456789,987654321,'ABC123ABC',1234.56789,"Hi!@#$Hello"]
        self.posList1 = [12345,678,90]
        self.posList2 = [90,876,54321]

        self.negList1 = [-21,-143343,-12312000,-904]
        self.negList2= [-100,-123,-123]

        self.floatList1 = [10.15,1.5,8.5]
        self.floatList2 = [-1.0,-2.5,99.99,100.1,5599,777] 

        self.strList1= ['Hello this is my world'] 
        self.strList2 = ['This is testing messgage']

        self.empList= []
        
        self.multiList1=[8.9,-8,(1,4),"Welcome!",5,'',-20]

        self.intValue= 12
        self.strValue1 = "Hi"
        
    def test_for_repeat(self):

        result = list(repeat(self.strValue1,2))       
        self.assertEqual(result,['Hi','Hi']) #Testing with string      

        result = list(repeat(self.intValue,5))       
        self.assertEqual(result,[12,12,12,12,12]) #Testing with integer             

        result = list(repeat(self.strList1,5))       
        self.assertEqual(result,[['Hello this is my world'],['Hello this is my world'],['Hello this is my world'],['Hello this is my world'],['Hello this is my world']]) #Testing with string list         

        result = list(repeat(self.multiList1, 2))
        self.assertEqual(result,[[8.9,-8,(1,4),"Welcome!",5,'',-20], [8.9,-8,(1,4),"Welcome!",5,'',-20]]) ##testing a list with different type of values
    
        result = list(repeat(self.negList2, 2**2))
        self.assertEqual(result,[[-100,-123,-123], [-100,-123,-123], [-100,-123,-123], [-100,-123,-123]]) #testing with list of negative values 
        
        
    def test_for_repeat_Emtpy(self):
        
        result = list(repeat("",3))
        self.assertEqual(result,['', '', '']) #Testing with empty string        

        result = list(repeat(self.empList,3))
        self.assertEqual(result,[[],[],[]]) #Testing with empty List         

        result = list(repeat(self.strValue1, 0))
        self.assertEqual(result,[]) #testing a string with 0 cycles  

    
    def test_for_repeat_withOtherFunction(self):
        
        result = list(repeat(self.posList,2))
        
        chainresult =list(chain(result,self.posList))
        self.assertEqual(chainresult,[['Test', 0, -123456789, 987654321, 'ABC123ABC', 1234.56789, 'Hi!@#$Hello'],
                                  ['Test', 0, -123456789, 987654321, 'ABC123ABC', 1234.56789, 'Hi!@#$Hello'],
                                  'Test', 0, -123456789, 987654321, 'ABC123ABC', 1234.56789, 'Hi!@#$Hello'])
        
        prodresult=list(product(result,self.empList))
        self.assertEqual(prodresult,[])
        
        prodresult=list(product(result,"123"))
        self.assertEqual(prodresult,[(['Test', 0, -123456789, 987654321, 'ABC123ABC', 1234.56789, 'Hi!@#$Hello'], '1'), 
                                     (['Test', 0, -123456789, 987654321, 'ABC123ABC', 1234.56789, 'Hi!@#$Hello'], '2'),
                                     (['Test', 0, -123456789, 987654321, 'ABC123ABC', 1234.56789, 'Hi!@#$Hello'], '3'),
                                     (['Test', 0, -123456789, 987654321, 'ABC123ABC', 1234.56789, 'Hi!@#$Hello'], '1'),
                                     (['Test', 0, -123456789, 987654321, 'ABC123ABC', 1234.56789, 'Hi!@#$Hello'], '2'),
                                     (['Test', 0, -123456789, 987654321, 'ABC123ABC', 1234.56789, 'Hi!@#$Hello'], '3')])


    
    def test_for_repeat_error(self):
        self.assertRaises(TypeError, repeat) # testing TypeError: no argument given
        self.assertRaises(TypeError, repeat,self.intValue,self.strValue1,3) #Testing Type Error with extra argument
        self.assertRaises(TypeError, repeat,self.intValue,5.7) # testing typeError:- integer argument expected, got float
        self.assertRaises(OverflowError,repeat,self.strList2,4**40) #testing OverflowError: Python int too large to convert to C ssize_t

''' 

def isEven(x):
    'Test predicate'
    return x%2==0
def take(n, seq):
    'Convenience function for partially consuming a long of infinite iterable'
    return list(islice(seq, n))
class Itertools_In_Test(unittest.TestCase): 
    
    def test_1(self):
        self.assertEqual(list(filterfalse(isEven, range(6))), [1,3,5])
        self.assertEqual(list(filterfalse(None, [0,1,0,2,0])), [0,0,0])
        self.assertEqual(list(filterfalse(bool, [0,1,0,2,0])), [0,0,0])
        self.assertEqual(take(4, filterfalse(isEven, count())), [1,3,5,7])
         
        
    def test_2(self):   
        self.assertRaises(TypeError, filterfalse)
        self.assertRaises(TypeError, filterfalse, lambda x:x)
        self.assertRaises(TypeError, filterfalse, lambda x:x, range(6), 7)
        self.assertRaises(TypeError, filterfalse, isEven, 3)
        self.assertRaises(TypeError, next, filterfalse(range(6), range(6)))
         
   
    def test_3(self):
        x = [2, 4, 5, 7, 8, 10, 20]
        self.assertEqual(list(filterfalse(lambda x: x%2, range(10))), [0,2,4,6,8])
        self.assertEqual(list(filterfalse(lambda x: x>2, range(10))),[0,1,2])
        self.assertEqual(list(filterfalse(None, x)),[])
        self.assertEqual(list(filterfalse(lambda x: x%2==0, x)), [5,7])
       
        
    def filterfalse(y):
        return (y < 5) 
        self.assertEqual(list(itertools.filterfalse(filterfalse, x)),[5,7,8,10,20]) 
        self.assertEqual(list(filterfalse(lambda x: x%2==0, x)), [5,7])
    
    def test_4(self):
       t1=(1,2,3,4,5)
        #Iterating through filterfalse object using for loop
       num1=["red","rain","region",'blue','purple']
       d1=filterfalse(lambda x:x.startswith("r"),num1)
       for i in d1:
         print (i)
        #Iterating through filterfalse object using next() function 
       self.assertEqual(list(filter(lambda x:x%2!=0,t1)),[1,3,5])
      
        
      
'''             
class Itertools_In_Test(unittest.TestCase): 
    
        def test_accumulate(self):
            # one positional argument
            self.assertEqual(list(accumulate(range(10))),[0, 1, 3, 6, 10, 15, 21, 28, 36, 45])
            self.assertEqual(list(accumulate(iterable=range(10))),[0, 1, 3, 6, 10, 15, 21, 28, 36, 45])
            self.assertEqual(list(accumulate('abc')), ['a', 'ab', 'abc'])   
            self.assertEqual(list(accumulate([])), [])                   
            self.assertEqual(list(accumulate([7])), [7])                
        def test_error(self):
            self.assertRaises(TypeError, accumulate, range(10), 5, 6)    
            self.assertRaises(TypeError, accumulate)                     
            self.assertRaises(TypeError, accumulate, x=range(10))        
            self.assertRaises(TypeError, list, accumulate([1, []]))
        def test_min_max(self): 
            s = [2, 8, 9, 5, 7, 0, 3, 4, 1, 6]
            self.assertEqual(list(accumulate(s, min)),[2, 2, 2, 2, 2, 0, 0, 0, 0, 0])
            self.assertEqual(list(accumulate(s, max)),[2, 8, 9, 9, 9, 9, 9, 9, 9, 9])
            self.assertEqual(list(accumulate(s, operator.mul)),[2, 16, 144, 720, 5040, 0, 0, 0, 0, 0])
            self.assertEqual(list(accumulate(s,operator.add)),[2,10,19,24,31,31,34,38,39,45])
            
        def test_add(self):
            s = [2, 8, 9, 5, 7, 0, 3, 4, 1, 6]
            self.assertEqual(list(accumulate([1,2,3,4,5])), [1, 3, 6, 10, 15])
            self.assertEqual(list(accumulate(s,operator.add)),[2,10,19,24,31,31,34,38,39,45])
            self.assertEqual(list( accumulate([0, 7, 19, 13], lambda a, b: b - a)),[0,7,12,1])
        def test(self):
            self.assertEqual(list(accumulate([10, 5, 1], initial=None)), [10, 15, 16])
            self.assertEqual(list(accumulate([10, 5, 1], initial=100)), [100, 110, 115, 116])
            self.assertEqual(list(accumulate([], initial=100)), [100])
        def test_accumulate_1(self):
             # multiple types
            for typ in int, complex, Decimal, Fraction:                  
                self.assertEqual(list(accumulate(map(typ, range(10)))),
                list(map(typ, [0, 1, 3, 6, 10, 15, 21, 28, 36, 45])))
               
                 
'''
class TestCount(unittest.TestCase):
    def setUp(self):
        self.start=1
        self.step=4
        self.loops = 20

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
              
       

class TestIslice(unittest.TestCase):
    def test_ziplongest(self):
        for args in [
                ['abc', range(6)],
                [range(6), 'abc'],
                [range(10), range(20,25), range(30,35)],
                [range(10), range(0), range(30,35), range(12), range(15)],
                [range(10), range(0), range(30,35), range(12), range(15), range(0)],
               
            ]:
            target = [tuple([arg[i] if i < len(arg) else None for arg in args])
                      for i in range(max(map(len, args)))]
                      
                 
            self.assertEqual(list(zip_longest(*args)), target)      # Check for normal input     
            
            self.assertEqual(list(zip_longest(*args, **{})), target) # Check with blank dictionary to append the result
            
            target = [tuple((e is None and 'X' or e) for e in t) for t in target]   # Replace None fills with 'X'
            self.assertEqual(list(zip_longest(*args, **dict(fillvalue='X'))), target)
            
            self.assertEqual(list(zip_longest()), list(zip()))        #check for black values 
            
            self.assertEqual(list(zip_longest([])), list(zip([])))    #check with blank dictionary
            
            self.assertEqual(list(zip_longest('abcdef')), list(zip('abcdef')))      #list of string for matching values in list

            self.assertEqual(list(zip_longest('abc', 'defg', **{})),list(zip(list('abc')+[None], 'defg')))  
            
            print(self.assertRaises(TypeError, zip_longest, 2))                # Check whether it accepts arguments correctly     
            print(self.assertRaises(TypeError, zip_longest, range(2), 2))



# root level methods
def testR(r):
    return r[0]

def testR2(r):
    return r[2]


class Testgroupby(unittest.TestCase):
    

 
    def test_groupby(self):
        # Check whether it accepts arguments correctly
        self.assertEqual([], list(groupby([])))
        
        self.assertEqual([], list(groupby([], key=id)))
        
        self.assertRaises(TypeError, list, groupby('abc', []))
        
        self.assertRaises(TypeError, groupby, None)
        self.assertRaises(TypeError, groupby, 'abc', lambda x:x, 5)

        # Check normal input
        s = [(0, 1, 0), (0, 1,1), (0,2,2), (1,3,2), (1,4,2),
             (2,5,2), (3,6,3), (3,7,3)]
        dup = []
        for k, g in groupby(s, lambda r:r[0]):
            for elem in g:
                print(g)
                self.assertEqual(k, elem[0])
                dup.append(elem)
        self.assertEqual(s, dup)

       
        # Check nested case
        dup = []
        for k, g in groupby(s, testR):
            for ik, ig in groupby(g, testR2):
                for elem in ig:
                    self.assertEqual(k, elem[0])
                    self.assertEqual(ik, elem[2])      #check for different key
                    dup.append(elem)
        self.assertEqual(s, dup)


        # Check case where inner iterator is not used
        keys = [k for k, g in groupby(s, testR)]
        expectedkeys = set([r[0] for r in s])
        self.assertEqual(set(keys), expectedkeys)
        self.assertEqual(len(keys), len(expectedkeys))
		



def is_potato(self):
    if self != "potato":
        return self

class Test_Itertools(unittest.TestCase):

    def setUp(self):
        self.value_Integers = [0, 8, 2, 6, 4, 5, 3, 7, 1, 9]
        self.value_Float = [0.0, 4.0, 2.0, 6.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
        self.value_Continuous_Float = [5.0, 5.4, 5.2, 5.3, 5.4, 5.5]
        self.value_Continuous_Negative_Float = [-4.0, -5.6, -5.2, -5.3, -5.4, -5.5]
        self.negative_Integer = [4, 2, 1, 0, -1, -2, -3, -4]
        self.negative_Float = [2.0, 4.0, -10, 0.0, -0.5, -1.0, -2.0]
        self.string = ["apple", "banana", "mango", "orange", "potato",
                      "passionfruit", "grape"]



    def test_integer(self):
        result = list(dropwhile(lambda x : x % 2 == 0, self.value_Integers))
        self.assertEqual([5, 3, 7, 1, 9], result)

    def test_float(self):
        result = list(dropwhile(lambda x : x % 2 == 0, self.value_Float))
        self.assertEqual([5.0, 6.0, 7.0, 8.0, 9.0, 10.0], result)

    def test_continous_float(self):
        result = list(dropwhile(lambda x : x % 2 == 0,self.value_Continuous_Float))
        self.assertEqual([5.0, 5.4, 5.2, 5.3, 5.4, 5.5], result)

    def test_negative_continous_float(self):
        result = list(dropwhile(lambda x: x % 2 == 0, self.value_Continuous_Negative_Float))
        self.assertEqual([-5.6, -5.2, -5.3, -5.4, -5.5], result)

    def test_negative_float(self):
        result = list(dropwhile(lambda x: x % 2 == 0, self.negative_Float))
        self.assertEqual([-0.5, -1.0, -2.0], result)

    def test_negative_integer(self):
        result = list(dropwhile(lambda x: x % 2 == 0, self.negative_Integer))
        self.assertEqual([1, 0, -1, -2, -3, -4], result)

    def test_string(self):
        result = list(dropwhile(lambda x : x  != "potato", self.string))
        self.assertEqual(['potato', 'passionfruit', 'grape'], result)


'''
class Itertools_MyTest(unittest.TestCase):

    def setUp(self):
        self.posList1 = [12345, 678, 90]
        self.posList2 = [90, 876, 54321]
        self.integer_list = (self.posList1, self.posList2)

        self.negList1 = [-21,-143343,-12312000,-904]
        self.negList2= [-100,-123,-123]
        self.negList = (self.negList1, self.negList2)

        self.posNegList = (self.integer_list, self.negList)

        self.floatList1 = [10.15,1.5,8.5]
        self.floatList2 = [-1.0,-2.5,99.99,100.1,5599,777]
        self.floatList = (self.floatList1, self.floatList2)

        self.strList1= ['Hello this is my world']
        self.strList2 = ['This is testing messgage']
        self.strList = (self.strList1, self.strList2)

        self.emptyList1= []
        self.emptyList2= []
        self.emptyList = (self.emptyList1, self.emptyList2)

        self.multiList=[[8.9,-8,(1,4),"Welcome!",5,'',-20]]

        self.multiEmpty = (self.multiList, self.emptyList)


    def test_for_chain_iterable(self):
        chainlist = list(chain.from_iterable(self.integer_list))
        self.assertListEqual(chainlist, [12345, 678, 90, 90, 876, 54321])

    def test_for_chain_iterable1(self):
        chainlist = list(chain.from_iterable(self.negList))
        self.assertListEqual(chainlist, [-21, -143343, -12312000, -904, -100, -123,
                                         -123])  # Testing with list of negative values

    def test_for_chain_iterable2(self):
        chainlist = list(chain.from_iterable(self.posNegList))  # Testing with list of positive and negative values
        self.assertListEqual(chainlist, [[12345, 678, 90], [90, 876, 54321], [-21, -143343, -12312000, -904], [-100, -123, -123]])

    def test_for_chain_iterable3(self):
        chainlist = list(chain.from_iterable(self.strList))  # Testing for list of string values
        self.assertListEqual(chainlist, ['Hello this is my world', 'This is testing messgage'])


    def test_for_chain_iterable4(self):
        emptyList = list(chain.from_iterable(self.emptyList))  # Testing for empty list
        self.assertListEqual(emptyList, [])

    def test_for_chain_iterable5(self):
        multiList = list(chain.from_iterable(self.multiEmpty))
        self.assertListEqual(multiList, [[8.9, -8, (1, 4), 'Welcome!', 5, '', -20], [], []])  # Testing multi value list and empty list




class Itertools_MyTest(unittest.TestCase):
     
  def setUp (self) :
         
      self.strValue = ['A','B','C','D']
      self.intList = [0,1,2,3]
      self.StrList = ['smith','Jones','Justin']
      
      
  def test_for_combination(self):
         result = list(combinations(self.strValue,2)) # Testing combinations of list of letters
         self.assertEqual(result, [('A', 'B'),('A', 'C'),('A', 'D'),('B', 'C'),('B', 'D'),('C', 'D')])
         
         result = list(combinations(self.intList,2))
         self.assertEqual(result, ([(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]))
         
         result = list(combinations(self.StrList,2))
         self.assertEqual(result, ([('smith', 'Jones'),('smith', 'Justin'),('Jones', 'Justin')]))
         
         self.assertRaises(TypeError,combinations,self.intList,repeat=1)
         self.assertRaises(TypeError,combinations,self.strValue,repeat=2)
        
         range1 = list(combinations(range(4)))
         self.assertEqual(range1,([(0,), (1,), (2,),(3,),]))


class Itertools_MyTest(unittest.TestCase):
  
 def setUp (self) :  
     self.StrList ="GEeks"
     self.intList = [1,2]
     self.Str = 'D.P.S'
  
 def test1_for_combination_with_replacement(self):
     #list
     result = list(combinations_with_replacement(self.StrList, 2))
     self.assertEqual(result,[('G', 'G'), ('G', 'E'), ('G', 'e'), ('G', 'k'), ('G', 's'), ('E', 'E'), ('E', 'e'), ('E', 'k'), ('E', 's'), ('e', 'e'), ('e', 'k'), ('e', 's'), ('k', 'k'), ('k', 's'), ('s', 's')])
 def test2_for_combination_with_replacement(self):  
    #Range
     result = list(combinations_with_replacement(range(3),2))
     self.assertEqual(result,([(0,0),(0,1),(0,2),(1,1),(1,2),(2,2)]))
     
 def test3_for_combination_with_replacement(self):  
    #list in sorted order
    result = list(combinations_with_replacement('D.P.S.', 2))
    self.assertEqual(result,([('D', 'D'), ('D', '.'), ('D', 'P'), ('D', '.'), ('D', 'S'), ('D', '.'), ('.', '.'), ('.', 'P'), ('.', '.'), ('.', 'S'), ('.', '.'), ('P', 'P'), ('P', '.'), ('P', 'S'), ('P', '.'), ('.', '.'), ('.', 'S'), ('.', '.'), ('S', 'S'), ('S', '.'), ('.', '.')]))



'''
'''
class TestIslice(unittest.TestCase):

 def test_cycle(self):
    self.assertEqual(list(it.islice(it.cycle('ABCD'), 13)), list('ABCDABCDABCDA'))
    self.assertEqual(list(it.islice(it.cycle(""), 4)), list(""))  # testing with an empty string and multiple cycles
    self.assertRaises(TypeError, it.cycle, 3) # testing TypeError: argument is not an iterable
 def test_cycle1(self):
    self.assertEqual(list(it.cycle('')), [])
    self.assertRaises(TypeError, it.cycle)
    self.assertRaises(TypeError, it.cycle, 5)        



def is_even(self):
    return self % 2 == 0

def is_potato(self):
    if self != "potato":
        return self

class Test_Itertools(unittest.TestCase):

    def setUp(self):
        self.value_Integers = [0, 8, 2, 6, 4, 5, 3, 7, 1, 9]
        self.value_Float = [0.0, 4.0, 2.0, 6.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
        self.value_Continuous_Float = [5.0, 5.4, 5.2, 5.3, 5.4, 5.5]
        self.value_Continuous_Negative_Float = [-4.0, -5.6, -5.2, -5.3, -5.4, -5.5]
        self.negative_Integer = [4, 2, 1, 0, -1, -2, -3, -4]
        self.negative_Float = [2.0, 4.0, -10, 0.0, -0.5, -1.0, -2.0]
        self.string = ["apple", "banana", "mango", "orange", "potato"
                      "passionfruit", "grape"]



    def test_integer(self):
        result = list(takewhile(is_even, self.value_Integers))
        self.assertEqual([0, 8, 2, 6, 4], result)

    def test_float(self):
        result = list(takewhile(is_even, self.value_Float))
        self.assertEqual([0.0, 4.0, 2.0, 6.0, 4.0], result)

    def test_continous_float(self):
        result = list(takewhile(is_even, self.value_Continuous_Float))
        self.assertEqual([], result)

    def test_negative_continous_float(self):
        result = list(takewhile(is_even, self.value_Continuous_Negative_Float))
        self.assertEqual([-4.0], result)

    def test_negative_float(self):
        result = list(takewhile(is_even, self.negative_Float))
        self.assertEqual([2.0, 4.0, -10, 0.0], result)

    def test_negative_integer(self):
        result = list(takewhile(is_even, self.negative_Integer))
        self.assertEqual([4, 2], result)

    def test_string(self):
        result = list(takewhile(is_potato, self.string))
        self.assertEqual(['apple', 'banana', 'mango', 'orange', 'potatopassionfruit', 'grape'], result)
'''

if __name__ == '__main__':
    unittest.main()
