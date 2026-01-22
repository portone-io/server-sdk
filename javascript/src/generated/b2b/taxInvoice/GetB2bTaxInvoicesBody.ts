import type { B2bTaxInvoiceSortInput } from "./../../b2b/taxInvoice/B2bTaxInvoiceSortInput"
import type { GetB2bTaxInvoicesBodyFilter } from "./../../b2b/taxInvoice/GetB2bTaxInvoicesBodyFilter"
/** 세금 계산서 다건 조회를 위한 입력 정보 */
export type GetB2bTaxInvoicesBody = {
	/**
	 * 테스트 모드 여부
	 *
	 * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
	 */
	test?: boolean
	/**
	 * 페이지 번호
	 *
	 * 0부터 시작하는 페이지 번호. 기본 값은 0.
	 * (int32)
	 */
	pageNumber?: number
	/**
	 * 페이지 크기
	 *
	 * 각 페이지 당 포함할 객체 수. 기본 값은 500이며 최대 1000까지 요청가능합니다.
	 * (int32)
	 */
	pageSize?: number
	/** 필터 */
	filter?: GetB2bTaxInvoicesBodyFilter
	/**
	 * 정렬 조건
	 *
	 * 미입력 시 상태 업데이트 일시 내림차순 정렬됩니다.
	 */
	sort?: B2bTaxInvoiceSortInput
}
