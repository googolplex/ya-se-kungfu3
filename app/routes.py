from ferris.core import routing, plugins

# Routes all App handlers
routing.auto_route()

# Default root route
# modificado por roger cillo
# el 2016.7.13a
# routing.default_root()


routing.redirect('/', to='/user/reclamos')

# Plugins
#plugins.enable('settings')
#plugins.enable('oauth_manager')
