import axios from "axios";
import _ from "lodash";

const path = process.env.REACT_APP_BACKEND_URL || "http://localhost:5000/api/";

export function getRequest(endpoint, data) {
    return axios.get(removeLastSlash(path + endpoint), sendWithAuth(data));
}

export function postRequest(endpoint, data) {
    return axios.post(removeLastSlash(path + endpoint), sendWithAuth(data));
}

export function deleteRequest(endpoint, data) {
    return axios.delete(removeLastSlash(path + endpoint), sendWithAuth(data));
}

export function putRequest(endpoint, data) {
    return axios.put(removeLastSlash(path + endpoint), sendWithAuth(data));
}

function removeLastSlash(path) {
    return _.trimEnd(path, "/");
}

function sendWithAuth(data) {
    return {
        data: data,
        headers: {
            Authorization: "Bearer " + sessionStorage.getItem("auth-avtal"),
        },
    };
}
