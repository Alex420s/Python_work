import typer 
from rich.console import Console
from rich.table import Table
from rich import print
# Local imports
from model import Todo
from database import get_all_todos, delete_todo, insert_todo, complete_todo, update_todo


# Define la consola de rich
console = Console()

# Create a typer.Typer() app
# Es un paquete diseñado para crear herramientas CMD usando tipado
app = typer.Typer()



@app.command(short_help='adds a task and a related category')
def add( task: str, category: str, description:str = "" ):
    """
    Add a task and a related category

    Args:
        task (str): A to-do task
        category (str): A related category
        description (str): Optional description
    """
    # print to te comand line
    typer.echo(f"adding { task }, { category }, { description }") 
    todo = Todo(task, category, description)
    insert_todo(todo)
    list()
 
    
@app.command(short_help='delete a task')
def delete( position: int ):
    typer.echo(f"deleting { position }")
    # indices in UI begin at 1, but in database at 0
    delete_todo(position-1)
    list()


@app.command(short_help='')
def update( position: int, task: str = "", category: str = "", description: str = ' '):
    typer.echo(f"updating { position }")
    update_todo(position-1, task, category, description)
    list()
    
        
@app.command(short_help='')    
def complete( position: int):
    typer.echo(f"complete { position }")   
    complete_todo(position-1)
    list()
    
    
@app.command(short_help='')
def list( ):
    
    tasks = get_all_todos()
    
    console.print("[bold magenta]Todos[/bold magenta]!", "💻")
    
    table = Table(show_header=True, header_style="bold blue")
    table.add_column("#", style="dim", width=6)
    table.add_column("Todo", min_width=20)
    table.add_column("Category", min_width=12, justify="right")
    table.add_column("Done", min_width=12, justify="right")
    table.add_column("Description", min_width=20)
    
    def get_category_color(category):
        COLORS = {'Learn': 'cyan', 'YouTube': 'red', 'Sports': 'cyan', 'Study': 'green'}
        if category in COLORS:
            return COLORS[category]
        return 'white'
    
    
    for idx, task in enumerate(tasks, start=1):
        c = get_category_color(task.category)
        is_done_str = '✅' if task.status == 2 else '❌'
        table.add_row(str(idx), task.task, f'[{c}]{task.category}[/{c}]', is_done_str, task.description)
    console.print(table)
        
if __name__ == "__main__":
    app()