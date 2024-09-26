import type { PlatformSettlementFormulaInvalidFunction } from "#generated/platform/PlatformSettlementFormulaInvalidFunction"
import type { PlatformSettlementFormulaInvalidOperator } from "#generated/platform/PlatformSettlementFormulaInvalidOperator"
import type { PlatformSettlementFormulaInvalidSyntax } from "#generated/platform/PlatformSettlementFormulaInvalidSyntax"
import type { PlatformSettlementFormulaInvalidVariable } from "#generated/platform/PlatformSettlementFormulaInvalidVariable"
import type { PlatformSettlementFormulaUnexpectedFunctionArguments } from "#generated/platform/PlatformSettlementFormulaUnexpectedFunctionArguments"
import type { PlatformSettlementFormulaUnknownError } from "#generated/platform/PlatformSettlementFormulaUnknownError"
import type { PlatformSettlementFormulaUnsupportedVariable } from "#generated/platform/PlatformSettlementFormulaUnsupportedVariable"

export type PlatformSettlementFormulaError =
	| PlatformSettlementFormulaInvalidFunction
	| PlatformSettlementFormulaInvalidOperator
	| PlatformSettlementFormulaInvalidSyntax
	| PlatformSettlementFormulaInvalidVariable
	| PlatformSettlementFormulaUnexpectedFunctionArguments
	| PlatformSettlementFormulaUnknownError
	| PlatformSettlementFormulaUnsupportedVariable
