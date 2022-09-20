using Microsoft.EntityFrameworkCore;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddDbContext<TodoDb>(options => options.UseInMemoryDatabase("Todos"));

builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

var app = builder.Build();

if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI(options =>
    {
        options.SwaggerEndpoint("/swagger/v1/swagger.json", "v1");
        options.RoutePrefix = string.Empty;
    });
}

// Endpoints
app.MapGet("/todos", async (TodoDb db) => await db.Todos.ToListAsync());
app.MapGet("todos/{id:guid}", async (Guid id, TodoDb db) =>
{
    var todo = await db.Todos.FindAsync(id); 
    return todo == null ? Results.NotFound() : Results.Ok(todo);
});
app.MapGet("/todos/complete", async (TodoDb db) => await db.Todos.Where(todo => todo.IsComplete).ToListAsync());
app.MapPost("todos", async (Todo todo, TodoDb db) =>
{
    db.Todos.Add(todo);
    await db.SaveChangesAsync();

    return Results.Created($"/todos/{todo.Id}", todo);
});

app.MapPut("todos/{id:guid}", async (Guid id, Todo update, TodoDb db) =>
{
    var todo = await db.Todos.FindAsync(id);

    if (todo == null)
    {
        return Results.NotFound();
    }

    todo.Title = update.Title;
    todo.IsComplete = update.IsComplete;

    await db.SaveChangesAsync();
    return Results.NoContent();
});

app.MapDelete("todos/{id:guid}", async (Guid id, TodoDb db) =>
{
    var todo = await db.Todos.FindAsync(id); 
    if (todo == null)
    {
        return Results.NotFound();
    }

    db.Todos.Remove(todo);
    await db.SaveChangesAsync();
    return Results.NoContent();
});

app.Run();

public class Todo
{
    public Guid Id {get; set;} = Guid.NewGuid();
    public string? Title {get; set;}
    public bool IsComplete {get; set;}
}

internal class TodoDb : DbContext
{
    public TodoDb(DbContextOptions<TodoDb> options) : base(options)
    {
    }

    public DbSet<Todo> Todos => Set<Todo>();
}