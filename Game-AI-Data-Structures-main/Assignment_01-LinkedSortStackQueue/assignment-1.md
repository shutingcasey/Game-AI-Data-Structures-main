# Assignment 1

## Due Dates:

* **Repo Creation:** October 1, 2024
* **Part A Due:** October 7, 2024
* **Part B, C, D and E Due:** October 15, 2024

### This assignment is worth 10% of your final grade.  40 marks total

### Late penalties

#### Repo Creation and Part A

* Repo Creation:  -5 marks per day
* Part A: must be completed by due date for part A (no lates accepted).

#### Part B, C, D and E:

* 10% for first week
* 10% per day thereafter

  
### Testing Requirement

Parts B, C and D are programming and they must pass testing on github to get any marks (Green check mark for the part in actions tab).

Passing testing is the **minimum requirement** for the component to receive any marks.  It does not mean you will receive full marks for passing test.  For grading guidelines, please see the rubrics at the bottom of the document 


## Assignment Objectives

In this assignment we will:

*  draw diagrams of your implementation in order to gain a better insight as to how this is accomplished.
*  implement a sorted linked list
*  implement array based data structures
*  implement a recursive function


NOTE: **as this assignment is about implementing data structures, you are not allowed to make use of any python libraries or use built-in python data structures and functions unless specified.  If you are not sure, please ask your professor.  Any use a built-in libraries or functions without approval will result in having to redo the assignment with a grade penalty of -50%**

## Repo Creation - Due: October 1, 2024

### Video instructions:

https://youtu.be/xqiNw5g5pqk

In this assignment you can choose to work in a group of two or three.  You have until October 1 to create a team of your choosing and create your repo.  After this date, students not in a team will be teamed up together by their profs.  **Working alone is not an option.**  In general we will try not to make adjustments to teams that you put together but there may be situations where we have no other ways of placing every student into a team without making changes to existing teams.  Our preference will always be to add someone to a team rather than breaking a team up and thus a three person team is very unlikely to be altered where as a two person team may end up with an additional person (but we will try to avoid this).

**Make sure you are clear how many people you are working with and who they are before using the appropriate link.  You will not be able to modify this once you have created the teams.  When you create your team, your team name will need to use every member's seneca user name**

