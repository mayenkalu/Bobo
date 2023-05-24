import React, { useState } from 'react';
import apiService from '../../services/apiService';
import { useNavigate } from 'react-router-dom';

const DeleteAccount = () => {
    const [username, setUsername] = useState('');

    const navigate = useNavigate();

    const handleDelete = async (e) => {
        e.preventDefault();
        const response = await apiService.deleteUser(username);
        if (response) {
            localStorage.removeItem('token');
            navigate('/signup');
        } else {
            alert('Error deleting account');
        }
    };

    return (
        <div>
            <h1>Delete Account</h1>
            <form onSubmit={handleDelete}>
                <input type="text" placeholder="Username" onChange={e => setUsername(e.target.value)} />
                <button type="submit">Delete</button>
            </form>
        </div>
    );
}

export default DeleteAccount;
