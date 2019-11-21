import React from "react";

import { DigitHeader, DigitProviders } from "@cthit/react-digit-components";
import Avtal from "../use-cases/avtal/index";

import { Switch, Route } from "react-router-dom";

const App = () => {
    return (
        <DigitProviders>
            <Switch>
                <Route path="/:service" component={Avtal}>
                    <DigitHeader title={"Avtal"} renderMain={() => <Avtal />} />
                </Route>
            </Switch>
        </DigitProviders>
    );
};

export default App;