If you do not have a team, try to find one by posting to [course discussion](https://github.com/orgs/seneca-dsa456-f24/discussions) boards.  Be sure to include which section you are in as you cannot work with people not in your section.

**Make sure you use the correct link below!  It must match your team size.  Individual teams will receive a penalty.  READ The TEAM NAMING DETAILS CAREFULLY!**

* [Repo Creation for teams of 2](repo-creation-g2.md)
* [Repo Creation for teams of 3](repo-creation-g3.md)

Your team will last for only 1 assignment.  If you decide that you were not able to work together after assignment 1, you can find new partners for the next assignment. 

Every member of the team must submit a link to their assignment repo by the repo creation due date.  This means that not only must the repo be created, but every team member must have also joined the correct team.


## Work Divsion (IMPORTANT!)

* Every member of the team must contribute to the coding portions (parts B, C and D) of the assignment.  As there are 3 coding components, we expect each member to be the lead author in one of the 3 sections.  It doesn't mean that other team members can't help ... but the lead should be the main contributer to that part of the assignment.
* Every member is expected to push their own code.
  * it is NOT ok to use email your code to one member or have just one person commit all the code. git/github is a professional tool that employers expect our graduates to know how to use, so learn it now.  If you aren't sure, check out the git tutorial listed in the resources section in course repo.
* **Any team member who isn't the main contributer according to commmits for at least one of the coding components(parts B,C and D) will not receive any credit for the assignment.**

## Part A: Drawings (5 marks), Due October 7. No late submissions accepted for part A

In your repository you will find two pdf file containing some diagrams.  Decide if you will implement your part B with or without the use of sentinel nodes and use the diagram file that matches your decision for Part A.

Read through the specs part B, C and D to get an idea of the functionalities asked for in Part A.

Modify each of the lists in the drawings to show the result of the operation indicated in the diagram

* Be clear about what is changing and how.  
* The diagrams do not need to be neat.. but they need to be understandable so clearly scribbling over a link that no longer exsists is perfectly acceptable.  The idea is to think through what you need to change to based on a written specification.
* You can modify the diagrams electronically using something like paint on windows, or preview on macs.  You can also use other diagramming software 
* Alternatively you can print out the pdf and then hand draw on the printed diagrams. If you choose this method you must:
     * take a picture of each drawing and put them into word document in same order as original
     * convert that document to a pdf (print to a pdf) and name the pdf file the same as the original file.
     * Upload the file to your github repo.
     * A bunch of individual images will not be graded, it needs to be in **one** pdf file.


## Part B: Implement a Sorted Doubly Linked list (10 marks)

The class declarations have been created in the a1_partb.py starter file.  You are responsible to write all the listed functions.

* You are allowed to add data members and helper functions to both Node and DoublyLInked classes.
* You are not allowed to remove/change the interfaces of the listed functions
* Only the listed functions will be called directly by the tester, thus any helper functions you add must be called from those listed below

### Node

The Node class is declared within SortedList.  It stores:
* a piece of data
* a reference to the next Node in the SortedList (None if Node is last node)
* a reference to the previous Node in the SortedList (None if Node is first node)
    
When a Node is initialized, it is passed a data value.  Optionally it is also passed a reference to the next node and a reference to the previous node (in that order).  If the data values are not passed in, they are defaulted to None.

The Node function has the following member functions:

---

```python
def get_data(self)
```
function returns data stored in node

---

```python
def get_next(self)
```
function returns reference to next node in SortedList

---

```python
def get_previous(self)
```
function returns reference to previous node in SortedList

---

### SortedList

A SortedList is a sorted doubly linked list. 


A sorted linked list is a linked list where values stay sorted from smallest to biggest with the smallest node at the front of the list and the largest node at the back.

When the SortedList is first created it is empty.

The SortedList has the following member functions

```python
def get_front(self)
```
This function returns a reference to the first data node in the list.  If list is empty, function returns None

---

```python
def get_back(self)
```
This function returns a reference to the last data node in the list.  If list is empty, function returns None

---

```python  

def is_empty(self)
```
This function returns True if the list is empty, False otherwise

---


```python
def __len__(self)
```
This function returns the number of values stored in the list

---

```python
def insert(self,data)
```
this function inserts data into the list such that the list stays sorted. You may assume that the data being added can be compared using comparison operators.  Function returns reference to newly added node.

---

```python
def erase(self, node)
```
This function removes the node referred to by the node argument.   This function returns nothing. If node is None, function does not alter list and will raise the ValueError with this statement:

```python
  raise ValueError('Cannot erase node referred to by None')
```

---

```python
def search(self, data)
```
This function returns a reference to the node containing data if it exists within the list, None if no node contains data





## Part C - Stack, Queue, Deque(10 marks)

Implementation of the three classes are done in a1_partc.py

These three classes must use a python list based (not linked list based) implementation. NOTE, you can use a python list only.. no other python collection is allowed.

You are allowed to use **most** of the functions available for a python list in your solution.  However the following functions are prohibited (you cannot use them in your solution, or your solution will be subject to deductions or possibly resubmissions):

* append()
* pop()
* insert() 


Furthermore, the functions you are asked to write will have a runtime requirement.  Using a python function that causes the function to exceed the required run time will result in a reduced grade.

This reference may be useful in determining whether or not you can make use of a certain function:

https://wiki.python.org/moin/TimeComplexity#list

In functions that add an item to the data structure (enqueue and other push functions) , there is a possibility that the underlying list will require a resizing operation.  You do not need to count this resizing operation when considering the runtime.

When resizing a data structure, always double the current capacity.  The reason for this is because it can be proved that if we were to double our capacity on resize when list is full, the cost of the resize operation can be amortized over the cost of all insertions allowing for the run time to be O(1) on average.  If we were to do increase the capacity by some other method, by adding some constant amount to our capacity for example, the run time will not be O(1) average.  This type of analysis is called an amortized analysis which is beyond the scope of this course.  Thus, it is good enough to simply know that you should resize by doubling the current capacity.


### Stack class


The Stack class implements a FILO data structure.  This class must be implemented using a python list (not a linked list) based solution.


```python
def __init__(self, cap):
```
This function initializes the Stack class data members. It is passed a value representing it's capacity, with a default capacity of 10 if no capacity is passed in.

---


```python
def capacity(self):
```
This function returns capacity.  

Runtime requirement for this function is O(1)

---


``` python
def push(self, data):
```
This function adds data to the "top" of the Stack.  function does not return anything.  When this operation causes the number of items stored to exceed the current capacity, a resizing operation will need to take place.  Resizing always doubles the current capacity of the array.


Runtime requirement for this function is O(1) when no resizing occurs, O(n) when resizing occurs




---

``` python
def pop(self):
```
This function removes the newest value from the Stack (the value at the "top" of the Stack).  function returns value removed.  

If the function is called on an empty Stack, raise the IndexError with this statement

```python
raise IndexError('pop() used on empty stack')
```


Runtime requirement for this function is O(1)

---

``` python
def get_top(self):
```
This function returns the the newest value (value at "top") from the Stack without removing it.  Function returns None if stack is empty 

Runtime requirement for this function is O(1)

---

``` python

  def is_empty(self):
```
This function returns True if Stack is empty, False otherwise.  

Runtime requirement for this function is O(1)


---

``` python

  def __len__(self):
```
This function returns the number of values in the Stack.  

Runtime requirement for this function is O(1)





### Queue class:

The Queue class implements a FIFO data structure.  This class must be implemented using a python list (not a linked list) based solution.


```python
def __init__(self, cap):
```
This function initializes the Queue class data members. It is passed a value representing it's capacity, with a default capacity of 10 if no capacity is passed in.

---

```python
def capacity(self):
```
This function returns capacity.

Runtime requirement for this function is O(1)

---

``` python
def enqueue(self, data):
```
This function adds data to the "back" of the Queue.  function does not return anything.  When this operation causes the number of items stored to exceed the current capacity, a resizing operation will need to take place.  Resizing always doubles the current capacity of the array.


Runtime requirement for this function is O(1) when no resizing occurs, O(n) when resizing occurs

---

``` python
def dequeue(self):
```
This function removes the oldest value from the Queue (the value at the "front" of the Queue).  Function returns value removed.  

If the function is called on an empty Queue, raise the IndexError with this statement

---

```python
raise IndexError('dequeue() used on empty queue')
```


Runtime requirement for this function is O(1)

---

``` python
def get_front(self):
```
This function returns the the oldest value (value at "front") from the Queue without removing it. Function returns None if Queue is empty.

Runtime requirement for this function is O(1)

---

``` python

def is_empty(self):
```
This function returns True if Queue is empty, False otherwise.  Runtime requirement for this function is O(1)

---

``` python

def __len__(self):
```
This function returns the number of values in the Queue.  Runtime requirement for this function is O(1)



### Deque class 


A Deque is a double ended queue.  This class allows you to add/remove items from front or the back of the data structure.  This class must be implemented using a python list (not a linked list) based solution.  

```python

def __init__(self, cap):
```
This function initializes the Deque class data members. It is passed a value representing it's capacity, with a default capacity of 10 if no capacity is passed in.


```python
def capacity(self):
```
This function returns capacity

Runtime requirement for this function is O(1)

---

``` python
def push_front(self, data):
```
This function adds data to the "front" of the Deque.  Function does not return anything.  When this operation causes the number of items stored to exceed the current capcity, a resizing operation will need to take place.  Resizing always doubles the current capcity of the array.


Runtime requirement for this function is O(1) when no resizing occurs, O(n) when resizing occurs

---

``` python
def pop_front(self):
```
This function removes the  value from the "front" of the Deque. Function returns value removed.  


If the function is called on an empty Deque, raise the IndexError with this statement


```python
raise IndexError('pop_front() used on empty deque')
```

Runtime requirement for this function is O(1)

---

``` python
def push_back(self):
```
This function adds data to the "back" of the Deque.  Function does not return anything.  When this operation causes the number of items stored to exceed the current capcity, a resizing operation will need to take place.  Resizing always doubles the current capcity of the array.


Runtime requirement for this function is O(1) when no resizing occurs, O(n) when resizing occurs

---
``` python
def pop_back(self):
```
This function removes the  value from the "back" of the Deque. Function returns value removed.  

If the function is called on an empty Deque, raise the IndexError with this statement


```python
  raise IndexError('pop_back() used on empty deque')
```


Runtime requirement for this function is O(1)

---

``` python
  def get_front(self):
```
This function returns the value from the "front" of the Deque without removing it.  Runtime requirement for this function is O(1)

---

``` python
  def get_back(self):
```
This function returns the value from the "back" of the Deque without removing it.  Runtime requirement for this function is O(1)

---

``` python

def is_empty(self):
```
This function returns True if Deque is empty, False otherwise.  Runtime requirement for this function is O(1)

---

``` python
def __len__(self):
```
This function returns the number of values in the Deque.  Runtime requirement for this function is O(1)

---


``` python
def __getitem__(self, k):
```
This function returns the k'th value from the "front" of the Deque without removing it.  For example, if k == 0, this function would return the item at front of the Deque.  if k == 1, function would return the second item from the of the front item of the Deque.  


If k is out of range, raise the IndexError exception using the statement:

```python
raise IndexError('Index out of range')
```

Runtime requirement for this function is O(1)

---


## Part D - Overflow (10 marks):

Implementation of these function are done in a1_partd.py


### get_overflow_list() function

```python
def get_overflow_list(grid):
```

This function is passed a grid (2D array) of numbers and returns a list of 2 valued tuples (see below). You may assume the grid is rectangular (no need to test if each row has same length as the other rows).  Each cell within the grid has a number of "neighbours".  The neighbours are cells that are beside a cell either vertically or horizontally.  Thus:

* cells in the corners of the grid have exactly two neighbours
* other cells at edge of grid have exactly 3 neighbours
* cells that are not on the outside have exactly 4 neighbours

Each cell is defined by a row and column, indexed from 0.  Thus, the top left corner is row 0, column 0, and the bottom right corner is indexed (number of rows-1, number of columns-1)

The ascii picture below shows the number of neighbours each cell contains on a 4 X 5 grid:

```
|-----|-----|-----|-----|-----|
|  2  |  3  |  3  |  3  |  2  |
|-----|-----|-----|-----|-----| 
|  3  |  4  |  4  |  4  |  3  |
|-----|-----|-----|-----|-----| 
|  3  |  4  |  4  |  4  |  3  |
|-----|-----|-----|-----|-----| 
|  2  |  3  |  3  |  3  |  2  |
|-----|-----|-----|-----|-----| 

```

The number of neighbours contained within a cell define when a cell will overflow.

The grid of numbers passed to this function can be positive, negative or zero.  The absolute value of these numbers represent the number of items within each cell.

This function returns a list of tuples (row,col) indicating all the cells that will overflow.  A cell will overflow if a cell has as at least as many items as neighbours.  If there are no cells that will overflow, function returns None

The original grid must not be modified by this function


#### Example 1

For example, given the following grid:

```
|-----|-----|-----|-----|-----|
|  2  |  0  |  0  |  0  |  0  |
|-----|-----|-----|-----|-----| 
|  0  | -3  |  0  |  0  |  0  |
|-----|-----|-----|-----|-----| 
|  0  |  0  |  -2 |  0  |  0  |
|-----|-----|-----|-----|-----| 
|  -1 |  0  |  0  |  0  |  3  |
|-----|-----|-----|-----|-----| 

```

Given the above grid, the function would return the following list

[(0,0), (3,4)].  This is because both the top left and bottom right cells contain cells that are greater than or equal to the number of neighbours


#### Example 2

For example, given the following grid:

```
|-----|-----|-----|-----|-----|
|  -2 |  0  |  2  |  0  |  0  |
|-----|-----|-----|-----|-----| 
|  0  | -4  |  0  |  -5 |  0  |
|-----|-----|-----|-----|-----| 
|  0  |  0  |  -2 |  0  |  1  |
|-----|-----|-----|-----|-----| 
|  -2 |  0  |  0  |  0  |  1  |
|-----|-----|-----|-----|-----| 

```

Given the above grid, the function would return the following list

[(0,0), (1,1), (1,3), (3,0)].  the two corner cells with -2, as well as the cells with -4 and -5 have all reached or exceeded the capacity for their cells, so their locations are part of the result list.

---

### overflow() function


```python
def overflow(grid, a_queue):
```

**This function must be written recursively.  An iterative solution will not be accepted and subject to resubmission with penalty**

This function is passed a grid of numbers and an instance of the Queue data structure from part C.  The absolute value of the numbers within each cell represent the number of items within a cell.  This function will perform an overflow operation on the **grid** (described in detail below) making it the result of the overflow process, adding intermediate results to **a_queue** and returning the number of grids added to **a_queue**

A grid is "overflowing" if the following conditions are both true:

a) the grid contains one or more cells that are overflowing
b) the signs of all non-zero cells are not all the same.  In otherwords, if the signs are the same, then the grid is not overflowing.

