# −*− coding: UTF−8 −*−

import web

#Version

print web.__version__

# URL:

urls = (
    # regex para url', 'clase donde se envia la petición'
    '/', 'index'

)

# Aplicacion donde se especifican las urls.      
app = web.application(urls, globals())

class index:
    def GET(self):
        return 'Tonces Mostro'

if __name__ == "__main__":
    app.run()
