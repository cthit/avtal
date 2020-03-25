import { ACCEPT } from "../utils/endpoints";
import { getRequest } from "../utils/api";

export function getAccept(serviceName) {
    return getRequest(ACCEPT + serviceName, "");
}
