from __future__ import annotations
import httpx
import json
from httpx import AsyncClient
from ..._user_agent import USER_AGENT
from typing import Optional
from ..errors import ForbiddenError, InvalidRequestError, PlatformAccountVerificationAlreadyUsedError, PlatformAccountVerificationFailedError, PlatformAccountVerificationNotFoundError, PlatformAdditionalFeePolicyNotFoundError, PlatformAdditionalFeePolicyScheduleAlreadyExistsError, PlatformArchivedAdditionalFeePolicyError, PlatformArchivedContractError, PlatformArchivedDiscountSharePolicyError, PlatformArchivedPartnerError, PlatformArchivedPartnersCannotBeScheduledError, PlatformCompanyVerificationAlreadyUsedError, PlatformContractNotFoundError, PlatformContractScheduleAlreadyExistsError, PlatformDiscountSharePolicyNotFoundError, PlatformDiscountSharePolicyScheduleAlreadyExistsError, PlatformInsufficientDataToChangePartnerTypeError, PlatformInvalidSettlementFormulaError, PlatformMemberCompanyConnectedPartnerBrnUnchangeableError, PlatformMemberCompanyConnectedPartnerCannotBeScheduledError, PlatformMemberCompanyConnectedPartnerTypeUnchangeableError, PlatformMemberCompanyConnectedPartnersCannotBeScheduledError, PlatformNotEnabledError, PlatformPartnerNotFoundError, PlatformPartnerScheduleAlreadyExistsError, PlatformPartnerSchedulesAlreadyExistError, PlatformUserDefinedPropertyNotFoundError, UnauthorizedError, UnknownError
from ..common.forbidden_error import _deserialize_forbidden_error
from ..common.invalid_request_error import _deserialize_invalid_request_error
from ..platform.platform_account_verification_already_used_error import _deserialize_platform_account_verification_already_used_error
from ..platform.platform_account_verification_failed_error import _deserialize_platform_account_verification_failed_error
from ..platform.platform_account_verification_not_found_error import _deserialize_platform_account_verification_not_found_error
from ..platform.platform_additional_fee_policy_not_found_error import _deserialize_platform_additional_fee_policy_not_found_error
from ..platform.platform_additional_fee_policy_schedule_already_exists_error import _deserialize_platform_additional_fee_policy_schedule_already_exists_error
from ..platform.platform_archived_additional_fee_policy_error import _deserialize_platform_archived_additional_fee_policy_error
from ..platform.platform_archived_contract_error import _deserialize_platform_archived_contract_error
from ..platform.platform_archived_discount_share_policy_error import _deserialize_platform_archived_discount_share_policy_error
from ..platform.platform_archived_partner_error import _deserialize_platform_archived_partner_error
from ..platform.platform_archived_partners_cannot_be_scheduled_error import _deserialize_platform_archived_partners_cannot_be_scheduled_error
from ..platform.platform_company_verification_already_used_error import _deserialize_platform_company_verification_already_used_error
from ..platform.platform_contract_not_found_error import _deserialize_platform_contract_not_found_error
from ..platform.platform_contract_schedule_already_exists_error import _deserialize_platform_contract_schedule_already_exists_error
from ..platform.platform_discount_share_policy_not_found_error import _deserialize_platform_discount_share_policy_not_found_error
from ..platform.platform_discount_share_policy_schedule_already_exists_error import _deserialize_platform_discount_share_policy_schedule_already_exists_error
from ..platform.platform_insufficient_data_to_change_partner_type_error import _deserialize_platform_insufficient_data_to_change_partner_type_error
from ..platform.platform_invalid_settlement_formula_error import _deserialize_platform_invalid_settlement_formula_error
from ..platform.platform_member_company_connected_partner_brn_unchangeable_error import _deserialize_platform_member_company_connected_partner_brn_unchangeable_error
from ..platform.platform_member_company_connected_partner_cannot_be_scheduled_error import _deserialize_platform_member_company_connected_partner_cannot_be_scheduled_error
from ..platform.platform_member_company_connected_partner_type_unchangeable_error import _deserialize_platform_member_company_connected_partner_type_unchangeable_error
from ..platform.platform_member_company_connected_partners_cannot_be_scheduled_error import _deserialize_platform_member_company_connected_partners_cannot_be_scheduled_error
from ..platform.platform_not_enabled_error import _deserialize_platform_not_enabled_error
from ..platform.platform_partner_not_found_error import _deserialize_platform_partner_not_found_error
from ..platform.platform_partner_schedule_already_exists_error import _deserialize_platform_partner_schedule_already_exists_error
from ..platform.platform_partner_schedules_already_exist_error import _deserialize_platform_partner_schedules_already_exist_error
from ..platform.platform_user_defined_property_not_found_error import _deserialize_platform_user_defined_property_not_found_error
from ..common.unauthorized_error import _deserialize_unauthorized_error
from ..platform.cancel_platform_additional_fee_policy_schedule_response import CancelPlatformAdditionalFeePolicyScheduleResponse, _deserialize_cancel_platform_additional_fee_policy_schedule_response, _serialize_cancel_platform_additional_fee_policy_schedule_response
from ..platform.cancel_platform_contract_schedule_response import CancelPlatformContractScheduleResponse, _deserialize_cancel_platform_contract_schedule_response, _serialize_cancel_platform_contract_schedule_response
from ..platform.cancel_platform_discount_share_policy_schedule_response import CancelPlatformDiscountSharePolicyScheduleResponse, _deserialize_cancel_platform_discount_share_policy_schedule_response, _serialize_cancel_platform_discount_share_policy_schedule_response
from ..platform.cancel_platform_partner_schedule_response import CancelPlatformPartnerScheduleResponse, _deserialize_cancel_platform_partner_schedule_response, _serialize_cancel_platform_partner_schedule_response
from ..platform.platform import Platform, _deserialize_platform, _serialize_platform
from ..platform.platform_additional_fee_policy import PlatformAdditionalFeePolicy, _deserialize_platform_additional_fee_policy, _serialize_platform_additional_fee_policy
from ..platform.platform_contract import PlatformContract, _deserialize_platform_contract, _serialize_platform_contract
from ..platform.platform_discount_share_policy import PlatformDiscountSharePolicy, _deserialize_platform_discount_share_policy, _serialize_platform_discount_share_policy
from ..platform.platform_discount_share_policy_filter_options import PlatformDiscountSharePolicyFilterOptions, _deserialize_platform_discount_share_policy_filter_options, _serialize_platform_discount_share_policy_filter_options
from ..platform.platform_partner import PlatformPartner, _deserialize_platform_partner, _serialize_platform_partner
from ..platform.platform_partner_filter_input import PlatformPartnerFilterInput, _deserialize_platform_partner_filter_input, _serialize_platform_partner_filter_input
from ..platform.platform_partner_filter_options import PlatformPartnerFilterOptions, _deserialize_platform_partner_filter_options, _serialize_platform_partner_filter_options
from ..platform.platform_round_type import PlatformRoundType, _deserialize_platform_round_type, _serialize_platform_round_type
from ..platform.platform_setting import PlatformSetting, _deserialize_platform_setting, _serialize_platform_setting
from ..platform.reschedule_platform_additional_fee_policy_response import ReschedulePlatformAdditionalFeePolicyResponse, _deserialize_reschedule_platform_additional_fee_policy_response, _serialize_reschedule_platform_additional_fee_policy_response
from ..platform.reschedule_platform_contract_response import ReschedulePlatformContractResponse, _deserialize_reschedule_platform_contract_response, _serialize_reschedule_platform_contract_response
from ..platform.reschedule_platform_discount_share_policy_response import ReschedulePlatformDiscountSharePolicyResponse, _deserialize_reschedule_platform_discount_share_policy_response, _serialize_reschedule_platform_discount_share_policy_response
from ..platform.reschedule_platform_partner_response import ReschedulePlatformPartnerResponse, _deserialize_reschedule_platform_partner_response, _serialize_reschedule_platform_partner_response
from ..platform.schedule_platform_additional_fee_policy_response import SchedulePlatformAdditionalFeePolicyResponse, _deserialize_schedule_platform_additional_fee_policy_response, _serialize_schedule_platform_additional_fee_policy_response
from ..platform.schedule_platform_contract_response import SchedulePlatformContractResponse, _deserialize_schedule_platform_contract_response, _serialize_schedule_platform_contract_response
from ..platform.schedule_platform_discount_share_policy_response import SchedulePlatformDiscountSharePolicyResponse, _deserialize_schedule_platform_discount_share_policy_response, _serialize_schedule_platform_discount_share_policy_response
from ..platform.schedule_platform_partner_response import SchedulePlatformPartnerResponse, _deserialize_schedule_platform_partner_response, _serialize_schedule_platform_partner_response
from ..platform.schedule_platform_partners_body_update import SchedulePlatformPartnersBodyUpdate, _deserialize_schedule_platform_partners_body_update, _serialize_schedule_platform_partners_body_update
from ..platform.schedule_platform_partners_response import SchedulePlatformPartnersResponse, _deserialize_schedule_platform_partners_response, _serialize_schedule_platform_partners_response
from ..platform.update_platform_additional_fee_policy_body import UpdatePlatformAdditionalFeePolicyBody, _deserialize_update_platform_additional_fee_policy_body, _serialize_update_platform_additional_fee_policy_body
from ..platform.update_platform_body_settlement_formula import UpdatePlatformBodySettlementFormula, _deserialize_update_platform_body_settlement_formula, _serialize_update_platform_body_settlement_formula
from ..platform.update_platform_body_settlement_rule import UpdatePlatformBodySettlementRule, _deserialize_update_platform_body_settlement_rule, _serialize_update_platform_body_settlement_rule
from ..platform.update_platform_contract_body import UpdatePlatformContractBody, _deserialize_update_platform_contract_body, _serialize_update_platform_contract_body
from ..platform.update_platform_discount_share_policy_body import UpdatePlatformDiscountSharePolicyBody, _deserialize_update_platform_discount_share_policy_body, _serialize_update_platform_discount_share_policy_body
from ..platform.update_platform_partner_body import UpdatePlatformPartnerBody, _deserialize_update_platform_partner_body, _serialize_update_platform_partner_body
from ..platform.update_platform_response import UpdatePlatformResponse, _deserialize_update_platform_response, _serialize_update_platform_response
from ..platform.update_platform_setting_response import UpdatePlatformSettingResponse, _deserialize_update_platform_setting_response, _serialize_update_platform_setting_response
from urllib.parse import quote
from .policy.client import PolicyClient
from .partner.client import PartnerClient
from .transfer.client import TransferClient
from .partner_settlement.client import PartnerSettlementClient
from .payout.client import PayoutClient
from .bulk_payout.client import BulkPayoutClient
from .account.client import AccountClient
from .company.client import CompanyClient
from .account_transfer.client import AccountTransferClient
class PlatformClient:
    _secret: str
    _base_url: str
    _store_id: Optional[str]
    _client: AsyncClient
    policy: PolicyClient
    partner: PartnerClient
    transfer: TransferClient
    partner_settlement: PartnerSettlementClient
    payout: PayoutClient
    bulk_payout: BulkPayoutClient
    account: AccountClient
    company: CompanyClient
    account_transfer: AccountTransferClient

    def __init__(self, *, secret: str, base_url: str = "https://api.portone.io", store_id: Optional[str] = None):
        """API Secret을 사용해 포트원 API 클라이언트를 생성합니다."""
        self._secret = secret
        self._base_url = base_url
        self._store_id = store_id
        self._client = AsyncClient()
        self.policy = PolicyClient(secret=secret, base_url=base_url, store_id=store_id)
        self.partner = PartnerClient(secret=secret, base_url=base_url, store_id=store_id)
        self.transfer = TransferClient(secret=secret, base_url=base_url, store_id=store_id)
        self.partner_settlement = PartnerSettlementClient(secret=secret, base_url=base_url, store_id=store_id)
        self.payout = PayoutClient(secret=secret, base_url=base_url, store_id=store_id)
        self.bulk_payout = BulkPayoutClient(secret=secret, base_url=base_url, store_id=store_id)
        self.account = AccountClient(secret=secret, base_url=base_url, store_id=store_id)
        self.company = CompanyClient(secret=secret, base_url=base_url, store_id=store_id)
        self.account_transfer = AccountTransferClient(secret=secret, base_url=base_url, store_id=store_id)
    def get_platform(
        self,
    ) -> Platform:
        """고객사의 플랫폼 정보를 조회합니다.
        요청된 Authorization header 를 통해 자동으로 요청자의 고객사를 특정합니다.

        Raises:
            GetPlatformError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        response = httpx.request(
            "GET",
            f"{self._base_url}/platform",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": USER_AGENT,
            },
        )
        if response.status_code != 200:
            error_response = response.json()
            error = None
            try:
                error = _deserialize_invalid_request_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise InvalidRequestError(error)
            try:
                error = _deserialize_platform_not_enabled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformNotEnabledError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_platform(response.json())
    async def get_platform_async(
        self,
    ) -> Platform:
        """고객사의 플랫폼 정보를 조회합니다.
        요청된 Authorization header 를 통해 자동으로 요청자의 고객사를 특정합니다.

        Raises:
            GetPlatformError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        response = await self._client.request(
            "GET",
            f"{self._base_url}/platform",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": USER_AGENT,
            },
        )
        if response.status_code != 200:
            error_response = response.json()
            error = None
            try:
                error = _deserialize_invalid_request_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise InvalidRequestError(error)
            try:
                error = _deserialize_platform_not_enabled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformNotEnabledError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_platform(response.json())
    def update_platform(
        self,
        *,
        round_type: Optional[PlatformRoundType] = None,
        settlement_formula: Optional[UpdatePlatformBodySettlementFormula] = None,
        settlement_rule: Optional[UpdatePlatformBodySettlementRule] = None,
    ) -> UpdatePlatformResponse:
        """고객사의 플랫폼 관련 정보를 업데이트합니다.
        요청된 Authorization header 를 통해 자동으로 요청자의 고객사를 특정합니다.

        Args:
            round_type (PlatformRoundType, optional):
                파트너 정산금액의 소수점 처리 방식
            settlement_formula (UpdatePlatformBodySettlementFormula, optional):
                수수료 및 할인 분담 정책 관련 계산식
            settlement_rule (UpdatePlatformBodySettlementRule, optional):
                정산 규칙


        Raises:
            UpdatePlatformError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        if round_type is not None:
            request_body["roundType"] = _serialize_platform_round_type(round_type)
        if settlement_formula is not None:
            request_body["settlementFormula"] = _serialize_update_platform_body_settlement_formula(settlement_formula)
        if settlement_rule is not None:
            request_body["settlementRule"] = _serialize_update_platform_body_settlement_rule(settlement_rule)
        query = []
        response = httpx.request(
            "PATCH",
            f"{self._base_url}/platform",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": USER_AGENT,
            },
            json=request_body,
        )
        if response.status_code != 200:
            error_response = response.json()
            error = None
            try:
                error = _deserialize_forbidden_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise ForbiddenError(error)
            try:
                error = _deserialize_invalid_request_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise InvalidRequestError(error)
            try:
                error = _deserialize_platform_invalid_settlement_formula_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformInvalidSettlementFormulaError(error)
            try:
                error = _deserialize_platform_not_enabled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformNotEnabledError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_update_platform_response(response.json())
    async def update_platform_async(
        self,
        *,
        round_type: Optional[PlatformRoundType] = None,
        settlement_formula: Optional[UpdatePlatformBodySettlementFormula] = None,
        settlement_rule: Optional[UpdatePlatformBodySettlementRule] = None,
    ) -> UpdatePlatformResponse:
        """고객사의 플랫폼 관련 정보를 업데이트합니다.
        요청된 Authorization header 를 통해 자동으로 요청자의 고객사를 특정합니다.

        Args:
            round_type (PlatformRoundType, optional):
                파트너 정산금액의 소수점 처리 방식
            settlement_formula (UpdatePlatformBodySettlementFormula, optional):
                수수료 및 할인 분담 정책 관련 계산식
            settlement_rule (UpdatePlatformBodySettlementRule, optional):
                정산 규칙


        Raises:
            UpdatePlatformError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        if round_type is not None:
            request_body["roundType"] = _serialize_platform_round_type(round_type)
        if settlement_formula is not None:
            request_body["settlementFormula"] = _serialize_update_platform_body_settlement_formula(settlement_formula)
        if settlement_rule is not None:
            request_body["settlementRule"] = _serialize_update_platform_body_settlement_rule(settlement_rule)
        query = []
        response = await self._client.request(
            "PATCH",
            f"{self._base_url}/platform",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": USER_AGENT,
            },
            json=request_body,
        )
        if response.status_code != 200:
            error_response = response.json()
            error = None
            try:
                error = _deserialize_forbidden_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise ForbiddenError(error)
            try:
                error = _deserialize_invalid_request_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise InvalidRequestError(error)
            try:
                error = _deserialize_platform_invalid_settlement_formula_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformInvalidSettlementFormulaError(error)
            try:
                error = _deserialize_platform_not_enabled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformNotEnabledError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_update_platform_response(response.json())
    def get_platform_discount_share_policy_filter_options(
        self,
        *,
        is_archived: Optional[bool] = None,
    ) -> PlatformDiscountSharePolicyFilterOptions:
        """할인 분담 정책 다건 조회 시 필요한 필터 옵션을 조회합니다.

        Args:
            is_archived (bool, optional):
                보관 조회 여부

                true 이면 보관된 할인 분담의 필터 옵션을 조회하고, false 이면 보관되지 않은 할인 분담의 필터 옵션을 조회합니다. 기본값은 false 입니다.


        Raises:
            GetPlatformDiscountSharePolicyFilterOptionsError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        if is_archived is not None:
            query.append(("isArchived", is_archived))
        response = httpx.request(
            "GET",
            f"{self._base_url}/platform/discount-share-policy-filter-options",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": USER_AGENT,
            },
        )
        if response.status_code != 200:
            error_response = response.json()
            error = None
            try:
                error = _deserialize_forbidden_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise ForbiddenError(error)
            try:
                error = _deserialize_invalid_request_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise InvalidRequestError(error)
            try:
                error = _deserialize_platform_not_enabled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformNotEnabledError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_platform_discount_share_policy_filter_options(response.json())
    async def get_platform_discount_share_policy_filter_options_async(
        self,
        *,
        is_archived: Optional[bool] = None,
    ) -> PlatformDiscountSharePolicyFilterOptions:
        """할인 분담 정책 다건 조회 시 필요한 필터 옵션을 조회합니다.

        Args:
            is_archived (bool, optional):
                보관 조회 여부

                true 이면 보관된 할인 분담의 필터 옵션을 조회하고, false 이면 보관되지 않은 할인 분담의 필터 옵션을 조회합니다. 기본값은 false 입니다.


        Raises:
            GetPlatformDiscountSharePolicyFilterOptionsError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        if is_archived is not None:
            query.append(("isArchived", is_archived))
        response = await self._client.request(
            "GET",
            f"{self._base_url}/platform/discount-share-policy-filter-options",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": USER_AGENT,
            },
        )
        if response.status_code != 200:
            error_response = response.json()
            error = None
            try:
                error = _deserialize_forbidden_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise ForbiddenError(error)
            try:
                error = _deserialize_invalid_request_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise InvalidRequestError(error)
            try:
                error = _deserialize_platform_not_enabled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformNotEnabledError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_platform_discount_share_policy_filter_options(response.json())
    def get_platform_discount_share_policy_schedule(
        self,
        *,
        id: str,
    ) -> PlatformDiscountSharePolicy:
        """주어진 아이디에 대응되는 할인 분담의 예약 업데이트를 조회합니다.

        Args:
            id (str):
                할인 분담 정책 아이디


        Raises:
            GetPlatformDiscountSharePolicyScheduleError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        response = httpx.request(
            "GET",
            f"{self._base_url}/platform/discount-share-policies/{quote(id, safe='')}/schedule",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": USER_AGENT,
            },
        )
        if response.status_code != 200:
            error_response = response.json()
            error = None
            try:
                error = _deserialize_forbidden_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise ForbiddenError(error)
            try:
                error = _deserialize_invalid_request_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise InvalidRequestError(error)
            try:
                error = _deserialize_platform_discount_share_policy_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformDiscountSharePolicyNotFoundError(error)
            try:
                error = _deserialize_platform_not_enabled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformNotEnabledError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_platform_discount_share_policy(response.json())
    async def get_platform_discount_share_policy_schedule_async(
        self,
        *,
        id: str,
    ) -> PlatformDiscountSharePolicy:
        """주어진 아이디에 대응되는 할인 분담의 예약 업데이트를 조회합니다.

        Args:
            id (str):
                할인 분담 정책 아이디


        Raises:
            GetPlatformDiscountSharePolicyScheduleError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        response = await self._client.request(
            "GET",
            f"{self._base_url}/platform/discount-share-policies/{quote(id, safe='')}/schedule",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": USER_AGENT,
            },
        )
        if response.status_code != 200:
            error_response = response.json()
            error = None
            try:
                error = _deserialize_forbidden_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise ForbiddenError(error)
            try:
                error = _deserialize_invalid_request_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise InvalidRequestError(error)
            try:
                error = _deserialize_platform_discount_share_policy_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformDiscountSharePolicyNotFoundError(error)
            try:
                error = _deserialize_platform_not_enabled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformNotEnabledError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_platform_discount_share_policy(response.json())
    def reschedule_discount_share_policy(
        self,
        *,
        id: str,
        update: UpdatePlatformDiscountSharePolicyBody,
        applied_at: str,
    ) -> ReschedulePlatformDiscountSharePolicyResponse:
        """주어진 아이디에 대응되는 할인 분담에 예약 업데이트를 재설정합니다.

        Args:
            id (str):
                할인 분담 정책 아이디
            update (UpdatePlatformDiscountSharePolicyBody):
                반영할 업데이트 내용
            applied_at (str):
                업데이트 적용 시점


        Raises:
            RescheduleDiscountSharePolicyError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        request_body["update"] = _serialize_update_platform_discount_share_policy_body(update)
        request_body["appliedAt"] = applied_at
        query = []
        response = httpx.request(
            "PUT",
            f"{self._base_url}/platform/discount-share-policies/{quote(id, safe='')}/schedule",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": USER_AGENT,
            },
            json=request_body,
        )
        if response.status_code != 200:
            error_response = response.json()
            error = None
            try:
                error = _deserialize_forbidden_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise ForbiddenError(error)
            try:
                error = _deserialize_invalid_request_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise InvalidRequestError(error)
            try:
                error = _deserialize_platform_discount_share_policy_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformDiscountSharePolicyNotFoundError(error)
            try:
                error = _deserialize_platform_not_enabled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformNotEnabledError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_reschedule_platform_discount_share_policy_response(response.json())
    async def reschedule_discount_share_policy_async(
        self,
        *,
        id: str,
        update: UpdatePlatformDiscountSharePolicyBody,
        applied_at: str,
    ) -> ReschedulePlatformDiscountSharePolicyResponse:
        """주어진 아이디에 대응되는 할인 분담에 예약 업데이트를 재설정합니다.

        Args:
            id (str):
                할인 분담 정책 아이디
            update (UpdatePlatformDiscountSharePolicyBody):
                반영할 업데이트 내용
            applied_at (str):
                업데이트 적용 시점


        Raises:
            RescheduleDiscountSharePolicyError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        request_body["update"] = _serialize_update_platform_discount_share_policy_body(update)
        request_body["appliedAt"] = applied_at
        query = []
        response = await self._client.request(
            "PUT",
            f"{self._base_url}/platform/discount-share-policies/{quote(id, safe='')}/schedule",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": USER_AGENT,
            },
            json=request_body,
        )
        if response.status_code != 200:
            error_response = response.json()
            error = None
            try:
                error = _deserialize_forbidden_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise ForbiddenError(error)
            try:
                error = _deserialize_invalid_request_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise InvalidRequestError(error)
            try:
                error = _deserialize_platform_discount_share_policy_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformDiscountSharePolicyNotFoundError(error)
            try:
                error = _deserialize_platform_not_enabled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformNotEnabledError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_reschedule_platform_discount_share_policy_response(response.json())
    def schedule_discount_share_policy(
        self,
        *,
        id: str,
        update: UpdatePlatformDiscountSharePolicyBody,
        applied_at: str,
    ) -> SchedulePlatformDiscountSharePolicyResponse:
        """주어진 아이디에 대응되는 할인 분담에 업데이트를 예약합니다.

        Args:
            id (str):
                할인 분담 정책 아이디
            update (UpdatePlatformDiscountSharePolicyBody):
                반영할 업데이트 내용
            applied_at (str):
                업데이트 적용 시점


        Raises:
            ScheduleDiscountSharePolicyError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        request_body["update"] = _serialize_update_platform_discount_share_policy_body(update)
        request_body["appliedAt"] = applied_at
        query = []
        response = httpx.request(
            "POST",
            f"{self._base_url}/platform/discount-share-policies/{quote(id, safe='')}/schedule",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": USER_AGENT,
            },
            json=request_body,
        )
        if response.status_code != 200:
            error_response = response.json()
            error = None
            try:
                error = _deserialize_forbidden_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise ForbiddenError(error)
            try:
                error = _deserialize_invalid_request_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise InvalidRequestError(error)
            try:
                error = _deserialize_platform_archived_discount_share_policy_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformArchivedDiscountSharePolicyError(error)
            try:
                error = _deserialize_platform_discount_share_policy_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformDiscountSharePolicyNotFoundError(error)
            try:
                error = _deserialize_platform_discount_share_policy_schedule_already_exists_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformDiscountSharePolicyScheduleAlreadyExistsError(error)
            try:
                error = _deserialize_platform_not_enabled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformNotEnabledError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_schedule_platform_discount_share_policy_response(response.json())
    async def schedule_discount_share_policy_async(
        self,
        *,
        id: str,
        update: UpdatePlatformDiscountSharePolicyBody,
        applied_at: str,
    ) -> SchedulePlatformDiscountSharePolicyResponse:
        """주어진 아이디에 대응되는 할인 분담에 업데이트를 예약합니다.

        Args:
            id (str):
                할인 분담 정책 아이디
            update (UpdatePlatformDiscountSharePolicyBody):
                반영할 업데이트 내용
            applied_at (str):
                업데이트 적용 시점


        Raises:
            ScheduleDiscountSharePolicyError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        request_body["update"] = _serialize_update_platform_discount_share_policy_body(update)
        request_body["appliedAt"] = applied_at
        query = []
        response = await self._client.request(
            "POST",
            f"{self._base_url}/platform/discount-share-policies/{quote(id, safe='')}/schedule",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": USER_AGENT,
            },
            json=request_body,
        )
        if response.status_code != 200:
            error_response = response.json()
            error = None
            try:
                error = _deserialize_forbidden_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise ForbiddenError(error)
            try:
                error = _deserialize_invalid_request_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise InvalidRequestError(error)
            try:
                error = _deserialize_platform_archived_discount_share_policy_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformArchivedDiscountSharePolicyError(error)
            try:
                error = _deserialize_platform_discount_share_policy_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformDiscountSharePolicyNotFoundError(error)
            try:
                error = _deserialize_platform_discount_share_policy_schedule_already_exists_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformDiscountSharePolicyScheduleAlreadyExistsError(error)
            try:
                error = _deserialize_platform_not_enabled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformNotEnabledError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_schedule_platform_discount_share_policy_response(response.json())
    def cancel_platform_discount_share_policy_schedule(
        self,
        *,
        id: str,
    ) -> CancelPlatformDiscountSharePolicyScheduleResponse:
        """주어진 아이디에 대응되는 할인 분담의 예약 업데이트를 취소합니다.

        Args:
            id (str):
                할인 분담 정책 아이디


        Raises:
            CancelPlatformDiscountSharePolicyScheduleError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        response = httpx.request(
            "DELETE",
            f"{self._base_url}/platform/discount-share-policies/{quote(id, safe='')}/schedule",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": USER_AGENT,
            },
        )
        if response.status_code != 200:
            error_response = response.json()
            error = None
            try:
                error = _deserialize_forbidden_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise ForbiddenError(error)
            try:
                error = _deserialize_invalid_request_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise InvalidRequestError(error)
            try:
                error = _deserialize_platform_discount_share_policy_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformDiscountSharePolicyNotFoundError(error)
            try:
                error = _deserialize_platform_not_enabled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformNotEnabledError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_cancel_platform_discount_share_policy_schedule_response(response.json())
    async def cancel_platform_discount_share_policy_schedule_async(
        self,
        *,
        id: str,
    ) -> CancelPlatformDiscountSharePolicyScheduleResponse:
        """주어진 아이디에 대응되는 할인 분담의 예약 업데이트를 취소합니다.

        Args:
            id (str):
                할인 분담 정책 아이디


        Raises:
            CancelPlatformDiscountSharePolicyScheduleError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        response = await self._client.request(
            "DELETE",
            f"{self._base_url}/platform/discount-share-policies/{quote(id, safe='')}/schedule",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": USER_AGENT,
            },
        )
        if response.status_code != 200:
            error_response = response.json()
            error = None
            try:
                error = _deserialize_forbidden_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise ForbiddenError(error)
            try:
                error = _deserialize_invalid_request_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise InvalidRequestError(error)
            try:
                error = _deserialize_platform_discount_share_policy_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformDiscountSharePolicyNotFoundError(error)
            try:
                error = _deserialize_platform_not_enabled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformNotEnabledError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_cancel_platform_discount_share_policy_schedule_response(response.json())
    def get_platform_additional_fee_policy_schedule(
        self,
        *,
        id: str,
    ) -> PlatformAdditionalFeePolicy:
        """주어진 아이디에 대응되는 추가 수수료 정책의 예약 업데이트를 조회합니다.

        Args:
            id (str):
                추가 수수료 정책 아이디


        Raises:
            GetPlatformAdditionalFeePolicyScheduleError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        response = httpx.request(
            "GET",
            f"{self._base_url}/platform/additional-fee-policies/{quote(id, safe='')}/schedule",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": USER_AGENT,
            },
        )
        if response.status_code != 200:
            error_response = response.json()
            error = None
            try:
                error = _deserialize_forbidden_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise ForbiddenError(error)
            try:
                error = _deserialize_invalid_request_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise InvalidRequestError(error)
            try:
                error = _deserialize_platform_additional_fee_policy_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformAdditionalFeePolicyNotFoundError(error)
            try:
                error = _deserialize_platform_not_enabled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformNotEnabledError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_platform_additional_fee_policy(response.json())
    async def get_platform_additional_fee_policy_schedule_async(
        self,
        *,
        id: str,
    ) -> PlatformAdditionalFeePolicy:
        """주어진 아이디에 대응되는 추가 수수료 정책의 예약 업데이트를 조회합니다.

        Args:
            id (str):
                추가 수수료 정책 아이디


        Raises:
            GetPlatformAdditionalFeePolicyScheduleError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        response = await self._client.request(
            "GET",
            f"{self._base_url}/platform/additional-fee-policies/{quote(id, safe='')}/schedule",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": USER_AGENT,
            },
        )
        if response.status_code != 200:
            error_response = response.json()
            error = None
            try:
                error = _deserialize_forbidden_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise ForbiddenError(error)
            try:
                error = _deserialize_invalid_request_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise InvalidRequestError(error)
            try:
                error = _deserialize_platform_additional_fee_policy_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformAdditionalFeePolicyNotFoundError(error)
            try:
                error = _deserialize_platform_not_enabled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformNotEnabledError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_platform_additional_fee_policy(response.json())
    def reschedule_additional_fee_policy(
        self,
        *,
        id: str,
        update: UpdatePlatformAdditionalFeePolicyBody,
        applied_at: str,
    ) -> ReschedulePlatformAdditionalFeePolicyResponse:
        """Args:
            id (str):
                추가 수수료 정책 아이디
            update (UpdatePlatformAdditionalFeePolicyBody):
                반영할 업데이트 내용
            applied_at (str):
                업데이트 적용 시점


        Raises:
            RescheduleAdditionalFeePolicyError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        request_body["update"] = _serialize_update_platform_additional_fee_policy_body(update)
        request_body["appliedAt"] = applied_at
        query = []
        response = httpx.request(
            "PUT",
            f"{self._base_url}/platform/additional-fee-policies/{quote(id, safe='')}/schedule",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": USER_AGENT,
            },
            json=request_body,
        )
        if response.status_code != 200:
            error_response = response.json()
            error = None
            try:
                error = _deserialize_forbidden_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise ForbiddenError(error)
            try:
                error = _deserialize_invalid_request_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise InvalidRequestError(error)
            try:
                error = _deserialize_platform_additional_fee_policy_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformAdditionalFeePolicyNotFoundError(error)
            try:
                error = _deserialize_platform_not_enabled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformNotEnabledError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_reschedule_platform_additional_fee_policy_response(response.json())
    async def reschedule_additional_fee_policy_async(
        self,
        *,
        id: str,
        update: UpdatePlatformAdditionalFeePolicyBody,
        applied_at: str,
    ) -> ReschedulePlatformAdditionalFeePolicyResponse:
        """Args:
            id (str):
                추가 수수료 정책 아이디
            update (UpdatePlatformAdditionalFeePolicyBody):
                반영할 업데이트 내용
            applied_at (str):
                업데이트 적용 시점


        Raises:
            RescheduleAdditionalFeePolicyError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        request_body["update"] = _serialize_update_platform_additional_fee_policy_body(update)
        request_body["appliedAt"] = applied_at
        query = []
        response = await self._client.request(
            "PUT",
            f"{self._base_url}/platform/additional-fee-policies/{quote(id, safe='')}/schedule",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": USER_AGENT,
            },
            json=request_body,
        )
        if response.status_code != 200:
            error_response = response.json()
            error = None
            try:
                error = _deserialize_forbidden_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise ForbiddenError(error)
            try:
                error = _deserialize_invalid_request_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise InvalidRequestError(error)
            try:
                error = _deserialize_platform_additional_fee_policy_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformAdditionalFeePolicyNotFoundError(error)
            try:
                error = _deserialize_platform_not_enabled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformNotEnabledError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_reschedule_platform_additional_fee_policy_response(response.json())
    def schedule_additional_fee_policy(
        self,
        *,
        id: str,
        update: UpdatePlatformAdditionalFeePolicyBody,
        applied_at: str,
    ) -> SchedulePlatformAdditionalFeePolicyResponse:
        """주어진 아이디에 대응되는 추가 수수료 정책에 업데이트를 예약합니다.

        Args:
            id (str):
                추가 수수료 정책 아이디
            update (UpdatePlatformAdditionalFeePolicyBody):
                반영할 업데이트 내용
            applied_at (str):
                업데이트 적용 시점


        Raises:
            ScheduleAdditionalFeePolicyError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        request_body["update"] = _serialize_update_platform_additional_fee_policy_body(update)
        request_body["appliedAt"] = applied_at
        query = []
        response = httpx.request(
            "POST",
            f"{self._base_url}/platform/additional-fee-policies/{quote(id, safe='')}/schedule",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": USER_AGENT,
            },
            json=request_body,
        )
        if response.status_code != 200:
            error_response = response.json()
            error = None
            try:
                error = _deserialize_forbidden_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise ForbiddenError(error)
            try:
                error = _deserialize_invalid_request_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise InvalidRequestError(error)
            try:
                error = _deserialize_platform_additional_fee_policy_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformAdditionalFeePolicyNotFoundError(error)
            try:
                error = _deserialize_platform_additional_fee_policy_schedule_already_exists_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformAdditionalFeePolicyScheduleAlreadyExistsError(error)
            try:
                error = _deserialize_platform_archived_additional_fee_policy_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformArchivedAdditionalFeePolicyError(error)
            try:
                error = _deserialize_platform_not_enabled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformNotEnabledError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_schedule_platform_additional_fee_policy_response(response.json())
    async def schedule_additional_fee_policy_async(
        self,
        *,
        id: str,
        update: UpdatePlatformAdditionalFeePolicyBody,
        applied_at: str,
    ) -> SchedulePlatformAdditionalFeePolicyResponse:
        """주어진 아이디에 대응되는 추가 수수료 정책에 업데이트를 예약합니다.

        Args:
            id (str):
                추가 수수료 정책 아이디
            update (UpdatePlatformAdditionalFeePolicyBody):
                반영할 업데이트 내용
            applied_at (str):
                업데이트 적용 시점


        Raises:
            ScheduleAdditionalFeePolicyError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        request_body["update"] = _serialize_update_platform_additional_fee_policy_body(update)
        request_body["appliedAt"] = applied_at
        query = []
        response = await self._client.request(
            "POST",
            f"{self._base_url}/platform/additional-fee-policies/{quote(id, safe='')}/schedule",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": USER_AGENT,
            },
            json=request_body,
        )
        if response.status_code != 200:
            error_response = response.json()
            error = None
            try:
                error = _deserialize_forbidden_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise ForbiddenError(error)
            try:
                error = _deserialize_invalid_request_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise InvalidRequestError(error)
            try:
                error = _deserialize_platform_additional_fee_policy_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformAdditionalFeePolicyNotFoundError(error)
            try:
                error = _deserialize_platform_additional_fee_policy_schedule_already_exists_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformAdditionalFeePolicyScheduleAlreadyExistsError(error)
            try:
                error = _deserialize_platform_archived_additional_fee_policy_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformArchivedAdditionalFeePolicyError(error)
            try:
                error = _deserialize_platform_not_enabled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformNotEnabledError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_schedule_platform_additional_fee_policy_response(response.json())
    def cancel_platform_additional_fee_policy_schedule(
        self,
        *,
        id: str,
    ) -> CancelPlatformAdditionalFeePolicyScheduleResponse:
        """주어진 아이디에 대응되는 추가 수수료 정책의 예약 업데이트를 취소합니다.

        Args:
            id (str):
                추가 수수료 정책 아이디


        Raises:
            CancelPlatformAdditionalFeePolicyScheduleError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        response = httpx.request(
            "DELETE",
            f"{self._base_url}/platform/additional-fee-policies/{quote(id, safe='')}/schedule",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": USER_AGENT,
            },
        )
        if response.status_code != 200:
            error_response = response.json()
            error = None
            try:
                error = _deserialize_forbidden_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise ForbiddenError(error)
            try:
                error = _deserialize_invalid_request_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise InvalidRequestError(error)
            try:
                error = _deserialize_platform_additional_fee_policy_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformAdditionalFeePolicyNotFoundError(error)
            try:
                error = _deserialize_platform_not_enabled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformNotEnabledError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_cancel_platform_additional_fee_policy_schedule_response(response.json())
    async def cancel_platform_additional_fee_policy_schedule_async(
        self,
        *,
        id: str,
    ) -> CancelPlatformAdditionalFeePolicyScheduleResponse:
        """주어진 아이디에 대응되는 추가 수수료 정책의 예약 업데이트를 취소합니다.

        Args:
            id (str):
                추가 수수료 정책 아이디


        Raises:
            CancelPlatformAdditionalFeePolicyScheduleError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        response = await self._client.request(
            "DELETE",
            f"{self._base_url}/platform/additional-fee-policies/{quote(id, safe='')}/schedule",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": USER_AGENT,
            },
        )
        if response.status_code != 200:
            error_response = response.json()
            error = None
            try:
                error = _deserialize_forbidden_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise ForbiddenError(error)
            try:
                error = _deserialize_invalid_request_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise InvalidRequestError(error)
            try:
                error = _deserialize_platform_additional_fee_policy_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformAdditionalFeePolicyNotFoundError(error)
            try:
                error = _deserialize_platform_not_enabled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformNotEnabledError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_cancel_platform_additional_fee_policy_schedule_response(response.json())
    def get_platform_partner_filter_options(
        self,
        *,
        is_archived: Optional[bool] = None,
    ) -> PlatformPartnerFilterOptions:
        """파트너 다건 조회 시 필요한 필터 옵션을 조회합니다.

        Args:
            is_archived (bool, optional):
                보관 조회 여부

                true 이면 보관된 파트너의 필터 옵션을 조회하고, false 이면 보관되지 않은 파트너의 필터 옵션을 조회합니다. 기본값은 false 입니다.


        Raises:
            GetPlatformPartnerFilterOptionsError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        if is_archived is not None:
            query.append(("isArchived", is_archived))
        response = httpx.request(
            "GET",
            f"{self._base_url}/platform/partner-filter-options",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": USER_AGENT,
            },
        )
        if response.status_code != 200:
            error_response = response.json()
            error = None
            try:
                error = _deserialize_forbidden_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise ForbiddenError(error)
            try:
                error = _deserialize_invalid_request_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise InvalidRequestError(error)
            try:
                error = _deserialize_platform_not_enabled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformNotEnabledError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_platform_partner_filter_options(response.json())
    async def get_platform_partner_filter_options_async(
        self,
        *,
        is_archived: Optional[bool] = None,
    ) -> PlatformPartnerFilterOptions:
        """파트너 다건 조회 시 필요한 필터 옵션을 조회합니다.

        Args:
            is_archived (bool, optional):
                보관 조회 여부

                true 이면 보관된 파트너의 필터 옵션을 조회하고, false 이면 보관되지 않은 파트너의 필터 옵션을 조회합니다. 기본값은 false 입니다.


        Raises:
            GetPlatformPartnerFilterOptionsError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        if is_archived is not None:
            query.append(("isArchived", is_archived))
        response = await self._client.request(
            "GET",
            f"{self._base_url}/platform/partner-filter-options",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": USER_AGENT,
            },
        )
        if response.status_code != 200:
            error_response = response.json()
            error = None
            try:
                error = _deserialize_forbidden_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise ForbiddenError(error)
            try:
                error = _deserialize_invalid_request_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise InvalidRequestError(error)
            try:
                error = _deserialize_platform_not_enabled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformNotEnabledError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_platform_partner_filter_options(response.json())
    def get_platform_partner_schedule(
        self,
        *,
        id: str,
    ) -> PlatformPartner:
        """주어진 아이디에 대응되는 파트너의 예약 업데이트를 조회합니다.

        Args:
            id (str):
                파트너 아이디


        Raises:
            GetPlatformPartnerScheduleError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        response = httpx.request(
            "GET",
            f"{self._base_url}/platform/partners/{quote(id, safe='')}/schedule",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": USER_AGENT,
            },
        )
        if response.status_code != 200:
            error_response = response.json()
            error = None
            try:
                error = _deserialize_forbidden_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise ForbiddenError(error)
            try:
                error = _deserialize_invalid_request_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise InvalidRequestError(error)
            try:
                error = _deserialize_platform_not_enabled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformNotEnabledError(error)
            try:
                error = _deserialize_platform_partner_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformPartnerNotFoundError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_platform_partner(response.json())
    async def get_platform_partner_schedule_async(
        self,
        *,
        id: str,
    ) -> PlatformPartner:
        """주어진 아이디에 대응되는 파트너의 예약 업데이트를 조회합니다.

        Args:
            id (str):
                파트너 아이디


        Raises:
            GetPlatformPartnerScheduleError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        response = await self._client.request(
            "GET",
            f"{self._base_url}/platform/partners/{quote(id, safe='')}/schedule",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": USER_AGENT,
            },
        )
        if response.status_code != 200:
            error_response = response.json()
            error = None
            try:
                error = _deserialize_forbidden_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise ForbiddenError(error)
            try:
                error = _deserialize_invalid_request_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise InvalidRequestError(error)
            try:
                error = _deserialize_platform_not_enabled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformNotEnabledError(error)
            try:
                error = _deserialize_platform_partner_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformPartnerNotFoundError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_platform_partner(response.json())
    def reschedule_partner(
        self,
        *,
        id: str,
        update: UpdatePlatformPartnerBody,
        applied_at: str,
    ) -> ReschedulePlatformPartnerResponse:
        """주어진 아이디에 대응되는 파트너에 예약 업데이트를 재설정합니다.

        Args:
            id (str):
                파트너 아이디
            update (UpdatePlatformPartnerBody):
                반영할 업데이트 내용
            applied_at (str):
                업데이트 적용 시점


        Raises:
            ReschedulePartnerError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        request_body["update"] = _serialize_update_platform_partner_body(update)
        request_body["appliedAt"] = applied_at
        query = []
        response = httpx.request(
            "PUT",
            f"{self._base_url}/platform/partners/{quote(id, safe='')}/schedule",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": USER_AGENT,
            },
            json=request_body,
        )
        if response.status_code != 200:
            error_response = response.json()
            error = None
            try:
                error = _deserialize_forbidden_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise ForbiddenError(error)
            try:
                error = _deserialize_invalid_request_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise InvalidRequestError(error)
            try:
                error = _deserialize_platform_contract_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformContractNotFoundError(error)
            try:
                error = _deserialize_platform_member_company_connected_partner_cannot_be_scheduled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformMemberCompanyConnectedPartnerCannotBeScheduledError(error)
            try:
                error = _deserialize_platform_not_enabled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformNotEnabledError(error)
            try:
                error = _deserialize_platform_partner_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformPartnerNotFoundError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_reschedule_platform_partner_response(response.json())
    async def reschedule_partner_async(
        self,
        *,
        id: str,
        update: UpdatePlatformPartnerBody,
        applied_at: str,
    ) -> ReschedulePlatformPartnerResponse:
        """주어진 아이디에 대응되는 파트너에 예약 업데이트를 재설정합니다.

        Args:
            id (str):
                파트너 아이디
            update (UpdatePlatformPartnerBody):
                반영할 업데이트 내용
            applied_at (str):
                업데이트 적용 시점


        Raises:
            ReschedulePartnerError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        request_body["update"] = _serialize_update_platform_partner_body(update)
        request_body["appliedAt"] = applied_at
        query = []
        response = await self._client.request(
            "PUT",
            f"{self._base_url}/platform/partners/{quote(id, safe='')}/schedule",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": USER_AGENT,
            },
            json=request_body,
        )
        if response.status_code != 200:
            error_response = response.json()
            error = None
            try:
                error = _deserialize_forbidden_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise ForbiddenError(error)
            try:
                error = _deserialize_invalid_request_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise InvalidRequestError(error)
            try:
                error = _deserialize_platform_contract_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformContractNotFoundError(error)
            try:
                error = _deserialize_platform_member_company_connected_partner_cannot_be_scheduled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformMemberCompanyConnectedPartnerCannotBeScheduledError(error)
            try:
                error = _deserialize_platform_not_enabled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformNotEnabledError(error)
            try:
                error = _deserialize_platform_partner_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformPartnerNotFoundError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_reschedule_platform_partner_response(response.json())
    def schedule_partner(
        self,
        *,
        id: str,
        update: UpdatePlatformPartnerBody,
        applied_at: str,
    ) -> SchedulePlatformPartnerResponse:
        """주어진 아이디에 대응되는 파트너에 업데이트를 예약합니다.

        Args:
            id (str):
                파트너 아이디
            update (UpdatePlatformPartnerBody):
                반영할 업데이트 내용
            applied_at (str):
                업데이트 적용 시점


        Raises:
            SchedulePartnerError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        request_body["update"] = _serialize_update_platform_partner_body(update)
        request_body["appliedAt"] = applied_at
        query = []
        response = httpx.request(
            "POST",
            f"{self._base_url}/platform/partners/{quote(id, safe='')}/schedule",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": USER_AGENT,
            },
            json=request_body,
        )
        if response.status_code != 200:
            error_response = response.json()
            error = None
            try:
                error = _deserialize_forbidden_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise ForbiddenError(error)
            try:
                error = _deserialize_invalid_request_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise InvalidRequestError(error)
            try:
                error = _deserialize_platform_account_verification_already_used_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformAccountVerificationAlreadyUsedError(error)
            try:
                error = _deserialize_platform_account_verification_failed_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformAccountVerificationFailedError(error)
            try:
                error = _deserialize_platform_account_verification_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformAccountVerificationNotFoundError(error)
            try:
                error = _deserialize_platform_archived_partner_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformArchivedPartnerError(error)
            try:
                error = _deserialize_platform_company_verification_already_used_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformCompanyVerificationAlreadyUsedError(error)
            try:
                error = _deserialize_platform_contract_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformContractNotFoundError(error)
            try:
                error = _deserialize_platform_insufficient_data_to_change_partner_type_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformInsufficientDataToChangePartnerTypeError(error)
            try:
                error = _deserialize_platform_member_company_connected_partner_brn_unchangeable_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformMemberCompanyConnectedPartnerBrnUnchangeableError(error)
            try:
                error = _deserialize_platform_member_company_connected_partner_cannot_be_scheduled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformMemberCompanyConnectedPartnerCannotBeScheduledError(error)
            try:
                error = _deserialize_platform_member_company_connected_partner_type_unchangeable_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformMemberCompanyConnectedPartnerTypeUnchangeableError(error)
            try:
                error = _deserialize_platform_not_enabled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformNotEnabledError(error)
            try:
                error = _deserialize_platform_partner_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformPartnerNotFoundError(error)
            try:
                error = _deserialize_platform_partner_schedule_already_exists_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformPartnerScheduleAlreadyExistsError(error)
            try:
                error = _deserialize_platform_user_defined_property_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformUserDefinedPropertyNotFoundError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_schedule_platform_partner_response(response.json())
    async def schedule_partner_async(
        self,
        *,
        id: str,
        update: UpdatePlatformPartnerBody,
        applied_at: str,
    ) -> SchedulePlatformPartnerResponse:
        """주어진 아이디에 대응되는 파트너에 업데이트를 예약합니다.

        Args:
            id (str):
                파트너 아이디
            update (UpdatePlatformPartnerBody):
                반영할 업데이트 내용
            applied_at (str):
                업데이트 적용 시점


        Raises:
            SchedulePartnerError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        request_body["update"] = _serialize_update_platform_partner_body(update)
        request_body["appliedAt"] = applied_at
        query = []
        response = await self._client.request(
            "POST",
            f"{self._base_url}/platform/partners/{quote(id, safe='')}/schedule",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": USER_AGENT,
            },
            json=request_body,
        )
        if response.status_code != 200:
            error_response = response.json()
            error = None
            try:
                error = _deserialize_forbidden_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise ForbiddenError(error)
            try:
                error = _deserialize_invalid_request_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise InvalidRequestError(error)
            try:
                error = _deserialize_platform_account_verification_already_used_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformAccountVerificationAlreadyUsedError(error)
            try:
                error = _deserialize_platform_account_verification_failed_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformAccountVerificationFailedError(error)
            try:
                error = _deserialize_platform_account_verification_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformAccountVerificationNotFoundError(error)
            try:
                error = _deserialize_platform_archived_partner_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformArchivedPartnerError(error)
            try:
                error = _deserialize_platform_company_verification_already_used_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformCompanyVerificationAlreadyUsedError(error)
            try:
                error = _deserialize_platform_contract_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformContractNotFoundError(error)
            try:
                error = _deserialize_platform_insufficient_data_to_change_partner_type_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformInsufficientDataToChangePartnerTypeError(error)
            try:
                error = _deserialize_platform_member_company_connected_partner_brn_unchangeable_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformMemberCompanyConnectedPartnerBrnUnchangeableError(error)
            try:
                error = _deserialize_platform_member_company_connected_partner_cannot_be_scheduled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformMemberCompanyConnectedPartnerCannotBeScheduledError(error)
            try:
                error = _deserialize_platform_member_company_connected_partner_type_unchangeable_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformMemberCompanyConnectedPartnerTypeUnchangeableError(error)
            try:
                error = _deserialize_platform_not_enabled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformNotEnabledError(error)
            try:
                error = _deserialize_platform_partner_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformPartnerNotFoundError(error)
            try:
                error = _deserialize_platform_partner_schedule_already_exists_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformPartnerScheduleAlreadyExistsError(error)
            try:
                error = _deserialize_platform_user_defined_property_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformUserDefinedPropertyNotFoundError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_schedule_platform_partner_response(response.json())
    def cancel_platform_partner_schedule(
        self,
        *,
        id: str,
    ) -> CancelPlatformPartnerScheduleResponse:
        """주어진 아이디에 대응되는 파트너의 예약 업데이트를 취소합니다.

        Args:
            id (str):
                파트너 아이디


        Raises:
            CancelPlatformPartnerScheduleError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        response = httpx.request(
            "DELETE",
            f"{self._base_url}/platform/partners/{quote(id, safe='')}/schedule",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": USER_AGENT,
            },
        )
        if response.status_code != 200:
            error_response = response.json()
            error = None
            try:
                error = _deserialize_forbidden_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise ForbiddenError(error)
            try:
                error = _deserialize_invalid_request_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise InvalidRequestError(error)
            try:
                error = _deserialize_platform_not_enabled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformNotEnabledError(error)
            try:
                error = _deserialize_platform_partner_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformPartnerNotFoundError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_cancel_platform_partner_schedule_response(response.json())
    async def cancel_platform_partner_schedule_async(
        self,
        *,
        id: str,
    ) -> CancelPlatformPartnerScheduleResponse:
        """주어진 아이디에 대응되는 파트너의 예약 업데이트를 취소합니다.

        Args:
            id (str):
                파트너 아이디


        Raises:
            CancelPlatformPartnerScheduleError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        response = await self._client.request(
            "DELETE",
            f"{self._base_url}/platform/partners/{quote(id, safe='')}/schedule",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": USER_AGENT,
            },
        )
        if response.status_code != 200:
            error_response = response.json()
            error = None
            try:
                error = _deserialize_forbidden_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise ForbiddenError(error)
            try:
                error = _deserialize_invalid_request_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise InvalidRequestError(error)
            try:
                error = _deserialize_platform_not_enabled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformNotEnabledError(error)
            try:
                error = _deserialize_platform_partner_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformPartnerNotFoundError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_cancel_platform_partner_schedule_response(response.json())
    def schedule_platform_partners(
        self,
        *,
        filter: Optional[PlatformPartnerFilterInput] = None,
        update: SchedulePlatformPartnersBodyUpdate,
        applied_at: str,
    ) -> SchedulePlatformPartnersResponse:
        """Args:
            filter (PlatformPartnerFilterInput, optional):

            update (SchedulePlatformPartnersBodyUpdate):

            applied_at (str):



        Raises:
            SchedulePlatformPartnersError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        if filter is not None:
            request_body["filter"] = _serialize_platform_partner_filter_input(filter)
        request_body["update"] = _serialize_schedule_platform_partners_body_update(update)
        request_body["appliedAt"] = applied_at
        query = []
        response = httpx.request(
            "POST",
            f"{self._base_url}/platform/partners/schedule",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": USER_AGENT,
            },
            json=request_body,
        )
        if response.status_code != 200:
            error_response = response.json()
            error = None
            try:
                error = _deserialize_forbidden_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise ForbiddenError(error)
            try:
                error = _deserialize_invalid_request_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise InvalidRequestError(error)
            try:
                error = _deserialize_platform_archived_partners_cannot_be_scheduled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformArchivedPartnersCannotBeScheduledError(error)
            try:
                error = _deserialize_platform_contract_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformContractNotFoundError(error)
            try:
                error = _deserialize_platform_member_company_connected_partners_cannot_be_scheduled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformMemberCompanyConnectedPartnersCannotBeScheduledError(error)
            try:
                error = _deserialize_platform_not_enabled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformNotEnabledError(error)
            try:
                error = _deserialize_platform_partner_schedules_already_exist_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformPartnerSchedulesAlreadyExistError(error)
            try:
                error = _deserialize_platform_user_defined_property_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformUserDefinedPropertyNotFoundError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_schedule_platform_partners_response(response.json())
    async def schedule_platform_partners_async(
        self,
        *,
        filter: Optional[PlatformPartnerFilterInput] = None,
        update: SchedulePlatformPartnersBodyUpdate,
        applied_at: str,
    ) -> SchedulePlatformPartnersResponse:
        """Args:
            filter (PlatformPartnerFilterInput, optional):

            update (SchedulePlatformPartnersBodyUpdate):

            applied_at (str):



        Raises:
            SchedulePlatformPartnersError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        if filter is not None:
            request_body["filter"] = _serialize_platform_partner_filter_input(filter)
        request_body["update"] = _serialize_schedule_platform_partners_body_update(update)
        request_body["appliedAt"] = applied_at
        query = []
        response = await self._client.request(
            "POST",
            f"{self._base_url}/platform/partners/schedule",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": USER_AGENT,
            },
            json=request_body,
        )
        if response.status_code != 200:
            error_response = response.json()
            error = None
            try:
                error = _deserialize_forbidden_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise ForbiddenError(error)
            try:
                error = _deserialize_invalid_request_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise InvalidRequestError(error)
            try:
                error = _deserialize_platform_archived_partners_cannot_be_scheduled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformArchivedPartnersCannotBeScheduledError(error)
            try:
                error = _deserialize_platform_contract_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformContractNotFoundError(error)
            try:
                error = _deserialize_platform_member_company_connected_partners_cannot_be_scheduled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformMemberCompanyConnectedPartnersCannotBeScheduledError(error)
            try:
                error = _deserialize_platform_not_enabled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformNotEnabledError(error)
            try:
                error = _deserialize_platform_partner_schedules_already_exist_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformPartnerSchedulesAlreadyExistError(error)
            try:
                error = _deserialize_platform_user_defined_property_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformUserDefinedPropertyNotFoundError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_schedule_platform_partners_response(response.json())
    def get_platform_contract_schedule(
        self,
        *,
        id: str,
    ) -> PlatformContract:
        """주어진 아이디에 대응되는 계약의 예약 업데이트를 조회합니다.

        Args:
            id (str):
                계약 아이디


        Raises:
            GetPlatformContractScheduleError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        response = httpx.request(
            "GET",
            f"{self._base_url}/platform/contracts/{quote(id, safe='')}/schedule",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": USER_AGENT,
            },
        )
        if response.status_code != 200:
            error_response = response.json()
            error = None
            try:
                error = _deserialize_forbidden_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise ForbiddenError(error)
            try:
                error = _deserialize_invalid_request_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise InvalidRequestError(error)
            try:
                error = _deserialize_platform_contract_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformContractNotFoundError(error)
            try:
                error = _deserialize_platform_not_enabled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformNotEnabledError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_platform_contract(response.json())
    async def get_platform_contract_schedule_async(
        self,
        *,
        id: str,
    ) -> PlatformContract:
        """주어진 아이디에 대응되는 계약의 예약 업데이트를 조회합니다.

        Args:
            id (str):
                계약 아이디


        Raises:
            GetPlatformContractScheduleError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        response = await self._client.request(
            "GET",
            f"{self._base_url}/platform/contracts/{quote(id, safe='')}/schedule",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": USER_AGENT,
            },
        )
        if response.status_code != 200:
            error_response = response.json()
            error = None
            try:
                error = _deserialize_forbidden_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise ForbiddenError(error)
            try:
                error = _deserialize_invalid_request_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise InvalidRequestError(error)
            try:
                error = _deserialize_platform_contract_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformContractNotFoundError(error)
            try:
                error = _deserialize_platform_not_enabled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformNotEnabledError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_platform_contract(response.json())
    def reschedule_contract(
        self,
        *,
        id: str,
        update: UpdatePlatformContractBody,
        applied_at: str,
    ) -> ReschedulePlatformContractResponse:
        """주어진 아이디에 대응되는 계약에 예약 업데이트를 재설정합니다.

        Args:
            id (str):
                계약 아이디
            update (UpdatePlatformContractBody):
                반영할 업데이트 내용
            applied_at (str):
                업데이트 적용 시점


        Raises:
            RescheduleContractError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        request_body["update"] = _serialize_update_platform_contract_body(update)
        request_body["appliedAt"] = applied_at
        query = []
        response = httpx.request(
            "PUT",
            f"{self._base_url}/platform/contracts/{quote(id, safe='')}/schedule",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": USER_AGENT,
            },
            json=request_body,
        )
        if response.status_code != 200:
            error_response = response.json()
            error = None
            try:
                error = _deserialize_forbidden_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise ForbiddenError(error)
            try:
                error = _deserialize_invalid_request_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise InvalidRequestError(error)
            try:
                error = _deserialize_platform_contract_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformContractNotFoundError(error)
            try:
                error = _deserialize_platform_not_enabled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformNotEnabledError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_reschedule_platform_contract_response(response.json())
    async def reschedule_contract_async(
        self,
        *,
        id: str,
        update: UpdatePlatformContractBody,
        applied_at: str,
    ) -> ReschedulePlatformContractResponse:
        """주어진 아이디에 대응되는 계약에 예약 업데이트를 재설정합니다.

        Args:
            id (str):
                계약 아이디
            update (UpdatePlatformContractBody):
                반영할 업데이트 내용
            applied_at (str):
                업데이트 적용 시점


        Raises:
            RescheduleContractError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        request_body["update"] = _serialize_update_platform_contract_body(update)
        request_body["appliedAt"] = applied_at
        query = []
        response = await self._client.request(
            "PUT",
            f"{self._base_url}/platform/contracts/{quote(id, safe='')}/schedule",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": USER_AGENT,
            },
            json=request_body,
        )
        if response.status_code != 200:
            error_response = response.json()
            error = None
            try:
                error = _deserialize_forbidden_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise ForbiddenError(error)
            try:
                error = _deserialize_invalid_request_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise InvalidRequestError(error)
            try:
                error = _deserialize_platform_contract_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformContractNotFoundError(error)
            try:
                error = _deserialize_platform_not_enabled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformNotEnabledError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_reschedule_platform_contract_response(response.json())
    def schedule_contract(
        self,
        *,
        id: str,
        update: UpdatePlatformContractBody,
        applied_at: str,
    ) -> SchedulePlatformContractResponse:
        """주어진 아이디에 대응되는 계약에 업데이트를 예약합니다.

        Args:
            id (str):
                계약 아이디
            update (UpdatePlatformContractBody):
                반영할 업데이트 내용
            applied_at (str):
                업데이트 적용 시점


        Raises:
            ScheduleContractError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        request_body["update"] = _serialize_update_platform_contract_body(update)
        request_body["appliedAt"] = applied_at
        query = []
        response = httpx.request(
            "POST",
            f"{self._base_url}/platform/contracts/{quote(id, safe='')}/schedule",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": USER_AGENT,
            },
            json=request_body,
        )
        if response.status_code != 200:
            error_response = response.json()
            error = None
            try:
                error = _deserialize_forbidden_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise ForbiddenError(error)
            try:
                error = _deserialize_invalid_request_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise InvalidRequestError(error)
            try:
                error = _deserialize_platform_archived_contract_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformArchivedContractError(error)
            try:
                error = _deserialize_platform_contract_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformContractNotFoundError(error)
            try:
                error = _deserialize_platform_contract_schedule_already_exists_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformContractScheduleAlreadyExistsError(error)
            try:
                error = _deserialize_platform_not_enabled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformNotEnabledError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_schedule_platform_contract_response(response.json())
    async def schedule_contract_async(
        self,
        *,
        id: str,
        update: UpdatePlatformContractBody,
        applied_at: str,
    ) -> SchedulePlatformContractResponse:
        """주어진 아이디에 대응되는 계약에 업데이트를 예약합니다.

        Args:
            id (str):
                계약 아이디
            update (UpdatePlatformContractBody):
                반영할 업데이트 내용
            applied_at (str):
                업데이트 적용 시점


        Raises:
            ScheduleContractError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        request_body["update"] = _serialize_update_platform_contract_body(update)
        request_body["appliedAt"] = applied_at
        query = []
        response = await self._client.request(
            "POST",
            f"{self._base_url}/platform/contracts/{quote(id, safe='')}/schedule",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": USER_AGENT,
            },
            json=request_body,
        )
        if response.status_code != 200:
            error_response = response.json()
            error = None
            try:
                error = _deserialize_forbidden_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise ForbiddenError(error)
            try:
                error = _deserialize_invalid_request_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise InvalidRequestError(error)
            try:
                error = _deserialize_platform_archived_contract_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformArchivedContractError(error)
            try:
                error = _deserialize_platform_contract_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformContractNotFoundError(error)
            try:
                error = _deserialize_platform_contract_schedule_already_exists_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformContractScheduleAlreadyExistsError(error)
            try:
                error = _deserialize_platform_not_enabled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformNotEnabledError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_schedule_platform_contract_response(response.json())
    def cancel_platform_contract_schedule(
        self,
        *,
        id: str,
    ) -> CancelPlatformContractScheduleResponse:
        """주어진 아이디에 대응되는 계약의 예약 업데이트를 취소합니다.

        Args:
            id (str):
                계약 아이디


        Raises:
            CancelPlatformContractScheduleError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        response = httpx.request(
            "DELETE",
            f"{self._base_url}/platform/contracts/{quote(id, safe='')}/schedule",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": USER_AGENT,
            },
        )
        if response.status_code != 200:
            error_response = response.json()
            error = None
            try:
                error = _deserialize_forbidden_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise ForbiddenError(error)
            try:
                error = _deserialize_invalid_request_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise InvalidRequestError(error)
            try:
                error = _deserialize_platform_contract_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformContractNotFoundError(error)
            try:
                error = _deserialize_platform_not_enabled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformNotEnabledError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_cancel_platform_contract_schedule_response(response.json())
    async def cancel_platform_contract_schedule_async(
        self,
        *,
        id: str,
    ) -> CancelPlatformContractScheduleResponse:
        """주어진 아이디에 대응되는 계약의 예약 업데이트를 취소합니다.

        Args:
            id (str):
                계약 아이디


        Raises:
            CancelPlatformContractScheduleError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        response = await self._client.request(
            "DELETE",
            f"{self._base_url}/platform/contracts/{quote(id, safe='')}/schedule",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": USER_AGENT,
            },
        )
        if response.status_code != 200:
            error_response = response.json()
            error = None
            try:
                error = _deserialize_forbidden_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise ForbiddenError(error)
            try:
                error = _deserialize_invalid_request_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise InvalidRequestError(error)
            try:
                error = _deserialize_platform_contract_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformContractNotFoundError(error)
            try:
                error = _deserialize_platform_not_enabled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformNotEnabledError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_cancel_platform_contract_schedule_response(response.json())
    def get_platform_setting(
        self,
    ) -> PlatformSetting:
        """플랫폼 설정 조회

        설정 정보를 조회합니다.

        Raises:
            GetPlatformSettingError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        response = httpx.request(
            "GET",
            f"{self._base_url}/platform/setting",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": USER_AGENT,
            },
        )
        if response.status_code != 200:
            error_response = response.json()
            error = None
            try:
                error = _deserialize_forbidden_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise ForbiddenError(error)
            try:
                error = _deserialize_invalid_request_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise InvalidRequestError(error)
            try:
                error = _deserialize_platform_not_enabled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformNotEnabledError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_platform_setting(response.json())
    async def get_platform_setting_async(
        self,
    ) -> PlatformSetting:
        """플랫폼 설정 조회

        설정 정보를 조회합니다.

        Raises:
            GetPlatformSettingError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        response = await self._client.request(
            "GET",
            f"{self._base_url}/platform/setting",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": USER_AGENT,
            },
        )
        if response.status_code != 200:
            error_response = response.json()
            error = None
            try:
                error = _deserialize_forbidden_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise ForbiddenError(error)
            try:
                error = _deserialize_invalid_request_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise InvalidRequestError(error)
            try:
                error = _deserialize_platform_not_enabled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformNotEnabledError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_platform_setting(response.json())
    def update_platform_setting(
        self,
        *,
        default_withdrawal_memo: Optional[str] = None,
        default_deposit_memo: Optional[str] = None,
    ) -> UpdatePlatformSettingResponse:
        """플랫폼 설정 업데이트

        설정 정보를 업데이트합니다.

        Args:
            default_withdrawal_memo (str, optional):
                기본 보내는 이 통장 메모
            default_deposit_memo (str, optional):
                기본 받는 이 통장 메모


        Raises:
            UpdatePlatformSettingError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        if default_withdrawal_memo is not None:
            request_body["defaultWithdrawalMemo"] = default_withdrawal_memo
        if default_deposit_memo is not None:
            request_body["defaultDepositMemo"] = default_deposit_memo
        query = []
        response = httpx.request(
            "PATCH",
            f"{self._base_url}/platform/setting",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": USER_AGENT,
            },
            json=request_body,
        )
        if response.status_code != 200:
            error_response = response.json()
            error = None
            try:
                error = _deserialize_forbidden_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise ForbiddenError(error)
            try:
                error = _deserialize_invalid_request_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise InvalidRequestError(error)
            try:
                error = _deserialize_platform_not_enabled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformNotEnabledError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_update_platform_setting_response(response.json())
    async def update_platform_setting_async(
        self,
        *,
        default_withdrawal_memo: Optional[str] = None,
        default_deposit_memo: Optional[str] = None,
    ) -> UpdatePlatformSettingResponse:
        """플랫폼 설정 업데이트

        설정 정보를 업데이트합니다.

        Args:
            default_withdrawal_memo (str, optional):
                기본 보내는 이 통장 메모
            default_deposit_memo (str, optional):
                기본 받는 이 통장 메모


        Raises:
            UpdatePlatformSettingError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        if default_withdrawal_memo is not None:
            request_body["defaultWithdrawalMemo"] = default_withdrawal_memo
        if default_deposit_memo is not None:
            request_body["defaultDepositMemo"] = default_deposit_memo
        query = []
        response = await self._client.request(
            "PATCH",
            f"{self._base_url}/platform/setting",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": USER_AGENT,
            },
            json=request_body,
        )
        if response.status_code != 200:
            error_response = response.json()
            error = None
            try:
                error = _deserialize_forbidden_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise ForbiddenError(error)
            try:
                error = _deserialize_invalid_request_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise InvalidRequestError(error)
            try:
                error = _deserialize_platform_not_enabled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformNotEnabledError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_update_platform_setting_response(response.json())
