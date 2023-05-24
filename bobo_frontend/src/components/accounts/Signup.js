import React, { useState } from 'react';
import apiService from '../../services/apiService';
import { useNavigate } from 'react-router-dom';

const Signup = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [email, setEmail] = useState('');
    const [loading, setLoading] = useState(false);

    const navigate = useNavigate();

    const handleSignup = async (e) => {
        e.preventDefault();
        setLoading(true);
        const data = {
            username: username,
            password: password,
            email: email
        }
        const response = await apiService.signup(data);
        if (response && response.username) {
            navigate('/login');
        } else {
            alert('Error signing up');
        }
        setLoading(false);
    };

    return (
        <div>
            <h1>Signup</h1>
            <form onSubmit={handleSignup}>
                <input type="text" placeholder="Username" onChange={e => setUsername(e.target.value)} />
                <input type="password" placeholder="Password" onChange={e => setPassword(e.target.value)} />
                <input type="email" placeholder="Email" onChange={e => setEmail(e.target.value)} />
                <button type="submit" disabled={loading}>{loading ? 'Loading...' : 'Signup'}</button>
            </form>
        </div>
    );
}

export default Signup;
