# Projeto Flask Api User!

Uma aplicação REST com Python e Flask Framework. No final deste projeto você será capaz de rodar localmente uma API com autenticação JWT.


# Dependências utilizadas

### Dependências de Test.

**flake8** - é um styleguide e também uma ferramenta de lint para melhorar a codificação.
**pytest** - é um framework de testes simples. `pytest-cov, pytest-flask, pytest-runner` são extensões do `pytest`
**Faker** - é um utilitário para gerar dados fakes e randômicos, por exemplo nomes de países, cidades, pessoas, data de 
nascimento, cores, datas e etc..

### Dependências de Desenvolvimento.

**Ipython** - melhora a experiência em utilizar o `REPL` do python adicionando cores, auto complete e demais outras facilidades.
**ipdb** - é um utilitário para melhorar a experiência e uso da depuração de erros do python `pdb`. Por utilizar o `Ipython` deu-se o nome de `ipdb`.
**flask-shell-ipython** - substituí o `flask shell` instalado por padrão pelo `flask`utilizando o `ipython`.
**isort** - nos ajuda a padronizar os `imports` de pacotes em ordem alfabética e por seções. É útil pois cada desenvolvedor tem manias e pode fazer de um jeito. Com esse utilitário definimos um padrão e a ferramenta fica responsável por automatizar esse processo nos arquivos da aplicação.

### Dependências de Produção.

**gunicorn** - é responsável por servir um servidor http utilizando o wsgi.


### Executando o projeto

- Criar o arquivo .env que é uma copia do .env-example e dar o comando flask run
