import React from 'react';
import { useAddTodo } from './hooks/useAddTodo';
import TodoItemForm from './TodoItemForm';

export default function AddTodo() {
	const { mutate: addTodo } = useAddTodo();

	return (
		<div className="w-full mt-2 items-center bg-gray-100 min-h-screen">
			<h1 className="text-4xl font-bold mb-4">New Todo</h1>
			<TodoItemForm todoItem={undefined} handleSubmit={addTodo} action="Add Todo" />
		</div>
	);
}
