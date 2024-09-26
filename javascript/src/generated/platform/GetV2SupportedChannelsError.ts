import type { ForbiddenError } from "#generated/common/ForbiddenError"
import type { InvalidRequestError } from "#generated/common/InvalidRequestError"
import type { UnauthorizedError } from "#generated/common/UnauthorizedError"

export type GetV2SupportedChannelsError =
	| ForbiddenError
	| InvalidRequestError
	| UnauthorizedError
