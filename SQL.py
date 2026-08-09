import os
import sqlite3

# This function creates a new SQLite database and returns the connection and cursor objects for further use.
def create_database():
    if os.path.exists('database.db'): # Check if the database file already exists
        os.remove('database.db') # If it exists, remove it to start fresh (optional, depending on your needs)

    conn = sqlite3.connect('database.db') # Create a new SQLite database 
    cursor = conn.cursor() # Create a cursor object to execute SQL commands

    return conn, cursor # Return the connection and cursor for further use in the main function

# This function creates the necessary tables in the database using SQL commands executed through the cursor
def create_tables(cursor): 
    # Create the Students table with columns for id, name, age, email, and city
    cursor.execute('''
        CREATE TABLE Students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            email TEXT NOT NULL UNIQUE,
            city VARCHAR
        )
    ''')

    # Create the Courses table with columns for id, course_name, instructor, and credits
    cursor.execute('''
        CREATE TABLE Courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            course_name TEXT NOT NULL,
            instructor TEXT NOT NULL,
            credits INTEGER NOT NULL            
        )
    ''')

# This function inserts sample data into the Students and Courses tables using the executemany method for efficient batch insertion
def insert_sample_data(cursor): 
    students = [
        ('Alice Johnson', 20, 'alice.johnson@example.com', 'New York'),
        ('Bob Smith', 22, 'bob.smith@example.com', 'Los Angeles'),
        ('Charlie Brown', 19, 'charlie.brown@example.com', 'Chicago'),
        ('David White', 18, 'david.white@example.com', 'Chicago'),
        ('Eve Davis', 21, 'eve.davis@example.com', 'San Francisco')
    ]
    courses = [
        ('Mathematics', 'Dr. John Smith', 3),
        ('Physics', 'Prof. Jane Doe', 4),
        ('Chemistry', 'Dr. Emily Johnson', 5),
        ('Biology', 'Dr. Michael Brown', 4),
        ('Computer Science', 'Dr. Sarah Davis', 3)
    ]

    # Use executemany to insert multiple records into the Students and Courses tables efficiently
    cursor.executemany('INSERT INTO Students (name, age, email, city) VALUES (?, ?, ?, ?)', students)
    cursor.executemany('INSERT INTO Courses (course_name, instructor, credits) VALUES (?, ?, ?)', courses)

    print("Sample data inserted successfully.")

