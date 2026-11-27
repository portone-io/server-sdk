import { ReconciliationError } from "./ReconciliationError"
import type { Unrecognized } from "./../../utils/unrecognized"
import { USER_AGENT, type PortOneClientInit } from "../../client"
import type { DateRange } from "../../generated/common/DateRange"
import type { ForbiddenError } from "../../generated/common/ForbiddenError"
import type { GetPaymentReconciliationSettlementVatReportResponse } from "../../generated/reconciliation/GetPaymentReconciliationSettlementVatReportResponse"
import type { GetPaymentReconciliationTransactionVatReportResponse } from "../../generated/reconciliation/GetPaymentReconciliationTransactionVatReportResponse"
import type { InvalidRequestError } from "../../generated/common/InvalidRequestError"
import type { PaymentReconciliationSettlementSummaryFilterInput } from "../../generated/reconciliation/PaymentReconciliationSettlementSummaryFilterInput"
import type { PaymentReconciliationTransactionSummaryFilterInput } from "../../generated/reconciliation/PaymentReconciliationTransactionSummaryFilterInput"
import type { UnauthorizedError } from "../../generated/common/UnauthorizedError"
/**
 * 포트원 API 클라이언트를 생성합니다.
 */
export function ReconciliationClient(init: PortOneClientInit): ReconciliationClient {
	const baseUrl = init.baseUrl ?? "https://api.portone.io"
	const secret = init.secret
	return {
		getPaymentReconciliationSettlementVatReport: async (
			options: {
				dateRange: DateRange,
				filter?: PaymentReconciliationSettlementSummaryFilterInput,
			}
		): Promise<GetPaymentReconciliationSettlementVatReportResponse> => {
			const {
				dateRange,
				filter,
			} = options
			const requestBody = JSON.stringify({
				dateRange,
				filter,
			})
			const query = [
				["requestBody", requestBody],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/payment-reconciliations/settlements/vat-report?${query}`, baseUrl),
				{
					method: "GET",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				throw new GetPaymentReconciliationSettlementVatReportError(await response.json())
			}
			return response.json()
		},
		getPaymentReconciliationTransactionVatReport: async (
			options: {
				dateRange: DateRange,
				filter?: PaymentReconciliationTransactionSummaryFilterInput,
			}
		): Promise<GetPaymentReconciliationTransactionVatReportResponse> => {
			const {
				dateRange,
				filter,
			} = options
			const requestBody = JSON.stringify({
				dateRange,
				filter,
			})
			const query = [
				["requestBody", requestBody],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/payment-reconciliations/transactions/vat-report?${query}`, baseUrl),
				{
					method: "GET",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				throw new GetPaymentReconciliationTransactionVatReportError(await response.json())
			}
			return response.json()
		},
	}
}
export type ReconciliationClient = {
	/**
	 * 정산일 기준 부가세 내역 조회
	 *
	 * @throws {@link GetPaymentReconciliationSettlementVatReportError}
	 *
	 * @unstable 실험적 API입니다. 하위호환성 정책과 무관하게 변경 및 지원 종료될 수 있으니 이용에 유의하세요.
	 */
	getPaymentReconciliationSettlementVatReport: (
		options: {
			/** 정산일 범위 */
			dateRange: DateRange,
			filter?: PaymentReconciliationSettlementSummaryFilterInput,
		}
	) => Promise<GetPaymentReconciliationSettlementVatReportResponse>
	/**
	 * 거래일 기준 부가세 내역 조회
	 *
	 * @throws {@link GetPaymentReconciliationTransactionVatReportError}
	 *
	 * @unstable 실험적 API입니다. 하위호환성 정책과 무관하게 변경 및 지원 종료될 수 있으니 이용에 유의하세요.
	 */
	getPaymentReconciliationTransactionVatReport: (
		options: {
			/** 거래일 범위 */
			dateRange: DateRange,
			filter?: PaymentReconciliationTransactionSummaryFilterInput,
		}
	) => Promise<GetPaymentReconciliationTransactionVatReportResponse>
}
export class GetPaymentReconciliationSettlementVatReportError extends ReconciliationError {
	declare readonly data: ForbiddenError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, GetPaymentReconciliationSettlementVatReportError.prototype)
		this.name = "GetPaymentReconciliationSettlementVatReportError"
	}
}
export class GetPaymentReconciliationTransactionVatReportError extends ReconciliationError {
	declare readonly data: ForbiddenError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, GetPaymentReconciliationTransactionVatReportError.prototype)
		this.name = "GetPaymentReconciliationTransactionVatReportError"
	}
}
