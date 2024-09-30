import type { CancelCashReceiptError } from "#generated/cashReceipt/CancelCashReceiptError"
import type { CancelCashReceiptResponse } from "#generated/cashReceipt/CancelCashReceiptResponse"
import type { CashReceipt } from "#generated/cashReceipt/CashReceipt"
import type { CashReceiptType } from "#generated/common/CashReceiptType"
import type { Currency } from "#generated/common/Currency"
import type { GetCashReceiptError } from "#generated/cashReceipt/GetCashReceiptError"
import type { IssueCashReceiptCustomerInput } from "#generated/cashReceipt/IssueCashReceiptCustomerInput"
import type { IssueCashReceiptError } from "#generated/cashReceipt/IssueCashReceiptError"
import type { IssueCashReceiptResponse } from "#generated/cashReceipt/IssueCashReceiptResponse"
import type { PaymentAmountInput } from "#generated/common/PaymentAmountInput"
import type { PaymentProductType } from "#generated/common/PaymentProductType"
import * as Errors from "#generated/errors"
export type { CancelCashReceiptResponse } from "./CancelCashReceiptResponse"
export type { CancelledCashReceipt } from "./CancelledCashReceipt"
export type { CashReceipt } from "./CashReceipt"
export type { CashReceiptSummary } from "./CashReceiptSummary"
export type { IssueCashReceiptBody } from "./IssueCashReceiptBody"
export type { IssueCashReceiptCustomerInput } from "./IssueCashReceiptCustomerInput"
export type { IssueCashReceiptResponse } from "./IssueCashReceiptResponse"
export type { IssueFailedCashReceipt } from "./IssueFailedCashReceipt"
export type { IssuedCashReceipt } from "./IssuedCashReceipt"
/** @ignore */
export function CashReceiptClient(secret: string, userAgent: string, baseUrl?: string, storeId?: string): CashReceiptClient {
	return {
		getCashReceiptByPaymentId: async (
			paymentId: string,
		): Promise<CashReceipt> => {
			const query = [
				["storeId", storeId],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/payments/${paymentId}/cash-receipt?${query}`, baseUrl),
				{
					method: "get",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": userAgent,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: GetCashReceiptError = await response.json()
				switch (errorResponse.type) {
				case "CASH_RECEIPT_NOT_FOUND":
					throw new Errors.CashReceiptNotFoundError(errorResponse)
				case "FORBIDDEN":
					throw new Errors.ForbiddenError(errorResponse)
				case "INVALID_REQUEST":
					throw new Errors.InvalidRequestError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
			}
			return response.json()
		},
		issueCashReceipt: async (
			options: {
				paymentId: string,
				channelKey: string,
				type: CashReceiptType,
				orderName: string,
				currency: Currency,
				amount: PaymentAmountInput,
				productType?: PaymentProductType,
				customer: IssueCashReceiptCustomerInput,
				paidAt?: string,
			}
		): Promise<IssueCashReceiptResponse> => {
			const {
				paymentId,
				channelKey,
				type,
				orderName,
				currency,
				amount,
				productType,
				customer,
				paidAt,
			} = options
			const requestBody = JSON.stringify({
				storeId,
				paymentId,
				channelKey,
				type,
				orderName,
				currency,
				amount,
				productType,
				customer,
				paidAt,
			})
			const response = await fetch(
				new URL("/cash-receipts", baseUrl),
				{
					method: "post",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": userAgent,
					},
					body: requestBody,
				},
			)
			if (!response.ok) {
				const errorResponse: IssueCashReceiptError = await response.json()
				switch (errorResponse.type) {
				case "CASH_RECEIPT_ALREADY_ISSUED":
					throw new Errors.CashReceiptAlreadyIssuedError(errorResponse)
				case "CHANNEL_NOT_FOUND":
					throw new Errors.ChannelNotFoundError(errorResponse)
				case "FORBIDDEN":
					throw new Errors.ForbiddenError(errorResponse)
				case "INVALID_REQUEST":
					throw new Errors.InvalidRequestError(errorResponse)
				case "PG_PROVIDER":
					throw new Errors.PgProviderError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
			}
			return response.json()
		},
		cancelCashReceiptByPaymentId: async (
			paymentId: string,
		): Promise<CancelCashReceiptResponse> => {
			const query = [
				["storeId", storeId],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/payments/${paymentId}/cash-receipt/cancel?${query}`, baseUrl),
				{
					method: "post",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": userAgent,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: CancelCashReceiptError = await response.json()
				switch (errorResponse.type) {
				case "CASH_RECEIPT_NOT_FOUND":
					throw new Errors.CashReceiptNotFoundError(errorResponse)
				case "CASH_RECEIPT_NOT_ISSUED":
					throw new Errors.CashReceiptNotIssuedError(errorResponse)
				case "FORBIDDEN":
					throw new Errors.ForbiddenError(errorResponse)
				case "INVALID_REQUEST":
					throw new Errors.InvalidRequestError(errorResponse)
				case "PG_PROVIDER":
					throw new Errors.PgProviderError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
			}
			return response.json()
		},
	}
}
export type CashReceiptClient = {
	/**
	 * 현금 영수증 단건 조회
	 *
	 * 주어진 결제 아이디에 대응되는 현금 영수증 내역을 조회합니다.
	 *
	 * @param paymentId
	 * 결제 건 아이디
	 *
	 * @throws {@link Errors.CashReceiptNotFoundError} 현금영수증이 존재하지 않는 경우
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getCashReceiptByPaymentId: (
		/** 결제 건 아이디 */
		paymentId: string,
	) => Promise<CashReceipt>
	/**
	 * 현금 영수증 수동 발급
	 *
	 * 현금 영수증 발급을 요청합니다.
	 *
	 * @throws {@link Errors.CashReceiptAlreadyIssuedError} 현금영수증이 이미 발급된 경우
	 * @throws {@link Errors.ChannelNotFoundError} 요청된 채널이 존재하지 않는 경우
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PgProviderError} PG사에서 오류를 전달한 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	issueCashReceipt: (
		options: {
			/**
			 * 결제 건 아이디
			 *
			 * 외부 결제 건에 대한 수동 발급의 경우, 아이디를 직접 채번하여 입력합니다.
			 */
			paymentId: string,
			/** 채널 키 */
			channelKey: string,
			/** 현금 영수증 유형 */
			type: CashReceiptType,
			/** 주문명 */
			orderName: string,
			/** 화폐 */
			currency: Currency,
			/** 금액 세부 입력 정보 */
			amount: PaymentAmountInput,
			/** 상품 유형 */
			productType?: PaymentProductType,
			/** 고객 정보 */
			customer: IssueCashReceiptCustomerInput,
			/**
			 * 결제 일자
			 * (RFC 3339 date-time)
			 */
			paidAt?: string,
		}
	) => Promise<IssueCashReceiptResponse>
	/**
	 * 현금 영수증 취소
	 *
	 * 현금 영수증 취소를 요청합니다.
	 *
	 * @param paymentId
	 * 결제 건 아이디
	 *
	 * @throws {@link Errors.CashReceiptNotFoundError} 현금영수증이 존재하지 않는 경우
	 * @throws {@link Errors.CashReceiptNotIssuedError} 현금영수증이 발급되지 않은 경우
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PgProviderError} PG사에서 오류를 전달한 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	cancelCashReceiptByPaymentId: (
		/** 결제 건 아이디 */
		paymentId: string,
	) => Promise<CancelCashReceiptResponse>
}

