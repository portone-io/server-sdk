export type * from "./BillingKeyFailure"
export type * from "./BillingKeyFilterInput"
export type * from "./BillingKeyInfo"
export type * from "./BillingKeyInfoSummary"
export type * from "./BillingKeyNotIssuedError"
export type * from "./BillingKeyPaymentMethod"
export type * from "./BillingKeyPaymentMethodCard"
export type * from "./BillingKeyPaymentMethodEasyPay"
export type * from "./BillingKeyPaymentMethodEasyPayCharge"
export type * from "./BillingKeyPaymentMethodEasyPayMethod"
export type * from "./BillingKeyPaymentMethodMobile"
export type * from "./BillingKeyPaymentMethodPaypal"
export type * from "./BillingKeyPaymentMethodTransfer"
export type * from "./BillingKeyPaymentMethodType"
export type * from "./BillingKeySortBy"
export type * from "./BillingKeySortInput"
export type * from "./BillingKeyStatus"
export type * from "./BillingKeyTextSearch"
export type * from "./BillingKeyTextSearchField"
export type * from "./BillingKeyTimeRangeField"
export type * from "./ChannelSpecificError"
export type * from "./ChannelSpecificFailure"
export type * from "./ChannelSpecificFailureInvalidRequest"
export type * from "./ChannelSpecificFailurePgProvider"
export type * from "./DeleteBillingKeyError"
export type * from "./DeleteBillingKeyResponse"
export type * from "./DeletedBillingKeyInfo"
export type * from "./FailedPgBillingKeyIssueResponse"
export type * from "./GetBillingKeyInfoError"
export type * from "./GetBillingKeyInfosBody"
export type * from "./GetBillingKeyInfosError"
export type * from "./GetBillingKeyInfosResponse"
export type * from "./InstantBillingKeyPaymentMethodInput"
export type * from "./InstantBillingKeyPaymentMethodInputCard"
export type * from "./IssueBillingKeyBody"
export type * from "./IssueBillingKeyError"
export type * from "./IssueBillingKeyResponse"
export type * from "./IssuedBillingKeyInfo"
export type * from "./IssuedPgBillingKeyIssueResponse"
export type * from "./PgBillingKeyIssueResponse"
import type { BillingKeyFilterInput } from "#generated/billingKey/BillingKeyFilterInput"
import type { BillingKeyInfo } from "#generated/billingKey/BillingKeyInfo"
import type { BillingKeySortInput } from "#generated/billingKey/BillingKeySortInput"
import type { CustomerInput } from "#generated/common/CustomerInput"
import type { DeleteBillingKeyResponse } from "#generated/billingKey/DeleteBillingKeyResponse"
import type { GetBillingKeyInfosResponse } from "#generated/billingKey/GetBillingKeyInfosResponse"
import type { InstantBillingKeyPaymentMethodInput } from "#generated/billingKey/InstantBillingKeyPaymentMethodInput"
import type { IssueBillingKeyResponse } from "#generated/billingKey/IssueBillingKeyResponse"
import type { PageInput } from "#generated/common/PageInput"

export type Operations = {
	/**
	 * 빌링키 단건 조회
	 *
	 * 주어진 빌링키에 대응되는 빌링키 정보를 조회합니다.
	 *
	 * @throws {@link Errors.BillingKeyNotFoundError} 빌링키가 존재하지 않는 경우
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getBillingKeyInfo: (
		/** 조회할 빌링키 */
		billingKey: string,
	) => Promise<BillingKeyInfo>
	/**
	 * 빌링키 삭제
	 *
	 * 빌링키를 삭제합니다.
	 *
	 * @throws {@link Errors.BillingKeyAlreadyDeletedError} 빌링키가 이미 삭제된 경우
	 * @throws {@link Errors.BillingKeyNotFoundError} 빌링키가 존재하지 않는 경우
	 * @throws {@link Errors.BillingKeyNotIssuedError} BillingKeyNotIssuedError
	 * @throws {@link Errors.ChannelSpecificError} 여러 채널을 지정한 요청에서, 채널 각각에서 오류가 발생한 경우
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PaymentScheduleAlreadyExistsError} 결제 예약건이 이미 존재하는 경우
	 * @throws {@link Errors.PgProviderError} PG사에서 오류를 전달한 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	deleteBillingKey: (
		/** 삭제할 빌링키 */
		billingKey: string,
	) => Promise<DeleteBillingKeyResponse>
	/**
	 * 빌링키 다건 조회
	 *
	 * 주어진 조건에 맞는 빌링키들을 페이지 기반으로 조회합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getBillingKeyInfos: (
		options?: {
			/**
			 * 요청할 페이지 정보
			 *
			 * 미 입력 시 number: 0, size: 10 으로 기본값이 적용됩니다.
			 */
			page?: PageInput,
			/**
			 * 정렬 조건
			 *
			 * 미 입력 시 sortBy: TIME_TO_PAY, sortOrder: DESC 으로 기본값이 적용됩니다.
			 */
			sort?: BillingKeySortInput,
			/**
			 * 조회할 빌링키 조건 필터
			 *
			 * V1 빌링키 건의 경우 일부 필드에 대해 필터가 적용되지 않을 수 있습니다.
			 */
			filter?: BillingKeyFilterInput,
		}
	) => Promise<GetBillingKeyInfosResponse>
	/**
	 * 빌링키 발급
	 *
	 * 빌링키 발급을 요청합니다.
	 *
	 * @throws {@link Errors.ChannelNotFoundError} 요청된 채널이 존재하지 않는 경우
	 * @throws {@link Errors.ChannelSpecificError} 여러 채널을 지정한 요청에서, 채널 각각에서 오류가 발생한 경우
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PgProviderError} PG사에서 오류를 전달한 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	issueBillingKey: (
		options: {
			/** 빌링키 결제 수단 정보 */
			method: InstantBillingKeyPaymentMethodInput,
			/**
			 * 채널 키
			 *
			 * 채널 키 또는 채널 그룹 ID 필수
			 */
			channelKey?: string,
			/**
			 * 채널 그룹 ID
			 *
			 * 채널 키 또는 채널 그룹 ID 필수
			 */
			channelGroupId?: string,
			/** 고객 정보 */
			customer?: CustomerInput,
			/** 사용자 지정 데이터 */
			customData?: string,
			/** PG사별 추가 파라미터 ("PG사별 연동 가이드" 참고) */
			bypass?: object,
			/**
			 * 웹훅 주소
			 *
			 * 빌링키 발급 시 요청을 받을 웹훅 주소입니다.
			 * 상점에 설정되어 있는 값보다 우선적으로 적용됩니다.
			 * 입력된 값이 없을 경우에는 빈 배열로 해석됩니다.
			 */
			noticeUrls?: string[],
		}
	) => Promise<IssueBillingKeyResponse>
}
