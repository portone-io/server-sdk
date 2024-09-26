/**
 * 검색 키워드 입력 정보
 *
 * 검색 키워드 적용을 위한 옵션으로, 명시된 키워드를 포함하는 계약만 조회합니다. 하나의 하위 필드에만 값을 명시하여 요청합니다.
 */
export type PlatformContractFilterInputKeyword = {
	/** 해당 값이 포함된 id 를 가진 계약만 조회합니다. */
	id?: string
	/** 해당 값이 포함된 name 을 가진 계약만 조회합니다. */
	name?: string
}
