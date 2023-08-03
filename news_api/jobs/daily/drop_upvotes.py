# @daily /newsproject/manage.py runjobs daily

from django_extensions.management.jobs import DailyJob
from news_api.models import Upvote


class DropUpvotesJob(DailyJob):
    """
    Recurring work for cleaning up posts upvotes

    Need to be run with cron
    """

    def execute(self):
        Upvote.objects.all().delete()
