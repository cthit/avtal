import React, { useState } from "react";
import styled from "styled-components";
import { putAccept, getAgreement } from "../../api/avtal/put.accept.api";
import { DigitMarkdown, DigitButton } from "@cthit/react-digit-components";
import { useParams } from "react-router";

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
    const { service } = useParams();
    const md = getAgreement(service);

    return (
        <AvtalHolder>
            <DigitMarkdown markdownSource={md} />
            <AvtalButton>
                <DigitButton
                    //Change to translated string
                    text="Accept the Agreement"
                    primary
                    raised
                    onClick={() => agreementAccepted(service)}
                />
            </AvtalButton>
        </AvtalHolder>
    );
};

function agreementAccepted(serviceName) {
    // TODO: GET SERIVCE NAME FROM ENDPOINT
    putAccept(serviceName);
    console.log(serviceName);
}

export default Avtal;
