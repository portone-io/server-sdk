from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...payment.billing_key.billing_key_payment_method import BillingKeyPaymentMethod, _deserialize_billing_key_payment_method, _serialize_billing_key_payment_method
from ...common.channel_group_summary import ChannelGroupSummary, _deserialize_channel_group_summary, _serialize_channel_group_summary
from ...common.customer import Customer, _deserialize_customer, _serialize_customer
from ...payment.billing_key.pg_billing_key_issue_response import PgBillingKeyIssueResponse, _deserialize_pg_billing_key_issue_response, _serialize_pg_billing_key_issue_response
from ...common.selected_channel import SelectedChannel, _deserialize_selected_channel, _serialize_selected_channel

@dataclass
class DeletedBillingKeyInfo:
    """빌링키 삭제 완료 상태 건
    """
    """빌링키 상태
    """
    billing_key: str
    """빌링키
    """
    merchant_id: str
    """고객사 아이디
    """
    store_id: str
    """상점 아이디
    """
    channels: list[SelectedChannel]
    """빌링키 발급 시 사용된 채널

    추후 슈퍼빌링키 기능 제공 시 여러 채널 정보가 담길 수 있습니다.
    """
    customer: Customer
    """고객 정보
    """
    issued_at: str
    """발급 시점
    (RFC 3339 date-time)
    """
    deleted_at: str
    """발급 삭제 시점
    (RFC 3339 date-time)
    """
    methods: Optional[list[BillingKeyPaymentMethod]] = field(default=None)
    """빌링키 결제수단 상세 정보

    추후 슈퍼빌링키 기능 제공 시 여러 결제수단 정보가 담길 수 있습니다.
    """
    custom_data: Optional[str] = field(default=None)
    """사용자 지정 데이터
    """
    issue_id: Optional[str] = field(default=None)
    """고객사가 채번하는 빌링키 발급 건 고유 아이디
    """
    issue_name: Optional[str] = field(default=None)
    """빌링키 발급 건 이름
    """
    requested_at: Optional[str] = field(default=None)
    """발급 요청 시점
    (RFC 3339 date-time)
    """
    channel_group: Optional[ChannelGroupSummary] = field(default=None)
    """채널 그룹
    """
    pg_billing_key_issue_responses: Optional[list[PgBillingKeyIssueResponse]] = field(default=None)
    """채널 별 빌링키 발급 응답

    슈퍼빌링키의 경우, 빌링키 발급이 성공하더라도 일부 채널에 대한 발급은 실패할 수 있습니다.
    """


def _serialize_deleted_billing_key_info(obj: DeletedBillingKeyInfo) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["status"] = "DELETED"
    entity["billingKey"] = obj.billing_key
    entity["merchantId"] = obj.merchant_id
    entity["storeId"] = obj.store_id
    entity["channels"] = list(map(_serialize_selected_channel, obj.channels))
    entity["customer"] = _serialize_customer(obj.customer)
    entity["issuedAt"] = obj.issued_at
    entity["deletedAt"] = obj.deleted_at
    if obj.methods is not None:
        entity["methods"] = list(map(_serialize_billing_key_payment_method, obj.methods))
    if obj.custom_data is not None:
        entity["customData"] = obj.custom_data
    if obj.issue_id is not None:
        entity["issueId"] = obj.issue_id
    if obj.issue_name is not None:
        entity["issueName"] = obj.issue_name
    if obj.requested_at is not None:
        entity["requestedAt"] = obj.requested_at
    if obj.channel_group is not None:
        entity["channelGroup"] = _serialize_channel_group_summary(obj.channel_group)
    if obj.pg_billing_key_issue_responses is not None:
        entity["pgBillingKeyIssueResponses"] = list(map(_serialize_pg_billing_key_issue_response, obj.pg_billing_key_issue_responses))
    return entity


