from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...platform.transfer.platform_transfer_filter_input import PlatformTransferFilterInput, _deserialize_platform_transfer_filter_input, _serialize_platform_transfer_filter_input
from ...platform.transfer.platform_transfer_sheet_field import PlatformTransferSheetField, _deserialize_platform_transfer_sheet_field, _serialize_platform_transfer_sheet_field

@dataclass
class DownloadPlatformTransferSheetBody:
    filter: Optional[PlatformTransferFilterInput] = field(default=None)
    fields: Optional[list[PlatformTransferSheetField]] = field(default=None)
    """다운로드 할 시트 컬럼
    """
    transfer_user_defined_property_keys: Optional[list[str]] = field(default=None)
    partner_user_defined_property_keys: Optional[list[str]] = field(default=None)


def _serialize_download_platform_transfer_sheet_body(obj: DownloadPlatformTransferSheetBody) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    if obj.filter is not None:
        entity["filter"] = _serialize_platform_transfer_filter_input(obj.filter)
    if obj.fields is not None:
        entity["fields"] = list(map(_serialize_platform_transfer_sheet_field, obj.fields))
    if obj.transfer_user_defined_property_keys is not None:
        entity["transferUserDefinedPropertyKeys"] = obj.transfer_user_defined_property_keys
    if obj.partner_user_defined_property_keys is not None:
        entity["partnerUserDefinedPropertyKeys"] = obj.partner_user_defined_property_keys
    return entity


def _deserialize_download_platform_transfer_sheet_body(obj: Any) -> DownloadPlatformTransferSheetBody:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "filter" in obj:
        filter = obj["filter"]
        filter = _deserialize_platform_transfer_filter_input(filter)
    else:
        filter = None
    if "fields" in obj:
        fields = obj["fields"]
        if not isinstance(fields, list):
            raise ValueError(f"{repr(fields)} is not list")
        for i, item in enumerate(fields):
            item = _deserialize_platform_transfer_sheet_field(item)
            fields[i] = item
    else:
        fields = None
    if "transferUserDefinedPropertyKeys" in obj:
        transfer_user_defined_property_keys = obj["transferUserDefinedPropertyKeys"]
        if not isinstance(transfer_user_defined_property_keys, list):
            raise ValueError(f"{repr(transfer_user_defined_property_keys)} is not list")
        for i, item in enumerate(transfer_user_defined_property_keys):
            if not isinstance(item, str):
                raise ValueError(f"{repr(item)} is not str")
    else:
        transfer_user_defined_property_keys = None
    if "partnerUserDefinedPropertyKeys" in obj:
        partner_user_defined_property_keys = obj["partnerUserDefinedPropertyKeys"]
        if not isinstance(partner_user_defined_property_keys, list):
            raise ValueError(f"{repr(partner_user_defined_property_keys)} is not list")
        for i, item in enumerate(partner_user_defined_property_keys):
            if not isinstance(item, str):
                raise ValueError(f"{repr(item)} is not str")
    else:
        partner_user_defined_property_keys = None
    return DownloadPlatformTransferSheetBody(filter, fields, transfer_user_defined_property_keys, partner_user_defined_property_keys)
