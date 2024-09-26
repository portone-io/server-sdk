import type { B2bNotEnabledError } from "#generated/b2b/B2bNotEnabledError"
import type { InvalidRequestError } from "#generated/common/InvalidRequestError"
import type { UnauthorizedError } from "#generated/common/UnauthorizedError"

export type CreateB2bTaxInvoiceFileUploadLinkCreateError =
	| B2bNotEnabledError
	| InvalidRequestError
	| UnauthorizedError
