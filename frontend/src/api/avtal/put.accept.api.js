import { ACCEPT } from "../utils/endpoints";
import { putRequest } from "../utils/api";

export function putAccept(service_name) {
    return putRequest(ACCEPT + service);
}
