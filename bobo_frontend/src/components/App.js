import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './Home';
import Login from './accounts/Login';
import Signup from './accounts/Signup';
import DeleteAccount from './accounts/DeleteAccount';

const App = () => {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/login" element={<Login />} />
                <Route path="/signup" element={<Signup />} />
                <Route path="/delete-account" element={<DeleteAccount />} />
            </Routes>
        </Router>
    );
}

export default App;
