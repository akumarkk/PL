###### Venv
venv, virtualenv, pyenv, pipenv, poetry ;
- Used to contain a specific Python interpreter and software libraries and binaries which are needed to support a project (library or application). 
- Contained in a directory, conventionally named .venv or venv in the project directory, or under a container directory for lots of virtual environments, such as ~/.virtualenvs.
- isolated env for app and it's depdencies!
```
poetry config virtualenvs.in-project true
poetry config virtualenvs.in-project true
poetry init
poetry install # name - dir of app
poetry add requests
poetry remove requests

# publish packages to poetry
poetry config repositories.pypi-test https://pkg.pypi.org/legacy 
poetry config pypi-token.pypi-test <token>

```