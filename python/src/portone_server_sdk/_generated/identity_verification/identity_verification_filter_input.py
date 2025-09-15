from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ..identity_verification.carrier import Carrier, _deserialize_carrier, _serialize_carrier
from ..identity_verification.identity_verification_filter_customer_input import IdentityVerificationFilterCustomerInput, _deserialize_identity_verification_filter_customer_input, _serialize_identity_verification_filter_customer_input
from ..identity_verification.identity_verification_status import IdentityVerificationStatus, _deserialize_identity_verification_status, _serialize_identity_verification_status
from ..identity_verification.identity_verification_time_range_field import IdentityVerificationTimeRangeField, _deserialize_identity_verification_time_range_field, _serialize_identity_verification_time_range_field
from ..common.pg_company import PgCompany, _deserialize_pg_company, _serialize_pg_company
from ..common.pg_provider import PgProvider, _deserialize_pg_provider, _serialize_pg_provider
from ..common.port_one_version import PortOneVersion, _deserialize_port_one_version, _serialize_port_one_version

@dataclass
class IdentityVerificationFilterInput:
    """본인인증 다건 조회를 위한 입력 정보
    """
    store_id: Optional[str] = field(default=None)
    """상점 아이디

    Merchant 사용자만 사용가능하며, 지정되지 않은 경우 고객사 전체 본인인증 내역을 조회합니다.
    """
    time_range_field: Optional[IdentityVerificationTimeRangeField] = field(default=None)
    """조회 기준 시점 유형

    값을 입력하지 않으면 REQUESTED_AT으로 설정됩니다.
    """
    from_: Optional[str] = field(default=None)
    """조회 기준 시점 범위의 시작

    값을 입력하지 않으면 end의 90일 전으로 설정됩니다.
    (RFC 3339 date-time)
    """
    until: Optional[str] = field(default=None)
    """조회 기준 시점 범위의 끝

    값을 입력하지 않으면 현재 시점으로 설정됩니다.
    (RFC 3339 date-time)
    """
    identity_verification_id: Optional[str] = field(default=None)
    """고객사 본인인증 번호

    V1 본인인증 건의 경우 `imp_uid`에 대응됩니다.
    """
    identity_verification_tx_id: Optional[str] = field(default=None)
    """포트원 본인인증 시도 번호

    V1 본인인증 건의 경우 `imp_uid`에 대응됩니다.
    """
    is_test: Optional[bool] = field(default=None)
    """테스트 결제 필터링
    """
    statuses: Optional[list[IdentityVerificationStatus]] = field(default=None)
    """본인인증 상태 리스트

    값을 입력하지 않으면 필터링이 적용되지 않습니다.
    """
    pg_tx_id: Optional[str] = field(default=None)
    """PG사 본인인증 번호
    """
    pg_merchant_id: Optional[str] = field(default=None)
    """PG 상점아이디
    """
    pg_providers: Optional[list[PgProvider]] = field(default=None)
    """PG사 결제 모듈 리스트

    값을 입력하지 않으면 PG사 결제 모듈 필터링이 적용되지 않습니다.
    """
    pg_companies: Optional[list[PgCompany]] = field(default=None)
    """PG사 리스트

    값을 입력하지 않으면 PG사 필터링이 적용되지 않습니다.
    """
    carriers: Optional[list[Carrier]] = field(default=None)
    """통신사 리스트
    """
    version: Optional[PortOneVersion] = field(default=None)
    """포트원 버전
    """
    customer: Optional[IdentityVerificationFilterCustomerInput] = field(default=None)
    """고객 정보

    인증이 완료되지 않은 본인인증 내역의 경우 요청 시 고객 정보로, 인증이 완료된 본인인증 내역의 경우 인증된 고객 정보로 필터링합니다.
    """


def _serialize_identity_verification_filter_input(obj: IdentityVerificationFilterInput) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    if obj.store_id is not None:
        entity["storeId"] = obj.store_id
    if obj.time_range_field is not None:
        entity["timeRangeField"] = _serialize_identity_verification_time_range_field(obj.time_range_field)
    if obj.from_ is not None:
        entity["from"] = obj.from_
    if obj.until is not None:
        entity["until"] = obj.until
    if obj.identity_verification_id is not None:
        entity["identityVerificationId"] = obj.identity_verification_id
    if obj.identity_verification_tx_id is not None:
        entity["identityVerificationTxId"] = obj.identity_verification_tx_id
    if obj.is_test is not None:
        entity["isTest"] = obj.is_test
    if obj.statuses is not None:
        entity["statuses"] = list(map(_serialize_identity_verification_status, obj.statuses))
    if obj.pg_tx_id is not None:
        entity["pgTxId"] = obj.pg_tx_id
    if obj.pg_merchant_id is not None:
        entity["pgMerchantId"] = obj.pg_merchant_id
    if obj.pg_providers is not None:
        entity["pgProviders"] = list(map(_serialize_pg_provider, obj.pg_providers))
    if obj.pg_companies is not None:
        entity["pgCompanies"] = list(map(_serialize_pg_company, obj.pg_companies))
    if obj.carriers is not None:
        entity["carriers"] = list(map(_serialize_carrier, obj.carriers))
    if obj.version is not None:
        entity["version"] = _serialize_port_one_version(obj.version)
    if obj.customer is not None:
        entity["customer"] = _serialize_identity_verification_filter_customer_input(obj.customer)
    return entity


