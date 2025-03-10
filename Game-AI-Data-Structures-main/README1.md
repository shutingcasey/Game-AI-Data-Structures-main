# 📚 Data Structures & Algorithms

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


# 🏆 Assignment 2: Hash Tables, Game Trees & AI Bot

## 📌 Overview
This project is part of the **DSA456 - Data Structures and Algorithms** course at **Seneca College**.  
The assignment focuses on implementing **custom hash tables, game trees, and AI-based decision-making** for a board game.  


## 🔹 Assignment Objectives  
1. **Implement a Hash Table** using **chaining** or **linear probing** for collision resolution.  
2. **Build a Game AI Bot** using **game trees** and **Minimax algorithm**.  
3. **Enhance the Game Features** with additional **UI/UX improvements**.


## 🛠 Implemented Components  

### **1️⃣ Hash Table**
✅ **Operations:** `insert()`, `modify()`, `remove()`, `search()`  
✅ **Collision Resolution:** **Chaining** or **Linear Probing**  
✅ **Dynamic Resizing:** **Auto-resizes** when load factor > 0.7  
✅ **Performance Consideration:** Uses **Python’s `hash()` function** for key hashing  

### **2️⃣ AI Game Bot (Game Tree & Minimax Algorithm)**
✅ **Game Tree Implementation**  
- Each node represents a **potential board state**  
- Uses **Minimax Algorithm** for AI decision-making  
- Prunes branches to improve efficiency  

✅ **Evaluation Function**  
- Assigns scores to board states  
- Higher score = **better move** for AI  
- Winning moves have **highest priority**  

### **3️⃣ Game Feature Enhancements**
✅ **Undo Functionality**: Allows human players to revert the last move  
✅ **Animated Effects**: Smooth transitions when pieces move or overflow  
✅ **AI Difficulty Levels**: Players can adjust AI intelligence  


