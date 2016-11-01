def part1(studentList):
    for listVal in studentList:
        print listVal['first_name'], listVal['last_name']

def part2(studentInstructorList):
    print "Students"
    lineNo = 1
    for key, data in studentInstructorList.items():
        for listVal in data:
            print str(lineNo), "-", listVal['first_name'], listVal['last_name'], "-",   str(len(listVal['first_name']) + len(listVal['last_name']))
            if lineNo == 4:
                print "Instructors"
                lineNo = 0
            lineNo+=1

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

# part1(students)

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

part2(users)
