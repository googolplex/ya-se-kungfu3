from ferris.tests.lib import WithTestBed
from app.models.reclamo import Reclamo


class ProbarReclamo(WithTestBed):

    def testQueries(self):
        # log in user one
        self.loginUser('user1@example.com')

        # create two posts
        post1 = Reclamo(titulo='Titulo 1',contenido="Contenido1")
        post1.put()

        post2 = Reclamo(titulo='Titulo 2',contenido="Contenido2")
        post2.put()

        # log in user two
        self.loginUser('user2@example.com')

        # create two more posts
        post3 = Reclamo(titulo='Titulo 3',contenido="Contenido3")
        post3.put()

        post4 = Reclamo(titulo='Titulo 3',contenido="Contenido3")
        post4.put()

        # Get all posts
        all_posts = list(Reclamo.todos_reclamos())

        # Make sure there are 4 posts in total
        assert len(all_posts) == 4

        # Make sure they're in the right order
        assert all_posts == [post4, post3, post2, post1]

        # Make sure we only get two for user2, and that they're the right posts
        user2_posts = list(Reclamo.todos_reclamos_por_usuario())

        assert len(user2_posts) == 2
        assert user2_posts == [post4, post3]