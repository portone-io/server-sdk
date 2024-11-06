from __future__ import annotations
import httpx
import json
from httpx import AsyncClient
from typing import Optional
from portone_server_sdk._generated.platform.cancel_platform_additional_fee_policy_schedule_response import CancelPlatformAdditionalFeePolicyScheduleResponse, _deserialize_cancel_platform_additional_fee_policy_schedule_response, _serialize_cancel_platform_additional_fee_policy_schedule_response
from portone_server_sdk._generated.platform.cancel_platform_contract_schedule_response import CancelPlatformContractScheduleResponse, _deserialize_cancel_platform_contract_schedule_response, _serialize_cancel_platform_contract_schedule_response
from portone_server_sdk._generated.platform.cancel_platform_discount_share_policy_schedule_response import CancelPlatformDiscountSharePolicyScheduleResponse, _deserialize_cancel_platform_discount_share_policy_schedule_response, _serialize_cancel_platform_discount_share_policy_schedule_response
from portone_server_sdk._generated.platform.cancel_platform_partner_schedule_response import CancelPlatformPartnerScheduleResponse, _deserialize_cancel_platform_partner_schedule_response, _serialize_cancel_platform_partner_schedule_response
from portone_server_sdk._generated.common.forbidden_error import ForbiddenError, _deserialize_forbidden_error, _serialize_forbidden_error
from portone_server_sdk._generated.common.invalid_request_error import InvalidRequestError, _deserialize_invalid_request_error, _serialize_invalid_request_error
from portone_server_sdk._generated.platform.platform import Platform, _deserialize_platform, _serialize_platform
from portone_server_sdk._generated.platform.platform_account_verification_already_used_error import PlatformAccountVerificationAlreadyUsedError, _deserialize_platform_account_verification_already_used_error, _serialize_platform_account_verification_already_used_error
from portone_server_sdk._generated.platform.platform_account_verification_failed_error import PlatformAccountVerificationFailedError, _deserialize_platform_account_verification_failed_error, _serialize_platform_account_verification_failed_error
from portone_server_sdk._generated.platform.platform_account_verification_not_found_error import PlatformAccountVerificationNotFoundError, _deserialize_platform_account_verification_not_found_error, _serialize_platform_account_verification_not_found_error
from portone_server_sdk._generated.platform.platform_additional_fee_policy import PlatformAdditionalFeePolicy, _deserialize_platform_additional_fee_policy, _serialize_platform_additional_fee_policy
from portone_server_sdk._generated.platform.platform_additional_fee_policy_not_found_error import PlatformAdditionalFeePolicyNotFoundError, _deserialize_platform_additional_fee_policy_not_found_error, _serialize_platform_additional_fee_policy_not_found_error
from portone_server_sdk._generated.platform.platform_additional_fee_policy_schedule_already_exists_error import PlatformAdditionalFeePolicyScheduleAlreadyExistsError, _deserialize_platform_additional_fee_policy_schedule_already_exists_error, _serialize_platform_additional_fee_policy_schedule_already_exists_error
from portone_server_sdk._generated.platform.platform_archived_additional_fee_policy_error import PlatformArchivedAdditionalFeePolicyError, _deserialize_platform_archived_additional_fee_policy_error, _serialize_platform_archived_additional_fee_policy_error
from portone_server_sdk._generated.platform.platform_archived_contract_error import PlatformArchivedContractError, _deserialize_platform_archived_contract_error, _serialize_platform_archived_contract_error
from portone_server_sdk._generated.platform.platform_archived_discount_share_policy_error import PlatformArchivedDiscountSharePolicyError, _deserialize_platform_archived_discount_share_policy_error, _serialize_platform_archived_discount_share_policy_error
from portone_server_sdk._generated.platform.platform_archived_partner_error import PlatformArchivedPartnerError, _deserialize_platform_archived_partner_error, _serialize_platform_archived_partner_error
from portone_server_sdk._generated.platform.platform_archived_partners_cannot_be_scheduled_error import PlatformArchivedPartnersCannotBeScheduledError, _deserialize_platform_archived_partners_cannot_be_scheduled_error, _serialize_platform_archived_partners_cannot_be_scheduled_error
from portone_server_sdk._generated.platform.platform_contract import PlatformContract, _deserialize_platform_contract, _serialize_platform_contract
from portone_server_sdk._generated.platform.platform_contract_not_found_error import PlatformContractNotFoundError, _deserialize_platform_contract_not_found_error, _serialize_platform_contract_not_found_error
from portone_server_sdk._generated.platform.platform_contract_schedule_already_exists_error import PlatformContractScheduleAlreadyExistsError, _deserialize_platform_contract_schedule_already_exists_error, _serialize_platform_contract_schedule_already_exists_error
from portone_server_sdk._generated.platform.platform_discount_share_policy import PlatformDiscountSharePolicy, _deserialize_platform_discount_share_policy, _serialize_platform_discount_share_policy
from portone_server_sdk._generated.platform.platform_discount_share_policy_filter_options import PlatformDiscountSharePolicyFilterOptions, _deserialize_platform_discount_share_policy_filter_options, _serialize_platform_discount_share_policy_filter_options
from portone_server_sdk._generated.platform.platform_discount_share_policy_not_found_error import PlatformDiscountSharePolicyNotFoundError, _deserialize_platform_discount_share_policy_not_found_error, _serialize_platform_discount_share_policy_not_found_error
from portone_server_sdk._generated.platform.platform_discount_share_policy_schedule_already_exists_error import PlatformDiscountSharePolicyScheduleAlreadyExistsError, _deserialize_platform_discount_share_policy_schedule_already_exists_error, _serialize_platform_discount_share_policy_schedule_already_exists_error
from portone_server_sdk._generated.platform.platform_insufficient_data_to_change_partner_type_error import PlatformInsufficientDataToChangePartnerTypeError, _deserialize_platform_insufficient_data_to_change_partner_type_error, _serialize_platform_insufficient_data_to_change_partner_type_error
from portone_server_sdk._generated.platform.platform_invalid_settlement_formula_error import PlatformInvalidSettlementFormulaError, _deserialize_platform_invalid_settlement_formula_error, _serialize_platform_invalid_settlement_formula_error
from portone_server_sdk._generated.platform.platform_not_enabled_error import PlatformNotEnabledError, _deserialize_platform_not_enabled_error, _serialize_platform_not_enabled_error
from portone_server_sdk._generated.platform.platform_partner import PlatformPartner, _deserialize_platform_partner, _serialize_platform_partner
from portone_server_sdk._generated.platform.platform_partner_filter_input import PlatformPartnerFilterInput, _deserialize_platform_partner_filter_input, _serialize_platform_partner_filter_input
from portone_server_sdk._generated.platform.platform_partner_filter_options import PlatformPartnerFilterOptions, _deserialize_platform_partner_filter_options, _serialize_platform_partner_filter_options
from portone_server_sdk._generated.platform.platform_partner_not_found_error import PlatformPartnerNotFoundError, _deserialize_platform_partner_not_found_error, _serialize_platform_partner_not_found_error
from portone_server_sdk._generated.platform.platform_partner_schedule_already_exists_error import PlatformPartnerScheduleAlreadyExistsError, _deserialize_platform_partner_schedule_already_exists_error, _serialize_platform_partner_schedule_already_exists_error
from portone_server_sdk._generated.platform.platform_partner_schedules_already_exist_error import PlatformPartnerSchedulesAlreadyExistError, _deserialize_platform_partner_schedules_already_exist_error, _serialize_platform_partner_schedules_already_exist_error
from portone_server_sdk._generated.platform.platform_round_type import PlatformRoundType, _deserialize_platform_round_type, _serialize_platform_round_type
from portone_server_sdk._generated.platform.platform_user_defined_property_not_found_error import PlatformUserDefinedPropertyNotFoundError, _deserialize_platform_user_defined_property_not_found_error, _serialize_platform_user_defined_property_not_found_error
from portone_server_sdk._generated.platform.reschedule_platform_additional_fee_policy_response import ReschedulePlatformAdditionalFeePolicyResponse, _deserialize_reschedule_platform_additional_fee_policy_response, _serialize_reschedule_platform_additional_fee_policy_response
from portone_server_sdk._generated.platform.reschedule_platform_contract_response import ReschedulePlatformContractResponse, _deserialize_reschedule_platform_contract_response, _serialize_reschedule_platform_contract_response
from portone_server_sdk._generated.platform.reschedule_platform_discount_share_policy_response import ReschedulePlatformDiscountSharePolicyResponse, _deserialize_reschedule_platform_discount_share_policy_response, _serialize_reschedule_platform_discount_share_policy_response
from portone_server_sdk._generated.platform.reschedule_platform_partner_response import ReschedulePlatformPartnerResponse, _deserialize_reschedule_platform_partner_response, _serialize_reschedule_platform_partner_response
from portone_server_sdk._generated.platform.schedule_platform_additional_fee_policy_response import SchedulePlatformAdditionalFeePolicyResponse, _deserialize_schedule_platform_additional_fee_policy_response, _serialize_schedule_platform_additional_fee_policy_response
from portone_server_sdk._generated.platform.schedule_platform_contract_response import SchedulePlatformContractResponse, _deserialize_schedule_platform_contract_response, _serialize_schedule_platform_contract_response
from portone_server_sdk._generated.platform.schedule_platform_discount_share_policy_response import SchedulePlatformDiscountSharePolicyResponse, _deserialize_schedule_platform_discount_share_policy_response, _serialize_schedule_platform_discount_share_policy_response
from portone_server_sdk._generated.platform.schedule_platform_partner_response import SchedulePlatformPartnerResponse, _deserialize_schedule_platform_partner_response, _serialize_schedule_platform_partner_response
from portone_server_sdk._generated.platform.schedule_platform_partners_body_update import SchedulePlatformPartnersBodyUpdate, _deserialize_schedule_platform_partners_body_update, _serialize_schedule_platform_partners_body_update
from portone_server_sdk._generated.platform.schedule_platform_partners_response import SchedulePlatformPartnersResponse, _deserialize_schedule_platform_partners_response, _serialize_schedule_platform_partners_response
from portone_server_sdk._generated.common.unauthorized_error import UnauthorizedError, _deserialize_unauthorized_error, _serialize_unauthorized_error
from portone_server_sdk._generated.platform.update_platform_additional_fee_policy_body import UpdatePlatformAdditionalFeePolicyBody, _deserialize_update_platform_additional_fee_policy_body, _serialize_update_platform_additional_fee_policy_body
from portone_server_sdk._generated.platform.update_platform_body_settlement_formula import UpdatePlatformBodySettlementFormula, _deserialize_update_platform_body_settlement_formula, _serialize_update_platform_body_settlement_formula
from portone_server_sdk._generated.platform.update_platform_body_settlement_rule import UpdatePlatformBodySettlementRule, _deserialize_update_platform_body_settlement_rule, _serialize_update_platform_body_settlement_rule
from portone_server_sdk._generated.platform.update_platform_contract_body import UpdatePlatformContractBody, _deserialize_update_platform_contract_body, _serialize_update_platform_contract_body
from portone_server_sdk._generated.platform.update_platform_discount_share_policy_body import UpdatePlatformDiscountSharePolicyBody, _deserialize_update_platform_discount_share_policy_body, _serialize_update_platform_discount_share_policy_body
from portone_server_sdk._generated.platform.update_platform_partner_body import UpdatePlatformPartnerBody, _deserialize_update_platform_partner_body, _serialize_update_platform_partner_body
from portone_server_sdk._generated.platform.update_platform_response import UpdatePlatformResponse, _deserialize_update_platform_response, _serialize_update_platform_response
from urllib.parse import quote
from .policy import PolicyClient
from .partner import PartnerClient
from .transfer import TransferClient
from .partner_settlement import PartnerSettlementClient
from .payout import PayoutClient
from .bulk_payout import BulkPayoutClient
from .account import AccountClient
from .account_transfer import AccountTransferClient
from portone_server_sdk._generated import errors
class PlatformClient:
    _secret: str
    _user_agent: str
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
    account_transfer: AccountTransferClient

    def __init__(self, secret: str, user_agent: str, base_url: str, store_id: Optional[str]):
        self._secret = secret
        self._user_agent = user_agent
        self._base_url = base_url
        self._store_id = store_id
        self._client = AsyncClient()
        self.policy = PolicyClient(secret, user_agent, base_url, store_id)
        self.partner = PartnerClient(secret, user_agent, base_url, store_id)
        self.transfer = TransferClient(secret, user_agent, base_url, store_id)
        self.partner_settlement = PartnerSettlementClient(secret, user_agent, base_url, store_id)
        self.payout = PayoutClient(secret, user_agent, base_url, store_id)
        self.bulk_payout = BulkPayoutClient(secret, user_agent, base_url, store_id)
        self.account = AccountClient(secret, user_agent, base_url, store_id)
        self.account_transfer = AccountTransferClient(secret, user_agent, base_url, store_id)
    def get_platform(
        self,
    ) -> Platform:
        """고객사의 플랫폼 정보를 조회합니다.
        요청된 Authorization header 를 통해 자동으로 요청자의 고객사를 특정합니다.

        Raises:
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            PlatformNotEnabledError: 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
                플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        query = []
        response = httpx.request(
            "GET",
            f"{self._base_url}/platform",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": self._user_agent,
            },
        )
        if response.status_code != 200:
            error_response = response.json()
            error_type = error_response["type"]
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "PLATFORM_NOT_ENABLED":
                raise errors.PlatformNotEnabledError(_deserialize_platform_not_enabled_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_platform(response.json())
    async def get_platform_async(
        self,
    ) -> Platform:
        """고객사의 플랫폼 정보를 조회합니다.
        요청된 Authorization header 를 통해 자동으로 요청자의 고객사를 특정합니다.

        Raises:
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            PlatformNotEnabledError: 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
                플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        query = []
        response = await self._client.request(
            "GET",
            f"{self._base_url}/platform",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": self._user_agent,
            },
        )
        if response.status_code != 200:
            error_response = response.json()
            error_type = error_response["type"]
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "PLATFORM_NOT_ENABLED":
                raise errors.PlatformNotEnabledError(_deserialize_platform_not_enabled_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
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
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            PlatformInvalidSettlementFormulaError: PlatformInvalidSettlementFormulaError
            PlatformNotEnabledError: 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
                플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
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
                "User-Agent": self._user_agent,
            },
            json=request_body,
        )
        if response.status_code != 200:
            error_response = response.json()
            error_type = error_response["type"]
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "PLATFORM_INVALID_SETTLEMENT_FORMULA":
                raise errors.PlatformInvalidSettlementFormulaError(_deserialize_platform_invalid_settlement_formula_error(error_response))
            if error_type == "PLATFORM_NOT_ENABLED":
                raise errors.PlatformNotEnabledError(_deserialize_platform_not_enabled_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
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
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            PlatformInvalidSettlementFormulaError: PlatformInvalidSettlementFormulaError
            PlatformNotEnabledError: 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
                플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
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
                "User-Agent": self._user_agent,
            },
            json=request_body,
        )
        if response.status_code != 200:
            error_response = response.json()
            error_type = error_response["type"]
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "PLATFORM_INVALID_SETTLEMENT_FORMULA":
                raise errors.PlatformInvalidSettlementFormulaError(_deserialize_platform_invalid_settlement_formula_error(error_response))
            if error_type == "PLATFORM_NOT_ENABLED":
                raise errors.PlatformNotEnabledError(_deserialize_platform_not_enabled_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
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
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            PlatformNotEnabledError: 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
                플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
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
                "User-Agent": self._user_agent,
            },
        )
        if response.status_code != 200:
            error_response = response.json()
            error_type = error_response["type"]
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "PLATFORM_NOT_ENABLED":
                raise errors.PlatformNotEnabledError(_deserialize_platform_not_enabled_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
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
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            PlatformNotEnabledError: 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
                플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
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
                "User-Agent": self._user_agent,
            },
        )
        if response.status_code != 200:
            error_response = response.json()
            error_type = error_response["type"]
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "PLATFORM_NOT_ENABLED":
                raise errors.PlatformNotEnabledError(_deserialize_platform_not_enabled_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
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
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            PlatformDiscountSharePolicyNotFoundError: PlatformDiscountSharePolicyNotFoundError
            PlatformNotEnabledError: 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
                플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        query = []
        response = httpx.request(
            "GET",
            f"{self._base_url}/platform/discount-share-policies/{quote(id, safe='')}/schedule",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": self._user_agent,
            },
        )
        if response.status_code != 200:
            error_response = response.json()
            error_type = error_response["type"]
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "PLATFORM_DISCOUNT_SHARE_POLICY_NOT_FOUND":
                raise errors.PlatformDiscountSharePolicyNotFoundError(_deserialize_platform_discount_share_policy_not_found_error(error_response))
            if error_type == "PLATFORM_NOT_ENABLED":
                raise errors.PlatformNotEnabledError(_deserialize_platform_not_enabled_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
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
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            PlatformDiscountSharePolicyNotFoundError: PlatformDiscountSharePolicyNotFoundError
            PlatformNotEnabledError: 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
                플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        query = []
        response = await self._client.request(
            "GET",
            f"{self._base_url}/platform/discount-share-policies/{quote(id, safe='')}/schedule",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": self._user_agent,
            },
        )
        if response.status_code != 200:
            error_response = response.json()
            error_type = error_response["type"]
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "PLATFORM_DISCOUNT_SHARE_POLICY_NOT_FOUND":
                raise errors.PlatformDiscountSharePolicyNotFoundError(_deserialize_platform_discount_share_policy_not_found_error(error_response))
            if error_type == "PLATFORM_NOT_ENABLED":
                raise errors.PlatformNotEnabledError(_deserialize_platform_not_enabled_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
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
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            PlatformDiscountSharePolicyNotFoundError: PlatformDiscountSharePolicyNotFoundError
            PlatformNotEnabledError: 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
                플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
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
                "User-Agent": self._user_agent,
            },
            json=request_body,
        )
        if response.status_code != 200:
            error_response = response.json()
            error_type = error_response["type"]
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "PLATFORM_DISCOUNT_SHARE_POLICY_NOT_FOUND":
                raise errors.PlatformDiscountSharePolicyNotFoundError(_deserialize_platform_discount_share_policy_not_found_error(error_response))
            if error_type == "PLATFORM_NOT_ENABLED":
                raise errors.PlatformNotEnabledError(_deserialize_platform_not_enabled_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
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
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            PlatformDiscountSharePolicyNotFoundError: PlatformDiscountSharePolicyNotFoundError
            PlatformNotEnabledError: 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
                플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
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
                "User-Agent": self._user_agent,
            },
            json=request_body,
        )
        if response.status_code != 200:
            error_response = response.json()
            error_type = error_response["type"]
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "PLATFORM_DISCOUNT_SHARE_POLICY_NOT_FOUND":
                raise errors.PlatformDiscountSharePolicyNotFoundError(_deserialize_platform_discount_share_policy_not_found_error(error_response))
            if error_type == "PLATFORM_NOT_ENABLED":
                raise errors.PlatformNotEnabledError(_deserialize_platform_not_enabled_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
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
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            PlatformArchivedDiscountSharePolicyError: 보관된 할인 분담 정책을 업데이트하려고 하는 경우
                보관된 할인 분담 정책을 업데이트하려고 하는 경우
            PlatformDiscountSharePolicyNotFoundError: PlatformDiscountSharePolicyNotFoundError
            PlatformDiscountSharePolicyScheduleAlreadyExistsError: PlatformDiscountSharePolicyScheduleAlreadyExistsError
            PlatformNotEnabledError: 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
                플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
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
                "User-Agent": self._user_agent,
            },
            json=request_body,
        )
        if response.status_code != 200:
            error_response = response.json()
            error_type = error_response["type"]
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "PLATFORM_ARCHIVED_DISCOUNT_SHARE_POLICY":
                raise errors.PlatformArchivedDiscountSharePolicyError(_deserialize_platform_archived_discount_share_policy_error(error_response))
            if error_type == "PLATFORM_DISCOUNT_SHARE_POLICY_NOT_FOUND":
                raise errors.PlatformDiscountSharePolicyNotFoundError(_deserialize_platform_discount_share_policy_not_found_error(error_response))
            if error_type == "PLATFORM_DISCOUNT_SHARE_POLICY_SCHEDULE_ALREADY_EXISTS":
                raise errors.PlatformDiscountSharePolicyScheduleAlreadyExistsError(_deserialize_platform_discount_share_policy_schedule_already_exists_error(error_response))
            if error_type == "PLATFORM_NOT_ENABLED":
                raise errors.PlatformNotEnabledError(_deserialize_platform_not_enabled_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
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
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            PlatformArchivedDiscountSharePolicyError: 보관된 할인 분담 정책을 업데이트하려고 하는 경우
                보관된 할인 분담 정책을 업데이트하려고 하는 경우
            PlatformDiscountSharePolicyNotFoundError: PlatformDiscountSharePolicyNotFoundError
            PlatformDiscountSharePolicyScheduleAlreadyExistsError: PlatformDiscountSharePolicyScheduleAlreadyExistsError
            PlatformNotEnabledError: 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
                플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
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
                "User-Agent": self._user_agent,
            },
            json=request_body,
        )
        if response.status_code != 200:
            error_response = response.json()
            error_type = error_response["type"]
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "PLATFORM_ARCHIVED_DISCOUNT_SHARE_POLICY":
                raise errors.PlatformArchivedDiscountSharePolicyError(_deserialize_platform_archived_discount_share_policy_error(error_response))
            if error_type == "PLATFORM_DISCOUNT_SHARE_POLICY_NOT_FOUND":
                raise errors.PlatformDiscountSharePolicyNotFoundError(_deserialize_platform_discount_share_policy_not_found_error(error_response))
            if error_type == "PLATFORM_DISCOUNT_SHARE_POLICY_SCHEDULE_ALREADY_EXISTS":
                raise errors.PlatformDiscountSharePolicyScheduleAlreadyExistsError(_deserialize_platform_discount_share_policy_schedule_already_exists_error(error_response))
            if error_type == "PLATFORM_NOT_ENABLED":
                raise errors.PlatformNotEnabledError(_deserialize_platform_not_enabled_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
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
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            PlatformDiscountSharePolicyNotFoundError: PlatformDiscountSharePolicyNotFoundError
            PlatformNotEnabledError: 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
                플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        query = []
        response = httpx.request(
            "DELETE",
            f"{self._base_url}/platform/discount-share-policies/{quote(id, safe='')}/schedule",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": self._user_agent,
            },
        )
        if response.status_code != 200:
            error_response = response.json()
            error_type = error_response["type"]
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "PLATFORM_DISCOUNT_SHARE_POLICY_NOT_FOUND":
                raise errors.PlatformDiscountSharePolicyNotFoundError(_deserialize_platform_discount_share_policy_not_found_error(error_response))
            if error_type == "PLATFORM_NOT_ENABLED":
                raise errors.PlatformNotEnabledError(_deserialize_platform_not_enabled_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
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
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            PlatformDiscountSharePolicyNotFoundError: PlatformDiscountSharePolicyNotFoundError
            PlatformNotEnabledError: 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
                플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        query = []
        response = await self._client.request(
            "DELETE",
            f"{self._base_url}/platform/discount-share-policies/{quote(id, safe='')}/schedule",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": self._user_agent,
            },
        )
        if response.status_code != 200:
            error_response = response.json()
            error_type = error_response["type"]
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "PLATFORM_DISCOUNT_SHARE_POLICY_NOT_FOUND":
                raise errors.PlatformDiscountSharePolicyNotFoundError(_deserialize_platform_discount_share_policy_not_found_error(error_response))
            if error_type == "PLATFORM_NOT_ENABLED":
                raise errors.PlatformNotEnabledError(_deserialize_platform_not_enabled_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
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
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            PlatformAdditionalFeePolicyNotFoundError: PlatformAdditionalFeePolicyNotFoundError
            PlatformNotEnabledError: 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
                플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        query = []
        response = httpx.request(
            "GET",
            f"{self._base_url}/platform/additional-fee-policies/{quote(id, safe='')}/schedule",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": self._user_agent,
            },
        )
        if response.status_code != 200:
            error_response = response.json()
            error_type = error_response["type"]
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "PLATFORM_ADDITIONAL_FEE_POLICY_NOT_FOUND":
                raise errors.PlatformAdditionalFeePolicyNotFoundError(_deserialize_platform_additional_fee_policy_not_found_error(error_response))
            if error_type == "PLATFORM_NOT_ENABLED":
                raise errors.PlatformNotEnabledError(_deserialize_platform_not_enabled_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
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
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            PlatformAdditionalFeePolicyNotFoundError: PlatformAdditionalFeePolicyNotFoundError
            PlatformNotEnabledError: 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
                플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        query = []
        response = await self._client.request(
            "GET",
            f"{self._base_url}/platform/additional-fee-policies/{quote(id, safe='')}/schedule",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": self._user_agent,
            },
        )
        if response.status_code != 200:
            error_response = response.json()
            error_type = error_response["type"]
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "PLATFORM_ADDITIONAL_FEE_POLICY_NOT_FOUND":
                raise errors.PlatformAdditionalFeePolicyNotFoundError(_deserialize_platform_additional_fee_policy_not_found_error(error_response))
            if error_type == "PLATFORM_NOT_ENABLED":
                raise errors.PlatformNotEnabledError(_deserialize_platform_not_enabled_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
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
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            PlatformAdditionalFeePolicyNotFoundError: PlatformAdditionalFeePolicyNotFoundError
            PlatformNotEnabledError: 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
                플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
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
                "User-Agent": self._user_agent,
            },
            json=request_body,
        )
        if response.status_code != 200:
            error_response = response.json()
            error_type = error_response["type"]
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "PLATFORM_ADDITIONAL_FEE_POLICY_NOT_FOUND":
                raise errors.PlatformAdditionalFeePolicyNotFoundError(_deserialize_platform_additional_fee_policy_not_found_error(error_response))
            if error_type == "PLATFORM_NOT_ENABLED":
                raise errors.PlatformNotEnabledError(_deserialize_platform_not_enabled_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
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
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            PlatformAdditionalFeePolicyNotFoundError: PlatformAdditionalFeePolicyNotFoundError
            PlatformNotEnabledError: 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
                플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
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
                "User-Agent": self._user_agent,
            },
            json=request_body,
        )
        if response.status_code != 200:
            error_response = response.json()
            error_type = error_response["type"]
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "PLATFORM_ADDITIONAL_FEE_POLICY_NOT_FOUND":
                raise errors.PlatformAdditionalFeePolicyNotFoundError(_deserialize_platform_additional_fee_policy_not_found_error(error_response))
            if error_type == "PLATFORM_NOT_ENABLED":
                raise errors.PlatformNotEnabledError(_deserialize_platform_not_enabled_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
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
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            PlatformAdditionalFeePolicyNotFoundError: PlatformAdditionalFeePolicyNotFoundError
            PlatformAdditionalFeePolicyScheduleAlreadyExistsError: PlatformAdditionalFeePolicyScheduleAlreadyExistsError
            PlatformArchivedAdditionalFeePolicyError: 보관된 추가 수수료 정책을 업데이트하려고 하는 경우
                보관된 추가 수수료 정책을 업데이트하려고 하는 경우
            PlatformNotEnabledError: 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
                플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
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
                "User-Agent": self._user_agent,
            },
            json=request_body,
        )
        if response.status_code != 200:
            error_response = response.json()
            error_type = error_response["type"]
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "PLATFORM_ADDITIONAL_FEE_POLICY_NOT_FOUND":
                raise errors.PlatformAdditionalFeePolicyNotFoundError(_deserialize_platform_additional_fee_policy_not_found_error(error_response))
            if error_type == "PLATFORM_ADDITIONAL_FEE_POLICY_SCHEDULE_ALREADY_EXISTS":
                raise errors.PlatformAdditionalFeePolicyScheduleAlreadyExistsError(_deserialize_platform_additional_fee_policy_schedule_already_exists_error(error_response))
            if error_type == "PLATFORM_ARCHIVED_ADDITIONAL_FEE_POLICY":
                raise errors.PlatformArchivedAdditionalFeePolicyError(_deserialize_platform_archived_additional_fee_policy_error(error_response))
            if error_type == "PLATFORM_NOT_ENABLED":
                raise errors.PlatformNotEnabledError(_deserialize_platform_not_enabled_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
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
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            PlatformAdditionalFeePolicyNotFoundError: PlatformAdditionalFeePolicyNotFoundError
            PlatformAdditionalFeePolicyScheduleAlreadyExistsError: PlatformAdditionalFeePolicyScheduleAlreadyExistsError
            PlatformArchivedAdditionalFeePolicyError: 보관된 추가 수수료 정책을 업데이트하려고 하는 경우
                보관된 추가 수수료 정책을 업데이트하려고 하는 경우
            PlatformNotEnabledError: 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
                플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
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
                "User-Agent": self._user_agent,
            },
            json=request_body,
        )
        if response.status_code != 200:
            error_response = response.json()
            error_type = error_response["type"]
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "PLATFORM_ADDITIONAL_FEE_POLICY_NOT_FOUND":
                raise errors.PlatformAdditionalFeePolicyNotFoundError(_deserialize_platform_additional_fee_policy_not_found_error(error_response))
            if error_type == "PLATFORM_ADDITIONAL_FEE_POLICY_SCHEDULE_ALREADY_EXISTS":
                raise errors.PlatformAdditionalFeePolicyScheduleAlreadyExistsError(_deserialize_platform_additional_fee_policy_schedule_already_exists_error(error_response))
            if error_type == "PLATFORM_ARCHIVED_ADDITIONAL_FEE_POLICY":
                raise errors.PlatformArchivedAdditionalFeePolicyError(_deserialize_platform_archived_additional_fee_policy_error(error_response))
            if error_type == "PLATFORM_NOT_ENABLED":
                raise errors.PlatformNotEnabledError(_deserialize_platform_not_enabled_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
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
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            PlatformAdditionalFeePolicyNotFoundError: PlatformAdditionalFeePolicyNotFoundError
            PlatformNotEnabledError: 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
                플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        query = []
        response = httpx.request(
            "DELETE",
            f"{self._base_url}/platform/additional-fee-policies/{quote(id, safe='')}/schedule",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": self._user_agent,
            },
        )
        if response.status_code != 200:
            error_response = response.json()
            error_type = error_response["type"]
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "PLATFORM_ADDITIONAL_FEE_POLICY_NOT_FOUND":
                raise errors.PlatformAdditionalFeePolicyNotFoundError(_deserialize_platform_additional_fee_policy_not_found_error(error_response))
            if error_type == "PLATFORM_NOT_ENABLED":
                raise errors.PlatformNotEnabledError(_deserialize_platform_not_enabled_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
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
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            PlatformAdditionalFeePolicyNotFoundError: PlatformAdditionalFeePolicyNotFoundError
            PlatformNotEnabledError: 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
                플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        query = []
        response = await self._client.request(
            "DELETE",
            f"{self._base_url}/platform/additional-fee-policies/{quote(id, safe='')}/schedule",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": self._user_agent,
            },
        )
        if response.status_code != 200:
            error_response = response.json()
            error_type = error_response["type"]
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "PLATFORM_ADDITIONAL_FEE_POLICY_NOT_FOUND":
                raise errors.PlatformAdditionalFeePolicyNotFoundError(_deserialize_platform_additional_fee_policy_not_found_error(error_response))
            if error_type == "PLATFORM_NOT_ENABLED":
                raise errors.PlatformNotEnabledError(_deserialize_platform_not_enabled_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
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
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            PlatformNotEnabledError: 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
                플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
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
                "User-Agent": self._user_agent,
            },
        )
        if response.status_code != 200:
            error_response = response.json()
            error_type = error_response["type"]
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "PLATFORM_NOT_ENABLED":
                raise errors.PlatformNotEnabledError(_deserialize_platform_not_enabled_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
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
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            PlatformNotEnabledError: 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
                플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
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
                "User-Agent": self._user_agent,
            },
        )
        if response.status_code != 200:
            error_response = response.json()
            error_type = error_response["type"]
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "PLATFORM_NOT_ENABLED":
                raise errors.PlatformNotEnabledError(_deserialize_platform_not_enabled_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
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
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            PlatformNotEnabledError: 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
                플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
            PlatformPartnerNotFoundError: PlatformPartnerNotFoundError
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        query = []
        response = httpx.request(
            "GET",
            f"{self._base_url}/platform/partners/{quote(id, safe='')}/schedule",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": self._user_agent,
            },
        )
        if response.status_code != 200:
            error_response = response.json()
            error_type = error_response["type"]
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "PLATFORM_NOT_ENABLED":
                raise errors.PlatformNotEnabledError(_deserialize_platform_not_enabled_error(error_response))
            if error_type == "PLATFORM_PARTNER_NOT_FOUND":
                raise errors.PlatformPartnerNotFoundError(_deserialize_platform_partner_not_found_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
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
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            PlatformNotEnabledError: 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
                플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
            PlatformPartnerNotFoundError: PlatformPartnerNotFoundError
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        query = []
        response = await self._client.request(
            "GET",
            f"{self._base_url}/platform/partners/{quote(id, safe='')}/schedule",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": self._user_agent,
            },
        )
        if response.status_code != 200:
            error_response = response.json()
            error_type = error_response["type"]
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "PLATFORM_NOT_ENABLED":
                raise errors.PlatformNotEnabledError(_deserialize_platform_not_enabled_error(error_response))
            if error_type == "PLATFORM_PARTNER_NOT_FOUND":
                raise errors.PlatformPartnerNotFoundError(_deserialize_platform_partner_not_found_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
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
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            PlatformContractNotFoundError: PlatformContractNotFoundError
            PlatformNotEnabledError: 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
                플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
            PlatformPartnerNotFoundError: PlatformPartnerNotFoundError
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
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
                "User-Agent": self._user_agent,
            },
            json=request_body,
        )
        if response.status_code != 200:
            error_response = response.json()
            error_type = error_response["type"]
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "PLATFORM_CONTRACT_NOT_FOUND":
                raise errors.PlatformContractNotFoundError(_deserialize_platform_contract_not_found_error(error_response))
            if error_type == "PLATFORM_NOT_ENABLED":
                raise errors.PlatformNotEnabledError(_deserialize_platform_not_enabled_error(error_response))
            if error_type == "PLATFORM_PARTNER_NOT_FOUND":
                raise errors.PlatformPartnerNotFoundError(_deserialize_platform_partner_not_found_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
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
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            PlatformContractNotFoundError: PlatformContractNotFoundError
            PlatformNotEnabledError: 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
                플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
            PlatformPartnerNotFoundError: PlatformPartnerNotFoundError
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
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
                "User-Agent": self._user_agent,
            },
            json=request_body,
        )
        if response.status_code != 200:
            error_response = response.json()
            error_type = error_response["type"]
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "PLATFORM_CONTRACT_NOT_FOUND":
                raise errors.PlatformContractNotFoundError(_deserialize_platform_contract_not_found_error(error_response))
            if error_type == "PLATFORM_NOT_ENABLED":
                raise errors.PlatformNotEnabledError(_deserialize_platform_not_enabled_error(error_response))
            if error_type == "PLATFORM_PARTNER_NOT_FOUND":
                raise errors.PlatformPartnerNotFoundError(_deserialize_platform_partner_not_found_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
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
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            PlatformAccountVerificationAlreadyUsedError: 파트너 계좌 검증 아이디를 이미 사용한 경우
                파트너 계좌 검증 아이디를 이미 사용한 경우
            PlatformAccountVerificationFailedError: 파트너 계좌 인증이 실패한 경우
                파트너 계좌 인증이 실패한 경우
            PlatformAccountVerificationNotFoundError: 파트너 계좌 검증 아이디를 찾을 수 없는 경우
                파트너 계좌 검증 아이디를 찾을 수 없는 경우
            PlatformArchivedPartnerError: 보관된 파트너를 업데이트하려고 하는 경우
                보관된 파트너를 업데이트하려고 하는 경우
            PlatformContractNotFoundError: PlatformContractNotFoundError
            PlatformInsufficientDataToChangePartnerTypeError: 파트너 타입 수정에 필요한 데이터가 부족한 경우
                파트너 타입 수정에 필요한 데이터가 부족한 경우
            PlatformNotEnabledError: 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
                플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
            PlatformPartnerNotFoundError: PlatformPartnerNotFoundError
            PlatformPartnerScheduleAlreadyExistsError: PlatformPartnerScheduleAlreadyExistsError
            PlatformUserDefinedPropertyNotFoundError: 사용자 정의 속성이 존재 하지 않는 경우
                사용자 정의 속성이 존재 하지 않는 경우
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
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
                "User-Agent": self._user_agent,
            },
            json=request_body,
        )
        if response.status_code != 200:
            error_response = response.json()
            error_type = error_response["type"]
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "PLATFORM_ACCOUNT_VERIFICATION_ALREADY_USED":
                raise errors.PlatformAccountVerificationAlreadyUsedError(_deserialize_platform_account_verification_already_used_error(error_response))
            if error_type == "PLATFORM_ACCOUNT_VERIFICATION_FAILED":
                raise errors.PlatformAccountVerificationFailedError(_deserialize_platform_account_verification_failed_error(error_response))
            if error_type == "PLATFORM_ACCOUNT_VERIFICATION_NOT_FOUND":
                raise errors.PlatformAccountVerificationNotFoundError(_deserialize_platform_account_verification_not_found_error(error_response))
            if error_type == "PLATFORM_ARCHIVED_PARTNER":
                raise errors.PlatformArchivedPartnerError(_deserialize_platform_archived_partner_error(error_response))
            if error_type == "PLATFORM_CONTRACT_NOT_FOUND":
                raise errors.PlatformContractNotFoundError(_deserialize_platform_contract_not_found_error(error_response))
            if error_type == "PLATFORM_INSUFFICIENT_DATA_TO_CHANGE_PARTNER_TYPE":
                raise errors.PlatformInsufficientDataToChangePartnerTypeError(_deserialize_platform_insufficient_data_to_change_partner_type_error(error_response))
            if error_type == "PLATFORM_NOT_ENABLED":
                raise errors.PlatformNotEnabledError(_deserialize_platform_not_enabled_error(error_response))
            if error_type == "PLATFORM_PARTNER_NOT_FOUND":
                raise errors.PlatformPartnerNotFoundError(_deserialize_platform_partner_not_found_error(error_response))
            if error_type == "PLATFORM_PARTNER_SCHEDULE_ALREADY_EXISTS":
                raise errors.PlatformPartnerScheduleAlreadyExistsError(_deserialize_platform_partner_schedule_already_exists_error(error_response))
            if error_type == "PLATFORM_USER_DEFINED_PROPERTY_NOT_FOUND":
                raise errors.PlatformUserDefinedPropertyNotFoundError(_deserialize_platform_user_defined_property_not_found_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
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
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            PlatformAccountVerificationAlreadyUsedError: 파트너 계좌 검증 아이디를 이미 사용한 경우
                파트너 계좌 검증 아이디를 이미 사용한 경우
            PlatformAccountVerificationFailedError: 파트너 계좌 인증이 실패한 경우
                파트너 계좌 인증이 실패한 경우
            PlatformAccountVerificationNotFoundError: 파트너 계좌 검증 아이디를 찾을 수 없는 경우
                파트너 계좌 검증 아이디를 찾을 수 없는 경우
            PlatformArchivedPartnerError: 보관된 파트너를 업데이트하려고 하는 경우
                보관된 파트너를 업데이트하려고 하는 경우
            PlatformContractNotFoundError: PlatformContractNotFoundError
            PlatformInsufficientDataToChangePartnerTypeError: 파트너 타입 수정에 필요한 데이터가 부족한 경우
                파트너 타입 수정에 필요한 데이터가 부족한 경우
            PlatformNotEnabledError: 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
                플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
            PlatformPartnerNotFoundError: PlatformPartnerNotFoundError
            PlatformPartnerScheduleAlreadyExistsError: PlatformPartnerScheduleAlreadyExistsError
            PlatformUserDefinedPropertyNotFoundError: 사용자 정의 속성이 존재 하지 않는 경우
                사용자 정의 속성이 존재 하지 않는 경우
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
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
                "User-Agent": self._user_agent,
            },
            json=request_body,
        )
        if response.status_code != 200:
            error_response = response.json()
            error_type = error_response["type"]
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "PLATFORM_ACCOUNT_VERIFICATION_ALREADY_USED":
                raise errors.PlatformAccountVerificationAlreadyUsedError(_deserialize_platform_account_verification_already_used_error(error_response))
            if error_type == "PLATFORM_ACCOUNT_VERIFICATION_FAILED":
                raise errors.PlatformAccountVerificationFailedError(_deserialize_platform_account_verification_failed_error(error_response))
            if error_type == "PLATFORM_ACCOUNT_VERIFICATION_NOT_FOUND":
                raise errors.PlatformAccountVerificationNotFoundError(_deserialize_platform_account_verification_not_found_error(error_response))
            if error_type == "PLATFORM_ARCHIVED_PARTNER":
                raise errors.PlatformArchivedPartnerError(_deserialize_platform_archived_partner_error(error_response))
            if error_type == "PLATFORM_CONTRACT_NOT_FOUND":
                raise errors.PlatformContractNotFoundError(_deserialize_platform_contract_not_found_error(error_response))
            if error_type == "PLATFORM_INSUFFICIENT_DATA_TO_CHANGE_PARTNER_TYPE":
                raise errors.PlatformInsufficientDataToChangePartnerTypeError(_deserialize_platform_insufficient_data_to_change_partner_type_error(error_response))
            if error_type == "PLATFORM_NOT_ENABLED":
                raise errors.PlatformNotEnabledError(_deserialize_platform_not_enabled_error(error_response))
            if error_type == "PLATFORM_PARTNER_NOT_FOUND":
                raise errors.PlatformPartnerNotFoundError(_deserialize_platform_partner_not_found_error(error_response))
            if error_type == "PLATFORM_PARTNER_SCHEDULE_ALREADY_EXISTS":
                raise errors.PlatformPartnerScheduleAlreadyExistsError(_deserialize_platform_partner_schedule_already_exists_error(error_response))
            if error_type == "PLATFORM_USER_DEFINED_PROPERTY_NOT_FOUND":
                raise errors.PlatformUserDefinedPropertyNotFoundError(_deserialize_platform_user_defined_property_not_found_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
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
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            PlatformNotEnabledError: 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
                플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
            PlatformPartnerNotFoundError: PlatformPartnerNotFoundError
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        query = []
        response = httpx.request(
            "DELETE",
            f"{self._base_url}/platform/partners/{quote(id, safe='')}/schedule",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": self._user_agent,
            },
        )
        if response.status_code != 200:
            error_response = response.json()
            error_type = error_response["type"]
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "PLATFORM_NOT_ENABLED":
                raise errors.PlatformNotEnabledError(_deserialize_platform_not_enabled_error(error_response))
            if error_type == "PLATFORM_PARTNER_NOT_FOUND":
                raise errors.PlatformPartnerNotFoundError(_deserialize_platform_partner_not_found_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
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
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            PlatformNotEnabledError: 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
                플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
            PlatformPartnerNotFoundError: PlatformPartnerNotFoundError
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        query = []
        response = await self._client.request(
            "DELETE",
            f"{self._base_url}/platform/partners/{quote(id, safe='')}/schedule",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": self._user_agent,
            },
        )
        if response.status_code != 200:
            error_response = response.json()
            error_type = error_response["type"]
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "PLATFORM_NOT_ENABLED":
                raise errors.PlatformNotEnabledError(_deserialize_platform_not_enabled_error(error_response))
            if error_type == "PLATFORM_PARTNER_NOT_FOUND":
                raise errors.PlatformPartnerNotFoundError(_deserialize_platform_partner_not_found_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
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
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            PlatformArchivedPartnersCannotBeScheduledError: 보관된 파트너들을 예약 업데이트하려고 하는 경우
                보관된 파트너들을 예약 업데이트하려고 하는 경우
            PlatformContractNotFoundError: PlatformContractNotFoundError
            PlatformNotEnabledError: 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
                플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
            PlatformPartnerSchedulesAlreadyExistError: PlatformPartnerSchedulesAlreadyExistError
            PlatformUserDefinedPropertyNotFoundError: 사용자 정의 속성이 존재 하지 않는 경우
                사용자 정의 속성이 존재 하지 않는 경우
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
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
                "User-Agent": self._user_agent,
            },
            json=request_body,
        )
        if response.status_code != 200:
            error_response = response.json()
            error_type = error_response["type"]
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "PLATFORM_ARCHIVED_PARTNERS_CANNOT_BE_SCHEDULED":
                raise errors.PlatformArchivedPartnersCannotBeScheduledError(_deserialize_platform_archived_partners_cannot_be_scheduled_error(error_response))
            if error_type == "PLATFORM_CONTRACT_NOT_FOUND":
                raise errors.PlatformContractNotFoundError(_deserialize_platform_contract_not_found_error(error_response))
            if error_type == "PLATFORM_NOT_ENABLED":
                raise errors.PlatformNotEnabledError(_deserialize_platform_not_enabled_error(error_response))
            if error_type == "PLATFORM_PARTNER_SCHEDULES_ALREADY_EXIST":
                raise errors.PlatformPartnerSchedulesAlreadyExistError(_deserialize_platform_partner_schedules_already_exist_error(error_response))
            if error_type == "PLATFORM_USER_DEFINED_PROPERTY_NOT_FOUND":
                raise errors.PlatformUserDefinedPropertyNotFoundError(_deserialize_platform_user_defined_property_not_found_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
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
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            PlatformArchivedPartnersCannotBeScheduledError: 보관된 파트너들을 예약 업데이트하려고 하는 경우
                보관된 파트너들을 예약 업데이트하려고 하는 경우
            PlatformContractNotFoundError: PlatformContractNotFoundError
            PlatformNotEnabledError: 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
                플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
            PlatformPartnerSchedulesAlreadyExistError: PlatformPartnerSchedulesAlreadyExistError
            PlatformUserDefinedPropertyNotFoundError: 사용자 정의 속성이 존재 하지 않는 경우
                사용자 정의 속성이 존재 하지 않는 경우
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
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
                "User-Agent": self._user_agent,
            },
            json=request_body,
        )
        if response.status_code != 200:
            error_response = response.json()
            error_type = error_response["type"]
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "PLATFORM_ARCHIVED_PARTNERS_CANNOT_BE_SCHEDULED":
                raise errors.PlatformArchivedPartnersCannotBeScheduledError(_deserialize_platform_archived_partners_cannot_be_scheduled_error(error_response))
            if error_type == "PLATFORM_CONTRACT_NOT_FOUND":
                raise errors.PlatformContractNotFoundError(_deserialize_platform_contract_not_found_error(error_response))
            if error_type == "PLATFORM_NOT_ENABLED":
                raise errors.PlatformNotEnabledError(_deserialize_platform_not_enabled_error(error_response))
            if error_type == "PLATFORM_PARTNER_SCHEDULES_ALREADY_EXIST":
                raise errors.PlatformPartnerSchedulesAlreadyExistError(_deserialize_platform_partner_schedules_already_exist_error(error_response))
            if error_type == "PLATFORM_USER_DEFINED_PROPERTY_NOT_FOUND":
                raise errors.PlatformUserDefinedPropertyNotFoundError(_deserialize_platform_user_defined_property_not_found_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
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
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            PlatformContractNotFoundError: PlatformContractNotFoundError
            PlatformNotEnabledError: 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
                플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        query = []
        response = httpx.request(
            "GET",
            f"{self._base_url}/platform/contracts/{quote(id, safe='')}/schedule",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": self._user_agent,
            },
        )
        if response.status_code != 200:
            error_response = response.json()
            error_type = error_response["type"]
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "PLATFORM_CONTRACT_NOT_FOUND":
                raise errors.PlatformContractNotFoundError(_deserialize_platform_contract_not_found_error(error_response))
            if error_type == "PLATFORM_NOT_ENABLED":
                raise errors.PlatformNotEnabledError(_deserialize_platform_not_enabled_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
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
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            PlatformContractNotFoundError: PlatformContractNotFoundError
            PlatformNotEnabledError: 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
                플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        query = []
        response = await self._client.request(
            "GET",
            f"{self._base_url}/platform/contracts/{quote(id, safe='')}/schedule",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": self._user_agent,
            },
        )
        if response.status_code != 200:
            error_response = response.json()
            error_type = error_response["type"]
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "PLATFORM_CONTRACT_NOT_FOUND":
                raise errors.PlatformContractNotFoundError(_deserialize_platform_contract_not_found_error(error_response))
            if error_type == "PLATFORM_NOT_ENABLED":
                raise errors.PlatformNotEnabledError(_deserialize_platform_not_enabled_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
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
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            PlatformContractNotFoundError: PlatformContractNotFoundError
            PlatformNotEnabledError: 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
                플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
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
                "User-Agent": self._user_agent,
            },
            json=request_body,
        )
        if response.status_code != 200:
            error_response = response.json()
            error_type = error_response["type"]
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "PLATFORM_CONTRACT_NOT_FOUND":
                raise errors.PlatformContractNotFoundError(_deserialize_platform_contract_not_found_error(error_response))
            if error_type == "PLATFORM_NOT_ENABLED":
                raise errors.PlatformNotEnabledError(_deserialize_platform_not_enabled_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
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
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            PlatformContractNotFoundError: PlatformContractNotFoundError
            PlatformNotEnabledError: 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
                플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
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
                "User-Agent": self._user_agent,
            },
            json=request_body,
        )
        if response.status_code != 200:
            error_response = response.json()
            error_type = error_response["type"]
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "PLATFORM_CONTRACT_NOT_FOUND":
                raise errors.PlatformContractNotFoundError(_deserialize_platform_contract_not_found_error(error_response))
            if error_type == "PLATFORM_NOT_ENABLED":
                raise errors.PlatformNotEnabledError(_deserialize_platform_not_enabled_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
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
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            PlatformArchivedContractError: 보관된 계약을 업데이트하려고 하는 경우
                보관된 계약을 업데이트하려고 하는 경우
            PlatformContractNotFoundError: PlatformContractNotFoundError
            PlatformContractScheduleAlreadyExistsError: PlatformContractScheduleAlreadyExistsError
            PlatformNotEnabledError: 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
                플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
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
                "User-Agent": self._user_agent,
            },
            json=request_body,
        )
        if response.status_code != 200:
            error_response = response.json()
            error_type = error_response["type"]
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "PLATFORM_ARCHIVED_CONTRACT":
                raise errors.PlatformArchivedContractError(_deserialize_platform_archived_contract_error(error_response))
            if error_type == "PLATFORM_CONTRACT_NOT_FOUND":
                raise errors.PlatformContractNotFoundError(_deserialize_platform_contract_not_found_error(error_response))
            if error_type == "PLATFORM_CONTRACT_SCHEDULE_ALREADY_EXISTS":
                raise errors.PlatformContractScheduleAlreadyExistsError(_deserialize_platform_contract_schedule_already_exists_error(error_response))
            if error_type == "PLATFORM_NOT_ENABLED":
                raise errors.PlatformNotEnabledError(_deserialize_platform_not_enabled_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
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
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            PlatformArchivedContractError: 보관된 계약을 업데이트하려고 하는 경우
                보관된 계약을 업데이트하려고 하는 경우
            PlatformContractNotFoundError: PlatformContractNotFoundError
            PlatformContractScheduleAlreadyExistsError: PlatformContractScheduleAlreadyExistsError
            PlatformNotEnabledError: 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
                플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
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
                "User-Agent": self._user_agent,
            },
            json=request_body,
        )
        if response.status_code != 200:
            error_response = response.json()
            error_type = error_response["type"]
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "PLATFORM_ARCHIVED_CONTRACT":
                raise errors.PlatformArchivedContractError(_deserialize_platform_archived_contract_error(error_response))
            if error_type == "PLATFORM_CONTRACT_NOT_FOUND":
                raise errors.PlatformContractNotFoundError(_deserialize_platform_contract_not_found_error(error_response))
            if error_type == "PLATFORM_CONTRACT_SCHEDULE_ALREADY_EXISTS":
                raise errors.PlatformContractScheduleAlreadyExistsError(_deserialize_platform_contract_schedule_already_exists_error(error_response))
            if error_type == "PLATFORM_NOT_ENABLED":
                raise errors.PlatformNotEnabledError(_deserialize_platform_not_enabled_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
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
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            PlatformContractNotFoundError: PlatformContractNotFoundError
            PlatformNotEnabledError: 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
                플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        query = []
        response = httpx.request(
            "DELETE",
            f"{self._base_url}/platform/contracts/{quote(id, safe='')}/schedule",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": self._user_agent,
            },
        )
        if response.status_code != 200:
            error_response = response.json()
            error_type = error_response["type"]
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "PLATFORM_CONTRACT_NOT_FOUND":
                raise errors.PlatformContractNotFoundError(_deserialize_platform_contract_not_found_error(error_response))
            if error_type == "PLATFORM_NOT_ENABLED":
                raise errors.PlatformNotEnabledError(_deserialize_platform_not_enabled_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
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
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            PlatformContractNotFoundError: PlatformContractNotFoundError
            PlatformNotEnabledError: 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
                플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        query = []
        response = await self._client.request(
            "DELETE",
            f"{self._base_url}/platform/contracts/{quote(id, safe='')}/schedule",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": self._user_agent,
            },
        )
        if response.status_code != 200:
            error_response = response.json()
            error_type = error_response["type"]
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "PLATFORM_CONTRACT_NOT_FOUND":
                raise errors.PlatformContractNotFoundError(_deserialize_platform_contract_not_found_error(error_response))
            if error_type == "PLATFORM_NOT_ENABLED":
                raise errors.PlatformNotEnabledError(_deserialize_platform_not_enabled_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_cancel_platform_contract_schedule_response(response.json())
