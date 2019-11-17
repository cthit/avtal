import axios from "axios";
import _ from "lodash";

const path = process.env.REACT_APP_BACKEND_URL || "http://localhost:5000/api";

export function getRequest() {
    return axios.get(removeLastSlash(path + endpoint));
}

export function postRequest(endpoint, data) {
    return axios.post(removeLastSlash(path + endpoint), data);
}

export function deleteRequest(endpoint, data) {
    return axios.delete(removeLastSlash(path + endpoint), {
        data: data,
    });
}

export function putRequest(endpoint, data) {
    return axios.put(removeLastSlash(path + endpoint), data);
}

function removeLastSlash(path) {
    return _.trimEnd(path, "/");
}