If the grid is overflowing, a new grid is created based on the following rules and added to the queue:

- you may assume that all overflowing cells will have the same sign (either all positive or all negative)
- any cell that is overflowing becomes empty (assigned 0)
- every neighbour of an overflowing cell gets one extra item
- every neighbour of an overflowing cell takes on the same sign as the overflowing cell (ie overflowing cell "takes over" its neighbours if they were not the same sign)
- all overflowing cells overflow at the same time to form the next grid


this process continues until either:
1. the grid does not contain any overflowing cells.
2. the grid contains cells with all the same signs regardless of the number of overflowing cells.

This function returns number of grids added to the queue.  Note, this is not necessarily the same as the number length of the queue as the queue does not have to be initially empty.

#### Example 1:

Suppose you are given the following:

```
|-----|-----|-----|-----|-----|
|  -2 |  2  |  -3 |  0  |  0  |
|-----|-----|-----|-----|-----| 
|  0  | -4  |  0  |  0  |  0  |
|-----|-----|-----|-----|-----| 
|  0  |  0  |  3  |  0  |  1  |
|-----|-----|-----|-----|-----| 
|  -1 |  0  |  0  |  0  |  1  |
|-----|-----|-----|-----|-----| 

cells with -2, -3, and -4 are all overflowing
```


