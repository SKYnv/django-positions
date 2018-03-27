from django.db.models import Manager
from django.db.models.query import QuerySet


class PositionQuerySet(QuerySet):
    def __init__(
            self,
            model=None, query=None, using=None,
            position_field_name='position', hints=None):

        super(PositionQuerySet, self).__init__(model, query, using, hints=hints)
        self.position_field_name = position_field_name

    def _clone(self):
        queryset = super(PositionQuerySet, self)._clone()
        queryset.position_field_name = self.position_field_name
        return queryset


class PositionManager(Manager):
    def __init__(self, position_field_name='position'):
        super(PositionManager, self).__init__()
        self.position_field_name = position_field_name

    def get_queryset(self):
        return PositionQuerySet(self.model, position_field_name=self.position_field_name)
