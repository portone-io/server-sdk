import type { Currency } from "./../../common/Currency"
import type { Customer } from "./../../common/Customer"
import type { PaymentProduct } from "./../../common/PaymentProduct"
/** 결제 예약 완료 상태 */
export type ScheduledPaymentSchedule = {
	/** 결제 예약 건 상태 */
	status: "SCHEDULED"
	/** 결제 예약 건 아이디 */
	id: string
	/** 고객사 아이디 */
	merchantId: string
	/** 상점 아이디 */
	storeId: string
	/** 결제 건 아이디 */
	paymentId: string
	/** 빌링키 */
	billingKey: string
	/** 주문명 */
	orderName: string
	/** 문화비 지출 여부 */
	isCulturalExpense: boolean
	/** 에스크로 결제 여부 */
	isEscrow: boolean
	/** 고객 정보 */
	customer: Customer
	/** 사용자 지정 데이터 */
	customData: string
	/**
	 * 결제 총 금액
	 * (int64)
	 */
	totalAmount: number
	/**
	 * 면세액
	 * (int64)
	 */
	taxFreeAmount?: number
	/**
	 * 부가세
	 * (int64)
	 */
	vatAmount?: number
	/** 통화 */
	currency: Currency
	/**
	 * 할부 개월 수
	 * (int32)
	 */
	installmentMonth?: number
	/** 웹훅 주소 */
	noticeUrls?: string[]
	/** 상품 정보 */
	products?: PaymentProduct[]
	/**
	 * 결제 예약 등록 시점
	 * (RFC 3339 date-time)
	 */
	createdAt: string
	/**
	 * 결제 예정 시점
	 * (RFC 3339 date-time)
	 */
	timeToPay: string
}
