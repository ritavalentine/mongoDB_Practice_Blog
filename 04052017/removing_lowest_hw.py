import pymongo

connection = pymongo.MongoClient("mongodb://localhost")


def remove_lowest_score():
    db=connection.school
    grades = db.students
    students = grades.distinct('student_id')
    count = 0
    for student in students:
        print (student)
        #lowest_score = grades.find({'type':'homework', 'student_id':student},{'score':1,'_id':0}).sort("score",pymongo.ASCENDING).limit(1)
        grades.find_one_and_delete({'type':'homework', 'student_id':student},sort=[("score",pymongo.ASCENDING)])
        #grades.remove({'type':'homework', 'student_id':student,'score':lowest_score})



remove_lowest_score()
