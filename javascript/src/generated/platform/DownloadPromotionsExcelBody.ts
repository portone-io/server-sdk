import type { DateTimeRange } from "#generated/common/DateTimeRange"
import type { PromotionTimeRangeField } from "#generated/platform/PromotionTimeRangeField"

/** 프로모션 내역 엑셀 다운로드를 위한 입력 정보 */
export type DownloadPromotionsExcelBody = {
	/**
	 * 상점 아이디
	 *
	 * 접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 토큰에 담긴 상점 아이디를 사용합니다.
	 */
	storeId: string
	/** 시각 범위 */
	datetimeRange?: DateTimeRange
	/** 시각 범위를 적용할 필드 */
	datetimeRangeField?: PromotionTimeRangeField
}
