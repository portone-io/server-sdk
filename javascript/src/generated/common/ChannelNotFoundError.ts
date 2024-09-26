/** 요청된 채널이 존재하지 않는 경우 */
export type ChannelNotFoundError = {
	type: "CHANNEL_NOT_FOUND"
	message?: string
}
