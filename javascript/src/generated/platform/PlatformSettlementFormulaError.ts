import type { Unrecognized } from "./../../utils/unrecognized"
import type { PlatformSettlementFormulaInvalidFunction } from "./../platform/PlatformSettlementFormulaInvalidFunction"
import type { PlatformSettlementFormulaInvalidOperator } from "./../platform/PlatformSettlementFormulaInvalidOperator"
import type { PlatformSettlementFormulaInvalidSyntax } from "./../platform/PlatformSettlementFormulaInvalidSyntax"
import type { PlatformSettlementFormulaInvalidVariable } from "./../platform/PlatformSettlementFormulaInvalidVariable"
import type { PlatformSettlementFormulaUnexpectedFunctionArguments } from "./../platform/PlatformSettlementFormulaUnexpectedFunctionArguments"
import type { PlatformSettlementFormulaUnknownError } from "./../platform/PlatformSettlementFormulaUnknownError"
import type { PlatformSettlementFormulaUnsupportedVariable } from "./../platform/PlatformSettlementFormulaUnsupportedVariable"
export type PlatformSettlementFormulaError =
	| PlatformSettlementFormulaInvalidFunction
	| PlatformSettlementFormulaInvalidOperator
	| PlatformSettlementFormulaInvalidSyntax
	| PlatformSettlementFormulaInvalidVariable
	| PlatformSettlementFormulaUnexpectedFunctionArguments
	| PlatformSettlementFormulaUnknownError
	| PlatformSettlementFormulaUnsupportedVariable
	| { readonly type: Unrecognized }

export function isUnrecognizedPlatformSettlementFormulaError(entity: PlatformSettlementFormulaError): entity is { readonly type: Unrecognized } {
	return entity.type !== "INVALID_FUNCTION"
		&& entity.type !== "INVALID_OPERATOR"
		&& entity.type !== "INVALID_SYNTAX"
		&& entity.type !== "INVALID_VARIABLE"
		&& entity.type !== "UNEXPECTED_FUNCTION_ARGUMENTS"
		&& entity.type !== "UNKNOWN_ERROR"
		&& entity.type !== "UNSUPPORTED_VARIABLE"
}
