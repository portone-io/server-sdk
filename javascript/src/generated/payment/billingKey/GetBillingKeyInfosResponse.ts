import type { BillingKeyInfo } from "#generated/payment/billingKey/BillingKeyInfo"
import type { PageInfo } from "#generated/common/PageInfo"

/** 빌링키 다건 조회 성공 응답 정보 */
export type GetBillingKeyInfosResponse = {
	/** 조회된 빌링키 리스트 */
	items: BillingKeyInfo[]
	/** 조회된 페이지 정보 */
	page: PageInfo
}
