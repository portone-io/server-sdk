import type { PaymentWebhookPaymentStatus } from "./../payment/PaymentWebhookPaymentStatus"
import type { PaymentWebhookRequest } from "./../payment/PaymentWebhookRequest"
import type { PaymentWebhookResponse } from "./../payment/PaymentWebhookResponse"
import type { PaymentWebhookStatus } from "./../payment/PaymentWebhookStatus"
import type { PaymentWebhookTrigger } from "./../payment/PaymentWebhookTrigger"

/** 성공 웹훅 내역 */
export type PaymentWebhook = {
	/**
	 * 웹훅 발송 시 결제 건 상태
	 *
	 * V1 결제 건인 경우, 값이 존재하지 않습니다.
	 */
	paymentStatus?: PaymentWebhookPaymentStatus
	/** 웹훅 아이디 */
	id: string
	/** 웹훅 상태 */
	status?: PaymentWebhookStatus
	/**
	 * 웹훅이 발송된 url
	 *
	 * V1 결제 건인 경우, 값이 존재하지 않습니다.
	 */
	url: string
	/**
	 * 비동기 웹훅 여부
	 *
	 * V1 결제 건인 경우, 값이 존재하지 않습니다.
	 */
	isAsync?: boolean
	/**
	 * 현재 발송 횟수
	 * (int32)
	 */
	currentExecutionCount?: number
	/**
	 * 최대 발송 횟수
	 * (int32)
	 */
	maxExecutionCount?: number
	/** 웹훅 실행 맥락 */
	trigger?: PaymentWebhookTrigger
	/** 웹훅 요청 정보 */
	request?: PaymentWebhookRequest
	/** 웹훅 응답 정보 */
	response?: PaymentWebhookResponse
	/**
	 * 웹훅 처리 시작 시점
	 * (RFC 3339 date-time)
	 */
	triggeredAt?: string
}
