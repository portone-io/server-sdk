import type { B2bExternalServiceError } from "#generated/b2b/B2bExternalServiceError"
import type { B2bFileNotFoundError } from "#generated/b2b/B2bFileNotFoundError"
import type { B2bNotEnabledError } from "#generated/b2b/B2bNotEnabledError"
import type { B2bTaxInvoiceNotFoundError } from "#generated/b2b/B2bTaxInvoiceNotFoundError"
import type { B2bTaxInvoiceNotRegisteredStatusError } from "#generated/b2b/B2bTaxInvoiceNotRegisteredStatusError"
import type { InvalidRequestError } from "#generated/common/InvalidRequestError"
import type { UnauthorizedError } from "#generated/common/UnauthorizedError"

export type AttachB2bTaxInvoiceFileError =
	| B2bExternalServiceError
	| B2bFileNotFoundError
	| B2bNotEnabledError
	| B2bTaxInvoiceNotFoundError
	| B2bTaxInvoiceNotRegisteredStatusError
	| InvalidRequestError
	| UnauthorizedError
