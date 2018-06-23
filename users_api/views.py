from .filters import UserFilter
from django.db.models import Count
from django.http import HttpResponse, JsonResponse
from django.views import View
from rest_framework import generics
from rest_framework.response import Response
from users_api.models import *
from users_api.serializers import *


class UserList(generics.ListCreateAPIView):
    '''API to view list of all available users
    - View list of existing users
    - Create new user, `login` and `email` are mandatory fields
    '''

    def create(self, serializer):
        '''Overwriting the default functionality to perform create or update'''

        V = Validator()
        validated_user_data = V.user_data(self.request.POST.dict())

        # Update if user with same `login` and `email` is POSTed
        # Else create new user record
        obj, created = User.objects.update_or_create(
            login=self.request.POST.get('login'),
            email=self.request.POST.get('email'),
            defaults=validated_user_data)

        obj.avatar = self.request.FILES.get('avatar')
        obj.save()

        if obj.avatar:
            validated_user_data.update({'avatar': obj.avatar.name})

        return Response(validated_user_data)

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    '''API to View, Update & Delete details of request User'''

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserSearchView(View):
    '''Search view for users with filters'''

    def get(self, request):

        R = Request()
        user_list = User.objects.all()
        user_filter = UserFilter(request.GET, queryset=user_list)
        query_set = user_filter.qs
        response = {'users': [usr for usr in query_set.values()],
                    'total': len(query_set)}
        R.save()

        return JsonResponse(response)


class Validator():
    '''Validator for various data sections'''

    def user_data(self, data):
        '''Validate and return user data'''

        if data.get('hireable') != 'True':
            hireable = False
        if 'total_private_repos' in list(data.keys()) and not data.get('total_private_repos'):
            del data['total_private_repos']
        if 'owned_private_repos' in list(data.keys()) and not data.get('owned_private_repos'):
            del data['owned_private_repos']
        if 'public_repos' in list(data.keys()) and not data.get('public_repos'):
            del data['public_repos']
        if 'public_gists' in list(data.keys()) and not data.get('public_gists'):
            del data['public_gists']
        if 'followers' in list(data.keys()) and not data.get('followers'):
            del data['followers']
        if 'following' in list(data.keys()) and not data.get('following'):
            del data['following']
        if 'private_gists' in list(data.keys()) and not data.get('private_gists'):
            del data['private_gists']
        if 'disk_usage' in list(data.keys()) and not data.get('disk_usage'):
            del data['disk_usage']
        if 'two_factor_authentication' in list(data.keys()) and not data.get('two_factor_authentication'):
            del data['two_factor_authentication']
        if 'collaborators' in list(data.keys()) and not data.get('collaborators'):
            del data['collaborators']
        if 'site_admin' in list(data.keys()) and not data.get('site_admin'):
            del data['site_admin']
        if data.get('csrfmiddlewaretoken'):
            del data['csrfmiddlewaretoken']

        return data
