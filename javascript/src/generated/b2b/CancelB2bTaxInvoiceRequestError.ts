import type { B2bExternalServiceError } from "#generated/b2b/B2bExternalServiceError"
import type { B2bNotEnabledError } from "#generated/b2b/B2bNotEnabledError"
import type { B2bTaxInvoiceNoRecipientDocumentKeyError } from "#generated/b2b/B2bTaxInvoiceNoRecipientDocumentKeyError"
import type { B2bTaxInvoiceNotFoundError } from "#generated/b2b/B2bTaxInvoiceNotFoundError"
import type { B2bTaxInvoiceNotRequestedStatusError } from "#generated/b2b/B2bTaxInvoiceNotRequestedStatusError"
import type { InvalidRequestError } from "#generated/common/InvalidRequestError"
import type { UnauthorizedError } from "#generated/common/UnauthorizedError"

export type CancelB2bTaxInvoiceRequestError =
	| B2bExternalServiceError
	| B2bNotEnabledError
	| B2bTaxInvoiceNotFoundError
	| B2bTaxInvoiceNotRequestedStatusError
	| B2bTaxInvoiceNoRecipientDocumentKeyError
	| InvalidRequestError
	| UnauthorizedError
