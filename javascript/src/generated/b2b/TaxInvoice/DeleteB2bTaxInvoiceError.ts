import type { B2bExternalServiceError } from "#generated/common/B2bExternalServiceError"
import type { B2bNotEnabledError } from "#generated/common/B2bNotEnabledError"
import type { B2bTaxInvoiceNonDeletableStatusError } from "#generated/b2b/TaxInvoice/B2bTaxInvoiceNonDeletableStatusError"
import type { B2bTaxInvoiceNotFoundError } from "#generated/b2b/TaxInvoice/B2bTaxInvoiceNotFoundError"
import type { ForbiddenError } from "#generated/common/ForbiddenError"
import type { InvalidRequestError } from "#generated/common/InvalidRequestError"
import type { UnauthorizedError } from "#generated/common/UnauthorizedError"

export type DeleteB2bTaxInvoiceError =
	| B2bExternalServiceError
	| B2bNotEnabledError
	| B2bTaxInvoiceNonDeletableStatusError
	| B2bTaxInvoiceNotFoundError
	| ForbiddenError
	| InvalidRequestError
	| UnauthorizedError
