import * as Errors from "../../../generated/errors"
import { USER_AGENT, type PortOneClientInit } from "../../../client"
import type { CancelCashReceiptResponse } from "../../../generated/payment/cashReceipt/CancelCashReceiptResponse"
import type { CashReceipt } from "../../../generated/payment/cashReceipt/CashReceipt"
import type { CashReceiptType } from "../../../generated/common/CashReceiptType"
import type { Currency } from "../../../generated/common/Currency"
import type { IssueCashReceiptCustomerInput } from "../../../generated/payment/cashReceipt/IssueCashReceiptCustomerInput"
import type { IssueCashReceiptResponse } from "../../../generated/payment/cashReceipt/IssueCashReceiptResponse"
import type { PaymentAmountInput } from "../../../generated/common/PaymentAmountInput"
import type { PaymentProductType } from "../../../generated/common/PaymentProductType"
import type { CancelCashReceiptError as _InternalCancelCashReceiptError } from "../../../generated/payment/cashReceipt/CancelCashReceiptError"
import type { GetCashReceiptError as _InternalGetCashReceiptError } from "../../../generated/payment/cashReceipt/GetCashReceiptError"
import type { IssueCashReceiptError as _InternalIssueCashReceiptError } from "../../../generated/payment/cashReceipt/IssueCashReceiptError"
export function CashReceiptClient(init: PortOneClientInit): CashReceiptClient {
	const baseUrl = init.baseUrl ?? "https://api.portone.io"
	const secret = init.secret
	return {
		getCashReceiptByPaymentId: async (
			options: {
				paymentId: string,
				storeId?: string,
			}
		): Promise<CashReceipt> => {
			const {
				paymentId,
				storeId,
			} = options
			const query = [
				["storeId", storeId],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/payments/${encodeURIComponent(paymentId)}/cash-receipt?${query}`, baseUrl),
				{
					method: "GET",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: _InternalGetCashReceiptError = await response.json()
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
				storeId?: string,
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
			} = options
			const requestBody = JSON.stringify({
				storeId: storeId ?? init.storeId,
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
					method: "POST",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
					body: requestBody,
				},
			)
			if (!response.ok) {
				const errorResponse: _InternalIssueCashReceiptError = await response.json()
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
			options: {
				paymentId: string,
				storeId?: string,
			}
		): Promise<CancelCashReceiptResponse> => {
			const {
				paymentId,
				storeId,
			} = options
			const query = [
				["storeId", storeId],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/payments/${encodeURIComponent(paymentId)}/cash-receipt/cancel?${query}`, baseUrl),
				{
					method: "POST",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: _InternalCancelCashReceiptError = await response.json()
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
	 * @throws {@link GetCashReceiptError}
	 */
	getCashReceiptByPaymentId: (
		options: {
			/** 결제 건 아이디 */
			paymentId: string,
			/**
			 * 상점 아이디
			 *
			 * 접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 토큰에 담긴 상점 아이디를 사용합니다.
			 */
			storeId?: string,
		}
	) => Promise<CashReceipt>
	/**
	 * 현금 영수증 수동 발급
	 *
	 * 현금 영수증 발급을 요청합니다.
	 *
	 * @throws {@link IssueCashReceiptError}
	 */
	issueCashReceipt: (
		options: {
			/**
			 * 상점 아이디
			 *
			 * 접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 토큰에 담긴 상점 아이디를 사용합니다.
			 */
			storeId?: string,
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
	 * @throws {@link CancelCashReceiptError}
	 */
	cancelCashReceiptByPaymentId: (
		options: {
			/** 결제 건 아이디 */
			paymentId: string,
			/**
			 * 상점 아이디
			 *
			 * 접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 토큰에 담긴 상점 아이디를 사용합니다.
			 */
			storeId?: string,
		}
	) => Promise<CancelCashReceiptResponse>
}
export type GetCashReceiptError =
	| Errors.CashReceiptNotFoundError
	| Errors.ForbiddenError
	| Errors.InvalidRequestError
	| Errors.UnauthorizedError
export function isGetCashReceiptError(error: Error): error is GetCashReceiptError {
	return (
		error instanceof Errors.CashReceiptNotFoundError
		|| error instanceof Errors.ForbiddenError
		|| error instanceof Errors.InvalidRequestError
		|| error instanceof Errors.UnauthorizedError
	)
}
export type IssueCashReceiptError =
	| Errors.CashReceiptAlreadyIssuedError
	| Errors.ChannelNotFoundError
	| Errors.ForbiddenError
	| Errors.InvalidRequestError
	| Errors.PgProviderError
	| Errors.UnauthorizedError
export function isIssueCashReceiptError(error: Error): error is IssueCashReceiptError {
	return (
		error instanceof Errors.CashReceiptAlreadyIssuedError
		|| error instanceof Errors.ChannelNotFoundError
		|| error instanceof Errors.ForbiddenError
		|| error instanceof Errors.InvalidRequestError
		|| error instanceof Errors.PgProviderError
		|| error instanceof Errors.UnauthorizedError
	)
}
export type CancelCashReceiptError =
	| Errors.CashReceiptNotFoundError
	| Errors.CashReceiptNotIssuedError
	| Errors.ForbiddenError
	| Errors.InvalidRequestError
	| Errors.PgProviderError
	| Errors.UnauthorizedError
export function isCancelCashReceiptError(error: Error): error is CancelCashReceiptError {
	return (
		error instanceof Errors.CashReceiptNotFoundError
		|| error instanceof Errors.CashReceiptNotIssuedError
		|| error instanceof Errors.ForbiddenError
		|| error instanceof Errors.InvalidRequestError
		|| error instanceof Errors.PgProviderError
		|| error instanceof Errors.UnauthorizedError
	)
}
