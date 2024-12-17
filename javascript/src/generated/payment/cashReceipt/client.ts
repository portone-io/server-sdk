import { CashReceiptError } from "./CashReceiptError"
import type { Unrecognized } from "./../../../utils/unrecognized"
import { USER_AGENT, type PortOneClientInit } from "../../../client"
import type { CancelCashReceiptResponse } from "../../../generated/payment/cashReceipt/CancelCashReceiptResponse"
import type { CashReceipt } from "../../../generated/payment/cashReceipt/CashReceipt"
import type { CashReceiptAlreadyIssuedError } from "../../../generated/payment/cashReceipt/CashReceiptAlreadyIssuedError"
import type { CashReceiptNotFoundError } from "../../../generated/payment/cashReceipt/CashReceiptNotFoundError"
import type { CashReceiptNotIssuedError } from "../../../generated/payment/cashReceipt/CashReceiptNotIssuedError"
import type { CashReceiptType } from "../../../generated/common/CashReceiptType"
import type { ChannelNotFoundError } from "../../../generated/common/ChannelNotFoundError"
import type { Currency } from "../../../generated/common/Currency"
import type { ForbiddenError } from "../../../generated/common/ForbiddenError"
import type { InvalidRequestError } from "../../../generated/common/InvalidRequestError"
import type { IssueCashReceiptCustomerInput } from "../../../generated/payment/cashReceipt/IssueCashReceiptCustomerInput"
import type { IssueCashReceiptResponse } from "../../../generated/payment/cashReceipt/IssueCashReceiptResponse"
import type { PaymentAmountInput } from "../../../generated/common/PaymentAmountInput"
import type { PaymentProductType } from "../../../generated/common/PaymentProductType"
import type { PgProviderError } from "../../../generated/common/PgProviderError"
import type { UnauthorizedError } from "../../../generated/common/UnauthorizedError"
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
				throw new GetCashReceiptError(await response.json())
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
				throw new IssueCashReceiptError(await response.json())
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
				throw new CancelCashReceiptError(await response.json())
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
export class GetCashReceiptError extends CashReceiptError {
	declare readonly data: CashReceiptNotFoundError | ForbiddenError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: CashReceiptNotFoundError | ForbiddenError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, GetCashReceiptError.prototype)
		this.name = "GetCashReceiptError"
	}
}
export class IssueCashReceiptError extends CashReceiptError {
	declare readonly data: CashReceiptAlreadyIssuedError | ChannelNotFoundError | ForbiddenError | InvalidRequestError | PgProviderError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: CashReceiptAlreadyIssuedError | ChannelNotFoundError | ForbiddenError | InvalidRequestError | PgProviderError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, IssueCashReceiptError.prototype)
		this.name = "IssueCashReceiptError"
	}
}
export class CancelCashReceiptError extends CashReceiptError {
	declare readonly data: CashReceiptNotFoundError | CashReceiptNotIssuedError | ForbiddenError | InvalidRequestError | PgProviderError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: CashReceiptNotFoundError | CashReceiptNotIssuedError | ForbiddenError | InvalidRequestError | PgProviderError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, CancelCashReceiptError.prototype)
		this.name = "CancelCashReceiptError"
	}
}