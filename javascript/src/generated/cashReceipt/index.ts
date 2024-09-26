export type * from "./CancelCashReceiptError"
export type * from "./CancelCashReceiptResponse"
export type * from "./CancelledCashReceipt"
export type * from "./CashReceipt"
export type * from "./CashReceiptAlreadyIssuedError"
export type * from "./CashReceiptNotFoundError"
export type * from "./CashReceiptNotIssuedError"
export type * from "./CashReceiptSummary"
export type * from "./GetCashReceiptError"
export type * from "./IssueCashReceiptBody"
export type * from "./IssueCashReceiptCustomerInput"
export type * from "./IssueCashReceiptError"
export type * from "./IssueCashReceiptResponse"
export type * from "./IssueFailedCashReceipt"
export type * from "./IssuedCashReceipt"
import type { CancelCashReceiptResponse } from "#generated/cashReceipt/CancelCashReceiptResponse"
import type { CashReceipt } from "#generated/cashReceipt/CashReceipt"
import type { CashReceiptType } from "#generated/common/CashReceiptType"
import type { Currency } from "#generated/common/Currency"
import type { IssueCashReceiptCustomerInput } from "#generated/cashReceipt/IssueCashReceiptCustomerInput"
import type { IssueCashReceiptResponse } from "#generated/cashReceipt/IssueCashReceiptResponse"
import type { PaymentAmountInput } from "#generated/common/PaymentAmountInput"
import type { PaymentProductType } from "#generated/common/PaymentProductType"

export type Operations = {
	/**
	 * 현금 영수증 단건 조회
	 *
	 * 주어진 결제 아이디에 대응되는 현금 영수증 내역을 조회합니다.
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
