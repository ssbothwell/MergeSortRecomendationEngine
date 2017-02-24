class Person:
    """ Base class for all people """

    def __init__(self, name):
        self.name = name
        self.skills = []
        self.wantsToLearn = []

    def addSkill(self, skill):
        self.skills.append(skill)
