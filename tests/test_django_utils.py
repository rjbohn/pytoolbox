# -*- encoding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals

from pytoolbox.django.utils import collections

from . import base


class TestDjangoUtils(base.TestCase):

    tags = ('django', 'utils')

    def test_FieldsToValuesLookupDict(self):
        class File(object):
            pass

        class Media(object):
            pass

        class MediaForm(object):
            class Meta:
                model = Media

        numbers = collections.FieldsToValuesLookupDict(
            'numbers', {'MediaForm.name': 1, 'Media.url': 2, 'url': 3})
        self.equal(numbers[(File, 'url')], 3)
        self.equal(numbers[(Media, 'url')], 2)
        self.equal(numbers[(MediaForm, 'url')], 2)
        self.equal(numbers[(MediaForm, 'name')], 1)
