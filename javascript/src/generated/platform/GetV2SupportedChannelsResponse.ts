import type { Channel } from "#generated/platform/Channel"

/** 채널 다건 조회 성공 응답 정보 */
export type GetV2SupportedChannelsResponse = {
	/** 조회된 채널 리스트 */
	items: Channel[]
}
