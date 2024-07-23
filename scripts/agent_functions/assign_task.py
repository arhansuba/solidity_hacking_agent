from crewai import Task, Crew

class TaskManager:
    def __init__(self, crew):
        self.crew = crew
        self.tasks = []

    def add_task(self, description: str, expected_output: str):
        """
        Add a new task to the task list.
        """
        task = Task(description=description, expected_output=expected_output)
        self.tasks.append(task)

    def assign_tasks(self):
        """
        Assign all tasks to the crew.
        """
        if not self.tasks:
            raise ValueError("No tasks to assign.")
        
        self.crew.tasks = self.tasks
        print(f"Assigned {len(self.tasks)} tasks to the crew.")

    def get_task_summary(self):
        """
        Get a summary of all tasks.
        """
        summary = []
        for idx, task in enumerate(self.tasks):
            summary.append({
                'Task ID': idx,
                'Description': task.description,
                'Expected Output': task.expected_output
            })
        return summary

# Example usage
def main():
    # Initialize crew and task manager
    crew = Crew()
    task_manager = TaskManager(crew)

    # Define tasks
    task_manager.add_task(
        description='Identify new vulnerabilities in Solidity smart contracts',
        expected_output='Detailed report on new vulnerabilities with examples.'
    )

    task_manager.add_task(
        description='Audit smart contracts for known vulnerabilities',
        expected_output='Audit report with identified vulnerabilities and recommendations.'
    )

    task_manager.add_task(
        description='Develop and execute attack strategies on test contracts',
        expected_output='Detailed report on attack effectiveness and vulnerabilities exploited.'
    )

    # Assign tasks and print summary
    task_manager.assign_tasks()
    task_summary = task_manager.get_task_summary()
    
    for task in task_summary:
        print(f"Task ID: {task['Task ID']}")
        print(f"Description: {task['Description']}")
        print(f"Expected Output: {task['Expected Output']}")
        print('---')

if __name__ == "__main__":
    main()
