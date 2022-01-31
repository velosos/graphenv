import graphene
import movie.api.schema as movie

class Query(movie.Query, graphene.ObjectType):
    pass

class Mutation(movie.Mutation, graphene.ObjectType):
    pass    

schema = graphene.Schema(query=Query, mutation=Mutation)  