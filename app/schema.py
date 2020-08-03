import graphene

from app.graphql.mutations.mutation import Mutation
from app.graphql.queries.query import Query

schema = graphene.Schema(query=Query, mutation=Mutation)
