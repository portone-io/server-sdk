import type { Country } from "./../common/Country"
import type { Currency } from "./../common/Currency"
import type { CustomerInput } from "./../common/CustomerInput"
import type { InstantPaymentMethodInput } from "./../payment/InstantPaymentMethodInput"
import type { PaymentAmountInput } from "./../common/PaymentAmountInput"
import type { PaymentProduct } from "./../common/PaymentProduct"
import type { PaymentProductType } from "./../common/PaymentProductType"
import type { SeparatedAddressInput } from "./../common/SeparatedAddressInput"
/** 수기 결제 요청 정보 */
export type InstantPaymentInput = {
	/**
	 * 상점 아이디
	 *
	 * 접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 토큰에 담긴 상점 아이디를 사용합니다.
	 */
	storeId?: string
	/**
	 * 채널 키
	 *
	 * 채널 키 또는 채널 그룹 ID 필수
	 */
	channelKey?: string
	/**
	 * 채널 그룹 ID
	 *
	 * 채널 키 또는 채널 그룹 ID 필수
	 */
	channelGroupId?: string
	/** 결제수단 정보 */
	method: InstantPaymentMethodInput
	/** 주문명 */
	orderName: string
	/**
	 * 문화비 지출 여부
	 *
	 * 기본값은 false 입니다.
	 */
	isCulturalExpense?: boolean
	/**
	 * 에스크로 결제 여부
	 *
	 * 기본값은 false 입니다.
	 */
	isEscrow?: boolean
	/** 고객 정보 */
	customer?: CustomerInput
	/** 사용자 지정 데이터 */
	customData?: string
	/** 결제 금액 세부 입력 정보 */
	amount: PaymentAmountInput
	/** 통화 */
	currency: Currency
	/** 결제 국가 */
	country?: Country
	/**
	 * 웹훅 주소
	 *
	 * 결제 승인/실패 시 요청을 받을 웹훅 주소입니다.
	 * 상점에 설정되어 있는 값보다 우선적으로 적용됩니다.
	 * 입력된 값이 없을 경우에는 빈 배열로 해석됩니다.
	 */
	noticeUrls?: string[]
	/**
	 * 상품 정보
	 *
	 * 입력된 값이 없을 경우에는 빈 배열로 해석됩니다.
	 */
	products?: PaymentProduct[]
	/**
	 * 상품 개수
	 * (int32)
	 */
	productCount?: number
	/** 상품 유형 */
	productType?: PaymentProductType
	/** 배송지 주소 */
	shippingAddress?: SeparatedAddressInput
	/** 해당 결제에 적용할 프로모션 아이디 */
	promotionId?: string
}
