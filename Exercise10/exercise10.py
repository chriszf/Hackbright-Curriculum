#!/usr/bin/env python

def make_student(name, age, hometown):
    return {"name": name,
            "age": age,
            "hometown": hometown,
            "course_list": [] }

def make_course(name, instructor):
    return {"name": name,
            "instructor": instructor}

def print_student(student):
    print "Student Details"
    print "==============="
    print "%s"%(student['name'])
    print "Age: %d"%(student['age'])
    print "Hometown: %s"%(student['hometown'])
    print "Current semester course list"
    for c in student['course_list']:
        print "\t%s"%c['name']
    else:
        print "\tNo courses"
    print ""

def take_course(student, course):
    if course not in student['course_list']:
        student['course_list'].append(course)

def main():
    """Add additional code to test your classes in here"""
    dave = make_student("David", 24, "Orinda, CA")
    print_student(dave)

    anthro = make_course("Anthropology 101", "Professor Snugglesworth")
    take_course(dave, anthro)

if __name__ == "__main__":
    main()
