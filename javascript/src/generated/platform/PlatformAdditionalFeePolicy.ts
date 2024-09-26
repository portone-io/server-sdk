import type { PlatformFee } from "#generated/platform/PlatformFee"
import type { PlatformPayer } from "#generated/platform/PlatformPayer"

/**
 * 추가 수수료 정책
 *
 * 추가 수수료 정책는 고객사의 주문건에 대한 중개수수료에 별도로 추가로 부여되는 수수료입니다. 대표적인 사용 예시로 풀필먼트 수수료, 로켓배송 수수료, 마케팅 채널 수수료등이 있습니다.
 */
export type PlatformAdditionalFeePolicy = {
	/** 추가 수수료 정책 고유 아이디 */
	id: string
	graphqlId: string
	/** 추가 수수료 정책 이름 */
	name: string
	/** 책정 수수료 */
	fee: PlatformFee
	/** 해당 추가 수수료 정책에 대한 메모 */
	memo?: string
	/** 부가세를 부담할 주체 */
	vatPayer: PlatformPayer
	/** 보관 여부 */
	isArchived: boolean
	/**
	 * 변경 적용 시점
	 * (RFC 3339 date-time)
	 */
	appliedAt: string
}
