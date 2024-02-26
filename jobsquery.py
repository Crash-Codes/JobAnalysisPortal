import graphene
from graphene_mongo import MongoengineObjectType, MongoengineConnectionField

class JobType(MongoengineObjectType):
    class Meta:
        model = Job

class Query(graphene.ObjectType):
    jobs = MongoengineConnectionField(JobType)

def resolve_jobs(root, info):
    return Job.objects()
