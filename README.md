# Student Grade Calculator (VIBE)

## Program Purpose
A command-line application that manages student records, calculates grade averages, and assigns letter grades. The program stores all student data persistently in a file and provides statistical analysis capabilities.

## Features

### 1. **Add New Student Records**
   - Enter student name and ID
   - Input three test scores (0-100)
   - Automatic average calculation
   - Automatic letter grade assignment
   - Duplicate ID prevention

### 2. **Display All Students**
   - View all students in a formatted table
   - Shows: Name, ID, Test Scores, Average, Letter Grade
   - All scores formatted to 2 decimal places

### 3. **Class Statistics**
   - Highest average score with student name
   - Lowest average score with student name
   - Overall class average
   - Total student count

### 4. **Search Functionality**
   - Case-insensitive search by student name
   - Partial name matching
   - Returns all matching records in table format

### 5. **Data Persistence**
   - Automatic save to `student_grades.txt` on exit
   - Automatic load on program startup
   - Pipe-delimited file format for easy parsing

## Grading Scale

| Grade | Range |
|-------|-------|
| A | 90-100 |
| B | 80-89 |
| C | 70-79 |
| D | 60-69 |
| F | Below 60 |

## Data Structure

### Student Class
- **name**: Student's full name (string)
- **student_id**: Unique student identifier (string)
- **test1, test2, test3**: Test scores (floats)
- **average**: Calculated average of three tests (float)
- **grade**: Letter grade based on average (string)

## File Format

File: `student_grades.txt`

Format: `name|id|test1|test2|test3|average|grade`

Example:
```
John Doe|S001|85.50|90.00|88.75|88.08|B
Jane Smith|S002|92.00|95.50|91.25|92.92|A
```

## Program Menu

```
1. Add new student
2. Display all students
3. View class statistics
4. Search for student
5. Save and exit (ESC)
```

## Usage

### Running the Program
```bash
python VIBE.py
```

### Adding a Student
1. Select option `1`
2. Enter student name (cannot be empty)
3. Enter student ID (cannot be empty, must be unique)
4. Enter Test 1 score (0-100)
5. Enter Test 2 score (0-100)
6. Enter Test 3 score (0-100)

### Exiting
- Press `5` or type `ESC` to save and exit
- All records automatically saved to `student_grades.txt`

## Error Handling

- **File Operations**: Gracefully handles missing or corrupted files
- **Input Validation**: Validates all numeric inputs
- **Duplicate Prevention**: Prevents duplicate student IDs
- **Empty Fields**: Prevents empty names or IDs

## Example Session

```
WELCOME TO STUDENT GRADE CALCULATOR

✓ Loaded 0 student records from file.

============================================================
STUDENT GRADE CALCULATOR
============================================================
1. Add new student
2. Display all students
3. View class statistics
4. Search for student
5. Save and exit (ESC)
============================================================
Enter your choice (1-5 or ESC to exit): 1

============================================================
ADD NEW STUDENT
============================================================
Enter student name: John Doe
Enter student ID: S001
Enter test scores (0-100):
   Test 1 score: 85
   Test 2 score: 90
   Test 3 score: 88

✓ Student added successfully!
   Name: John Doe
   ID: S001
   Average: 87.67
   Grade: B
```

## Requirements

- Python 3.x
- No external dependencies required
- Cross-platform compatible (Windows, macOS, Linux)

## Author
Alicie Robertson  
CIS261 - Week 10 Assignment