def basic_queries(cursor):
    # === SELECT ALL ===
    # Example of a basic query to retrieve all students from the Students table
    cursor.execute('SELECT * FROM Students') # Execute the SQL command to select all records from the Students table
    students = cursor.fetchall() # Fetch all results from the executed query

    for student in students: 
        print(f"ID: {student[0]}, Name: {student[1]}, Age: {student[2]}, Email: {student[3]}, City: {student[4]}") # Print each student's details in a formatted string
    
    # Output: Example output of the basic query showing all students with their details
    # ID: 1, Name: Alice Johnson, Age: 20, Email: alice.johnson@example.com, City: New York
    # ID: 2, Name: Bob Smith, Age: 22, Email: bob.smith@example.com, City: Los Angeles
    # ID: 3, Name: Charlie Brown, Age: 19, Email: charlie.brown@example.com, City: Chicago
    # ID: 4, Name: David White, Age: 18, Email: david.white@example.com, City: Chicago
    # ID: 5, Name: Eve Davis, Age: 21, Email: eve.davis@example.com, City: San Francisco

    # === COLUMNS ===
    # Example of a query to select specific columns (name and email) from the Students table
    cursor.execute('SELECT name, email FROM Students') # Execute the SQL command to select only the name and email columns from the Students table
    students = cursor.fetchall() # Fetch all results from the executed query    

    for student in students:
        print(f"Name: {student[0]}, Email: {student[1]}") # Print each student's name and email in a formatted string
    
    # Output: Example output of the COLUMNS query showing only the name and email of each student
    # Name: Alice Johnson, Email: alice.johnson@example.com
    # Name: Bob Smith, Email: bob.smith@example.com
    # Name: Charlie Brown, Email: charlie.brown@example.com
    # Name: David White, Email: david.white@example.com
    # Name: Eve Davis, Email: eve.davis@example.com

    # === LIMIT ===
    # Example of a query to select only the first 3 students from the Students table
    cursor.execute('SELECT * FROM Students LIMIT 3') # Execute the SQL command to select only the first 3 records from the Students table
    students = cursor.fetchall() # Fetch all results from the executed query    

    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}, Age: {student[2]}, Email: {student[3]}, City: {student[4]}") # Print each student's details in a formatted string

    # Output: Example output of the LIMIT query showing only the first 3 students with their details
    # ID: 1, Name: Alice Johnson, Age: 20, Email: alice.johnson@example.com, City: New York
    # ID: 2, Name: Bob Smith, Age: 22, Email: bob.smith@example.com, City: Los Angeles
    # ID: 3, Name: Charlie Brown, Age: 19, Email: charlie.brown@example.com, City: Chicago

    # === ORDER BY ===
    # Example of a query to select all students from the Students table and order them by age in ascending order
    cursor.execute('SELECT * FROM Students ORDER BY age ASC') # Execute the SQL command to select all records from the Students table and order them by age in ascending order
    students = cursor.fetchall() # Fetch all results from the executed query

    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}, Age: {student[2]}, Email: {student[3]}, City: {student[4]}") # Print each student's details in a formatted string
    
    # Output: Example output of the ORDER BY query showing all students ordered by age
    # ID: 4, Name: David White, Age: 18, Email: david.white@example.com, City: Chicago
    # ID: 3, Name: Charlie Brown, Age: 19, Email: charlie.brown@example.com, City: Chicago
    # ID: 1, Name: Alice Johnson, Age: 20, Email: alice.johnson@example.com, City: New York
    # ID: 5, Name: Eve Davis, Age: 21, Email: eve.davis@example.com, City: San Francisco
    # ID: 2, Name: Bob Smith, Age: 22, Email: bob.smith@example.com, City: Los Angeles

    # === WHERE ===
    # Example of a query to select students from the Students table where the city is 'Chicago'
    cursor.execute("SELECT * FROM Students WHERE city = 'Chicago'") # Execute the SQL command to select all records from the Students table where the city is 'Chicago'
    students = cursor.fetchall() # Fetch all results from the executed query    

    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}, Age: {student[2]}, Email: {student[3]}, City: {student[4]}") # Print each student's details in a formatted string
    
    # Output: Example output of the WHERE query showing only students from Chicago with their details
    # ID: 3, Name: Charlie Brown, Age: 19, Email: charlie.brown@example.com, City: Chicago 
    # ID: 4, Name: David White, Age: 18, Email: david.white@example.com, City: Chicago

    # === WHERE - NOT ===
    # Example of a query to select students from the Students table where the city is not 'Chicago'
    cursor.execute("SELECT name, city FROM Students WHERE city != 'Chicago'") # Execute the SQL command to select the name and city of all records from the Students table where the city is not 'Chicago'
    students = cursor.fetchall() # Fetch all results from the executed query
    for student in students:
        print(f"Name: {student[0]}, City: {student[1]}") # Print each student's name and city in a formatted string

    # Output: Example output of the WHERE - NOT query showing only students not from Chicago with their name and city
    # Name: Alice Johnson, City: New York
    # Name: Bob Smith, City: Los Angeles
    # Name: Eve Davis, City: San Francisco

    # === WHERE - IN ===
    # Example of a query to select students from the Students table where the city is either 'Chicago' or 'New York'
    cursor.execute("SELECT * FROM Students WHERE city IN ('Chicago', 'New York')") # Execute the SQL command to select all records from the Students table where the city is either 'Chicago' or 'New York'
    students = cursor.fetchall() # Fetch all results from the executed query

    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}, Age: {student[2]}, Email: {student[3]}, City: {student[4]}") # Print each student's details in a formatted string
    
    # Output: Example output of the WHERE - IN query showing only students from Chicago or New York with their details
    # ID: 1, Name: Alice Johnson, Age: 20, Email: alice.johnson@example.com, City: New York
    # ID: 3, Name: Charlie Brown, Age: 19, Email: charlie.brown@example.com, City: Chicago
    # ID: 4, Name: David White, Age: 18, Email: david.white@example.com, City: Chicago


