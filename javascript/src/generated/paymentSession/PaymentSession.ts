import type { CheckoutPaymentMethod } from "./../common/CheckoutPaymentMethod"
import type { Country } from "./../common/Country"
import type { Currency } from "./../common/Currency"
import type { PaymentSessionAgreement } from "./../paymentSession/PaymentSessionAgreement"
import type { PaymentSessionColors } from "./../paymentSession/PaymentSessionColors"
import type { PaymentSessionProduct } from "./../paymentSession/PaymentSessionProduct"
/** 결제 세션 */
export type PaymentSession = {
	/** 결제 세션 아이디 */
	id: string
	/** 상점 아이디 */
	storeId: string
	/** 결제 건 아이디 */
	paymentId: string
	/** 프로필 키 */
	profileKey: string
	/**
	 * 결제 수단 지정
	 *
	 * 지정한 경우, 정보 추가 입력이 필요하지 않은 경우에 주문서를 건너뛰고 결제로 바로 이동합니다.
	 */
	paymentMethod?: CheckoutPaymentMethod
	/** 국가 */
	country: Country
	/** 통화 */
	currency: Currency
	/**
	 * 전체 결제 금액
	 * (int64)
	 */
	totalAmount: number
	/** 주문명 */
	orderName: string
	/**
	 * 결제 완료 후 리다이렉트 URL
	 *
	 * 지정하지 않으면 기본 결과 페이지가 표시됩니다.
	 */
	redirectUrl?: string
	/** 주문 항목 목록 */
	products?: PaymentSessionProduct[]
	/** 구매자 이름 */
	customerName?: string
	/** 구매자 이메일 */
	customerEmail?: string
	/**
	 * 상점 이름
	 *
	 * 페이지 헤더 및 결제사 UI에 표시됩니다.
	 */
	storeName?: string
	/**
	 * 사용자 지정 약관 목록
	 *
	 * 구매자가 모든 약관에 동의해야 결제 버튼이 활성화됩니다.
	 */
	agreements?: PaymentSessionAgreement[]
	/** 주문 대표 이미지 URL */
	orderImageUrl?: string
	/**
	 * 사용자 지정 데이터
	 *
	 * 결제 완료 후 결제 건 조회에서도 확인할 수 있습니다.
	 */
	customData?: string
	/** 체크아웃 페이지 색 설정 */
	colors?: PaymentSessionColors
	/**
	 * 생성 시각
	 * (RFC 3339 date-time)
	 */
	createdAt: string
	/**
	 * 만료 시각
	 * (RFC 3339 date-time)
	 */
	expiresAt: string
}
