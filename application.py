from os import getenv
from os.path import dirname,isfile,join
from dotenv import load_dotenv

# A partir do arquivo atual adicione ao path o arquivo .env
_ENV_FILE = join(dirname(__file__), '.env')

# Existindo o arquivo faça a leitura do arquivo atraves da funcao load_do
if isfile(_ENV_FILE):
    load_dotenv(dotenv_path=_ENV_FILE)

from apps import create_app

# Instancia nossa funcao factory criada anteriormente
app = create_app(getenv('FLASK_ENV') or 'default')

if __name__ == '__main__':
    ip = '0.0.0.0'
    port = app.config['APP_PORT']
    debug = app.config['DEBUG']

    # executa o servidor web do flask
    app.run(
        host=ip, debug=debug, port=port, use_reloader=debug
    )
