# **How to Run C++ and Python Files in Ubuntu**

This guide explains how to compile and run C++ programs and execute Python programs using the Ubuntu Terminal.

## **1. Running C++ Programs in Ubuntu**

### **Step 1: Install the C++ Compiler**

Open the Ubuntu terminal and execute:

```
sudo apt update
sudo apt install g++ -y
```

Verify the installation:

```
g++ --version
```

### **Step 2: Create a C++ File**

Create a file named `main.cpp`:

```
nano main.cpp
```

Add the following code:

```
#include <iostream>
using namespace std;

int main() {
    cout << "Hello World!" << endl;
    return 0;
}
```

Save the file using `Ctrl + O`, press `Enter`, and exit using `Ctrl + X`.

### **Step 3: Compile the C++ File**

Run the following command:

```
g++ main.cpp -o main
```

This generates an executable file named `main`.

To compile using the C++17 standard:

```
g++ -std=c++17 main.cpp -o main
```

### **Step 4: Execute the Program**

```
./main
```

**Output:**

```
Hello World!
```

## **2. Running Python Programs in Ubuntu**

### **Step 1: Install Python**

Update the package list:

```
sudo apt update
```

Install Python 3:

```
sudo apt install python3 -y
```

Verify the installation:

```
python3 --version
```

### **Step 2: Create a Python File**

Create a file named `main.py`:

```
nano main.py
```

Add the following code:

```
print("Hello World!")
```

Save the file using `Ctrl + O`, press `Enter`, and exit using `Ctrl + X`.

### **Step 3: Execute the Python File**

Run the following command:

```
python3 main.py
```

**Output:**

```
Hello World!
```

Alternatively, you can make the Python file executable:

```
chmod +x main.py
```

Then execute it using:

```
./main.py
```

For this method, add the following line at the beginning of your Python file:

```
#!/usr/bin/env python3print("Hello World!")
```

## **3. Quick Reference Commands**

| Operation     | C++                       | Python                        |
| ------------- | ------------------------- | ----------------------------- |
| Check version | `g++ --version`           | `python3 --version`           |
| Compile       | `g++ main.cpp -o main`    | Not required                  |
| Run           | `./main`                  | `python3 main.py`             |
| Install       | `sudo apt install g++ -y` | `sudo apt install python3 -y` |

## **4. Running Programs in VS Code**

If you are using VS Code on Ubuntu, open the integrated terminal using:

\`Ctrl + \`\` (Backtick)

**For C++:**

```
g++ -std=c++17 main.cpp -o main && ./main
```

**For Python:**

```
python3 main.py
```

**Note:**

- C++ requires compilation before execution.
- Python is an interpreted language and can be executed directly using the Python interpreter.
- Make sure you are running commands from the directory containing your source files.
