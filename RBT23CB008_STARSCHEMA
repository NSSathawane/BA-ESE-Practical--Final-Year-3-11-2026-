
import sqlite3

# Step 1: Connect to the database
conn = sqlite3.connect("star_schema.db")
cursor = conn.cursor()

# Step 2: Create Product Dimension Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Product_Dimension (
    Product_ID INTEGER PRIMARY KEY,
    Product_Name TEXT,
    Category TEXT
)
""")

# Step 3: Create Customer Dimension Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Customer_Dimension (
    Customer_ID INTEGER PRIMARY KEY,
    Customer_Name TEXT,
    City TEXT
)
""")

# Step 4: Create Time Dimension Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Time_Dimension (
    Time_ID INTEGER PRIMARY KEY,
    Month TEXT,
    Year INTEGER
)
""")

# Step 5: Create Fact Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Sales_Fact (
    Sales_ID INTEGER PRIMARY KEY,
    Product_ID INTEGER,
    Customer_ID INTEGER,
    Time_ID INTEGER,
    Sales_Amount REAL,
    FOREIGN KEY (Product_ID)
        REFERENCES Product_Dimension(Product_ID),
    FOREIGN KEY (Customer_ID)
        REFERENCES Customer_Dimension(Customer_ID),
    FOREIGN KEY (Time_ID)
        REFERENCES Time_Dimension(Time_ID)
)
""")

# Step 6: Insert Product Data
cursor.executemany("""
INSERT OR IGNORE INTO Product_Dimension
VALUES (?, ?, ?)
""", [
    (101, "Laptop", "Electronics"),
    (102, "Mobile", "Electronics"),
    (103, "Chair", "Furniture")
])

# Step 7: Insert 9 Customer Records
cursor.executemany("""
INSERT OR IGNORE INTO Customer_Dimension
VALUES (?, ?, ?)
""", [
    (1, "Amit", "Pune"),
    (2, "Riya", "Mumbai"),
    (3, "Rahul", "Delhi"),
    (4, "Sneha", "Nashik"),
    (5, "Arjun", "Nagpur"),
    (6, "Priya", "Thane"),
    (7, "Karan", "Kolhapur"),
    (8, "Neha", "Aurangabad"),
    (9, "Vikas", "Solapur")
])

# Step 8: Insert Time Data
cursor.executemany("""
INSERT OR IGNORE INTO Time_Dimension
VALUES (?, ?, ?)
""", [
    (202601, "January", 2026),
    (202602, "February", 2026),
    (202603, "March", 2026),
    (202604, "April", 2026),
    (202605, "May", 2026),
    (202606, "June", 2026),
    (202607, "July", 2026),
    (202608, "August", 2026),
    (202609, "September", 2026)
])

# Step 9: Insert 9 Sales Records
cursor.executemany("""
INSERT OR IGNORE INTO Sales_Fact
VALUES (?, ?, ?, ?, ?)
""", [
    (1, 101, 1, 202601, 50000),
    (2, 102, 2, 202602, 30000),
    (3, 103, 3, 202603, 10000),
    (4, 101, 4, 202604, 55000),
    (5, 102, 5, 202605, 25000),
    (6, 103, 6, 202606, 12000),
    (7, 101, 7, 202607, 60000),
    (8, 102, 8, 202608, 35000),
    (9, 103, 9, 202609, 15000)
])

# Step 10: Display Star Schema Data
cursor.execute("""
SELECT
    Product_Dimension.Product_Name,
    Customer_Dimension.Customer_Name,
    Customer_Dimension.City,
    Time_Dimension.Month,
    Time_Dimension.Year,
    Sales_Fact.Sales_Amount
FROM Sales_Fact
JOIN Product_Dimension
    ON Sales_Fact.Product_ID =
       Product_Dimension.Product_ID
JOIN Customer_Dimension
    ON Sales_Fact.Customer_ID =
       Customer_Dimension.Customer_ID
JOIN Time_Dimension
    ON Sales_Fact.Time_ID =
       Time_Dimension.Time_ID
""")

# Step 11: Print the Result
print("\nSTAR SCHEMA - SALES REPORT")
print("-" * 85)

print(
    f"{'Product':<12}"
    f"{'Customer':<12}"
    f"{'City':<12}"
    f"{'Month':<12}"
    f"{'Year':<8}"
    f"{'Sales':<12}"
)

print("-" * 85)

for row in cursor.fetchall():
    print(
        f"{row[0]:<12}"
        f"{row[1]:<12}"
        f"{row[2]:<12}"
        f"{row[3]:<12}"
        f"{row[4]:<8}"
        f"{row[5]:<12.2f}"
    )

# Step 12: Close Database
conn.commit()
conn.close()

print("\nStar Schema implemented successfully!")
