import type { B2bExternalServiceError } from "#generated/common/B2bExternalServiceError"
import type { B2bNotEnabledError } from "#generated/common/B2bNotEnabledError"
import type { B2bTaxInvoiceAttachmentNotFoundError } from "#generated/b2b/TaxInvoice/B2bTaxInvoiceAttachmentNotFoundError"
import type { B2bTaxInvoiceNotDraftedStatusError } from "#generated/b2b/TaxInvoice/B2bTaxInvoiceNotDraftedStatusError"
import type { B2bTaxInvoiceNotFoundError } from "#generated/b2b/TaxInvoice/B2bTaxInvoiceNotFoundError"
import type { ForbiddenError } from "#generated/common/ForbiddenError"
import type { InvalidRequestError } from "#generated/common/InvalidRequestError"
import type { UnauthorizedError } from "#generated/common/UnauthorizedError"

export type DeleteB2bTaxInvoiceAttachmentError =
	| B2bExternalServiceError
	| B2bNotEnabledError
	| B2bTaxInvoiceAttachmentNotFoundError
	| B2bTaxInvoiceNotDraftedStatusError
	| B2bTaxInvoiceNotFoundError
	| ForbiddenError
	| InvalidRequestError
	| UnauthorizedError
