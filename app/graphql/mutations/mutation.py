import graphene
from app import db
from app.graphql.mutations.User.UserMutation import UserMutation
from app.graphql.mutations.Profile.ProfileMutation import ProfileMutation

class Mutation(graphene.ObjectType):
    mutate_user = UserMutation.Field()
    mutate_profile = ProfileMutation.Field()
