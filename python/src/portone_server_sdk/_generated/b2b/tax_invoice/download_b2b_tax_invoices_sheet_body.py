from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...b2b.tax_invoice.get_b2b_tax_invoices_body_filter import GetB2bTaxInvoicesBodyFilter, _deserialize_get_b2b_tax_invoices_body_filter, _serialize_get_b2b_tax_invoices_body_filter
from ...b2b.tax_invoice.tax_invoices_sheet_field import TaxInvoicesSheetField, _deserialize_tax_invoices_sheet_field, _serialize_tax_invoices_sheet_field

@dataclass
class DownloadB2bTaxInvoicesSheetBody:
    filter: Optional[GetB2bTaxInvoicesBodyFilter] = field(default=None)
    fields: Optional[list[TaxInvoicesSheetField]] = field(default=None)
    """다운로드 할 시트 컬럼
    """
    test: Optional[bool] = field(default=None)


def _serialize_download_b2b_tax_invoices_sheet_body(obj: DownloadB2bTaxInvoicesSheetBody) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    if obj.filter is not None:
        entity["filter"] = _serialize_get_b2b_tax_invoices_body_filter(obj.filter)
    if obj.fields is not None:
        entity["fields"] = list(map(_serialize_tax_invoices_sheet_field, obj.fields))
    if obj.test is not None:
        entity["test"] = obj.test
    return entity


def _deserialize_download_b2b_tax_invoices_sheet_body(obj: Any) -> DownloadB2bTaxInvoicesSheetBody:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "filter" in obj:
        filter = obj["filter"]
        filter = _deserialize_get_b2b_tax_invoices_body_filter(filter)
    else:
        filter = None
    if "fields" in obj:
        fields = obj["fields"]
        if not isinstance(fields, list):
            raise ValueError(f"{repr(fields)} is not list")
        for i, item in enumerate(fields):
            item = _deserialize_tax_invoices_sheet_field(item)
            fields[i] = item
    else:
        fields = None
    if "test" in obj:
        test = obj["test"]
        if not isinstance(test, bool):
            raise ValueError(f"{repr(test)} is not bool")
    else:
        test = None
    return DownloadB2bTaxInvoicesSheetBody(filter, fields, test)
