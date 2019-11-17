import { ACCEPT } from "../utils/endpoints";
import { getRequest } from "../utils/api";

export function getAccept(service_name) {
    return getRequest(ACCEPT + service);
}
