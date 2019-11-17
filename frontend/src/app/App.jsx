import React from "react";

import { DigitHeader, DigitProviders } from "@cthit/react-digit-components";
import Avtal from "../use-cases/avtal/index";

const App = () => {
    return (
        <DigitProviders>
            <DigitHeader title={"Avtal"} renderMain={() => <Avtal />} />
        </DigitProviders>
    );
};

export default App;
