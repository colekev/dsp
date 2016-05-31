# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Lists and tuples are similar in that they're both a sequence of values indexed by integers. An important difference is that tuples are immutable. Tuples are comma-separated lists, no brackets unlike lists.  
Tuples will work as keys in dictionaries. 


---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Similarities: Both group and store multiple elements into one structure. Can both hold any data type.  
Differences: Unordered (not sortable), non-duplicative.  
Performance: Sets are much faster than lists for finding an element. When searching for an element in a list, the command goes through the entire list in order. In a set, there is a defined hash for the set elements, so you can search directly for that element, not go through and search through every element in the entire set.

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> `lambda` is a way to create small anonymous functions, or functions without a name. These functions are just needed where they have been created, the result of which is the return value.  

>> Simplistic example using `lambda`  
```
>>> f = lambda x, y : x + y
>>> f(1,1)
2
```

>> Using `lambda` to sort without perference to uppercase:  
``` 
>>> sorted(['Some', 'words', 'sort', 'differently'], key=lambda word: word.lower())  
['differently', 'Some', 'sort', 'words']
```

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions provide a concise way to create lists. These new lists are made as the result of some operations applied to each member of another sequence or iterable, or to create a subsequence of those elements that satisfy a certain condition.  
List comprehension example:  
```
>>> def product10(a):
...     return a * 10
... 
>>> list1 = range(1,10)

>>> [product10(a) for a in list1]
```
Equivalent with `map`:
```
>>> list(map(product10, list1))
```
List comprehension:
```
>>> [a for a in list1 if a < 5]
```
Equivalent with `filter`:
```
list(filter(lambda a: a < 5, list1))
```
>> The capabilities of list comprehensions and `map()` and `filter()` are very similar, with list comprehensions being a bit more convoluted in their construction, at least for me.

>> Set comprehensions are similar to list comprehensions:
```
>>> set1 = set(range(1,10))
>>> {a for a in set1 if a < 5}
```
>> Dictionary comprehensions can be used to create the key:value pairs:
```
{a: a**2 for a in (2, 4, 6)}
```
>> Or:
```
{a + 3: a + 6 for a in range(1,10)}
```

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937 days

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





