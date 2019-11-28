import React, { useState } from "react";
import styled from "styled-components";
import { putAccept } from "../../api/avtal/put.accept.api";
import { getAgreement } from "../../api/avtal/get.agreement.api";
import { getAccept } from "../../api/avtal/get.accept.api";
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
    const [md, setMd] = useState("null");

    getAgreement(service)
        .then(res => {
            setMd(res.data);
        })
        .catch(error => {
            console.log("error wioo wioo:", error);
        });

    getAccept(service)
        .then(res => {
            console.log(res.data);
            if (res.data) {
                //redirectToSource("https://chalmers.it");
            }
        })
        .catch(error => {
            console.log("error: arbitrary");
        });

    return (
        <AvtalHolder>
            <DigitMarkdown markdownSource={md} />
            <AvtalButton>
                <DigitButton
                    //Change to translated stringimezone.utc)
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
    putAccept(serviceName)
        .then(res => {
            redirectToSource("https://google.com");
        })
        .catch(error => {
            console.log("hello darkness my old friend");
        });
}

function redirectToSource(source) {
    window.location.replace(source);
}

export default Avtal;
