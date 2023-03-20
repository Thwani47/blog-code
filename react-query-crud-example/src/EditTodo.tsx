
import React from 'react';
import { useParams } from 'react-router-dom';

import { useFetchTodo } from './hooks/useFetchTodo';
import { useEditTodo } from './hooks/useEditTodo';
import TodoItemForm from './TodoItemForm';


export default function EditTodo() {
	const { id } = useParams();
	const { data: todoItem, isLoading } = useFetchTodo(id ? parseInt(id) : 0);

	const { mutate: editTodo } = useEditTodo(id ? parseInt(id) : 0);
	return (
		<div className="w-full mt-2 items-center bg-gray-100 min-h-screen">
			<h1 className="text-4xl font-bold mb-4">Edit Todo</h1>
			{isLoading ? <h1>Fetching todo...</h1> : <TodoItemForm todoItem={todoItem} handleSubmit={editTodo} action="Edit Todo"/> }
		</div>
	);
}
