import React from "react";

import {
    DigitHeader,
} from "@cthit/react-digit-components";
import Avtal from "../use-cases/avtal/index";

import { Switch, Route, BrowserRouter as Router } from "react-router-dom";

const App = () => {
    //const name = "avtal";
    // const id = process.env.REACT_APP_GAMMA_ID || "id";
    // const secret = process.env.REACT_APP_GAMMA_SECRET || "secret";
    // const redirect =
    //     process.env.REACT_APP_FRONTEND_CALLBACK_URL ||
    //     "http://localhost:3001/auth/account/callback";
    // const gammaPath =
    //     process.env.REACT_APP_BACKEND_URL || "http://localhost:8081/api";


   // console.log(user);

    return (
        <Router>
            <Switch>
                <Route path="/:service" component={Avtal}>
                    <DigitHeader title={"Avtal"} renderMain={() => <Avtal />} />
                </Route>
                <Route path="/">
                    <DigitHeader title={"Avtal"} renderMain={() => <div>hello</div>} />
                </Route>
            </Switch>
        </Router>
    );
};

export default App;
