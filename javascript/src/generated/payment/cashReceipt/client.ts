import { CashReceiptError } from "./CashReceiptError"
import type { Unrecognized } from "./../../../utils/unrecognized"
import { USER_AGENT, type PortOneClientInit } from "../../../client"
import type { CancelCashReceiptResponse } from "../../../generated/payment/cashReceipt/CancelCashReceiptResponse"
import type { CashReceipt } from "../../../generated/payment/cashReceipt/CashReceipt"
import type { CashReceiptAlreadyIssuedError } from "../../../generated/payment/cashReceipt/CashReceiptAlreadyIssuedError"
import type { CashReceiptFilterInput } from "../../../generated/payment/cashReceipt/CashReceiptFilterInput"
import type { CashReceiptNotFoundError } from "../../../generated/payment/cashReceipt/CashReceiptNotFoundError"
import type { CashReceiptNotIssuedError } from "../../../generated/payment/cashReceipt/CashReceiptNotIssuedError"
import type { CashReceiptSortInput } from "../../../generated/payment/cashReceipt/CashReceiptSortInput"
import type { CashReceiptType } from "../../../generated/common/CashReceiptType"
import type { ChannelNotFoundError } from "../../../generated/common/ChannelNotFoundError"
import type { Currency } from "../../../generated/common/Currency"
import type { ForbiddenError } from "../../../generated/common/ForbiddenError"
import type { GetCashReceiptsResponse } from "../../../generated/payment/cashReceipt/GetCashReceiptsResponse"
import type { InvalidRequestError } from "../../../generated/common/InvalidRequestError"
import type { IssueCashReceiptCustomerInput } from "../../../generated/payment/cashReceipt/IssueCashReceiptCustomerInput"
import type { IssueCashReceiptPaymentMethodType } from "../../../generated/payment/cashReceipt/IssueCashReceiptPaymentMethodType"
import type { IssueCashReceiptResponse } from "../../../generated/payment/cashReceipt/IssueCashReceiptResponse"
import type { PageInput } from "../../../generated/common/PageInput"
import type { PaymentAmountInput } from "../../../generated/common/PaymentAmountInput"
import type { PaymentProductType } from "../../../generated/common/PaymentProductType"
import type { PgProviderError } from "../../../generated/common/PgProviderError"
import type { UnauthorizedError } from "../../../generated/common/UnauthorizedError"
/**
 * 포트원 API 클라이언트를 생성합니다.
 */
export function CashReceiptClient(init: PortOneClientInit): CashReceiptClient {
	const baseUrl = init.baseUrl ?? "https://api.portone.io"
	const secret = init.secret
	return {
		getCashReceipts: async (
			options?: {
				page?: PageInput,
				sort?: CashReceiptSortInput,
				filter?: CashReceiptFilterInput,
			}
		): Promise<GetCashReceiptsResponse> => {
			const page = options?.page
			const sort = options?.sort
			const filter = options?.filter
			const requestBody = JSON.stringify({
				page,
				sort,
				filter,
			})
			const query = [
				["requestBody", requestBody],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/cash-receipts?${query}`, baseUrl),
				{
					method: "GET",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				throw new GetCashReceiptsError(await response.json())
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
				businessRegistrationNumber?: string,
				paymentMethod?: IssueCashReceiptPaymentMethodType,
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
				businessRegistrationNumber,
				paymentMethod,
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
				businessRegistrationNumber,
				paymentMethod,
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
	}
}
export type CashReceiptClient = {
	/**
	 * 현금영수증 다건 조회
	 *
	 * 주어진 조건에 맞는 현금영수증들을 페이지 기반으로 조회합니다.
	 *
	 * @throws {@link GetCashReceiptsError}
	 */
	getCashReceipts: (
		options?: {
			/**
			 * 요청할 페이지 정보
			 *
			 * 미 입력 시 number: 0, size: 10 으로 기본값이 적용됩니다.
			 */
			page?: PageInput,
			/**
			 * 정렬 조건
			 *
			 * 미 입력 시 sortBy: ISSUED_AT, sortOrder: DESC 으로 기본값이 적용됩니다.
			 */
			sort?: CashReceiptSortInput,
			/** 조회할 현금영수증 조건 필터 */
			filter?: CashReceiptFilterInput,
		}
	) => Promise<GetCashReceiptsResponse>
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
			/**
			 * 사업자등록번호
			 *
			 * 웰컴페이먼츠의 경우에만 입력합니다.
			 */
			businessRegistrationNumber?: string,
			/**
			 * 결제 수단
			 *
			 * 웰컴페이먼츠의 경우에만 입력합니다.
			 */
			paymentMethod?: IssueCashReceiptPaymentMethodType,
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
}
export class GetCashReceiptsError extends CashReceiptError {
	declare readonly data: ForbiddenError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, GetCashReceiptsError.prototype)
		this.name = "GetCashReceiptsError"
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
export class GetCashReceiptError extends CashReceiptError {
	declare readonly data: CashReceiptNotFoundError | ForbiddenError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: CashReceiptNotFoundError | ForbiddenError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, GetCashReceiptError.prototype)
		this.name = "GetCashReceiptError"
	}
}
