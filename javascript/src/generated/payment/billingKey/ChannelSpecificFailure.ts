import type { ChannelSpecificFailureInvalidRequest } from "./../../payment/billingKey/ChannelSpecificFailureInvalidRequest"
import type { ChannelSpecificFailurePgProvider } from "./../../payment/billingKey/ChannelSpecificFailurePgProvider"

export type ChannelSpecificFailure =
	/** 요청된 입력 정보가 유효하지 않은 경우 */
	| ChannelSpecificFailureInvalidRequest
	/** PG사에서 오류를 전달한 경우 */
	| ChannelSpecificFailurePgProvider
	| { readonly type: unique symbol }
