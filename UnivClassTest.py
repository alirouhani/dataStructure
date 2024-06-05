class Univ:
    def __init__(self,first_name,last_name,student_ID):
        self.x = first_name
        self.y = last_name
        self.z = student_ID

    def Identification(self):
        return self.x + " " + self.y

std1=Univ("Ali", "Rouhani","201758")
std2=Univ("Mahboubeh", "Hor","201764")

print(std1.x + " " +std1.y + '\n' + std1.z)
print(std2.x + " " +std2.y + '\n' + std2.z)
print("===================")
print(std1.Identification() + '\n' + std1.z)
print(std2.Identification() + '\n' + std2.z)
