import type { PortOneClientInit } from "../../client"
import { TaxInvoiceClient } from "./taxInvoice/client"
/**
 * 포트원 API 클라이언트를 생성합니다.
 */
export function B2bClient(init: PortOneClientInit): B2bClient {
	return {
		taxInvoice: TaxInvoiceClient(init),
	}
}
export type B2bClient = {
	taxInvoice: TaxInvoiceClient
}
