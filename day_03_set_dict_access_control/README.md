# Day 03 – User Access System Using Python

## Overview

This project demonstrates Python concepts including:

- **Sets** – for tracking unique users  
- **Dictionaries** – for managing the activities of the user
- **Conditional Statements** – to determine access levels  

The goal is to build a **mini user access control system** that can:

1. Add the activites according to the roles 
2. Assign and manage roles for each user
3. Determine access permissions based on role
4. Provide Activities using Set operation combining with Dict

---

## Features

### 1. Unique User Tracking
- Uses Python `set` to ensure each user is counted only once
- Can display all unique roles and unique activites

### 2. User Role Management
- Uses Python `dict` to store role-activity mappings
- Add or update user roles dynamically

### 3. Access Control
- Conditional logic (`if / elif / else`) determines:
  - Admin, Employee, User -> Full access
  - Other user -> No access 



---

## Example Output

Enter the role : Admin
Enter the activites: A
Enter the activites: B
Enter the activites: C
Enter the activites: A
Enter the activites: D
Number of activities you entered : 4
Here are  the activities are {'activities': {'C', 'B', 'A', 'D'}}