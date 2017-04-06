import pymongo
from bson.son import SON

connection = pymongo.MongoClient("mongodb://localhost")


def remove_lowest_score():
    db=connection.school
    students = db.students
    student_ids = students.distinct('_id')
    count = 0
    for student in student_ids:
        command = [ { "$unwind": "$scores" }, {"$match":{"scores.type":"homework", "_id":student}},{'$group': {"_id":student,'low_score':{'$min':'$scores.score'}}},{"$sort": SON([("scores.score",1), ("_id", -1)])}]
        results = students.aggregate(command)
        for result in results:
            print result['low_score']
            print result['_id']
            students.update_one({'_id':student},{ '$pull': {'scores':{ 'score':result['low_score'], 'type':'homework' } }})

        #results = students.find_one({'_id': student, 'scores.type': "homework"},{'scores.score':1,'scores.type':'homework'},sort=[("scores.score",pymongo.ASCENDING)])
        #print results[1]
#        students.update_one({'_id': result['_id'], 'scores.score':});

remove_lowest_score()
