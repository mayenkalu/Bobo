// src/components/App.js

import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Home from './accounts/Home';
import Login from './accounts/Login';
import Signup from './accounts/Signup';
import DeleteAccount from './accounts/DeleteAccount';

const App = () => {
    return (
        <Router>
            <Switch>
                <Route exact path="/" component={Home} />
                <Route path="/login" component={Login} />
                <Route path="/signup" component={Signup} />
                <Route path="/delete-account" component={DeleteAccount} />
            </Switch>
        </Router>
    );
}

export default App;