import { UseBaseMutationResult } from '@tanstack/react-query';
import { useMutation, useQueryClient } from '@tanstack/react-query';
import { AxiosResponse } from 'axios';
import { client } from '../api/client';

const deleteTodo = async (todoId: number): Promise<AxiosResponse<any, any>> => {
	return await client.delete(`/${todoId}`);
};

export const useDeleteTodo = (): UseBaseMutationResult<AxiosResponse<any, any>, unknown, number, unknown> => {
	const queryClient = useQueryClient();
	return useMutation({
		mutationFn: (todoId: number) => deleteTodo(todoId),
		onSuccess: () => {
			queryClient.invalidateQueries([ 'todos' ]);
		}
	});
};
