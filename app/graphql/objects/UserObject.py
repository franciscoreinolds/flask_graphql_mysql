# app/graphql/objects/UserObject.py

import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType
from app.models.User import User as UserModel

class User(SQLAlchemyObjectType):

    class Meta:
        model = UserModel
        interfaces = (relay.Node,)
