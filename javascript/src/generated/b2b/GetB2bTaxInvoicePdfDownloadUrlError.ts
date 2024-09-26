import type { B2bExternalServiceError } from "#generated/b2b/B2bExternalServiceError"
import type { B2bNotEnabledError } from "#generated/b2b/B2bNotEnabledError"
import type { B2bTaxInvoiceNotFoundError } from "#generated/b2b/B2bTaxInvoiceNotFoundError"
import type { InvalidRequestError } from "#generated/common/InvalidRequestError"
import type { UnauthorizedError } from "#generated/common/UnauthorizedError"

export type GetB2bTaxInvoicePdfDownloadUrlError =
	| B2bExternalServiceError
	| B2bNotEnabledError
	| B2bTaxInvoiceNotFoundError
	| InvalidRequestError
	| UnauthorizedError
