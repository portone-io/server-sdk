import type { B2BCannotChangeTaxTypeError } from "#generated/b2b/TaxInvoice/B2BCannotChangeTaxTypeError"
import type { B2BTaxInvoiceStatusNotSendingCompletedError } from "#generated/b2b/TaxInvoice/B2BTaxInvoiceStatusNotSendingCompletedError"
import type { B2bExternalServiceError } from "#generated/common/B2bExternalServiceError"
import type { B2bIdAlreadyExistsError } from "#generated/common/B2bIdAlreadyExistsError"
import type { B2bModificationNotProvidedError } from "#generated/b2b/TaxInvoice/B2bModificationNotProvidedError"
import type { B2bNotEnabledError } from "#generated/common/B2bNotEnabledError"
import type { B2bOriginalTaxInvoiceNotFoundError } from "#generated/b2b/TaxInvoice/B2bOriginalTaxInvoiceNotFoundError"
import type { B2bRecipientNotFoundError } from "#generated/b2b/TaxInvoice/B2bRecipientNotFoundError"
import type { B2bSupplierNotFoundError } from "#generated/b2b/TaxInvoice/B2bSupplierNotFoundError"
import type { B2bTaxInvoiceNotFoundError } from "#generated/b2b/TaxInvoice/B2bTaxInvoiceNotFoundError"
import type { B2bTaxInvoiceRecipientDocumentKeyAlreadyUsedError } from "#generated/b2b/TaxInvoice/B2bTaxInvoiceRecipientDocumentKeyAlreadyUsedError"
import type { B2bTaxInvoiceSupplierDocumentKeyAlreadyUsedError } from "#generated/b2b/TaxInvoice/B2bTaxInvoiceSupplierDocumentKeyAlreadyUsedError"
import type { ForbiddenError } from "#generated/common/ForbiddenError"
import type { InvalidRequestError } from "#generated/common/InvalidRequestError"
import type { UnauthorizedError } from "#generated/common/UnauthorizedError"

export type RequestB2bTaxInvoiceReverseIssuanceError =
	| B2BCannotChangeTaxTypeError
	| B2bExternalServiceError
	| B2bIdAlreadyExistsError
	| B2bModificationNotProvidedError
	| B2bNotEnabledError
	| B2bOriginalTaxInvoiceNotFoundError
	| B2bRecipientNotFoundError
	| B2bSupplierNotFoundError
	| B2bTaxInvoiceNotFoundError
	| B2bTaxInvoiceRecipientDocumentKeyAlreadyUsedError
	| B2BTaxInvoiceStatusNotSendingCompletedError
	| B2bTaxInvoiceSupplierDocumentKeyAlreadyUsedError
	| ForbiddenError
	| InvalidRequestError
	| UnauthorizedError
