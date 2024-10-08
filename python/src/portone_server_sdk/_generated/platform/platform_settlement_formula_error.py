from __future__ import annotations
from typing import Any, Optional, Union
from portone_server_sdk._generated.platform.platform_settlement_formula_invalid_function import PlatformSettlementFormulaInvalidFunction, _deserialize_platform_settlement_formula_invalid_function, _serialize_platform_settlement_formula_invalid_function
from portone_server_sdk._generated.platform.platform_settlement_formula_invalid_operator import PlatformSettlementFormulaInvalidOperator, _deserialize_platform_settlement_formula_invalid_operator, _serialize_platform_settlement_formula_invalid_operator
from portone_server_sdk._generated.platform.platform_settlement_formula_invalid_syntax import PlatformSettlementFormulaInvalidSyntax, _deserialize_platform_settlement_formula_invalid_syntax, _serialize_platform_settlement_formula_invalid_syntax
from portone_server_sdk._generated.platform.platform_settlement_formula_invalid_variable import PlatformSettlementFormulaInvalidVariable, _deserialize_platform_settlement_formula_invalid_variable, _serialize_platform_settlement_formula_invalid_variable
from portone_server_sdk._generated.platform.platform_settlement_formula_unexpected_function_arguments import PlatformSettlementFormulaUnexpectedFunctionArguments, _deserialize_platform_settlement_formula_unexpected_function_arguments, _serialize_platform_settlement_formula_unexpected_function_arguments
from portone_server_sdk._generated.platform.platform_settlement_formula_unknown_error import PlatformSettlementFormulaUnknownError, _deserialize_platform_settlement_formula_unknown_error, _serialize_platform_settlement_formula_unknown_error
from portone_server_sdk._generated.platform.platform_settlement_formula_unsupported_variable import PlatformSettlementFormulaUnsupportedVariable, _deserialize_platform_settlement_formula_unsupported_variable, _serialize_platform_settlement_formula_unsupported_variable

PlatformSettlementFormulaError = Union[PlatformSettlementFormulaInvalidFunction, PlatformSettlementFormulaInvalidOperator, PlatformSettlementFormulaInvalidSyntax, PlatformSettlementFormulaInvalidVariable, PlatformSettlementFormulaUnexpectedFunctionArguments, PlatformSettlementFormulaUnknownError, PlatformSettlementFormulaUnsupportedVariable]


def _serialize_platform_settlement_formula_error(obj: PlatformSettlementFormulaError) -> Any:
    if obj.type == "INVALID_FUNCTION":
        return _serialize_platform_settlement_formula_invalid_function(obj)
    if obj.type == "INVALID_OPERATOR":
        return _serialize_platform_settlement_formula_invalid_operator(obj)
    if obj.type == "INVALID_SYNTAX":
        return _serialize_platform_settlement_formula_invalid_syntax(obj)
    if obj.type == "INVALID_VARIABLE":
        return _serialize_platform_settlement_formula_invalid_variable(obj)
    if obj.type == "UNEXPECTED_FUNCTION_ARGUMENTS":
        return _serialize_platform_settlement_formula_unexpected_function_arguments(obj)
    if obj.type == "UNKNOWN_ERROR":
        return _serialize_platform_settlement_formula_unknown_error(obj)
    if obj.type == "UNSUPPORTED_VARIABLE":
        return _serialize_platform_settlement_formula_unsupported_variable(obj)


def _deserialize_platform_settlement_formula_error(obj: Any) -> PlatformSettlementFormulaError:
    try:
        return _deserialize_platform_settlement_formula_invalid_function(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_settlement_formula_invalid_operator(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_settlement_formula_invalid_syntax(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_settlement_formula_invalid_variable(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_settlement_formula_unexpected_function_arguments(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_settlement_formula_unknown_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_settlement_formula_unsupported_variable(obj)
    except Exception:
        pass
    raise ValueError(f"{repr(obj)} is not PlatformSettlementFormulaError")
