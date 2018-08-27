from google.appengine.ext import ndb

class Student(ndb.Model):
    first_name = ndb.StringProperty(required=True)
    last_name = ndb.StringProperty(required=True)
    school_name = ndb.StringProperty(required=True)
    major = ndb.StringProperty(required=True)
    email = ndb.StringProperty(required=True)
    user_id = ndb.StringProperty(required=True)
    languages_spoken = ndb.StringProperty(required=True, repeated=True)
    friends = ndb.StringProperty(required=True, repeated=True)

class StudyGroup(ndb.Model):
    name = ndb.StringProperty(required=True)
    description = ndb.StringProperty(required=True)
    members = ndb.StringProperty(required=True, repeated=True)

#https://cloud.google.com/appengine/docs/standard/python/blobstore/
