# app/graphql/objects/SkillInputObject.py

import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType

class SkillInput(graphene.InputObjectType):
    name = graphene.String()
    score = graphene.Int()