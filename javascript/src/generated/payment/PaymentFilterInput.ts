import type { CardBrand } from "#generated/common/CardBrand"
import type { CardOwnerType } from "#generated/common/CardOwnerType"
import type { CardType } from "#generated/common/CardType"
import type { CashReceiptInputType } from "#generated/common/CashReceiptInputType"
import type { Currency } from "#generated/common/Currency"
import type { DateTimeRange } from "#generated/common/DateTimeRange"
import type { PaymentCashReceiptStatus } from "#generated/payment/PaymentCashReceiptStatus"
import type { PaymentClientType } from "#generated/common/PaymentClientType"
import type { PaymentFilterInputEscrowStatus } from "#generated/payment/PaymentFilterInputEscrowStatus"
import type { PaymentMethodGiftCertificateType } from "#generated/payment/PaymentMethodGiftCertificateType"
import type { PaymentMethodType } from "#generated/common/PaymentMethodType"
import type { PaymentSortBy } from "#generated/payment/PaymentSortBy"
import type { PaymentStatus } from "#generated/common/PaymentStatus"
import type { PaymentTextSearch } from "#generated/payment/PaymentTextSearch"
import type { PaymentTimestampType } from "#generated/payment/PaymentTimestampType"
import type { PaymentWebhookStatus } from "#generated/payment/PaymentWebhookStatus"
import type { PgProvider } from "#generated/common/PgProvider"
import type { PortOneVersion } from "#generated/common/PortOneVersion"
import type { SortOrder } from "#generated/common/SortOrder"

/** 결제 건 다건 조회를 위한 입력 정보 */
export type PaymentFilterInput = {
	/** 고객사 아이디 */
	merchantId?: string
	/**
	 * 상점 아이디
	 *
	 * Merchant 사용자만 사용가능하며, 지정되지 않은 경우 고객사 전체 결제 건을 조회합니다.
	 */
	storeId?: string
	/** 조회 기준 시점 유형 */
	timestampType?: PaymentTimestampType
	/**
	 * 결제 요청/상태 승인 시점 범위의 시작
	 *
	 * 값을 입력하지 않으면 end의 90일 전으로 설정됩니다.
	 * (RFC 3339 date-time)
	 */
	from?: string
	/**
	 * 결제 요청/상태 승인 시점 범위의 끝
	 *
	 * 값을 입력하지 않으면 현재 시점으로 설정됩니다.
	 * (RFC 3339 date-time)
	 */
	until?: string
	/**
	 * 결제 상태 리스트
	 *
	 * 값을 입력하지 않으면 결제상태 필터링이 적용되지 않습니다.
	 */
	status?: PaymentStatus[]
	/**
	 * 결제수단 리스트
	 *
	 * 값을 입력하지 않으면 결제수단 필터링이 적용되지 않습니다.
	 */
	methods?: PaymentMethodType[]
	/**
	 * PG사 리스트
	 *
	 * 값을 입력하지 않으면 결제대행사 필터링이 적용되지 않습니다.
	 */
	pgProvider?: PgProvider[]
	/** 테스트 결제 필터링 */
	isTest?: boolean
	/** 결제 예약 건 필터링 */
	isScheduled?: boolean
	/** 결제 건 정렬 기준 */
	sortBy?: PaymentSortBy
	/** 결제 건 정렬 방식 */
	sortOrder?: SortOrder
	/** 포트원 버전 */
	version?: PortOneVersion
	/** 웹훅 상태 */
	webhookStatus?: PaymentWebhookStatus
	/** 플랫폼 유형 */
	platformType?: PaymentClientType
	/** 통화 */
	currency?: Currency
	/** 에스크로 결제 여부 */
	isEscrow?: boolean
	/** 에스크로 결제의 배송 정보 상태 */
	escrowStatus?: PaymentFilterInputEscrowStatus
	/** 카드 브랜드 */
	cardBrand?: CardBrand
	/** 카드 유형 */
	cardType?: CardType
	/** 카드 소유주 유형 */
	cardOwnerType?: CardOwnerType
	/** 상품권 종류 */
	giftCertificateType?: PaymentMethodGiftCertificateType
	/** 현금영수증 유형 */
	cashReceiptType?: CashReceiptInputType
	/** 현금영수증 상태 */
	cashReceiptStatus?: PaymentCashReceiptStatus
	/** 현금영수증 발급 시간 범위 */
	cashReceiptIssuedAtRange?: DateTimeRange
	/** 현금영수증 취소 시간 범위 */
	cashReceiptCancelledAtRange?: DateTimeRange
	/** 통합 검색 리스트 필터 */
	textSearch?: PaymentTextSearch[]
}
