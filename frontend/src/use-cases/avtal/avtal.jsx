import React from "react";
import styled from "styled-components";
import { putAccept } from "../../api/avtal/put.accept.api";
import { DigitMarkdown, DigitButton } from "@cthit/react-digit-components";

const AvtalHolder = styled.div`
    background: #fff;
    border-radius: 0.5vw;
    padding: 20px;
    margin: 1vh 20vw;
    box-shadow: 0 3px 6px rgba(0, 0, 0, 0.16), 0 3px 6px rgba(0, 0, 0, 0.23);
`;

const AvtalButton = styled.div`
    margin-top: 2vh;
`;

const Avtal = () => {
    //Read from api
    const input = "# This is a header\nAnd this is a paragraph";
    return (
        <AvtalHolder>
            <DigitMarkdown markdownSource={input} />
            <AvtalButton>
                <DigitButton
                    //Change to translated string
                    text="Accept the Agreement"
                    primary
                    raised
                    onClick={() => agreementAccepted()}
                />
            </AvtalButton>
        </AvtalHolder>
    );
};

function agreementAccepted() {
    // TODO: GET SERIVCE NAME FROM ENDPOINT
    putAccept();
}

export default Avtal;