All overflows happen at the same time resulting in the following:

```
|-----|-----|-----|-----|-----|
|  0  |  -5 |  0  |  -1 |  0  |
|-----|-----|-----|-----|-----| 
|  -2 |  0  |  -2 |  0  |  0  |
|-----|-----|-----|-----|-----| 
|  0  |  -1 |  3  |  0  |  1  |
|-----|-----|-----|-----|-----| 
|  -1 |  0  |  0  |  0  |  1  |
|-----|-----|-----|-----|-----| 

All 3 of the overflowing cells become empty and spread.

Cell [0,1] with the -5 became -5 because it had 3 overflowing neighbours that added 1 item to that cell, it became negative because the overflowing neighbours were negative

Cell [1,0] and [1,2] -2 because it had 2 overflowing neighbours

Cell [2,1] and [0,3] became -1 because it had 1 overflowing neighbour

This grid is added to the queue

but.. not done as cell [0,1] is will overflow
```


after it overflows we get:


```
|-----|-----|-----|-----|-----|
|  -1 |  0  |  -1 |  -1 |  0  |
|-----|-----|-----|-----|-----| 
|  -2 |  -1 |  -2 |  0  |  0  |
|-----|-----|-----|-----|-----| 
|  0  |  -1 |  3  |  0  |  1  |
|-----|-----|-----|-----|-----| 
|  -1 |  0  |  0  |  0  |  1  |
|-----|-----|-----|-----|-----| 

overflowing cell become empty and spread.


Cell [0,0] [0,2] and [1,1] became -1 because it had 1 overflowing neighbour


This grid is added to the queue


```
Above grid is done, no cells are at overflow.
function returns 2


