import type { SelectedChannel } from "./../../common/SelectedChannel"

/** PG사에서 오류를 전달한 경우 */
export type ChannelSpecificFailurePgProvider = {
	type: "PG_PROVIDER"
	channel: SelectedChannel
	message?: string
	pgCode: string
	pgMessage: string
}
