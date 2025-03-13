import type { PortOneClientInit } from "../../client"
import { BusinessClient } from "./business/client"
/**
 * 포트원 API 클라이언트를 생성합니다.
 */
export function B2BClient(init: PortOneClientInit): B2BClient {
	return {
		business: BusinessClient(init),
	}
}
export type B2BClient = {
	business: BusinessClient
}
