import type { B2bExternalServiceError } from "#generated/b2b/B2bExternalServiceError"
import type { B2bNotEnabledError } from "#generated/b2b/B2bNotEnabledError"
import type { B2bTaxInvoiceNotIssuedStatusError } from "#generated/b2b/B2bTaxInvoiceNotIssuedStatusError"
import type { InvalidRequestError } from "#generated/common/InvalidRequestError"
import type { UnauthorizedError } from "#generated/common/UnauthorizedError"

export type CancelB2bTaxInvoiceIssuanceError =
	| B2bExternalServiceError
	| B2bNotEnabledError
	| B2bTaxInvoiceNotIssuedStatusError
	| InvalidRequestError
	| UnauthorizedError
