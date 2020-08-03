# app/graphql/objects/UserObject.py

import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType
from app.models.Skill import Skill as SkillModel

class Skill(SQLAlchemyObjectType):
    class Meta:
        model = SkillModel
        interfaces = (relay.Node,)