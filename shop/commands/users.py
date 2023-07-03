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
def profile():
    auth.is_authenticated()
    auth.print_current_user()


@app.command()
def list():
    auth.list_users()


@app.command()
def logout():
    auth.is_authenticated()
    auth.logout()
