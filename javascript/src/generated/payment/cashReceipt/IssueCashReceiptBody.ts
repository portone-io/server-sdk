import type { CashReceiptType } from "./../../common/CashReceiptType"
import type { Currency } from "./../../common/Currency"
import type { IssueCashReceiptCustomerInput } from "./../../payment/cashReceipt/IssueCashReceiptCustomerInput"
import type { IssueCashReceiptPaymentMethodType } from "./../../payment/cashReceipt/IssueCashReceiptPaymentMethodType"
import type { PaymentAmountInput } from "./../../common/PaymentAmountInput"
import type { PaymentProductType } from "./../../common/PaymentProductType"
/** 현금영수증 발급 요청 양식 */
export type IssueCashReceiptBody = {
	/**
	 * 상점 아이디
	 *
	 * 접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 인증 정보의 상점 아이디를 사용합니다.
	 */
	storeId?: string
	/**
	 * 결제 건 아이디
	 *
	 * 외부 결제 건에 대한 수동 발급의 경우, 아이디를 직접 채번하여 입력합니다.
	 */
	paymentId: string
	/** 채널 키 */
	channelKey: string
	/** 현금 영수증 유형 */
	type: CashReceiptType
	/** 주문명 */
	orderName: string
	/** 화폐 */
	currency: Currency
	/** 금액 세부 입력 정보 */
	amount: PaymentAmountInput
	/** 상품 유형 */
	productType?: PaymentProductType
	/** 고객 정보 */
	customer: IssueCashReceiptCustomerInput
	/**
	 * 결제 일자
	 * (RFC 3339 date-time)
	 */
	paidAt?: string
	/**
	 * 사업자등록번호
	 *
	 * 웰컴페이먼츠의 경우에만 입력합니다.
	 */
	businessRegistrationNumber?: string
	/**
	 * 결제 수단
	 *
	 * 웰컴페이먼츠의 경우에만 입력합니다.
	 */
	paymentMethod?: IssueCashReceiptPaymentMethodType
}
