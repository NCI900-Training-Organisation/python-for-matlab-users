

## Dataset

Create a `students.csv` file with the following content:

```csv
ID,Name,Age,Grade,City
1,Alice,20,85,New York
2,Bob,21,90,Los Angeles
3,Charlie,22,75,Chicago
4,Diana,20,95,New York
5,Edward,23,60,San Francisco
6,Fiona,21,88,Los Angeles
7,George,22,70,Chicago
8,Helen,20,92,New York
```

---

## Tasks

### 1. Load the Data
- Load the CSV file into a pandas DataFrame.
- Display the first 5 rows of the DataFrame.

*Hint: Use `pd.read_csv()`.*

---

### 2. Explore the Data
- Find out the number of rows and columns in the dataset.
- Display the column names.
- Check the data types of each column.

*Hint: Use `.shape`, `.columns`, and `.info()`.*

---

### 3. Filter and Query
- Find all students who are older than 21.
- List all students from "New York".

*Hint: Use conditional filtering (`df[...]`).*

---

### 4. Calculate Statistics
- What is the average grade of the students?
- Find the highest and lowest grades in the dataset.

*Hint: Use `.mean()`, `.max()`, and `.min()`.*

---

### 5. Group and Aggregate
- Group the students by `City` and calculate the average grade for each city.
- Count the number of students from each city.

*Hint: Use `.groupby()` with `.mean()` and `.size()`.*

---

### 6. Sorting
- Sort the dataset by `Grade` in descending order.

*Hint: Use `.sort_values()`.*

---

### 7. Save the Data
- Save the filtered dataset of students from "New York" to a new CSV file called `new_york_students.csv`.

*Hint: Use `.to_csv()`.*
```
