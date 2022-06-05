class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score
        print("This is the parent class ", name)


    def change_name(self, name):
        self.name = name
        print("new name is ", name)

    
    def change_age(self, age):
        self.age = age
        print("new age is ", age)

    def Add_track(self, track):
        self.track = track
        print("new track is ", track)

    def get_score(self, get_score):
        self.get_score = get_score
        print("new score is ", get_score)
    #(self, change_name, Change_age, Add_track, Get_score):



Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)
#Bob = Student('Bob', 26, ['FE', 'BE'], 20.98 )
Bob
#  Bob.change, change_name, change_age, add_track, get_score)
# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.Add_track("UI/UX")
Bob.get_score(50)
