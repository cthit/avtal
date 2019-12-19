import React from "react";
import ReactDOM from "react-dom";
import App from "./app";
import * as serviceWorker from "./serviceWorker";

import { DigitProviders } from "@cthit/react-digit-components";

ReactDOM.render(
    <DigitProviders>
        <App />
    </DigitProviders>,
    document.getElementById("root")
);

serviceWorker.unregister();
