from create_task import create_task

if __name__ == '__main__':
    print('Create Task (interactive mode):')
    summary = input("Enter summary: ")
    description = input("Enter description: ")
    create_task(summary, description)