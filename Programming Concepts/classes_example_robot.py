class Robot:
    def __init__(self, name, speed, job):
        self.name = name
        self.speed = speed
        self.job = job
    def clean_room(self, time):
        return time / self.speed
    def get_name(self):
        return self.name
    def get_job(self):
        return self.job

my_robot = Robot("Giti Robot", "100MPH", "Can Do everything")
print(my_robot.name)
my_robot.name = "Robot 2.0"
print(my_robot.name)

