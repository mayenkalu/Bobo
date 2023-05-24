import axios from 'axios';

const apiInstance = axios.create({
    baseURL: 'http://localhost:8000/api/',
    timeout: 5000,
    headers: {
        Authorization: 'Bearer ' + localStorage.getItem('token')
    }
});

export const signup = async (data) => {
    const response = await apiInstance.post('users/', data);
    return response.data;
}

export const login = async (data) => {
    const response = await apiInstance.post('token/login/', data);
    return response.data;
}

export const deleteUser = async (username) => {
    const response = await apiInstance.delete(`users/${username}/`);
    return response.data;
}

export const logout = () => {
    // remove user from local storage to log user out
    localStorage.removeItem('user');
}

export default apiInstance;
