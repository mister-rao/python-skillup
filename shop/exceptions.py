import typer


class ShopYooExit(typer.Exit):
    def __init__(self, message: str):
        super().__init__(1)
        self.print_error(message)
        self.message = message

    def print_error(self, msg):
        error = typer.style("Error:", fg=typer.colors.RED, bold=True)
        typer.echo(f"{error} {msg}")
