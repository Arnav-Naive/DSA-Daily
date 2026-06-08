# Comprehensive Guide: if __name__ == '__main__'

## 🟢 1. Beginner Level: The Simple Mental Model
Python me `__name__` ek hidden automatic variable hota hai jo har file (`.py`) ke paas pehle se hota hai. Yeh variable Python ko batata hai ki file **kahan** aur **kaise** chal rahi hai.



* **Rule 1:** Agar tum kisi file ko **Direct Run** karte ho (jaise terminal me `python script.py` likh kar), toh Python uske `__name__` variable ke andar ki value `"__main__"` set kar deta hai.
* **Rule 2:** Agar us file ko tum kisi doosri file me **`import`** karte ho, toh uske `__name__` variable ki value badal kar **uss file ka apna naam** ho jati hai.

---

## 🟡 2. Intermediate Level: Why and How to Use It
Jab tum `import` use karte ho, toh Python us imported file ke saare top-level code (functions ke bahar likhi hui cheezein) ko turant execute kar deta hai. Hum is automatic execution ko rokne ke liye conditional block lagate hain.

### The Problem (Bina Iske):
Socho tumne ek file banayi `math_helper.py`:
```python
def square(n):
    return n * n

# Yeh print statement hamesha chalega jab bhi koi is file ko touch karega
print("Testing square of 4:", square(4))