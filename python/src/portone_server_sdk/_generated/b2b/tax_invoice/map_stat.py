from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from ...b2b.tax_invoice.b2b_bulk_tax_invoice_stat import B2bBulkTaxInvoiceStat, _deserialize_b2b_bulk_tax_invoice_stat, _serialize_b2b_bulk_tax_invoice_stat

@dataclass
class Map_Stat:
    additional_properties: dict[str, B2bBulkTaxInvoiceStat]
    """추가 데이터
    """


def _serialize_map_stat(obj: Map_Stat) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    for key, value in obj.additional_properties.items():
        entity[key] = _serialize_b2b_bulk_tax_invoice_stat(value)
    return entity


def _deserialize_map_stat(obj: Any) -> Map_Stat:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    additional_properties = {}
    for key, value in obj.items():
        if key in []:
            continue
        additional_properties[key] = _deserialize_b2b_bulk_tax_invoice_stat(value)
    return Map_Stat(additional_properties)
