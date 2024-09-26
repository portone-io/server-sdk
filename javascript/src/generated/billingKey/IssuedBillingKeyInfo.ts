import type { BillingKeyPaymentMethod } from "#generated/billingKey/BillingKeyPaymentMethod"
import type { ChannelGroupSummary } from "#generated/common/ChannelGroupSummary"
import type { Customer } from "#generated/common/Customer"
import type { PgBillingKeyIssueResponse } from "#generated/billingKey/PgBillingKeyIssueResponse"
import type { SelectedChannel } from "#generated/common/SelectedChannel"

/** 빌링키 발급 완료 상태 건 */
export type IssuedBillingKeyInfo = {
	/** 빌링키 상태 */
	status: "ISSUED"
	/** 빌링키 */
	billingKey: string
	/** 고객사 아이디 */
	merchantId: string
	/** 상점 아이디 */
	storeId: string
	/**
	 * 빌링키 결제수단 상세 정보
	 *
	 * 추후 슈퍼빌링키 기능 제공 시 여러 결제수단 정보가 담길 수 있습니다.
	 */
	methods?: BillingKeyPaymentMethod[]
	/**
	 * 빌링키 발급 시 사용된 채널
	 *
	 * 추후 슈퍼빌링키 기능 제공 시 여러 채널 정보가 담길 수 있습니다.
	 */
	channels: SelectedChannel[]
	/** 고객 정보 */
	customer: Customer
	/** 사용자 지정 데이터 */
	customData?: string
	/** 고객사가 채번하는 빌링키 발급 건 고유 아이디 */
	issueId?: string
	/** 빌링키 발급 건 이름 */
	issueName?: string
	/**
	 * 발급 요청 시점
	 * (RFC 3339 date-time)
	 */
	requestedAt?: string
	/**
	 * 발급 시점
	 * (RFC 3339 date-time)
	 */
	issuedAt: string
	/** 채널 그룹 */
	channelGroup?: ChannelGroupSummary
	/**
	 * 채널 별 빌링키 발급 응답
	 *
	 * 슈퍼빌링키의 경우, 빌링키 발급이 성공하더라도 일부 채널에 대한 빌링키 발급은 실패할 수 있습니다.
	 */
	pgBillingKeyIssueResponses?: PgBillingKeyIssueResponse[]
}
