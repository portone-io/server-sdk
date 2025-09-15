from __future__ import annotations
from typing import Any, Optional, Union
from ...common.invalid_request_error import InvalidRequestError, _deserialize_invalid_request_error, _serialize_invalid_request_error
from ...common.unauthorized_error import UnauthorizedError, _deserialize_unauthorized_error, _serialize_unauthorized_error

DownloadB2bTaxInvoicesSheetError = Union[InvalidRequestError, UnauthorizedError, dict]


def _serialize_download_b2b_tax_invoices_sheet_error(obj: DownloadB2bTaxInvoicesSheetError) -> Any:
    if isinstance(obj, dict):
        return obj
    if isinstance(obj, InvalidRequestError):
        return _serialize_invalid_request_error(obj)
    if isinstance(obj, UnauthorizedError):
        return _serialize_unauthorized_error(obj)


def _deserialize_download_b2b_tax_invoices_sheet_error(obj: Any) -> DownloadB2bTaxInvoicesSheetError:
    try:
        return _deserialize_invalid_request_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_unauthorized_error(obj)
    except Exception:
        pass
    raise ValueError(f"{repr(obj)} is not DownloadB2bTaxInvoicesSheetError")