def _deserialize_identity_verification_filter_input(obj: Any) -> IdentityVerificationFilterInput:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "storeId" in obj:
        store_id = obj["storeId"]
        if not isinstance(store_id, str):
            raise ValueError(f"{repr(store_id)} is not str")
    else:
        store_id = None
    if "timeRangeField" in obj:
        time_range_field = obj["timeRangeField"]
        time_range_field = _deserialize_identity_verification_time_range_field(time_range_field)
    else:
        time_range_field = None
    if "from" in obj:
        from_ = obj["from"]
        if not isinstance(from_, str):
            raise ValueError(f"{repr(from_)} is not str")
    else:
        from_ = None
    if "until" in obj:
        until = obj["until"]
        if not isinstance(until, str):
            raise ValueError(f"{repr(until)} is not str")
    else:
        until = None
    if "identityVerificationId" in obj:
        identity_verification_id = obj["identityVerificationId"]
        if not isinstance(identity_verification_id, str):
            raise ValueError(f"{repr(identity_verification_id)} is not str")
    else:
        identity_verification_id = None
    if "identityVerificationTxId" in obj:
        identity_verification_tx_id = obj["identityVerificationTxId"]
        if not isinstance(identity_verification_tx_id, str):
            raise ValueError(f"{repr(identity_verification_tx_id)} is not str")
    else:
        identity_verification_tx_id = None
    if "isTest" in obj:
        is_test = obj["isTest"]
        if not isinstance(is_test, bool):
            raise ValueError(f"{repr(is_test)} is not bool")
    else:
        is_test = None
    if "statuses" in obj:
        statuses = obj["statuses"]
        if not isinstance(statuses, list):
            raise ValueError(f"{repr(statuses)} is not list")
        for i, item in enumerate(statuses):
            item = _deserialize_identity_verification_status(item)
            statuses[i] = item
    else:
        statuses = None
    if "pgTxId" in obj:
        pg_tx_id = obj["pgTxId"]
        if not isinstance(pg_tx_id, str):
            raise ValueError(f"{repr(pg_tx_id)} is not str")
    else:
        pg_tx_id = None
    if "pgMerchantId" in obj:
        pg_merchant_id = obj["pgMerchantId"]
        if not isinstance(pg_merchant_id, str):
            raise ValueError(f"{repr(pg_merchant_id)} is not str")
    else:
        pg_merchant_id = None
    if "pgProviders" in obj:
        pg_providers = obj["pgProviders"]
        if not isinstance(pg_providers, list):
            raise ValueError(f"{repr(pg_providers)} is not list")
        for i, item in enumerate(pg_providers):
            item = _deserialize_pg_provider(item)
            pg_providers[i] = item
    else:
        pg_providers = None
    if "pgCompanies" in obj:
        pg_companies = obj["pgCompanies"]
        if not isinstance(pg_companies, list):
            raise ValueError(f"{repr(pg_companies)} is not list")
        for i, item in enumerate(pg_companies):
            item = _deserialize_pg_company(item)
            pg_companies[i] = item
    else:
        pg_companies = None
    if "carriers" in obj:
        carriers = obj["carriers"]
        if not isinstance(carriers, list):
            raise ValueError(f"{repr(carriers)} is not list")
        for i, item in enumerate(carriers):
            item = _deserialize_carrier(item)
            carriers[i] = item
    else:
        carriers = None
    if "version" in obj:
        version = obj["version"]
        version = _deserialize_port_one_version(version)
    else:
        version = None
    if "customer" in obj:
        customer = obj["customer"]
        customer = _deserialize_identity_verification_filter_customer_input(customer)
    else:
        customer = None
    return IdentityVerificationFilterInput(store_id, time_range_field, from_, until, identity_verification_id, identity_verification_tx_id, is_test, statuses, pg_tx_id, pg_merchant_id, pg_providers, pg_companies, carriers, version, customer)
