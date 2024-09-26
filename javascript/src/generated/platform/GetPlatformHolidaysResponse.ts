import type { PlatformHoliday } from "#generated/platform/PlatformHoliday"

/** 공휴일 조회 */
export type GetPlatformHolidaysResponse = {
	/** 공휴일 리스트 */
	holidays: PlatformHoliday[]
}
