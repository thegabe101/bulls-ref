
from bard.app import db
from bard.models.common import IdModel, make_textid
from datetime import datetime
from sqlalchemy.dialects.postgresql import JSONB
import logging

log = logging.getLogger(__name__)


class Collection(db.Model, IdModel):
    label = db.Column(db.Unicode)

    def touch(self):
        db.session.add(self)

    def update(self, data):
        self.label = data.get("label", self.label)
        self.touch()
        db.session.flush()

    @classmethod
    def create(cls):
        collection = cls()
        # collection.id = str(make_textid())
        collection.update({})
        return collection

    def to_dict(self):
        data = self.to_dict_dates()
        data.update(
            {
                # "id": str(self.id),
                "player_id": str(self.id),
            }
        )
        return data

    def __repr__(self):
        return '<Collection %r>' % self.label