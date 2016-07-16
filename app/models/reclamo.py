from ferris import BasicModel
from google.appengine.ext import ndb
from google.appengine.api import users
from ferris.behaviors.searchable import Searchable


class Reclamo(BasicModel):
    class Meta:
        behaviors = (Searchable,)
        search_index = ('global',)

    titulo    = ndb.StringProperty(required=True)
    contenido = ndb.StringProperty(required=True)
    # contenido = ndb.TextProperty()
    @classmethod
    def todos_reclamos(cls):
        return cls.query().order(-cls.created)

    @classmethod
    def todos_reclamos_por_usuario(cls,user=None):
        if not user:
            user = users.get_current_user()
        return cls.find_all_by_created_by(user).order(-cls.created)
