from django.test import TestCase
from .models import PositionManagedModel


class TestManagers(TestCase):
    def test_clone(self):
        PositionManagedModel.objects.create()
        objects = PositionManagedModel.objects.all()
        cloned = objects._clone()
        assert len(objects)
        assert len(cloned) == len(objects)

        for base, clone in zip(objects, cloned):  # type: PositionManagedModel
            assert base.pk == clone.pk
            assert base.name == clone.name
            assert base.position == clone.position

    def test_get_queryset(self):
        pk1 = PositionManagedModel.objects.create(name=None).pk
        PositionManagedModel.objects.create(name='__abc__')
        PositionManagedModel.objects.create(name='a__abc__d')
        PositionManagedModel.objects.create(name='__abc__d')

        val1 = PositionManagedModel.objects.get(pk=pk1)
        assert val1
        assert val1.pk == pk1

        qs = PositionManagedModel.objects.filter(name__contains='__abc__')
        assert qs.count() == 3

        qs = PositionManagedModel.objects.filter(name=None)
        assert qs.count() == 1

    def test_reposition(self):
        PositionManagedModel.objects.all().delete()

        PositionManagedModel.objects.create(position=1)
        PositionManagedModel.objects.create(position=2)
        PositionManagedModel.objects.create(position=0)
        PositionManagedModel.objects.create(position=2)

        # check if values are unique
        positions_qs = PositionManagedModel.objects.values('position')
        assert positions_qs.count() == positions_qs.distinct().count()
