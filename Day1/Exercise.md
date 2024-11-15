

### **Exercise: Student Management System**

#### **Objective**:
Create a program that manages student records using classes. The program should allow users to add students, display student information, save the data to a file, and load it back. Make sure to handle potential errors that might arise during file operations or input processing.

#### **Requirements**:

1. **Define a `Student` class**:
   - The `Student` class should contain the following attributes:
     - `name` (string)
     - `age` (integer)
     - `student_id` (string, unique for each student)
     - `courses` (a list of tuples, each tuple containing a course name and a grade, e.g., `("Math", 85)`)

   - The class should include:
     - A constructor method (`__init__`) to initialize the student's details.
     - A method to add a course and grade to the `courses` list.
     - A method to display the student’s details and list of courses with grades.

2. **Define a `StudentManager` class**:
   - This class will handle multiple `Student` objects and contain a dictionary to store students by their `student_id`.

   - The class should include:
     - A method to add a new student. If a student with the same `student_id` exists, prompt the user for a different ID.
     - A method to display all students’ information, showing each student's name, age, ID, and their courses with grades.
     - A method to save all students' data to a text file called `students.txt`. Each student's details and their courses should be saved in a readable format.
     - A method to load students' data from the `students.txt` file and populate the dictionary.
     - Appropriate error handling for file operations (e.g., file not found or file permissions issues).

3. **User Interface**:
   - Implement a loop that repeatedly asks the user for an action:
     1. **Add a new student**.
     2. **Add a course and grade for an existing student**.
     3. **Display all students' information**.
     4. **Save data to file**.
     5. **Load data from file**.
     6. **Exit**.
   - Use `if-else` conditions to handle each action.

4. **Error Handling**:
   - Handle invalid inputs (e.g., non-integer age or grade, or duplicate student IDs).
   - Handle file errors (e.g., file not found, read/write errors).
   - Make sure the program handles any unexpected inputs gracefully.

#### **Example Output**:

1. When adding a student:
   ```
   Enter student name: Alice
   Enter age: 20
   Enter student ID: S123
   Student added successfully!
   ```

2. When adding a course:
   ```
   Enter student ID: S123
   Enter course name: Math
   Enter grade: 85
   Course and grade added for Alice.
   ```

3. When displaying all students:
   ```
   Student ID: S123
   Name: Alice
   Age: 20
   Courses:
     - Math: 85
     - History: 90
   ```

#### **Hints**:
- **File Handling**: Use `with open("students.txt", "w")` to write to a file, and `with open("students.txt", "r")` to read.
- **Error Handling**: Use `try-except` blocks around file operations and other potential errors.
- **Data Structure Choices**: Use a dictionary in `StudentManager` to store students by `student_id` for quick access.
