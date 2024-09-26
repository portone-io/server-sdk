import type { B2bTaxInvoiceBeforeSending } from "#generated/b2b/B2bTaxInvoiceBeforeSending"
import type { B2bTaxInvoiceIssuanceCancelled } from "#generated/b2b/B2bTaxInvoiceIssuanceCancelled"
import type { B2bTaxInvoiceIssued } from "#generated/b2b/B2bTaxInvoiceIssued"
import type { B2bTaxInvoiceRegistered } from "#generated/b2b/B2bTaxInvoiceRegistered"
import type { B2bTaxInvoiceRequestCancelled } from "#generated/b2b/B2bTaxInvoiceRequestCancelled"
import type { B2bTaxInvoiceRequestRefused } from "#generated/b2b/B2bTaxInvoiceRequestRefused"
import type { B2bTaxInvoiceRequested } from "#generated/b2b/B2bTaxInvoiceRequested"
import type { B2bTaxInvoiceSending } from "#generated/b2b/B2bTaxInvoiceSending"
import type { B2bTaxInvoiceSendingCompleted } from "#generated/b2b/B2bTaxInvoiceSendingCompleted"
import type { B2bTaxInvoiceSendingFailed } from "#generated/b2b/B2bTaxInvoiceSendingFailed"
import type { B2bTaxInvoiceWaitingSending } from "#generated/b2b/B2bTaxInvoiceWaitingSending"

export type B2bTaxInvoice =
	/** 전송전 */
	| B2bTaxInvoiceBeforeSending
	/** 공급자에 의한 발행 취소 */
	| B2bTaxInvoiceIssuanceCancelled
	/** 공급자의 발행거부 */
	| B2bTaxInvoiceRequestRefused
	/** 발행완료 */
	| B2bTaxInvoiceIssued
	/** 임시저장 */
	| B2bTaxInvoiceRegistered
	/** 역발행대기 (전자 서명 요청됨) */
	| B2bTaxInvoiceRequested
	/** 공급받는자에 의한 발행취소 */
	| B2bTaxInvoiceRequestCancelled
	/** 전송중 */
	| B2bTaxInvoiceSending
	/** 전송완료 */
	| B2bTaxInvoiceSendingCompleted
	/** 전송실패 */
	| B2bTaxInvoiceSendingFailed
	/** 전송대기 */
	| B2bTaxInvoiceWaitingSending
