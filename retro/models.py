from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    project_name = models.CharField('Project Name', max_length=200)

    def __str__(self):
        return self.project_name


class Team(models.Model):
    team_name = models.CharField('Team', max_length=50)

    def __str__(self):
        return self.team_name


class Category(models.Model):
    category = models.CharField('Category', max_length=200)

    def __str__(self):
        return self.category


STATUS_LIST = (
    ('O', 'Open'),
    ('I', 'In-Progress'),
    ('Cont', 'Continue'),
    ('C', 'Complete'),
)

RETRO_TYPE = (
    ('T', 'Team'),
    ('L', 'Leadership'),
)


class Retro(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    sprint = models.PositiveSmallIntegerField('Sprint')
    description = models.TextField('Description', max_length=200)
    action_item = models.CharField('Action Item', max_length=200)
    owner = models.CharField('Owner', max_length=200)
    retro_type = models.CharField(max_length=1, choices=RETRO_TYPE, default='T')
    status = models.CharField(max_length=4, choices=STATUS_LIST, default='O')
    eta = models.DateField('ETA')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_on = models.DateTimeField('Created On', auto_now_add=True)
    updated_on = models.DateTimeField('Last Modified On', auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.description


class Feedback(models.Model):
    name = models.CharField('Name', max_length=100)
    title = models.CharField('Title', max_length=200)
    description = models.TextField('Description', max_length=500)

    def __str__(self):
        return self.title

