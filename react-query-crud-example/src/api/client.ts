import axios from "axios";

export const client = axios.create({
    baseURL : 'http://localhost:5000/todos',
    headers : {
        'Content-Type' : 'application/json'
    }
})