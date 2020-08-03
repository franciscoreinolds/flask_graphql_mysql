import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField

# Objects
from app.graphql.objects.UserObject import User as User
from app.graphql.objects.ProfileObject import Profile as Profile 
from app.graphql.objects.SkillObject import Skill as Skill

# Models
from app.models.User import User as UserModel

class Query(graphene.ObjectType):
    node = relay.Node.Field()

    users = graphene.List(lambda: User, username=graphene.String())

    def resolve_users(self, info, username=None):
        query = User.get_query(info)
        if username:
            query = query.filter(UserModel.username == username)
        return query.all()

    profiles = SQLAlchemyConnectionField(Profile)
    skills = SQLAlchemyConnectionField(Skill)
