import { AGREEMENT } from "../utils/endpoints";
import { getRequest } from "../utils/api";

export function getAgreement(service_name) {
    return getRequest(AGREEMENT + service);
}
