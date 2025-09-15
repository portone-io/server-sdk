import type { DateTimeRange } from "./../../common/DateTimeRange"
import type { PlatformAccountTransferStatus } from "./../../platform/accountTransfer/PlatformAccountTransferStatus"
import type { PlatformAccountTransferType } from "./../../platform/accountTransfer/PlatformAccountTransferType"
export type PlatformAccountTransferFilter = {
	/** 이체 일시 범위 */
	tradeTimestampRange?: DateTimeRange
	/** 생성 일시 범위 */
	createdTimestampRange?: DateTimeRange
	/** 상태 업데이트 일시 범위 */
	statusUpdatedTimestampRange?: DateTimeRange
	/** 이체 예정 일시 범위 */
	scheduledTimestampRange?: DateTimeRange
	/** 이체 아이디 */
	accountTransferId?: string
	/** 계좌 아이디 */
	bankAccountId?: string
	/** 일괄 이체 아이디 */
	bulkAccountTransferId?: string
	/** 지급 아이디 */
	payoutId?: string
	/** 이체 아이디 리스트 */
	accountTransferIds?: string[]
	/** 구분 */
	types?: PlatformAccountTransferType[]
	/** 상태 */
	statuses?: PlatformAccountTransferStatus[]
	/** 입금자명 */
	depositorName?: string
	/** 예금주 */
	depositAccountHolder?: string
	/** 받는 이 통장 메모 */
	depositMemo?: string
	/** 보내는 이 통장 메모 */
	withdrawalMemo?: string
}
