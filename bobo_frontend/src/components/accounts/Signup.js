import React, { useState } from 'react';

const Signup = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [confirmPassword, setConfirmPassword] = useState('');

    const handleSignup = async (e) => {
        e.preventDefault();
        // handle signup
    };

    return (
        <div>
            <h1>Signup</h1>
            <form onSubmit={handleSignup}>
                <input type="text" placeholder="Username" onChange={e => setUsername(e.target.value)} />
                <input type="password" placeholder="Password" onChange={e => setPassword(e.target.value)} />
                <input type="password" placeholder="Confirm Password" onChange={e => setConfirmPassword(e.target.value)} />
                <button type="submit">Signup</button>
            </form>
        </div>
    );
}

export default Signup;