#### Example 2:

When 2 side by side cells are set to overflow, they both overflow at the same time.  This means that they both become empty (0) and both gain one from their overflowing neighbour:

```

|-----|-----|-----|-----|-----|
|  -1 |  0  |  -1 |  -1 |  0  |
|-----|-----|-----|-----|-----| 
|  -1 |  4  |  4  |  0  |  0  |
|-----|-----|-----|-----|-----| 
|  0  |  -1 |  3  |  0  |  1  |
|-----|-----|-----|-----|-----| 
|  -1 |  0  |  0  |  0  |  1  |
|-----|-----|-----|-----|-----| 

both cells with 4 are set to overflow

```
result:

```
|-----|-----|-----|-----|-----|
|  -1 |  1  |  2  |  -1 |  0  |
|-----|-----|-----|-----|-----| 
|  2  |  1  |  1  |  1  |  0  |
|-----|-----|-----|-----|-----| 
|  0  |  2  |  4  |  0  |  1  |
|-----|-----|-----|-----|-----| 
|  -1 |  0  |  0  |  0  |  1  |
|-----|-----|-----|-----|-----| 


The two cells with 4 became 0 at the same time, then each of them gained 1 from their neighbour that use to have 4
```
But we are not done as there is another cell with 4, so we will have to overflow that cell



