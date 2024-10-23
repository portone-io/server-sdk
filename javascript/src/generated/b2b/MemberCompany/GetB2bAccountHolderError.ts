import type { B2bBankAccountNotFoundError } from "#generated/b2b/MemberCompany/B2bBankAccountNotFoundError"
import type { B2bExternalServiceError } from "#generated/common/B2bExternalServiceError"
import type { B2bFinancialSystemCommunicationError } from "#generated/b2b/MemberCompany/B2bFinancialSystemCommunicationError"
import type { B2bFinancialSystemFailureError } from "#generated/b2b/MemberCompany/B2bFinancialSystemFailureError"
import type { B2bFinancialSystemUnderMaintenanceError } from "#generated/b2b/MemberCompany/B2bFinancialSystemUnderMaintenanceError"
import type { B2bForeignExchangeAccountError } from "#generated/b2b/MemberCompany/B2bForeignExchangeAccountError"
import type { B2bNotEnabledError } from "#generated/common/B2bNotEnabledError"
import type { B2bRegularMaintenanceTimeError } from "#generated/b2b/MemberCompany/B2bRegularMaintenanceTimeError"
import type { B2bSuspendedAccountError } from "#generated/b2b/MemberCompany/B2bSuspendedAccountError"
import type { ForbiddenError } from "#generated/common/ForbiddenError"
import type { InvalidRequestError } from "#generated/common/InvalidRequestError"
import type { UnauthorizedError } from "#generated/common/UnauthorizedError"

export type GetB2bAccountHolderError =
	| B2bBankAccountNotFoundError
	| B2bExternalServiceError
	| B2bFinancialSystemCommunicationError
	| B2bFinancialSystemFailureError
	| B2bFinancialSystemUnderMaintenanceError
	| B2bForeignExchangeAccountError
	| B2bNotEnabledError
	| B2bRegularMaintenanceTimeError
	| B2bSuspendedAccountError
	| ForbiddenError
	| InvalidRequestError
	| UnauthorizedError
