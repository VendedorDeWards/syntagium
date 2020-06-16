import React from 'react';
import { Route } from 'react-router-dom';

import SyntagiList from './components/syntagi-list.jsx';
import SyntagiDetail from './components/syntagi-detail.jsx';
import SyntagiForm from './components/syntagi-form.jsx';
import Login from './components/login.jsx';
import Signup from './components/signup.jsx'
import TermsOfService from './components/policy.jsx';

function BaseRouter() {
    return (
        <div>
            <Route exact path='/syntagi' component={SyntagiList} />
            <Route exact path='/syntagi/:id' component={SyntagiDetail} />
            <Route exact path='/import' component={SyntagiForm} />
            <Route exact path='/login' component={Login}/>
            <Route exact path='/signup' component={Signup}/>
            <Route exact path='/policy' component={TermsOfService}/>
        </div>
    )
}

export default BaseRouter;