import type { DownloadPaymentsExcelFilter } from "#generated/platform/DownloadPaymentsExcelFilter"

/** 결제건 엑셀 다운로드를 위한 입력 정보 */
export type DownloadPaymentsExcelBody = {
	/** 조회하여 다운로드할 결제 건의 조건 필터 */
	filter: DownloadPaymentsExcelFilter
}
