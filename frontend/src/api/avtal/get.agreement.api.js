import { AGREEMENT } from "../utils/endpoints";
import { getRequest } from "../utils/api";

export function getAgreement(serviceName) {
    return getRequest(AGREEMENT + serviceName);
}
