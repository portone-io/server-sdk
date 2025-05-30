import type { DateTimeRange } from "./../../common/DateTimeRange"
import type { PlatformAccountTransferType } from "./../../platform/accountTransfer/PlatformAccountTransferType"
import type { Status } from "./../../platform/accountTransfer/Status"
export type PlatformAccountTransferFilter = {
	/** 거래 시간 범위 */
	tradeTimestampRange?: DateTimeRange
	/** 이체 아이디 */
	accountTransferId?: string
	/** 구분 */
	types?: PlatformAccountTransferType[]
	/** 상태 */
	statuses?: Status[]
	/** 입금자명 */
	depositorName?: string
	/** 예금주 */
	depositAccountHolder?: string
	/** 받는 이 통장 메모 */
	depositMemo?: string
	/** 보내는 이 통장 메모 */
	withdrawalMemo?: string
}
