import type { B2bExternalServiceError } from "#generated/b2b/B2bExternalServiceError"
import type { B2bNotEnabledError } from "#generated/b2b/B2bNotEnabledError"
import type { B2bRecipientNotFoundError } from "#generated/b2b/B2bRecipientNotFoundError"
import type { B2bSupplierNotFoundError } from "#generated/b2b/B2bSupplierNotFoundError"
import type { InvalidRequestError } from "#generated/common/InvalidRequestError"
import type { UnauthorizedError } from "#generated/common/UnauthorizedError"

export type RequestB2bTaxInvoiceRegisterError =
	| B2bExternalServiceError
	| B2bNotEnabledError
	| B2bRecipientNotFoundError
	| B2bSupplierNotFoundError
	| InvalidRequestError
	| UnauthorizedError