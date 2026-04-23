/** 취소 정산건이 참조 중인 정산건이 포함된 경우 */
export type PlatformReferencedCancelOrderTransfersExistError = {
	type: "PLATFORM_REFERENCED_CANCEL_ORDER_TRANSFERS_EXIST"
	ids: string[]
	message?: string
}
