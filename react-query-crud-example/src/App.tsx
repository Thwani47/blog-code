import { useNavigate } from 'react-router-dom';
import './App.css';
import { useFetchTodos } from './hooks/useFetchTodos';
import {useDeleteTodo} from './hooks/useDeleteTodo'

function App() {
  const { data: todos, isLoading, isError } = useFetchTodos();
  const {mutate : deleteTodo} = useDeleteTodo()
  const navigate = useNavigate();
  return (
    <div className="w-full mt-2 items-center bg-gray-100 min-h-screen">
      <h1 className="text-4xl font-bold mb-4">Todo List</h1>
      <button className="bg-green-500 hover:bg-green-700 text-white font-bold py-1 px-2 ml-2 rounded mb-4" onClick={() => navigate('/add-todo')}>New Todo</button>
      <hr className="mb-2" />
      {
        isLoading ? <h1>Loading...</h1> : isError ? <h1>Error fetching todos</h1> : (
          <ul>
            {todos?.map(todo => {
              return <li className={`mb-2 text-xl ${todo.complete ? 'line-through' : ''}`} key={todo.id}>{todo.title}
                <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-1 px-2 ml-2 rounded" onClick={() => navigate(`/edit-todo/${todo.id}`)}>Edit</button>
                <button className="bg-red-500 hover:bg-red-700 text-white font-bold py-1 px-2 ml-2 rounded" onClick={() => deleteTodo(todo.id)}>Delete</button>
              </li>
            })}
          </ul>
        )
      }
    </div>
  );
}

export default App;
