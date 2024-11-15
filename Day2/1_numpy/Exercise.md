Here's a comprehensive exercise that covers several fundamental `numpy` operations, including array creation, indexing, mathematical operations, and basic statistics.

---

### **Exercise: Basic Data Analysis with NumPy**

#### **Objective**:
Write a Python program that simulates analyzing weather data using `numpy`. The program should generate random daily temperatures for a month and perform various operations on this data.

#### **Instructions**:

1. **Generate Data**:
   - Create a 2D NumPy array representing daily high and low temperatures for a month (30 days).
   - Use `numpy.random.randint()` to generate random integers between 10 and 40 for high temperatures, and between 0 and 30 for low temperatures. Each row in the array should represent one day, with the first column as the high and the second as the low temperature.
   

2. **Calculate Average Temperatures**:
   - Calculate the average high temperature for the month.
   - Calculate the average low temperature for the month.
   

3. **Identify Days Based on Conditions**:
   - Find the number of days when the high temperature was above 35 degrees.
   - Find the number of days when the low temperature was below 5 degrees.



4. **Find Specific Values**:
   - Identify the day (index) with the highest temperature.
   - Identify the day (index) with the lowest temperature.


5. **Calculate Temperature Differences**:
   - Calculate the daily temperature difference (high - low) for each day.
   - Find the average daily temperature difference for the month.


6. **Display the Results**:
   - Print out the array of temperatures.
   - Print the average high and low temperatures.
   - Print the number of hot days (high above 35) and cold days (low below 5).
   - Print the day with the highest temperature and the day with the lowest temperature.
   - Print the average daily temperature difference.

---

#### **Example Output**:

```plaintext
Temperatures for the month:
[[25 15]
 [30 10]
 [35 18]
  ...
 [32 22]]

Average high temperature: 28.5
Average low temperature: 12.3
Number of days with high temperature above 35: 5
Number of days with low temperature below 5: 3
Day with the highest temperature: Day 8
Day with the lowest temperature: Day 17
Average daily temperature difference: 15.2
```
