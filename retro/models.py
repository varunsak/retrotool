from django.db import models


class Project(models.Model):
    project_name = models.CharField('Project Name', max_length=200)

    def __str__(self):
        return self.project_name


class Team(models.Model):
    team_name = models.CharField('Team', max_length=50)

    def __str__(self):
        return self.team_name


class Sprint(models.Model):
    sprint_number = models.BigIntegerField('Sprint')

    def __str__(self):
        return str(self.sprint_number)


class Owner(models.Model):
    owner_name = models.CharField('Owner', max_length=50)

    def __str__(self):
        return self.owner_name


class Status(models.Model):
    status_item = models.CharField('Status', max_length=50)

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Statuses'

    def __str__(self):
        return self.status_item


class Retro(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    sprint = models.ForeignKey(Sprint, on_delete=models.CASCADE)
    description = models.CharField('Description', max_length=200)
    action_item = models.CharField('Action Item', max_length=200)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    eta = models.DateField('ETA')

    def __str__(self):
        return self.description