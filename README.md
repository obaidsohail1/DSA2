# **Algorithms Project**

This repository contains solutions to various algorithmic tasks implemented in Python, organized under a pre-configured virtual environment for convenience. The tasks include implementations of classic algorithms and problem-solving techniques, as described below.

---

## **Contents**

1. **Virtual Environment**:  
   A pre-configured virtual environment named `algorithms_env` with all required libraries installed.

2. **Task Files**:
   - `TASK_1.py`: Knight's Tour implementation with Backtracking and Las Vegas approaches.
   - `TASK_2.py`: Minimum Spanning Tree (MST) solution using Kruskal's Algorithm.
   - `TASK_3.py`: Implementation of an in-place Quicksort algorithm for sorting words alphabetically.
   - `TASK_3_Pseudocode.txt`: Pseudocode for the Quicksort algorithm.
   - `TASK_4.py`: Recursive function to check if a word is a palindrome.

---

## **How to Run the Project**

1. **Clone the Repository**:
   Download the repository or clone it to your local machine:
   ```bash
   git clone https://github.com/obaidsohail1/DSA2.git
   cd DSA2
   ```

2. **Activate the Virtual Environment**:
   The `algorithms_env` virtual environment is pre-configured with all required libraries. Activate it using the following commands:

   - On **Windows**:
     ```bash
     algorithms_env\Scripts\activate
     ```

   - On **macOS/Linux**:
     ```bash
     source algorithms_env/bin/activate
     ```

3. **Run the Python Files**:
   Execute the task files as needed:
   ```bash
   python TASK_1.py
   python TASK_2.py
   python TASK_3.py
   python TASK_4.py
   ```

4. **Deactivate the Environment** (Optional):
   Once done, deactivate the environment:
   ```bash
   deactivate
   ```

---

## **Task Descriptions**

### **Task 1: Knight’s Tour (TASK_1.py)**
- Implements both Open and Closed versions of the Knight's Tour problem.
- Provides Backtracking and Las Vegas algorithms for solving the problem.

### **Task 2: Minimum Spanning Tree (TASK_2.py)**
- Computes the MST for a given graph using Kruskal's Algorithm.
- Includes step-by-step visualization of the MST creation process.

### **Task 3: Quicksort Algorithm (TASK_3.py & TASK_3_Pseudocode.txt)**
- Implements an in-place Quicksort algorithm for sorting words alphabetically.
- Includes pseudocode for understanding the algorithm.
- Pivot is always the second-to-last element in the array.

### **Task 4: Palindrome Checker (TASK_4.py)**
- Implements a recursive function `isPalindrome()` to determine if a word is a palindrome.

---

## **Libraries Used**
The following Python libraries are required and pre-installed in the virtual environment:
- `networkx`: For graph representation and manipulation in Task 2.
- `matplotlib`: For visualizing graphs and MST creation in Task 2.

---