import type { PlatformUserDefinedPropertyKeyValue } from "./../../platform/transfer/PlatformUserDefinedPropertyKeyValue"
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
	 * 정산 면세 금액
	 * (int64)
	 */
	settlementTaxFreeAmount?: number
	/**
	 * 정산 일
	 *
	 * 날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
	 * (yyyy-MM-dd)
	 */
	settlementDate: string
	/**
	 * 테스트 모드 여부
	 *
	 * Query Parameter의 test에 값이 제공된 경우 Query Parameter의 test를 사용하고 해당 값은 무시됩니다.
	 * Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
	 */
	isForTest?: boolean
	/** 사용자 정의 속성 */
	userDefinedProperties?: PlatformUserDefinedPropertyKeyValue[]
}
