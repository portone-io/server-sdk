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
	| { readonly type: unique symbol }
