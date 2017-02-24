from personClass import *
def createMenteeIndex(menteeObject):
    return map(lambda x:
                    menteeObject.wantsToLearn.index(x),
                    menteeObject.wantsToLearn
                )

def createMentorIndex(mentorObject, menteeObject):
    return map(lambda x:
                    menteeObject.wantsToLearn.index(x),
                    mentorObject.skills
                )

def mergeSortInversions(arr):
    if len(arr) == 1:
        return arr, 0
    else:
        a = arr[:len(arr)/2]
        b = arr[len(arr)/2:]

        a, ai = mergeSortInversions(a)
        b, bi = mergeSortInversions(b)
        c = []

        i = 0
        j = 0
        inversions = 0 + ai + bi

        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                c.append(a[i])
                i += 1
            else:
                c.append(b[j])
                j += 1
                inversions += (len(a)-i)

        c += a[i:]
        c += b[j:]

        return c, inversions

def rankMentors(mentee, mentorList):
    """ return ranked list of mentors accepts a mentee object and a
    list of mentor objects """

    # Create menteeIndex
    menteeIndex = createMenteeIndex(mentee)

    # create list of mentorIndexes
    mentorIndexes = [ [x, createMentorIndex(x, mentee) ] for x in mentorList ]

    # Count inversions for mentors
    mentorInversions = [ [x[0].name, mergeSortInversions(x[1])[1]] for x in mentorIndexes ]
    return sorted(mentorInversions, reverse=True)

# Instantiate Mentee object
mentee = Person('solomon')
mentee.wantsToLearn = ['python','ruby','javascript','c++','lisp']

# Instantiate mentor objects
frank = Person('frank')
sally = Person('sally')
todd = Person('todd')

frank.skills = ['ruby','javascript','lisp','c++','python']
sally.skills = ['python','javascript','c++','ruby','lisp']
todd.skills = ['python','ruby','lisp','javascript','c++']

# Create Mentor List
mentorList = [ frank, sally, todd ]

print rankMentors(mentee, mentorList)

