# -*- coding: utf-8 -*-
from django.db import models

from rulez import registry as rulez_registry

from uuidfield import UUIDField
from jsonfield import JSONField

from beer.utils import get_namedtuple_choices

SENSOR_TYPES = get_namedtuple_choices('SENSOR_TYPES', (
    ('temperature_humidity', 'temperature_humidity', 'Temperature & Humidity'),
    ('weight', 'weight', 'Hive Weight'),
    ('in_out_counter', 'in_out_counter', 'In/Out Counter'),
    ('video_stream', 'video_stream', 'Video Stream'),
))

SENSOR_STATUSES = get_namedtuple_choices('SENSOR_STATUSES', (
    ('unknown', 'unknown', 'Unknown'),
    ('receiving', 'receiving', 'Receiving'),
    ('disconnected', 'disconnected', 'Disconnected'),
))


class Sensor(models.Model):
    uuid = UUIDField(auto=True, db_index=True)
    name = models.CharField(choices=SENSOR_TYPES.get_choices(), max_length=128, db_index=True)
    status = models.CharField(choices=SENSOR_STATUSES.get_choices(), max_length=128, db_index=True)
    boxes = models.ManyToManyField('box.Box')
    data = JSONField(default={})

    def can_read(self, user):
        return user.is_authenticated()

    def can_edit(self, user):
        return True

    def can_delete(self, user):
        return True


rulez_registry.register("can_read", Sensor)
rulez_registry.register("can_edit", Sensor)
rulez_registry.register("can_delete", Sensor)
