import { QueryObserverResult, useQuery } from '@tanstack/react-query';
import { AxiosResponse } from 'axios';
import { client } from '../api/client';
import { TodoItem } from '../types/todo.types';

const fetchTodo = async (todoId: number): Promise<AxiosResponse<TodoItem, any>> => {
	return await client.get<TodoItem>(`/${todoId}`);
};

export const useFetchTodo = (todoId: number): QueryObserverResult<TodoItem, any> => {
	return useQuery<TodoItem, any>({
		queryFn: async () => {
			const { data } = await fetchTodo(todoId);
			return data;
		},
		queryKey: [ 'todo', todoId ]
	});
};
