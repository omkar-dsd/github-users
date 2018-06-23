from django.db import models


class User(models.Model):

    login = models.CharField(max_length=200, unique=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=200)
    company = models.CharField(max_length=200, blank=True, null=True)
    avatar = models.ImageField(null=True)
    hireable = models.BooleanField(default=False)
    location = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    total_private_repos = models.IntegerField(default=0)
    owned_private_repos = models.IntegerField(default=0)
    public_repos = models.IntegerField(default=0)
    public_gists = models.IntegerField(default=0)
    followers = models.IntegerField(default=0)
    following = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    private_gists = models.IntegerField(default=0)
    disk_usage = models.IntegerField(default=0)
    collaborators = models.IntegerField(default=0)
    two_factor_authentication = models.BooleanField(default=False)
    site_admin = models.BooleanField(default=False)
    # Relevant urls
    url = models.URLField(default=None, blank=True, null=True)
    html_url = models.URLField(default=None, blank=True, null=True)
    followers_url = models.URLField(default=None, blank=True, null=True)
    following_url = models.URLField(default=None, blank=True, null=True)
    gists_url = models.URLField(default=None, blank=True, null=True)
    starred_url = models.URLField(default=None, blank=True, null=True)
    subscriptions_url = models.URLField(default=None, blank=True, null=True)
    organizations_url = models.URLField(default=None, blank=True, null=True)
    repos_url = models.URLField(default=None, blank=True, null=True)
    events_url = models.URLField(default=None, blank=True, null=True)
    received_events_url = models.URLField(default=None, blank=True, null=True)

    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.login

    def user_thumbnail(self):
        '''Returns user's avatar thumbnail if available'''

        if self.avatar:
            return u'<img src="%s" />' % self.avatar.url
        else:
            return '(Not Available)'

    user_thumbnail.short_description = 'Thumbnail'
    user_thumbnail.allow_tags = True


class Request(models.Model):
    '''Maintain the search request timestamp'''

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'request'


class RequestSummary(User):
    class Meta:
        proxy = True
        verbose_name = 'Summary'
        verbose_name_plural = 'Summary'
