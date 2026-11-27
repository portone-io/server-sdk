from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...b2b.tax_invoice.b2b_bulk_tax_invoice_source_type import B2bBulkTaxInvoiceSourceType, _deserialize_b2b_bulk_tax_invoice_source_type, _serialize_b2b_bulk_tax_invoice_source_type
from ...b2b.tax_invoice.b2b_bulk_tax_invoice_status import B2bBulkTaxInvoiceStatus, _deserialize_b2b_bulk_tax_invoice_status, _serialize_b2b_bulk_tax_invoice_status
from ...b2b.tax_invoice.b2b_tax_invoice_issuance_type import B2bTaxInvoiceIssuanceType, _deserialize_b2b_tax_invoice_issuance_type, _serialize_b2b_tax_invoice_issuance_type
from ...b2b.tax_invoice.map_stat import Map_Stat, _deserialize_map_stat, _serialize_map_stat

@dataclass
class B2bBulkTaxInvoice:
    id: str
    """일괄 세금계산서 고유 아이디
    """
    graphql_id: str
    status: B2bBulkTaxInvoiceStatus
    total_invoice_count: int
    """(int32)
    """
    total_amount: int
    """(int64)
    """
    stats: Map_Stat
    created_at: str
    """(RFC 3339 date-time)
    """
    status_updated_at: str
    """(RFC 3339 date-time)
    """
    source_type: B2bBulkTaxInvoiceSourceType
    issuance_type: B2bTaxInvoiceIssuanceType
    name: Optional[str] = field(default=None)
    scheduled_at: Optional[str] = field(default=None)
    """(RFC 3339 date-time)
    """
    requested_at: Optional[str] = field(default=None)
    """(RFC 3339 date-time)
    """


def _serialize_b2b_bulk_tax_invoice(obj: B2bBulkTaxInvoice) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["id"] = obj.id
    entity["graphqlId"] = obj.graphql_id
    entity["status"] = _serialize_b2b_bulk_tax_invoice_status(obj.status)
    entity["totalInvoiceCount"] = obj.total_invoice_count
    entity["totalAmount"] = obj.total_amount
    entity["stats"] = _serialize_map_stat(obj.stats)
    entity["createdAt"] = obj.created_at
    entity["statusUpdatedAt"] = obj.status_updated_at
    entity["sourceType"] = _serialize_b2b_bulk_tax_invoice_source_type(obj.source_type)
    entity["issuanceType"] = _serialize_b2b_tax_invoice_issuance_type(obj.issuance_type)
    if obj.name is not None:
        entity["name"] = obj.name
    if obj.scheduled_at is not None:
        entity["scheduledAt"] = obj.scheduled_at
    if obj.requested_at is not None:
        entity["requestedAt"] = obj.requested_at
    return entity


def _deserialize_b2b_bulk_tax_invoice(obj: Any) -> B2bBulkTaxInvoice:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "id" not in obj:
        raise KeyError("Missing required field 'id'")
    id = obj["id"]
    if not isinstance(id, str):
        raise ValueError("Expected str for id")
    if "graphqlId" not in obj:
        raise KeyError("Missing required field 'graphqlId'")
    graphql_id = obj["graphqlId"]
    if not isinstance(graphql_id, str):
        raise ValueError("Expected str for graphql_id")
    if "status" not in obj:
        raise KeyError("Missing required field 'status'")
    status = obj["status"]
    status = _deserialize_b2b_bulk_tax_invoice_status(status)
    if "totalInvoiceCount" not in obj:
        raise KeyError("Missing required field 'totalInvoiceCount'")
    total_invoice_count = obj["totalInvoiceCount"]
    if not isinstance(total_invoice_count, int):
        raise ValueError("Expected int for total_invoice_count")
    if "totalAmount" not in obj:
        raise KeyError("Missing required field 'totalAmount'")
    total_amount = obj["totalAmount"]
    if not isinstance(total_amount, int):
        raise ValueError("Expected int for total_amount")
    if "stats" not in obj:
        raise KeyError("Missing required field 'stats'")
    stats = obj["stats"]
    stats = _deserialize_map_stat(stats)
    if "createdAt" not in obj:
        raise KeyError("Missing required field 'createdAt'")
    created_at = obj["createdAt"]
    if not isinstance(created_at, str):
        raise ValueError("Expected str for created_at")
    if "statusUpdatedAt" not in obj:
        raise KeyError("Missing required field 'statusUpdatedAt'")
    status_updated_at = obj["statusUpdatedAt"]
    if not isinstance(status_updated_at, str):
        raise ValueError("Expected str for status_updated_at")
    if "sourceType" not in obj:
        raise KeyError("Missing required field 'sourceType'")
    source_type = obj["sourceType"]
    source_type = _deserialize_b2b_bulk_tax_invoice_source_type(source_type)
    if "issuanceType" not in obj:
        raise KeyError("Missing required field 'issuanceType'")
    issuance_type = obj["issuanceType"]
    issuance_type = _deserialize_b2b_tax_invoice_issuance_type(issuance_type)
    if "name" in obj:
        name = obj["name"]
        if not isinstance(name, str):
            raise ValueError("Expected str for name")
    else:
        name = None
    if "scheduledAt" in obj:
        scheduled_at = obj["scheduledAt"]
        if not isinstance(scheduled_at, str):
            raise ValueError("Expected str for scheduled_at")
    else:
        scheduled_at = None
    if "requestedAt" in obj:
        requested_at = obj["requestedAt"]
        if not isinstance(requested_at, str):
            raise ValueError("Expected str for requested_at")
    else:
        requested_at = None
    return B2bBulkTaxInvoice(id, graphql_id, status, total_invoice_count, total_amount, stats, created_at, status_updated_at, source_type, issuance_type, name, scheduled_at, requested_at)
