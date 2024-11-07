import type { BillingKeyPaymentMethodType } from "./../../payment/billingKey/BillingKeyPaymentMethodType"
import type { BillingKeyStatus } from "./../../payment/billingKey/BillingKeyStatus"
import type { BillingKeyTextSearch } from "./../../payment/billingKey/BillingKeyTextSearch"
import type { BillingKeyTimeRangeField } from "./../../payment/billingKey/BillingKeyTimeRangeField"
import type { PaymentClientType } from "./../../common/PaymentClientType"
import type { PgCompany } from "./../../payment/billingKey/PgCompany"
import type { PgProvider } from "./../../common/PgProvider"
import type { PortOneVersion } from "./../../common/PortOneVersion"

/** 빌링키 다건 조회를 위한 입력 정보 */
export type BillingKeyFilterInput = {
	/**
	 * 상점 아이디
	 *
	 * Merchant 사용자만 사용가능하며, 지정되지 않은 경우 고객사 전체 빌링키를 조회합니다.
	 */
	storeId?: string
	/** 조회 기준 시점 유형 */
	timeRangeField?: BillingKeyTimeRangeField
	/**
	 * 조회 기준 시점 범위의 시작
	 *
	 * 값을 입력하지 않으면 end의 90일 전으로 설정됩니다.
	 * (RFC 3339 date-time)
	 */
	from?: string
	/**
	 * 조회 기준 시점 범위의 끝
	 *
	 * 값을 입력하지 않으면 현재 시점으로 설정됩니다.
	 * (RFC 3339 date-time)
	 */
	until?: string
	/**
	 * 빌링키 상태 리스트
	 *
	 * 값을 입력하지 않으면 빌링키 상태 필터링이 적용되지 않습니다.
	 */
	status?: BillingKeyStatus[]
	/**
	 * 채널 그룹 아이디 리스트
	 *
	 * 값을 입력하지 않으면 스마트 라우팅 그룹 아이디 필터링이 적용되지 않습니다.
	 */
	channelGroupIds?: string[]
	/** 고객 ID */
	customerId?: string
	/** 플랫폼 유형 */
	platformType?: PaymentClientType
	/** 통합 검색 필터 */
	textSearch?: BillingKeyTextSearch
	/**
	 * PG사 결제 모듈 리스트
	 *
	 * 값을 입력하지 않으면 PG사 결제 모듈 필터링이 적용되지 않습니다.
	 */
	pgProviders?: PgProvider[]
	/**
	 * PG사 리스트
	 *
	 * 값을 입력하지 않으면 PG사 필터링이 적용되지 않습니다.
	 */
	pgCompanies?: PgCompany[]
	/**
	 * 결제수단 리스트
	 *
	 * 값을 입력하지 않으면 결제수단 필터링이 적용되지 않습니다.
	 */
	methods?: BillingKeyPaymentMethodType[]
	/** 포트원 버전 */
	version?: PortOneVersion
}