```
|-----|-----|-----|-----|-----|
|  -1 |  1  |  2  |  -1 |  0  |
|-----|-----|-----|-----|-----| 
|  2  |  1  |  2  |  1  |  0  |
|-----|-----|-----|-----|-----| 
|  0  |  3  |  0  |  1  |  1  |
|-----|-----|-----|-----|-----| 
|  -1 |  0  |  1  |  0  |  1  |
|-----|-----|-----|-----|-----| 


The cell with 4 becomes 0 and each of it's neighbour gains 1 item

```

### Example 3:


Suppose you are given the following:

```
|-----|-----|-----|-----|-----|
|  -2 |  -2 |  -3 |  0  |  0  |
|-----|-----|-----|-----|-----| 
|  0  | -4  |  0  |  0  |  0  |
|-----|-----|-----|-----|-----| 
|  0  |  0  |  -3 |  0  |  -1 |
|-----|-----|-----|-----|-----| 
|  -1 |  0  |  0  |  0  |  -1 |
|-----|-----|-----|-----|-----| 

Here, there are overflowing cells, but all non-zero cells are the same sign.  Thus, this grid is not in an overflowing state.  Function does nothing and returns 0


```



### Example 4:

Suppose you are given the following:

```
|-----|-----|-----|-----|-----|
|  -1 |  -2 |  -2 |  0  |  0  |
|-----|-----|-----|-----|-----| 
|  0  | -3  |  0  |  0  |  0  |
|-----|-----|-----|-----|-----| 
|  0  |  0  |  3  |  0  |  -1 |
|-----|-----|-----|-----|-----| 
|  -1 |  0  |  0  |  0  |  -1 |
|-----|-----|-----|-----|-----| 

Here, there are no overflowing cells. Thus, this grid is not in an overflowing state.  Function does nothing and returns 0

```




## Part E - Video Reflection (independent): (5 marks)


Create a **2 minute max video**, explaining what YOU did for the coding portion of the assignment.  Not your partners.. just you. 

The video should be between **1 to 2 minutes**.  **Marks will be deducted if it is more than 2 minutes long.  You need to be succinct**


**This video is not a line by line reading of the code.  It needs to show your understanding of why the code was written the way it was written.  Statements about what you didn't write is as important if not more important than what you did write**

In the video be sure to include the following:

