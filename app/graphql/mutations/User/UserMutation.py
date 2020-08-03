# app/graphql/mutations/User/UserMutation.py

import graphene
from app import db

# Objects
from app.graphql.objects.UserObject import User as User

# Models
from app.models.User import User as UserModel

class UserMutation(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        name = graphene.String(required=True)
        last_name = graphene.String(required=True)

    user = graphene.Field(lambda: User)

    def mutate(self, info, username, name, last_name):
        user = UserModel(username=username, name=name, last_name=last_name)

        db.session.add(user)
        db.session.commit()

        return UserMutation(user=user)
