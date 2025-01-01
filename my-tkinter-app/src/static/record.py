class ActionLogger:
    def __init__(self, log_file='actions.log'):
        self.log_file = log_file

    def log_action(self, action):
        with open(self.log_file, 'a') as file:
            file.write(f"{action}\n")

    def read_logs(self):
        with open(self.log_file, 'r') as file:
            return file.readlines()

    def clear_logs(self):
        open(self.log_file, 'w').close()