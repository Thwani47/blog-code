import { UseBaseMutationResult } from '@tanstack/react-query';
import { useMutation, useQueryClient } from '@tanstack/react-query';
import { AxiosResponse } from 'axios';
import { useNavigate } from 'react-router-dom';
import { client } from '../api/client';
import { TodoInput } from '../types/todo.types';

const addTodo = async (todo: TodoInput): Promise<AxiosResponse<TodoInput, any>> => {
	return await client.post<TodoInput>('/', todo);
};

export const useAddTodo = (): UseBaseMutationResult<AxiosResponse<TodoInput, any>, unknown, TodoInput, unknown> => {
	const queryClient = useQueryClient();
	const navigate = useNavigate();
	return useMutation({
		mutationFn: (todo: TodoInput) => addTodo(todo),
		onSuccess: () => {
			queryClient.invalidateQueries([ 'todos' ]);
			navigate('/', { replace: true });
		}
	});
};
