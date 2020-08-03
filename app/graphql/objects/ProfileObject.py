# app/graphql/objects/ProfileObject.py

import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType

# Models
from app.models.Profile import Profile as ProfileModel
from app.models.Skill import Skill as SkillModel

# Objects
from app.graphql.objects.SkillObject import Skill as Skill

class Profile(SQLAlchemyObjectType):
    class Meta:
        model = ProfileModel
        interfaces = (relay.Node,)

    skills = graphene.List(lambda: Skill, name=graphene.String(), score=graphene.Int())

    def resolve_skills(self, info, name=None, score=None):
        query = Skill.get_query(info=info)
        query = query.filter(SkillModel.profile_id == self.id)
        if name:
            query = query.filter(SkillModel.name == name)
        if score:
            query = query.filter(SkillModel.score == score)

        return query.all()
