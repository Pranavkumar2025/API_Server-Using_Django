# from django.contrib import admin
# from django.urls import path
# from graphene_django.views import GraphQLView
# from bankapi.schema import schema

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('gql/', GraphQLView.as_view(graphiql=True, schema=schema)),  # Ensure this is correct
# ]


from django.contrib import admin
from django.urls import path
from graphene_django.views import GraphQLView
from banks.views import home  # Import the home view from the banks app
from bankapi.schema import schema  # GraphQL schema

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin interface
    path('gql/', GraphQLView.as_view(graphiql=True, schema=schema)),  # GraphQL testing interface
    path('', home, name='home'),  # Home page route
]

