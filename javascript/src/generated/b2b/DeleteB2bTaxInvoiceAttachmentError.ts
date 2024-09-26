import type { B2bExternalServiceError } from "#generated/b2b/B2bExternalServiceError"
import type { B2bNotEnabledError } from "#generated/b2b/B2bNotEnabledError"
import type { B2bTaxInvoiceAttachmentNotFoundError } from "#generated/b2b/B2bTaxInvoiceAttachmentNotFoundError"
import type { B2bTaxInvoiceNotFoundError } from "#generated/b2b/B2bTaxInvoiceNotFoundError"
import type { B2bTaxInvoiceNotRegisteredStatusError } from "#generated/b2b/B2bTaxInvoiceNotRegisteredStatusError"
import type { InvalidRequestError } from "#generated/common/InvalidRequestError"
import type { UnauthorizedError } from "#generated/common/UnauthorizedError"

export type DeleteB2bTaxInvoiceAttachmentError =
	| B2bExternalServiceError
	| B2bNotEnabledError
	| B2bTaxInvoiceAttachmentNotFoundError
	| B2bTaxInvoiceNotFoundError
	| B2bTaxInvoiceNotRegisteredStatusError
	| InvalidRequestError
	| UnauthorizedError
