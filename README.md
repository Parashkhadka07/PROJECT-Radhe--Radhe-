PROJECT – Cli based task tracker
------------------------------------------------------------------------------------------------------
A simple Command Line Task Tracker built in Python.
This application allows you to manage tasks using basic CRUD operations directly from the terminal.
------------------------------------------------------------------------------------------------------
How to Start

Run the main program file:

python main.py
-----------------------------------------------------------------------------------------
The main menu will appear.

Choose an option between 1 – 5.
---------------------------------------------------------------------------------
 Main Menu Options
Option	Description
1	View Tasks
2	Update Task
3	Delete Task
4	Create Task
5	Exit Program
---------------------------------------------------------------------------------------------------------
Option 1 – View Tasks

Selecting Option 1 opens a secondary menu for filtering tasks by status.

You can:

View all tasks

View tasks filtered by their status

Pending

Completed

(Any other status you have defined)

When choosing View All, the program prints every task stored in the system.
-----------------------------------------------------------------------------------------------------
Each task displays:

ID

Title

Status
------------------------------------------------------------------------------------------------------------------
Option 2 – Update Task

Allows you to:

Select a task by its ID

Modify its title or status
------------------------------------------------------------------------------------------------------------------
 Option 3 – Delete Task

Select a task by its ID

Permanently remove it from the system
--------------------------------------------------------------------------------------------------------------------
 Option 4 – Create Task

Add a new task

Assign a title

Assign a status

The task will be stored in the JSON file automatically.


----------------------------------------------------------------------------------------------------------------------
 Option 5 – Exit

Closes the program safely.

-----------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------
Features

File-based storage using JSON

Full CRUD functionality

Status-based task filtering

Clean CLI-based interface
--------------------------------------------------------------------------------------------------------------------
project url
(https://roadmap.sh/projects/task-tracker)