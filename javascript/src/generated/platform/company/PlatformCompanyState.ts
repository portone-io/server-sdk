import type { PlatformBusinessStatus } from "./../../platform/company/PlatformBusinessStatus"
import type { PlatformTaxationType } from "./../../platform/company/PlatformTaxationType"
export type PlatformCompanyState = {
	taxationType: PlatformTaxationType
	/** 날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다. */
	taxationTypeDate?: string
	businessStatus: PlatformBusinessStatus
	/** 날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다. */
	closedSuspendedDate?: string
}
