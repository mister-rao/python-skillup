import typer
from typing_extensions import Annotated
from shop.services.authentication import UserSession, AuthenticationService

app = typer.Typer()

user_session = UserSession()
auth = AuthenticationService(user_session)


@app.command()
def signup(
    username: Annotated[str, typer.Option(prompt=True)],
    password: Annotated[
        str, typer.Option(prompt=True, confirmation_prompt=True, hide_input=True)
    ],
):
    auth.signup(username=username, password=password)


@app.command()
def login(
    username: Annotated[str, typer.Option(prompt=True)],
    password: Annotated[str, typer.Option(prompt=True, hide_input=True)],
):
    auth.login(username=username, password=password)


@app.command()
def user():
    auth.check_session()


@app.command()
def logout():
    auth.logout()
