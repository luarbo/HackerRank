class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = scores

    def calculate (self):
        average=0
        for eachscore in scores:
            average = average + eachscore
        average = average/len(scores)
        if average<40:
            return 'T'
        elif 40<=average<55:
            return 'D'
        elif 55<=average<70:
            return 'P'
        elif 70<=average<80:
            return 'A'
        elif 80<=average<90:
            return 'E'
        else:
            return 'O'
