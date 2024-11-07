import type { ChannelGroupSummary } from "./../common/ChannelGroupSummary"
import type { Country } from "./../common/Country"
import type { Currency } from "./../common/Currency"
import type { Customer } from "./../common/Customer"
import type { PaymentAmount } from "./../payment/PaymentAmount"
import type { PaymentEscrow } from "./../payment/PaymentEscrow"
import type { PaymentMethod } from "./../payment/PaymentMethod"
import type { PaymentProduct } from "./../common/PaymentProduct"
import type { PaymentWebhook } from "./../payment/PaymentWebhook"
import type { PortOneVersion } from "./../common/PortOneVersion"
import type { SelectedChannel } from "./../common/SelectedChannel"

/** 결제 완료 대기 상태 건 */
export type PayPendingPayment = {
	/** 결제 건 상태 */
	status: "PAY_PENDING"
	/** 결제 건 아이디 */
	id: string
	/** 고객사 아이디 */
	merchantId: string
	/** 상점 아이디 */
	storeId: string
	/** 결제수단 정보 */
	method?: PaymentMethod
	/** 결제 채널 */
	channel: SelectedChannel
	/** 결제 채널 그룹 정보 */
	channelGroup?: ChannelGroupSummary
	/** 포트원 버전 */
	version: PortOneVersion
	/**
	 * 결제 예약 건 아이디
	 *
	 * 결제 예약을 이용한 경우에만 존재
	 */
	scheduleId?: string
	/**
	 * 결제 시 사용된 빌링키
	 *
	 * 빌링키 결제인 경우에만 존재
	 */
	billingKey?: string
	/** 웹훅 발송 내역 */
	webhooks?: PaymentWebhook[]
	/**
	 * 결제 요청 시점
	 * (RFC 3339 date-time)
	 */
	requestedAt: string
	/**
	 * 업데이트 시점
	 * (RFC 3339 date-time)
	 */
	updatedAt: string
	/**
	 * 상태 업데이트 시점
	 * (RFC 3339 date-time)
	 */
	statusChangedAt: string
	/** 주문명 */
	orderName: string
	/** 결제 금액 관련 세부 정보 */
	amount: PaymentAmount
	/** 통화 */
	currency: Currency
	/** 구매자 정보 */
	customer: Customer
	/** 프로모션 아이디 */
	promotionId?: string
	/** 문화비 지출 여부 */
	isCulturalExpense?: boolean
	/**
	 * 에스크로 결제 정보
	 *
	 * 에스크로 결제인 경우 존재합니다.
	 */
	escrow?: PaymentEscrow
	/** 상품 정보 */
	products?: PaymentProduct[]
	/**
	 * 상품 갯수
	 * (int32)
	 */
	productCount?: number
	/** 사용자 지정 데이터 */
	customData?: string
	/** 국가 코드 */
	country?: Country
	/** PG사 거래 아이디 */
	pgTxId?: string
}
