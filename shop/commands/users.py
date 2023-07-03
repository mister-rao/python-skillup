import typer
from typing_extensions import Annotated
from shop.services.authentication import UserSession, Authentication

app = typer.Typer()

user_session = UserSession()
auth = Authentication(user_session)


@app.command()
def signup(
    username: str,
    password: Annotated[
        str, typer.Option(prompt=True, confirmation_prompt=True, hide_input=True)
    ],
):
    auth.signup(username=username, password=password)


@app.command()
def login(
    username: str,
    password: Annotated[str, typer.Option(prompt=True, hide_input=True)],
):
    auth.login(username=username, password=password)


@app.command()
def user():
    auth.check_session()


@app.command()
def logout():
    auth.logout()