def aggregate_functions(cursor):
    # === COUNT ===
    # Example of a query to count the number of students in the Students table
    cursor.execute('SELECT COUNT(*) FROM Students') # Execute the SQL command to count the total number of records in the Students table
    count = cursor.fetchone()[0] # Fetch the result of the COUNT query and extract the count value

    print(f"Total number of students: {count}") # Print the total number of students
    # Output: Example output of the COUNT query showing the total number of students
    # Total number of students: 5

    # === AVG ===
    # Example of a query to calculate the average age of students in the Students table
    cursor.execute('SELECT AVG(age) FROM Students') # Execute the SQL command to calculate the average age of students in the Students table
    average_age = cursor.fetchone()[0] # Fetch the result of the AVG query and extract the average age value

    print(f"Average age of students: {average_age:.2f}") # Print the average age of students formatted to 2 decimal places
    # Output: Example output of the AVG query showing the average age of students
    # Average age of students: 20.00

    # === MAX ===
    # Example of a query to find the maximum age of students in the Students table
    cursor.execute('SELECT MAX(age) FROM Students') # Execute the SQL command to find the maximum age of students in the Students table
    max_age = cursor.fetchone()[0] # Fetch the result of the MAX query and extract the maximum age value

    print(f"Maximum age of students: {max_age}") # Print the maximum age of students
    # Output: Example output of the MAX query showing the maximum age of students
    # Maximum age of students: 22

    # === MIN ===
    # Example of a query to find the minimum age of students in the Students table
    cursor.execute('SELECT MIN(age) FROM Students') # Execute the SQL command to find the minimum age of students in the Students table
    min_age = cursor.fetchone()[0] # Fetch the result of the MIN query and extract the minimum age value

    print(f"Minimum age of students: {min_age}") # Print the minimum age of students
    # Output: Example output of the MIN query showing the minimum age of students
    # Minimum age of students: 18

    # === GROUP BY ===
    # Example of a query to count the number of students in each city using GROUP BY
    cursor.execute('SELECT city, COUNT(*) FROM Students GROUP BY city') # Execute the SQL command to count the number of students in each city by grouping the results by the city column
    city_counts = cursor.fetchall() # Fetch all results from the executed GROUP BY query

    for city_count in city_counts:
        print(f"City: {city_count[0]}, Number of students: {city_count[1]}") # Print each city and the corresponding number of students in a formatted string

    # Output: Example output of the GROUP BY query showing the number of students in each city
    # SQLite returns GROUP BY results sorted by the grouped column, not insertion order
    # City: Chicago, Number of students: 2
    # City: Los Angeles, Number of students: 1
    # City: New York, Number of students: 1
    # City: San Francisco, Number of students: 1

def crud_operations(conn, cursor):
    # === CREATE ===
    # Example of a query to insert a new student into the Students table
    cursor.execute("INSERT INTO Students (name, age, email, city) VALUES ('Frank Miller', 23, 'frank.miller@example.com', 'Boston')") # Execute the SQL command to insert a new student into the Students table
    conn.commit() # Commit the changes to the database after inserting the new student

    # === UPDATE ===
    # Example of a query to update the age of a student in the Students table
    cursor.execute("UPDATE Students SET age = 24 WHERE id = 6") # Execute the SQL command to update the age of the student with id 6 in the Students table 
    conn.commit() # Commit the changes to the database after updating the student's age

    # === DELETE ===
    # Example of a query to delete a student from the Students table
    cursor.execute("DELETE FROM Students WHERE id = 6") # Execute the SQL command to delete the student with id 6 from the Students table
    conn.commit() # Commit the changes to the database after deleting the student

def main():
    conn, cursor = create_database() # Call the function to create the database and get the connection and cursor

    try: 
        create_tables(cursor) # Call the function to create the necessary tables in the database
        insert_sample_data(cursor) # Call the function to insert sample data into the tables
        basic_queries(cursor) # Call the function to perform basic SQL queries and display results
        crud_operations(conn, cursor) # Call the function to perform CRUD operations
        aggregate_functions(cursor) # Call the function to perform aggregate functions and display results

        conn.commit() # Commit the changes to the database
    except Exception as e:
        print(f"An error occurred: {e}") # Print any errors that occur during table creation
    finally:
        conn.close() # Ensure the database connection is closed after operations are complete

if __name__ == '__main__':  
    main() 