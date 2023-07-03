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
    print(f"User Signed Up: {username}")


@app.command()
def login(
    username: Annotated[str, typer.Option(prompt=True)],
    password: Annotated[str, typer.Option(prompt=True, hide_input=True)],
):
    auth.login(username=username, password=password)
    print(f"User Logged In: {username}")


@app.command()
def profile():
    auth.is_authenticated()
    user = auth.session.current_user
    print(f"username: {user}")


@app.command()
def list():
    print("All users:")
    auth.list_users()


@app.command()
def logout():
    auth.is_authenticated()
    auth.logout()
