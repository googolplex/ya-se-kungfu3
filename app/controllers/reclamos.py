from ferris import Controller, scaffold, route
from ferris.components.pagination import Pagination
from ferris.components.search import Search



class Reclamos(Controller):
    class Meta:
        prefixes = ('user',)
        components = (scaffold.Scaffolding,Pagination,Search)
        pagination_limit = 5

    user_list = scaffold.list  # lists all posts
    user_view = scaffold.view  # view a post
    user_add = scaffold.add  # add a new post
    user_edit = scaffold.edit  # edit a post
    user_delete = scaffold.delete  # delete a post
    @route
    def todoslosreclamosordenados(self):
        # self.context['reclamos'] = self.meta.Model.todos_reclamos()
        self.context['reclamos'] = self.components.search()

# agregado para dar orden al listado
# hecho el 14.7.2016
# por roger cillo

    def list(self):
        self.context['reclamos'] = self.meta.Model.todos_reclamos()
