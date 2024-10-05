#test-queue
import queue

# Define a TaskManager class that uses a queue
class TaskManager:
    def __init__(self):
        self.task_queue = queue.Queue()

    # Method to add tasks to the queue
    def add_task(self, task):
        print(f'Adding task: {task}')
        self.task_queue.put(task)

    # Method to process tasks from the queue
    def process_tasks(self):
        while not self.task_queue.empty():
            try:
                task = self.task_queue.get_nowait()  # Use get_nowait to avoid blocking
                print(f'Processing task: {task}')
                # Simulate task processing
                self.task_queue.task_done()
            except queue.Empty:
                print('No more tasks in the queue.')
                break

def main():
    try:
        # Instantiate the TaskManager
        manager = TaskManager()

        # Add tasks
        manager.add_task('Task 1')
        manager.add_task('Task 2')
        manager.add_task('Task 3')

        # Process tasks
        manager.process_tasks()
    except Exception as e:
        print(f'An error occurred: {e}')

if __name__ == '__main__':
    main()
    ...

