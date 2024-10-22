#!/usr/bin/env python3

""" Module for PyMongo using"""


def top_students(mongo_collection):
    """ Returns students sorted by average score"""
    top_student = mongo_collection.aggregate([
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ])

    return top_student
