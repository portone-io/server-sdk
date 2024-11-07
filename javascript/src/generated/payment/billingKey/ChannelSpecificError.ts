import type { ChannelSpecificFailure } from "./../../payment/billingKey/ChannelSpecificFailure"
import type { SelectedChannel } from "./../../common/SelectedChannel"

/** 여러 채널을 지정한 요청에서, 채널 각각에서 오류가 발생한 경우 */
export type ChannelSpecificError = {
	type: "CHANNEL_SPECIFIC"
	message?: string
	failures: ChannelSpecificFailure[]
	/** (결제, 본인인증 등에) 선택된 채널 정보 */
	succeededChannels: SelectedChannel[]
}
