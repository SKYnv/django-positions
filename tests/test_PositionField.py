from django.db import models
from django.test import TestCase
from pytest import raises

from django_positions_2 import PositionField
from .models import PositionManagedModel


class TestPositionField(TestCase):
    INSTANCE_COUNT = 5

    def setUp(self):
        self.instances = [
            PositionManagedModel.objects.create() for i in range(self.INSTANCE_COUNT)]

    @property
    def first(self) -> PositionManagedModel:
        return self.instances[0]

    @property
    def last(self) -> PositionManagedModel:
        return self.instances[self.INSTANCE_COUNT - 1]

    @property
    def field(self) -> PositionField:
        field = PositionManagedModel._meta.get_field('position')
        assert isinstance(field, PositionField)
        return field

    def tearDown(self):
        PositionManagedModel.objects.all().delete()

    def test___init__(self):
        assert PositionField().collection is None
        assert PositionField(collection='a').collection == ('a',)
        assert PositionField(collection=b'a').collection == (b'a',)
        assert PositionField(collection=('a', b'b')).collection == ('a', b'b')

        with raises(TypeError):
            PositionField(unique=True)

    def test_get_cache_name(self):
        assert self.field.get_cache_name() == '_position_cache'
        assert PositionField('Note', 'note_position').get_cache_name() == '_note_position_cache'

    def test_contribute_to_class(self):
        with raises(AttributeError, message='position must be accessed via instance.'):
            type(PositionManagedModel.position)

    def test_contribute_to_class__with_uniques(self):
        with raises(TypeError, message='PositionField can\'t be part of a unique constraint.'):
            class BadModel(models.Model):
                pos = PositionField()

                class Meta:
                    unique_together = ('pk', 'pos')

    def test_pre_save(self):
        pass

    def test___set__(self):
        with raises(AttributeError, message='position must be accessed via instance.'):
            PositionManagedModel.position.__set__(None, None)

        expected_position = self.last.position
        first = self.first
        last = self.last

        assert first._position_cache == (0, None)
        first.position = 100
        assert self.first.position == 100              # shouldn't be moved
        assert last.position == expected_position      # shouldn't be moved
        assert first._position_cache == (0, 100)
        assert last._position_cache == (expected_position, None)

        first.save()
        assert first.position == expected_position     # should be moved
        assert last.position == expected_position      # shouldn't be moved
        assert first._position_cache == (expected_position, None)
        assert last._position_cache == (expected_position, None)

        first.refresh_from_db()
        assert first.position == expected_position     # should be still moved (saved)
        assert last.position == expected_position      # shouldn't be moved
        assert first._position_cache == (expected_position, expected_position)
        assert last._position_cache == (expected_position, None)

        last.refresh_from_db()
        assert last.position == expected_position - 1  # should be still moved
        assert first._position_cache == (expected_position, expected_position)
        assert last._position_cache == (expected_position, expected_position - 1)

    def test_get_next_sibling(self):
        field = self.field
        assert field.get_next_sibling(self.last) is None

        for i in range(self.INSTANCE_COUNT - 1):  # don't get last one
            sibling = field.get_next_sibling(self.instances[i])
            sibling_pos = i + 1

            assert sibling is not None
            assert isinstance(sibling, PositionManagedModel)

            assert sibling.pk == self.instances[sibling_pos].pk
            assert sibling.position == sibling_pos

    def test_get_collection(self):
        pass

    def test_remove_from_collection(self):
        pass

    def test_prepare_delete(self):
        pass

    def test_update_on_delete(self):
        pass

    def test_update_on_save(self):
        pass
