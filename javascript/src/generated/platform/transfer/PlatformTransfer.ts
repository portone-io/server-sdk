import type { Unrecognized } from "./../../../utils/unrecognized"
import type { PlatformManualTransfer } from "./../../platform/transfer/PlatformManualTransfer"
import type { PlatformOrderCancelTransfer } from "./../../platform/transfer/PlatformOrderCancelTransfer"
import type { PlatformOrderTransfer } from "./../../platform/transfer/PlatformOrderTransfer"
/**
 * 정산건
 *
 * 정산건은 파트너에 정산해줄 정산 금액과 정산 방식 등이 포함되어 있는 정산 정보입니다.
 * 정산 방식은은 주문 정산, 주문 취소 정산, 수기 정산이 있습니다.
 */
export type PlatformTransfer =
	/** 수기 정산건 */
	| PlatformManualTransfer
	/** 주문 정산건 */
	| PlatformOrderTransfer
	/** 주문 취소 정산건 */
	| PlatformOrderCancelTransfer
	| { readonly type: Unrecognized }

export function isUnrecognizedPlatformTransfer(entity: PlatformTransfer): entity is { readonly type: Unrecognized } {
	return entity.type !== "MANUAL"
		&& entity.type !== "ORDER"
		&& entity.type !== "ORDER_CANCEL"
}