def _deserialize_deleted_billing_key_info(obj: Any) -> DeletedBillingKeyInfo:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "status" not in obj:
        raise KeyError(f"'status' is not in {obj}")
    status = obj["status"]
    if status != "DELETED":
        raise ValueError(f"{repr(status)} is not 'DELETED'")
    if "billingKey" not in obj:
        raise KeyError(f"'billingKey' is not in {obj}")
    billing_key = obj["billingKey"]
    if not isinstance(billing_key, str):
        raise ValueError(f"{repr(billing_key)} is not str")
    if "merchantId" not in obj:
        raise KeyError(f"'merchantId' is not in {obj}")
    merchant_id = obj["merchantId"]
    if not isinstance(merchant_id, str):
        raise ValueError(f"{repr(merchant_id)} is not str")
    if "storeId" not in obj:
        raise KeyError(f"'storeId' is not in {obj}")
    store_id = obj["storeId"]
    if not isinstance(store_id, str):
        raise ValueError(f"{repr(store_id)} is not str")
    if "channels" not in obj:
        raise KeyError(f"'channels' is not in {obj}")
    channels = obj["channels"]
    if not isinstance(channels, list):
        raise ValueError(f"{repr(channels)} is not list")
    for i, item in enumerate(channels):
        item = _deserialize_selected_channel(item)
        channels[i] = item
    if "customer" not in obj:
        raise KeyError(f"'customer' is not in {obj}")
    customer = obj["customer"]
    customer = _deserialize_customer(customer)
    if "issuedAt" not in obj:
        raise KeyError(f"'issuedAt' is not in {obj}")
    issued_at = obj["issuedAt"]
    if not isinstance(issued_at, str):
        raise ValueError(f"{repr(issued_at)} is not str")
    if "deletedAt" not in obj:
        raise KeyError(f"'deletedAt' is not in {obj}")
    deleted_at = obj["deletedAt"]
    if not isinstance(deleted_at, str):
        raise ValueError(f"{repr(deleted_at)} is not str")
    if "methods" in obj:
        methods = obj["methods"]
        if not isinstance(methods, list):
            raise ValueError(f"{repr(methods)} is not list")
        for i, item in enumerate(methods):
            item = _deserialize_billing_key_payment_method(item)
            methods[i] = item
    else:
        methods = None
    if "customData" in obj:
        custom_data = obj["customData"]
        if not isinstance(custom_data, str):
            raise ValueError(f"{repr(custom_data)} is not str")
    else:
        custom_data = None
    if "issueId" in obj:
        issue_id = obj["issueId"]
        if not isinstance(issue_id, str):
            raise ValueError(f"{repr(issue_id)} is not str")
    else:
        issue_id = None
    if "issueName" in obj:
        issue_name = obj["issueName"]
        if not isinstance(issue_name, str):
            raise ValueError(f"{repr(issue_name)} is not str")
    else:
        issue_name = None
    if "requestedAt" in obj:
        requested_at = obj["requestedAt"]
        if not isinstance(requested_at, str):
            raise ValueError(f"{repr(requested_at)} is not str")
    else:
        requested_at = None
    if "channelGroup" in obj:
        channel_group = obj["channelGroup"]
        channel_group = _deserialize_channel_group_summary(channel_group)
    else:
        channel_group = None
    if "pgBillingKeyIssueResponses" in obj:
        pg_billing_key_issue_responses = obj["pgBillingKeyIssueResponses"]
        if not isinstance(pg_billing_key_issue_responses, list):
            raise ValueError(f"{repr(pg_billing_key_issue_responses)} is not list")
        for i, item in enumerate(pg_billing_key_issue_responses):
            item = _deserialize_pg_billing_key_issue_response(item)
            pg_billing_key_issue_responses[i] = item
    else:
        pg_billing_key_issue_responses = None
    return DeletedBillingKeyInfo(billing_key, merchant_id, store_id, channels, customer, issued_at, deleted_at, methods, custom_data, issue_id, issue_name, requested_at, channel_group, pg_billing_key_issue_responses)
