import type { InvalidRequestError } from "./../../common/InvalidRequestError"
import type { UnauthorizedError } from "./../../common/UnauthorizedError"

export type DownloadPlatformTransferSheetError =
	| InvalidRequestError
	| UnauthorizedError
