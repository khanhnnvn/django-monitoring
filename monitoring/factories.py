"""Factories used to create data for testing."""
from __future__ import absolute_import

from datetime import timedelta

from django.contrib.auth import get_user_model
from django.contrib.admin.models import LogEntry, ADDITION, CHANGE, DELETION
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone

from .models import Log

import factory

user_model = get_user_model()
ACTION_LIST = [ADDITION, CHANGE, DELETION]
LEVEL_LIST = ['INFO', 'WARNING', 'ERROR']

class UserFactory(factory.DjangoModelFactory):
    FACTORY_FOR = user_model

    username = factory.Sequence(lambda n: 'testuser {0}'.format(n))


class LogEntryFactory(factory.DjangoModelFactory):
    FACTORY_FOR = LogEntry

    user = factory.SubFactory(UserFactory)
    object_id = factory.SelfAttribute('user.id')
    object_repr = 'User'
    action_flag = factory.Sequence(lambda n: ACTION_LIST[n % len(ACTION_LIST)])
    change_message = factory.Sequence(lambda n: 'Test Change {0}'.format(n))

class LogFactory(factory.DjangoModelFactory):
    FACTORY_FOR = Log

    level = factory.Sequence(lambda n: LEVEL_LIST [n % len(LEVEL_LIST)])
    msg = factory.Sequence(lambda n: 'Log Message {0}'.format(n))
    datetime = factory.Sequence(lambda n: timezone.now() - timedelta(hours=n*12))