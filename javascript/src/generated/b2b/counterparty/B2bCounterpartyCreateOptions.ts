/** 거래처 생성 옵션 */
export type B2bCounterpartyCreateOptions = {
	/**
	 * 사업자 정보 조회 여부
	 *
	 * true인 경우 사업자 정보를 조회하여 거래처에 반영합니다.
	 */
	checkBusinessInfo?: boolean
	/**
	 * 휴폐업 상태 조회 여부
	 *
	 * true인 경우 휴폐업 상태를 조회하여 거래처에 반영합니다.
	 */
	checkBusinessStatus?: boolean
	/**
	 * 사업자 정보 조회 결과 ID
	 *
	 * 이전에 조회한 사업자 정보 조회 결과의 ID를 입력하면 재조회 없이 해당 결과를 사용합니다.
	 */
	businessInfoVerificationId?: string
	/**
	 * 휴폐업 상태 조회 결과 ID
	 *
	 * 이전에 조회한 휴폐업 상태 조회 결과의 ID를 입력하면 재조회 없이 해당 결과를 사용합니다.
	 */
	businessStatusVerificationId?: string
}
