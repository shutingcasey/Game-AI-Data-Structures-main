# 📚 Data Structures & Algorithms Assignments 

## 🏆 Overview
This repository contains implementations of various data structures and algorithms as part of the **DSA456** course assignments at **Seneca College**. The projects focus on implementing fundamental data structures without using built-in Python libraries and exploring algorithmic problem-solving techniques.

## 📌 Assignment 1: **Fundamental Data Structures & Recursion**
### **🔹 Objectives**
In this assignment, we implemented core data structures from scratch, focusing on **linked lists, stacks, queues, deques, and recursive functions**.

### **🛠 Implemented Components**
1. **Sorted Doubly Linked List**  
   - Implemented insertion, deletion, and search operations.
   - Maintains elements in sorted order.

2. **Array-Based Stack, Queue, and Deque**  
   - **Stack:** Follows **LIFO** (Last-In-First-Out) principle.
   - **Queue:** Follows **FIFO** (First-In-First-Out) principle.
   - **Deque:** Allows insertion and removal from both ends.

3. **Recursive Grid Overflow Algorithm**  
   - Simulates a **cell overflow mechanism** where values propagate based on neighboring constraints.
   - Implemented **recursively** to model chain reactions.

4. **Testing & Performance Considerations**  
   - **No built-in Python data structures** (except lists for arrays).
   - Code efficiency optimized to ensure **O(1) or O(n) complexity** where applicable.

### **🚀 Running Assignment 1**
```sh
# Clone the repository
git clone <repo-link>
cd <repo-folder>

# Run unit tests
python -m unittest discover tests