* describe what you did and the approach you took, by going over the code YOU (not your partners) wrote (ie we should see actual code not just you talking. The description should focus on explaining the reasoning for the code, and other approaches you tried or thought about. It should not be restating the code in English. For example, "I decided to use a loop here instead of recursion because X, Y, and Z" is good. "here is a for loop that runs n times" is bad.
* what gave you the most trouble or what you thought was particularly well done.

You can also include:

* alternative solutions you thought would work but didn't work
* bugs that caused you a lot of grief
* choices that you had make when designing your solution and why you chose what you chose
* etc.




## Submitting your assignment

* After creating your repository/joining the repository team, submit the link to your assignment into Blackboard.

* Push your diagram into your repo (remember you can always use the file upload button).  Make the commit message clear that it is the version you want us to mark.

* Push your code into your repo and ensure it passes all the testings by checking the actions tab.

* For the video, you can either use stream over sharepoint or an unlisted youtube video (make sure to get a proper sharing link and submit that for part E).




## Rubrics:

Don't forget to check this style guide:

https://github.com/seneca-dsa456-f24/dsa456-f24/blob/main/style-guide.md

This sections describes how your assignment will be graded:

### Drawing Rubric:

| Criteria | Level 0 | Level 1 | Level 2 | Level 3 | Level 4 |
|---|---|---|---|---|---|
| Drawing completion | No diagrams present | Less than half the diagrams are completed without flaws | At least Half the diagrams are completed without flaws, but a signficant number are missing or has flaws  | Missing a diagram or one of the diagrams have flaws | All diagrams present and correctly drawn with clear changes to the list|


### Coding Rubric:

| Criteria | Level 0 | Level 1 | Level 2 | Level 3 | Level 4 |
|---|---|---|---|---|---|
| **Documentation - 20%** - Documentation is about Intention.  "This function is suppose to do" X.  It doesn't state HOW. "we loop, then there is an if, then ..." - this is an example of what not to do.  It doesn't repeat code.  For each function ensure that it describe what it does (at a high level), what it accepts as arguments and any sort of restrictions (number must be positive for example) and what the function should return under what condition (returns True if found for example) |Almost no documentation of any type |only a few functions got documented and documentation tends to be code description as opposed to code intention. | many function documentation missing or severe lack of details for function description or documentation is done only at code level (within the code) and not as an overall intention| a few functions documentation missing. or function description comments lack some detail.  Over documentation.  documenting every line of code is not a good... let the code speak | For all functions state what parameters are (and any limitations, what return value is, what it does. |
| **Code Styling - 10%** Consistent styling is key.  This category describes things like indentation, consistent naming strategies, good variable names, not adding public member functions etc. | more than 5 cases of inconsistent or bad styling | 3 to 5 cases of inconsistent  or bad styling | 2 to 3 cases of inconsistent or bad styling functions | 1 case of inconsistent  or bad styling | Consistency is key. same variable name styling, same data member styling, correct and consistent indentation, good variable names | 
|**Correctness and Completeness of Code - 35%**.  This category generally describes errors in logic or missing functionality that may occur only in some cases.  This category also includes using things you are not suppose to use or not following specifications correctly | 4 or more errors | 3 errors | 2 errors - using something you are not suppose to use will count at a minimum as two errors as it is a spec violation | 1 errors | all functions completed and correct |
| **Efficiency - 35%** - Anything that is completely off from optimal run time will always count as an instance of inefficiency.. thus if runtime can be O(n) and your code is written to O(n^2)  These count as a major instance. Writing unnecessary code will also be counted as inefficient even if runtime is same as the optimal run time, these are considered minor. 2 level deduction for major instance, 1 level for minor instance| some combination of multiple major/minor incidences of efficiency | 3 minor instance of inefficiency or 1 major and 1 minor instance | 2 instance of inefficiency or 1 major instance of inefficiency| 1 minor instance of inefficiency | Function is as efficient as possible |


### Reflection Rubric

 Criteria | Level 0 | Level 1 | Level 2 | Level 3 | Level 4 |
|---|---|---|---|---|---|
| Reflection | No reflection submitted | Video reflection does not have any details, statements made can apply to anything or statements made does not match the work that is submitted | Video is overly long (over 2min 30 sec) or Video reflection lacks depth, either the statements made are vague or simply a line by line reading of the code without explanation of the intention of that code | Video reflection shows some depth with some descriptions.  It does not go far beyond the basic requirements | A video reflection with clear thought that shows depth and understanding of the work|


