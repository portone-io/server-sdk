import type { B2bBulkTaxInvoiceSourceType } from "./../../b2b/taxInvoice/B2bBulkTaxInvoiceSourceType"
import type { B2bBulkTaxInvoiceStatus } from "./../../b2b/taxInvoice/B2bBulkTaxInvoiceStatus"
import type { B2bTaxInvoiceIssuanceType } from "./../../b2b/taxInvoice/B2bTaxInvoiceIssuanceType"
import type { Map_Stat } from "./../../b2b/taxInvoice/Map_Stat"
export type B2bBulkTaxInvoice = {
	/** 일괄 세금계산서 고유 아이디 */
	id: string
	graphqlId: string
	name?: string
	status: B2bBulkTaxInvoiceStatus
	/** (int32) */
	totalInvoiceCount: number
	/** (int64) */
	totalAmount: number
	stats: Map_Stat
	/** (RFC 3339 date-time) */
	createdAt: string
	/** (RFC 3339 date-time) */
	scheduledAt?: string
	/** (RFC 3339 date-time) */
	requestedAt?: string
	/** (RFC 3339 date-time) */
	statusUpdatedAt: string
	sourceType: B2bBulkTaxInvoiceSourceType
	issuanceType: B2bTaxInvoiceIssuanceType
}
