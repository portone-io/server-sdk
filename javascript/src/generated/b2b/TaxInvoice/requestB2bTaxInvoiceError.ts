import type { B2BCannotChangeTaxTypeError } from "#generated/b2b/TaxInvoice/B2BCannotChangeTaxTypeError"
import type { B2BTaxInvoiceStatusNotSendingCompletedError } from "#generated/b2b/TaxInvoice/B2BTaxInvoiceStatusNotSendingCompletedError"
import type { B2bExternalServiceError } from "#generated/common/B2bExternalServiceError"
import type { B2bModificationNotProvidedError } from "#generated/b2b/TaxInvoice/B2bModificationNotProvidedError"
import type { B2bNotEnabledError } from "#generated/common/B2bNotEnabledError"
import type { B2bOriginalTaxInvoiceNotFoundError } from "#generated/b2b/TaxInvoice/B2bOriginalTaxInvoiceNotFoundError"
import type { B2bTaxInvoiceNoRecipientDocumentKeyError } from "#generated/b2b/TaxInvoice/B2bTaxInvoiceNoRecipientDocumentKeyError"
import type { B2bTaxInvoiceNotDraftedStatusError } from "#generated/b2b/TaxInvoice/B2bTaxInvoiceNotDraftedStatusError"
import type { B2bTaxInvoiceNotFoundError } from "#generated/b2b/TaxInvoice/B2bTaxInvoiceNotFoundError"
import type { ForbiddenError } from "#generated/common/ForbiddenError"
import type { InvalidRequestError } from "#generated/common/InvalidRequestError"
import type { UnauthorizedError } from "#generated/common/UnauthorizedError"

export type requestB2bTaxInvoiceError =
	| B2BCannotChangeTaxTypeError
	| B2bExternalServiceError
	| B2bModificationNotProvidedError
	| B2bNotEnabledError
	| B2bOriginalTaxInvoiceNotFoundError
	| B2bTaxInvoiceNotDraftedStatusError
	| B2bTaxInvoiceNotFoundError
	| B2bTaxInvoiceNoRecipientDocumentKeyError
	| B2BTaxInvoiceStatusNotSendingCompletedError
	| ForbiddenError
	| InvalidRequestError
	| UnauthorizedError
