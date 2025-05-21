import os
import flask



def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    # Crear la carpeta instance si no existe
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Importar y registrar la base de datos
    from . import db
    db.init_app(app)

    # Registrar blueprint de autenticación
    from . import auth
    app.register_blueprint(auth.bp)

    # Registrar blueprint del blog
    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    return app
