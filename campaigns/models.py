from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=200, blank=False)
    code = models.CharField(max_length=50, blank=False, unique=True, db_index=True)
    color_set = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name


class Hashtag(models.Model):
    name = models.CharField(max_length=50, blank=False, unique=True, db_index=True)

    def __str__(self) -> str:
        return self.name


class Campaign(models.Model):
    name = models.CharField(max_length=200, blank=False, db_index=True)
    description = models.CharField(max_length=200)
    budget = models.FloatField()
    start_date = models.DateTimeField(blank=False)
    end_date = models.DateTimeField(blank=False)

    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    hashtags = models.ManyToManyField(Hashtag)

    def __str__(self) -> str:
        return self.name
