import React from 'react';
import { ErrorMessage, Field, Form, Formik } from 'formik';
import * as yup from 'yup';
import { TodoInput, TodoItem } from './types/todo.types';

type Props = {
	action: string;
	todoItem: TodoItem | undefined;
	handleSubmit: (values: TodoInput) => void;
};

export default function TodoItemForm({ todoItem, handleSubmit, action }: Props) {
	return (
		<Formik
			initialValues={{
				title: todoItem ? todoItem.title : '',
				complete: todoItem ? todoItem.complete : false
			}}
			validationSchema={yup.object({
				title: yup.string().required('Title is required')
			})}
			onSubmit={(values: TodoInput) => handleSubmit(values)}
		>
			<Form>
				<div className="mb-2">
					<label htmlFor="title" className="mr-2">
						Title
					</label>
					<Field
						name="title"
						type="text"
						id="title"
						className="shadow appearance-none border rounded py-1 px-2 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
					/>
					<ErrorMessage name="title" component="span" className="text-red-500" />
				</div>
				<div>
					<label htmlFor="complete" className="mr-2">
						Complete
					</label>
					<Field name="complete" type="checkbox" id="complete" />
				</div>
				<button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-1 px-2 ml-2 rounded">
					{action}
				</button>
			</Form>
		</Formik>
	);
}
