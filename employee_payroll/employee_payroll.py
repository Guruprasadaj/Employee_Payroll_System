import tkinter as tk
import sqlite3

# Create a SQLite database
conn = sqlite3.connect('employee_payroll.db')
cursor = conn.cursor()

# Create an Employee table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        job_title TEXT NOT NULL,
        hours_worked REAL NOT NULL,
        salary REAL NOT NULL
    )
''')
conn.commit()

# Function to add an employee to the database
def add_employee():
    name = name_entry.get()
    job_title = job_title_entry.get()
    hours_worked = float(hours_worked_entry.get())
    
    # Calculate salary based on hours worked (replace this with your salary calculation logic)
    salary = hours_worked * 20  # Assuming an hourly rate of $20

    cursor.execute('INSERT INTO employees (name, job_title, hours_worked, salary) VALUES (?, ?, ?, ?)', (name, job_title, hours_worked, salary))
    conn.commit()
    status_label.config(text='Employee added successfully!')

# Function to calculate total salary and display it
def calculate_total_salary():
    cursor.execute('SELECT SUM(salary) FROM employees')
    total_salary = cursor.fetchone()[0]
    status_label.config(text=f'Total Salary: ${total_salary:.2f}')

# Function to search for employees by name
def search_employee():
    search_name = search_name_entry.get()
    cursor.execute('SELECT * FROM employees WHERE name LIKE ?', ('%' + search_name + '%',))
    results = cursor.fetchall()
    
    # Display search results (replace with your preferred method)
    result_text.delete(1.0, tk.END)  # Clear previous results
    if results:
        for row in results:
            result_text.insert(tk.END, f'ID: {row[0]}, Name: {row[1]}, Job Title: {row[2]}, Hours Worked: {row[3]}, Salary: {row[4]}\n')
    else:
        result_text.insert(tk.END, 'No matching employees found.')

# Create the main window
root = tk.Tk()
root.title('Employee Payroll System')

# Create labels and entry fields for adding employees
name_label = tk.Label(root, text='Employee Name:')
name_label.pack()

name_entry = tk.Entry(root)
name_entry.pack()

job_title_label = tk.Label(root, text='Job Title:')
job_title_label.pack()

job_title_entry = tk.Entry(root)
job_title_entry.pack()

hours_worked_label = tk.Label(root, text='Hours Worked:')
hours_worked_label.pack()

hours_worked_entry = tk.Entry(root)
hours_worked_entry.pack()

add_button = tk.Button(root, text='Add Employee', command=add_employee)
add_button.pack()

# Create labels and entry fields for calculating total salary
calculate_salary_label = tk.Label(root, text='Calculate Total Salary:')
calculate_salary_label.pack()

calculate_button = tk.Button(root, text='Calculate', command=calculate_total_salary)
calculate_button.pack()

# Create labels, entry fields, and buttons for searching employees
search_label = tk.Label(root, text='Search Employees:')
search_label.pack()

search_name_label = tk.Label(root, text='Name:')
search_name_label.pack()

search_name_entry = tk.Entry(root)
search_name_entry.pack()

search_button = tk.Button(root, text='Search', command=search_employee)
search_button.pack()

# Create a label for displaying status messages
status_label = tk.Label(root, text='')
status_label.pack()

# Create a text widget to display search results
result_text = tk.Text(root, height=10, width=50)
result_text.pack()

root.mainloop()
