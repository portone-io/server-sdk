import type { Unrecognized } from "./../../../utils/unrecognized"
import type { InvalidRequestError } from "./../../common/InvalidRequestError"
import type { UnauthorizedError } from "./../../common/UnauthorizedError"
export type DownloadPlatformTransferSheetError =
	| InvalidRequestError
	| UnauthorizedError
	| { readonly type: Unrecognized }

export function isUnrecognizedDownloadPlatformTransferSheetError(entity: DownloadPlatformTransferSheetError): entity is { readonly type: Unrecognized } {
	return entity.type !== "INVALID_REQUEST"
		&& entity.type !== "UNAUTHORIZED"
}
