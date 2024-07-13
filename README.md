# Task Management System

## Overview

This Task Management System is designed to facilitate collaborative task handling among users. Users can create tasks and assign them to others for completion. The system ensures accountability and allows task creators to reopen tasks if they are not completed correctly.

## Features

- **Task Creation**: Users can create tasks with detailed descriptions, due dates, and rewards.
- **Task Assignment**: Tasks can be assigned to any user within the system for completion.
- **Task Completion**: Assigned users can mark tasks as completed.
- **Reopen Tasks**: Task creators can reopen tasks if they are not completed satisfactorily.
- **Task Status Tracking**: Tasks can be tracked through different statuses like Open, Closed, Reopen, and Expired.

## How It Works

1. **User Authentication**: Only authenticated users can create, complete, or reopen tasks.
2. **Task Lifecycle**:
    - A user creates a task with necessary details.
    - Another user can accept and complete the task.
    - If the task is not completed correctly, the creator can reopen it for further action.
    - If the task is completed correctly, the creator can resolve it.

## Getting Started

### Prerequisites

- Python 3.x
- Django

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/task-management-system.git
    cd task-management-system
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Apply migrations:
    ```bash
    python manage.py migrate
    ```

4. Run the development server:
    ```bash
    python manage.py runserver
    ```

5. Access the application at `http://127.0.0.1:8000`.

## Usage

1. Register or log in to the application.
2. Create a new task from the task creation page.
3. View available tasks and accept one to complete.
4. If the task creator reopens the task, take the necessary actions to complete it correctly.

## Author

👤 **Symon**

* Website: [https://sin1ter.github.io/Symon/](https://sin1ter.github.io/Symon/)
* Github: [@sin1ter](https://github.com/sin1ter)

---
