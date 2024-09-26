import type { PlatformUserDefinedPropertyKeyValue } from "#generated/platform/transfer/PlatformUserDefinedPropertyKeyValue"

/** 수기 정산건 생성을 위한 입력 정보 */
export type CreatePlatformManualTransferBody = {
	/** 파트너 아이디 */
	partnerId: string
	/** 메모 */
	memo?: string
	/**
	 * 정산 금액
	 * (int64)
	 */
	settlementAmount: number
	/**
	 * 정산 일
	 *
	 * 날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
	 */
	settlementDate: string
	/**
	 * 테스트 모드 여부
	 *
	 * 기본값은 false 입니다.
	 */
	isForTest?: boolean
	/** 사용자 정의 속성 */
	userDefinedProperties?: PlatformUserDefinedPropertyKeyValue[]
}
