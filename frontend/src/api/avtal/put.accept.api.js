import { ACCEPT } from "../utils/endpoints";
import { putRequest } from "../utils/api";

export function putAccept(serviceName) {
    return putRequest(ACCEPT + serviceName, "");
}
