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


## 🚀 Running the Game  
Ensure you have **Python 3.9+** installed, then run:  

```sh
# Clone the repository
git clone <repo-link>
cd <repo-folder>

# Run the game
python game.py
