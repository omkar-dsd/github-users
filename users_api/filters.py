from users_api.models import *
import django_filters


class UserFilter(django_filters.FilterSet):
    '''Dynamic filters for User Search API'''

    class Meta:
        model = User
        fields = ['login', 'name', 'company', 'email', 'hireable', 'location', 'total_private_repos', 'owned_private_repos', 'public_repos',
                  'public_gists', 'followers', 'following', 'created_at', 'private_gists', 'disk_usage', 'collaborators', 'two_factor_authentication', 'site_admin']
