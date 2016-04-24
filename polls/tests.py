from datetime import datetime, timedelta
from django.test import TestCase

import django
import pytz

from polls.models import Question

django.setup()

# Create your tests here.

tz = pytz.timezone('America/Winnipeg')


class TestPollQuestion(TestCase):

    def setUp(self):
        pub_date = datetime.now(tz=tz) - timedelta(days=5)
        self.instance = Question(question_text="What is your favourite beach?",
                                 pub_date=pub_date)
        self.instance.save()

    def test_new_question(self):
        pub_date = datetime.now(tz=tz)
        new = Question.objects.create(question_text="What?",
                                      pub_date=pub_date)
        assert(new.question_text == 'What?')

    def test_question_count(self):
        self.assertEqual(len(Question.objects.all()), 1)

    def test_pubdate_is_past(self):
        self.assertTrue(self.instance.pub_date < datetime.now(tz=tz))
