from __future__ import annotations
import httpx
import json
from httpx import AsyncClient, Client as SyncClient
from ..._user_agent import USER_AGENT
from typing import Optional
from ..errors import ForbiddenError, InvalidRequestError, PlatformAccountVerificationAlreadyUsedError, PlatformAccountVerificationFailedError, PlatformAccountVerificationNotFoundError, PlatformAdditionalFeePolicyNotFoundError, PlatformAdditionalFeePolicyScheduleAlreadyExistsError, PlatformArchivedAdditionalFeePolicyError, PlatformArchivedContractError, PlatformArchivedDiscountSharePolicyError, PlatformArchivedPartnerError, PlatformArchivedPartnersCannotBeScheduledError, PlatformCompanyVerificationAlreadyUsedError, PlatformContractNotFoundError, PlatformContractScheduleAlreadyExistsError, PlatformDiscountSharePolicyNotFoundError, PlatformDiscountSharePolicyScheduleAlreadyExistsError, PlatformInsufficientDataToChangePartnerTypeError, PlatformMemberCompanyConnectedPartnerBrnUnchangeableError, PlatformMemberCompanyConnectedPartnerCannotBeScheduledError, PlatformMemberCompanyConnectedPartnerTypeUnchangeableError, PlatformMemberCompanyConnectedPartnersCannotBeScheduledError, PlatformNotEnabledError, PlatformPartnerNotFoundError, PlatformPartnerScheduleAlreadyExistsError, PlatformPartnerSchedulesAlreadyExistError, PlatformUserDefinedPropertyNotFoundError, UnauthorizedError, UnknownError
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
from ..platform.platform_additional_fee_policy import PlatformAdditionalFeePolicy, _deserialize_platform_additional_fee_policy, _serialize_platform_additional_fee_policy
from ..platform.platform_contract import PlatformContract, _deserialize_platform_contract, _serialize_platform_contract
from ..platform.platform_discount_share_policy import PlatformDiscountSharePolicy, _deserialize_platform_discount_share_policy, _serialize_platform_discount_share_policy
from ..platform.platform_discount_share_policy_filter_options import PlatformDiscountSharePolicyFilterOptions, _deserialize_platform_discount_share_policy_filter_options, _serialize_platform_discount_share_policy_filter_options
from ..platform.platform_partner import PlatformPartner, _deserialize_platform_partner, _serialize_platform_partner
from ..platform.platform_partner_filter_input import PlatformPartnerFilterInput, _deserialize_platform_partner_filter_input, _serialize_platform_partner_filter_input
from ..platform.platform_partner_filter_options import PlatformPartnerFilterOptions, _deserialize_platform_partner_filter_options, _serialize_platform_partner_filter_options
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
from ..platform.settlement_amount_type import SettlementAmountType, _deserialize_settlement_amount_type, _serialize_settlement_amount_type
from ..platform.update_platform_additional_fee_policy_body import UpdatePlatformAdditionalFeePolicyBody, _deserialize_update_platform_additional_fee_policy_body, _serialize_update_platform_additional_fee_policy_body
from ..platform.update_platform_contract_body import UpdatePlatformContractBody, _deserialize_update_platform_contract_body, _serialize_update_platform_contract_body
from ..platform.update_platform_discount_share_policy_body import UpdatePlatformDiscountSharePolicyBody, _deserialize_update_platform_discount_share_policy_body, _serialize_update_platform_discount_share_policy_body
from ..platform.update_platform_partner_body import UpdatePlatformPartnerBody, _deserialize_update_platform_partner_body, _serialize_update_platform_partner_body
from ..platform.update_platform_setting_response import UpdatePlatformSettingResponse, _deserialize_update_platform_setting_response, _serialize_update_platform_setting_response
from urllib.parse import quote
from .company.client import CompanyClient
from .account_transfer.client import AccountTransferClient
from .policy.client import PolicyClient
from .account.client import AccountClient
from .bulk_account_transfer.client import BulkAccountTransferClient
from .bulk_payout.client import BulkPayoutClient
from .partner_settlement.client import PartnerSettlementClient
from .partner.client import PartnerClient
from .payout.client import PayoutClient
from .transfer.client import TransferClient
class PlatformClient:
    _secret: str
    _base_url: str
    _store_id: Optional[str]
    _async_client: AsyncClient
    _sync_client: SyncClient
    company: CompanyClient
    account_transfer: AccountTransferClient
    policy: PolicyClient
    account: AccountClient
    bulk_account_transfer: BulkAccountTransferClient
    bulk_payout: BulkPayoutClient
    partner_settlement: PartnerSettlementClient
    partner: PartnerClient
    payout: PayoutClient
    transfer: TransferClient

    def __init__(self, *, secret: str, base_url: str = "https://api.portone.io", store_id: Optional[str] = None):
        """
        API Secret을 사용해 포트원 API 클라이언트를 생성합니다.

        Args:
            secret (str): 포트원 API Secret입니다.
            base_url (str, optional): 포트원 REST API 주소입니다. 기본값은 `"https://api.portone.io"`입니다.
            store_id: 하위 상점에 대해 기능을 사용할 때 필요한 하위 상점의 ID입니다.
            """
        self._secret = secret
        self._base_url = base_url
        self._store_id = store_id
        self._async_client = AsyncClient(timeout=60.0)
        self._sync_client = SyncClient(timeout=60.0)
        self.company = CompanyClient(secret=secret, base_url=base_url, store_id=store_id)
        self.account_transfer = AccountTransferClient(secret=secret, base_url=base_url, store_id=store_id)
        self.policy = PolicyClient(secret=secret, base_url=base_url, store_id=store_id)
        self.account = AccountClient(secret=secret, base_url=base_url, store_id=store_id)
        self.bulk_account_transfer = BulkAccountTransferClient(secret=secret, base_url=base_url, store_id=store_id)
        self.bulk_payout = BulkPayoutClient(secret=secret, base_url=base_url, store_id=store_id)
        self.partner_settlement = PartnerSettlementClient(secret=secret, base_url=base_url, store_id=store_id)
        self.partner = PartnerClient(secret=secret, base_url=base_url, store_id=store_id)
        self.payout = PayoutClient(secret=secret, base_url=base_url, store_id=store_id)
        self.transfer = TransferClient(secret=secret, base_url=base_url, store_id=store_id)
    def get_platform_additional_fee_policy_schedule(
        self,
        *,
        id: str,
        test: Optional[bool] = None,
    ) -> PlatformAdditionalFeePolicy:
        """주어진 아이디에 대응되는 추가 수수료 정책의 예약 업데이트를 조회합니다.

        Args:
            id (str):
                추가 수수료 정책 아이디
            test (bool, optional):
                테스트 모드 여부

                테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.


        Raises:
            GetPlatformAdditionalFeePolicyScheduleError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        if test is not None:
            query.append(("test", test))
        response = self._sync_client.request(
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
        test: Optional[bool] = None,
    ) -> PlatformAdditionalFeePolicy:
        """주어진 아이디에 대응되는 추가 수수료 정책의 예약 업데이트를 조회합니다.

        Args:
            id (str):
                추가 수수료 정책 아이디
            test (bool, optional):
                테스트 모드 여부

                테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.


        Raises:
            GetPlatformAdditionalFeePolicyScheduleError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        if test is not None:
            query.append(("test", test))
        response = await self._async_client.request(
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
        test: Optional[bool] = None,
        update: UpdatePlatformAdditionalFeePolicyBody,
        applied_at: str,
    ) -> ReschedulePlatformAdditionalFeePolicyResponse:
        """Args:
            id (str):
                추가 수수료 정책 아이디
            test (bool, optional):
                테스트 모드 여부

                테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
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
        if test is not None:
            query.append(("test", test))
        response = self._sync_client.request(
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
        test: Optional[bool] = None,
        update: UpdatePlatformAdditionalFeePolicyBody,
        applied_at: str,
    ) -> ReschedulePlatformAdditionalFeePolicyResponse:
        """Args:
            id (str):
                추가 수수료 정책 아이디
            test (bool, optional):
                테스트 모드 여부

                테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
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
        if test is not None:
            query.append(("test", test))
        response = await self._async_client.request(
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
        test: Optional[bool] = None,
        update: UpdatePlatformAdditionalFeePolicyBody,
        applied_at: str,
    ) -> SchedulePlatformAdditionalFeePolicyResponse:
        """주어진 아이디에 대응되는 추가 수수료 정책에 업데이트를 예약합니다.

        Args:
            id (str):
                추가 수수료 정책 아이디
            test (bool, optional):
                테스트 모드 여부

                테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
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
        if test is not None:
            query.append(("test", test))
        response = self._sync_client.request(
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
        test: Optional[bool] = None,
        update: UpdatePlatformAdditionalFeePolicyBody,
        applied_at: str,
    ) -> SchedulePlatformAdditionalFeePolicyResponse:
        """주어진 아이디에 대응되는 추가 수수료 정책에 업데이트를 예약합니다.

        Args:
            id (str):
                추가 수수료 정책 아이디
            test (bool, optional):
                테스트 모드 여부

                테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
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
        if test is not None:
            query.append(("test", test))
        response = await self._async_client.request(
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
        test: Optional[bool] = None,
    ) -> CancelPlatformAdditionalFeePolicyScheduleResponse:
        """주어진 아이디에 대응되는 추가 수수료 정책의 예약 업데이트를 취소합니다.

        Args:
            id (str):
                추가 수수료 정책 아이디
            test (bool, optional):
                테스트 모드 여부

                테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.


        Raises:
            CancelPlatformAdditionalFeePolicyScheduleError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        if test is not None:
            query.append(("test", test))
        response = self._sync_client.request(
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
        test: Optional[bool] = None,
    ) -> CancelPlatformAdditionalFeePolicyScheduleResponse:
        """주어진 아이디에 대응되는 추가 수수료 정책의 예약 업데이트를 취소합니다.

        Args:
            id (str):
                추가 수수료 정책 아이디
            test (bool, optional):
                테스트 모드 여부

                테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.


        Raises:
            CancelPlatformAdditionalFeePolicyScheduleError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        if test is not None:
            query.append(("test", test))
        response = await self._async_client.request(
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
    def get_platform_contract_schedule(
        self,
        *,
        id: str,
        test: Optional[bool] = None,
    ) -> PlatformContract:
        """주어진 아이디에 대응되는 계약의 예약 업데이트를 조회합니다.

        Args:
            id (str):
                계약 아이디
            test (bool, optional):
                테스트 모드 여부

                테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.


        Raises:
            GetPlatformContractScheduleError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        if test is not None:
            query.append(("test", test))
        response = self._sync_client.request(
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
        test: Optional[bool] = None,
    ) -> PlatformContract:
        """주어진 아이디에 대응되는 계약의 예약 업데이트를 조회합니다.

        Args:
            id (str):
                계약 아이디
            test (bool, optional):
                테스트 모드 여부

                테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.


        Raises:
            GetPlatformContractScheduleError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        if test is not None:
            query.append(("test", test))
        response = await self._async_client.request(
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
        test: Optional[bool] = None,
        update: UpdatePlatformContractBody,
        applied_at: str,
    ) -> ReschedulePlatformContractResponse:
        """주어진 아이디에 대응되는 계약에 예약 업데이트를 재설정합니다.

        Args:
            id (str):
                계약 아이디
            test (bool, optional):
                테스트 모드 여부

                테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
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
        if test is not None:
            query.append(("test", test))
        response = self._sync_client.request(
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
        test: Optional[bool] = None,
        update: UpdatePlatformContractBody,
        applied_at: str,
    ) -> ReschedulePlatformContractResponse:
        """주어진 아이디에 대응되는 계약에 예약 업데이트를 재설정합니다.

        Args:
            id (str):
                계약 아이디
            test (bool, optional):
                테스트 모드 여부

                테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
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
        if test is not None:
            query.append(("test", test))
        response = await self._async_client.request(
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
        test: Optional[bool] = None,
        update: UpdatePlatformContractBody,
        applied_at: str,
    ) -> SchedulePlatformContractResponse:
        """주어진 아이디에 대응되는 계약에 업데이트를 예약합니다.

        Args:
            id (str):
                계약 아이디
            test (bool, optional):
                테스트 모드 여부

                테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
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
        if test is not None:
            query.append(("test", test))
        response = self._sync_client.request(
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
        test: Optional[bool] = None,
        update: UpdatePlatformContractBody,
        applied_at: str,
    ) -> SchedulePlatformContractResponse:
        """주어진 아이디에 대응되는 계약에 업데이트를 예약합니다.

        Args:
            id (str):
                계약 아이디
            test (bool, optional):
                테스트 모드 여부

                테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
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
        if test is not None:
            query.append(("test", test))
        response = await self._async_client.request(
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
        test: Optional[bool] = None,
    ) -> CancelPlatformContractScheduleResponse:
        """주어진 아이디에 대응되는 계약의 예약 업데이트를 취소합니다.

        Args:
            id (str):
                계약 아이디
            test (bool, optional):
                테스트 모드 여부

                테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.


        Raises:
            CancelPlatformContractScheduleError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        if test is not None:
            query.append(("test", test))
        response = self._sync_client.request(
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
        test: Optional[bool] = None,
    ) -> CancelPlatformContractScheduleResponse:
        """주어진 아이디에 대응되는 계약의 예약 업데이트를 취소합니다.

        Args:
            id (str):
                계약 아이디
            test (bool, optional):
                테스트 모드 여부

                테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.


        Raises:
            CancelPlatformContractScheduleError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        if test is not None:
            query.append(("test", test))
        response = await self._async_client.request(
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
    def get_platform_discount_share_policy_schedule(
        self,
        *,
        id: str,
        test: Optional[bool] = None,
    ) -> PlatformDiscountSharePolicy:
        """주어진 아이디에 대응되는 할인 분담의 예약 업데이트를 조회합니다.

        Args:
            id (str):
                할인 분담 정책 아이디
            test (bool, optional):
                테스트 모드 여부

                테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.


        Raises:
            GetPlatformDiscountSharePolicyScheduleError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        if test is not None:
            query.append(("test", test))
        response = self._sync_client.request(
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
        test: Optional[bool] = None,
    ) -> PlatformDiscountSharePolicy:
        """주어진 아이디에 대응되는 할인 분담의 예약 업데이트를 조회합니다.

        Args:
            id (str):
                할인 분담 정책 아이디
            test (bool, optional):
                테스트 모드 여부

                테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.


        Raises:
            GetPlatformDiscountSharePolicyScheduleError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        if test is not None:
            query.append(("test", test))
        response = await self._async_client.request(
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
        test: Optional[bool] = None,
        update: UpdatePlatformDiscountSharePolicyBody,
        applied_at: str,
    ) -> ReschedulePlatformDiscountSharePolicyResponse:
        """주어진 아이디에 대응되는 할인 분담에 예약 업데이트를 재설정합니다.

        Args:
            id (str):
                할인 분담 정책 아이디
            test (bool, optional):
                테스트 모드 여부

                테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
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
        if test is not None:
            query.append(("test", test))
        response = self._sync_client.request(
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
        test: Optional[bool] = None,
        update: UpdatePlatformDiscountSharePolicyBody,
        applied_at: str,
    ) -> ReschedulePlatformDiscountSharePolicyResponse:
        """주어진 아이디에 대응되는 할인 분담에 예약 업데이트를 재설정합니다.

        Args:
            id (str):
                할인 분담 정책 아이디
            test (bool, optional):
                테스트 모드 여부

                테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
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
        if test is not None:
            query.append(("test", test))
        response = await self._async_client.request(
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
        test: Optional[bool] = None,
        update: UpdatePlatformDiscountSharePolicyBody,
        applied_at: str,
    ) -> SchedulePlatformDiscountSharePolicyResponse:
        """주어진 아이디에 대응되는 할인 분담에 업데이트를 예약합니다.

        Args:
            id (str):
                할인 분담 정책 아이디
            test (bool, optional):
                테스트 모드 여부

                테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
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
        if test is not None:
            query.append(("test", test))
        response = self._sync_client.request(
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
        test: Optional[bool] = None,
        update: UpdatePlatformDiscountSharePolicyBody,
        applied_at: str,
    ) -> SchedulePlatformDiscountSharePolicyResponse:
        """주어진 아이디에 대응되는 할인 분담에 업데이트를 예약합니다.

        Args:
            id (str):
                할인 분담 정책 아이디
            test (bool, optional):
                테스트 모드 여부

                테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
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
        if test is not None:
            query.append(("test", test))
        response = await self._async_client.request(
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
        test: Optional[bool] = None,
    ) -> CancelPlatformDiscountSharePolicyScheduleResponse:
        """주어진 아이디에 대응되는 할인 분담의 예약 업데이트를 취소합니다.

        Args:
            id (str):
                할인 분담 정책 아이디
            test (bool, optional):
                테스트 모드 여부

                테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.


        Raises:
            CancelPlatformDiscountSharePolicyScheduleError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        if test is not None:
            query.append(("test", test))
        response = self._sync_client.request(
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
        test: Optional[bool] = None,
    ) -> CancelPlatformDiscountSharePolicyScheduleResponse:
        """주어진 아이디에 대응되는 할인 분담의 예약 업데이트를 취소합니다.

        Args:
            id (str):
                할인 분담 정책 아이디
            test (bool, optional):
                테스트 모드 여부

                테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.


        Raises:
            CancelPlatformDiscountSharePolicyScheduleError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        if test is not None:
            query.append(("test", test))
        response = await self._async_client.request(
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
    def get_platform_discount_share_policy_filter_options(
        self,
        *,
        test: Optional[bool] = None,
        is_archived: Optional[bool] = None,
    ) -> PlatformDiscountSharePolicyFilterOptions:
        """할인 분담 정책 다건 조회 시 필요한 필터 옵션을 조회합니다.

        Args:
            test (bool, optional):
                테스트 모드 여부

                테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
            is_archived (bool, optional):
                보관 조회 여부

                true 이면 보관된 할인 분담의 필터 옵션을 조회하고, false 이면 보관되지 않은 할인 분담의 필터 옵션을 조회합니다. 기본값은 false 입니다.


        Raises:
            GetPlatformDiscountSharePolicyFilterOptionsError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        if test is not None:
            query.append(("test", test))
        if is_archived is not None:
            query.append(("isArchived", is_archived))
        response = self._sync_client.request(
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
        test: Optional[bool] = None,
        is_archived: Optional[bool] = None,
    ) -> PlatformDiscountSharePolicyFilterOptions:
        """할인 분담 정책 다건 조회 시 필요한 필터 옵션을 조회합니다.

        Args:
            test (bool, optional):
                테스트 모드 여부

                테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
            is_archived (bool, optional):
                보관 조회 여부

                true 이면 보관된 할인 분담의 필터 옵션을 조회하고, false 이면 보관되지 않은 할인 분담의 필터 옵션을 조회합니다. 기본값은 false 입니다.


        Raises:
            GetPlatformDiscountSharePolicyFilterOptionsError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        if test is not None:
            query.append(("test", test))
        if is_archived is not None:
            query.append(("isArchived", is_archived))
        response = await self._async_client.request(
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
    def get_platform_partner_filter_options(
        self,
        *,
        test: Optional[bool] = None,
        is_archived: Optional[bool] = None,
    ) -> PlatformPartnerFilterOptions:
        """파트너 다건 조회 시 필요한 필터 옵션을 조회합니다.

        Args:
            test (bool, optional):
                테스트 모드 여부

                테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
            is_archived (bool, optional):
                보관 조회 여부

                true 이면 보관된 파트너의 필터 옵션을 조회하고, false 이면 보관되지 않은 파트너의 필터 옵션을 조회합니다. 기본값은 false 입니다.


        Raises:
            GetPlatformPartnerFilterOptionsError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        if test is not None:
            query.append(("test", test))
        if is_archived is not None:
            query.append(("isArchived", is_archived))
        response = self._sync_client.request(
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
        test: Optional[bool] = None,
        is_archived: Optional[bool] = None,
    ) -> PlatformPartnerFilterOptions:
        """파트너 다건 조회 시 필요한 필터 옵션을 조회합니다.

        Args:
            test (bool, optional):
                테스트 모드 여부

                테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
            is_archived (bool, optional):
                보관 조회 여부

                true 이면 보관된 파트너의 필터 옵션을 조회하고, false 이면 보관되지 않은 파트너의 필터 옵션을 조회합니다. 기본값은 false 입니다.


        Raises:
            GetPlatformPartnerFilterOptionsError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        if test is not None:
            query.append(("test", test))
        if is_archived is not None:
            query.append(("isArchived", is_archived))
        response = await self._async_client.request(
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
    def schedule_platform_partners(
        self,
        *,
        test: Optional[bool] = None,
        filter: Optional[PlatformPartnerFilterInput] = None,
        update: SchedulePlatformPartnersBodyUpdate,
        applied_at: str,
    ) -> SchedulePlatformPartnersResponse:
        """Args:
            test (bool, optional):
                테스트 모드 여부

                테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
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
        if test is not None:
            query.append(("test", test))
        response = self._sync_client.request(
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
        test: Optional[bool] = None,
        filter: Optional[PlatformPartnerFilterInput] = None,
        update: SchedulePlatformPartnersBodyUpdate,
        applied_at: str,
    ) -> SchedulePlatformPartnersResponse:
        """Args:
            test (bool, optional):
                테스트 모드 여부

                테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
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
        if test is not None:
            query.append(("test", test))
        response = await self._async_client.request(
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
    def get_platform_partner_schedule(
        self,
        *,
        id: str,
        test: Optional[bool] = None,
    ) -> PlatformPartner:
        """주어진 아이디에 대응되는 파트너의 예약 업데이트를 조회합니다.

        Args:
            id (str):
                파트너 아이디
            test (bool, optional):
                테스트 모드 여부

                테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.


        Raises:
            GetPlatformPartnerScheduleError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        if test is not None:
            query.append(("test", test))
        response = self._sync_client.request(
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
        test: Optional[bool] = None,
    ) -> PlatformPartner:
        """주어진 아이디에 대응되는 파트너의 예약 업데이트를 조회합니다.

        Args:
            id (str):
                파트너 아이디
            test (bool, optional):
                테스트 모드 여부

                테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.


        Raises:
            GetPlatformPartnerScheduleError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        if test is not None:
            query.append(("test", test))
        response = await self._async_client.request(
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
        test: Optional[bool] = None,
        update: UpdatePlatformPartnerBody,
        applied_at: str,
    ) -> ReschedulePlatformPartnerResponse:
        """주어진 아이디에 대응되는 파트너에 예약 업데이트를 재설정합니다.

        Args:
            id (str):
                파트너 아이디
            test (bool, optional):
                테스트 모드 여부

                테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
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
        if test is not None:
            query.append(("test", test))
        response = self._sync_client.request(
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
        test: Optional[bool] = None,
        update: UpdatePlatformPartnerBody,
        applied_at: str,
    ) -> ReschedulePlatformPartnerResponse:
        """주어진 아이디에 대응되는 파트너에 예약 업데이트를 재설정합니다.

        Args:
            id (str):
                파트너 아이디
            test (bool, optional):
                테스트 모드 여부

                테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
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
        if test is not None:
            query.append(("test", test))
        response = await self._async_client.request(
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
        test: Optional[bool] = None,
        update: UpdatePlatformPartnerBody,
        applied_at: str,
    ) -> SchedulePlatformPartnerResponse:
        """주어진 아이디에 대응되는 파트너에 업데이트를 예약합니다.

        Args:
            id (str):
                파트너 아이디
            test (bool, optional):
                테스트 모드 여부

                테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
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
        if test is not None:
            query.append(("test", test))
        response = self._sync_client.request(
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
        test: Optional[bool] = None,
        update: UpdatePlatformPartnerBody,
        applied_at: str,
    ) -> SchedulePlatformPartnerResponse:
        """주어진 아이디에 대응되는 파트너에 업데이트를 예약합니다.

        Args:
            id (str):
                파트너 아이디
            test (bool, optional):
                테스트 모드 여부

                테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
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
        if test is not None:
            query.append(("test", test))
        response = await self._async_client.request(
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
        test: Optional[bool] = None,
    ) -> CancelPlatformPartnerScheduleResponse:
        """주어진 아이디에 대응되는 파트너의 예약 업데이트를 취소합니다.

        Args:
            id (str):
                파트너 아이디
            test (bool, optional):
                테스트 모드 여부

                테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.


        Raises:
            CancelPlatformPartnerScheduleError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        if test is not None:
            query.append(("test", test))
        response = self._sync_client.request(
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
        test: Optional[bool] = None,
    ) -> CancelPlatformPartnerScheduleResponse:
        """주어진 아이디에 대응되는 파트너의 예약 업데이트를 취소합니다.

        Args:
            id (str):
                파트너 아이디
            test (bool, optional):
                테스트 모드 여부

                테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.


        Raises:
            CancelPlatformPartnerScheduleError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        if test is not None:
            query.append(("test", test))
        response = await self._async_client.request(
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
    def get_platform_setting(
        self,
        *,
        test: Optional[bool] = None,
    ) -> PlatformSetting:
        """플랫폼 설정 조회

        설정 정보를 조회합니다.

        Args:
            test (bool, optional):
                테스트 모드 여부

                테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.


        Raises:
            GetPlatformSettingError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        if test is not None:
            query.append(("test", test))
        response = self._sync_client.request(
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
        *,
        test: Optional[bool] = None,
    ) -> PlatformSetting:
        """플랫폼 설정 조회

        설정 정보를 조회합니다.

        Args:
            test (bool, optional):
                테스트 모드 여부

                테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.


        Raises:
            GetPlatformSettingError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        if test is not None:
            query.append(("test", test))
        response = await self._async_client.request(
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
        test: Optional[bool] = None,
        default_withdrawal_memo: Optional[str] = None,
        default_deposit_memo: Optional[str] = None,
        supports_multiple_order_transfers_per_partner: Optional[bool] = None,
        adjust_settlement_date_after_holiday_if_earlier: Optional[bool] = None,
        deduct_wht: Optional[bool] = None,
        settlement_amount_type: Optional[SettlementAmountType] = None,
    ) -> UpdatePlatformSettingResponse:
        """플랫폼 설정 업데이트

        설정 정보를 업데이트합니다.

        Args:
            test (bool, optional):
                테스트 모드 여부

                테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
            default_withdrawal_memo (str, optional):
                기본 보내는 이 통장 메모
            default_deposit_memo (str, optional):
                기본 받는 이 통장 메모
            supports_multiple_order_transfers_per_partner (bool, optional):
                paymentId, storeId, partnerId가 같은 주문 정산건에 대한 중복 정산 지원 여부
            adjust_settlement_date_after_holiday_if_earlier (bool, optional):
                정산일이 정산시작일보다 작거나 같을 경우 공휴일 후 영업일로 정산일 다시 계산 여부
            deduct_wht (bool, optional):
                지급 금액에서 원천징수세 차감 여부
            settlement_amount_type (SettlementAmountType, optional):
                정산 금액 취급 기준


        Raises:
            UpdatePlatformSettingError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        if default_withdrawal_memo is not None:
            request_body["defaultWithdrawalMemo"] = default_withdrawal_memo
        if default_deposit_memo is not None:
            request_body["defaultDepositMemo"] = default_deposit_memo
        if supports_multiple_order_transfers_per_partner is not None:
            request_body["supportsMultipleOrderTransfersPerPartner"] = supports_multiple_order_transfers_per_partner
        if adjust_settlement_date_after_holiday_if_earlier is not None:
            request_body["adjustSettlementDateAfterHolidayIfEarlier"] = adjust_settlement_date_after_holiday_if_earlier
        if deduct_wht is not None:
            request_body["deductWht"] = deduct_wht
        if settlement_amount_type is not None:
            request_body["settlementAmountType"] = _serialize_settlement_amount_type(settlement_amount_type)
        query = []
        if test is not None:
            query.append(("test", test))
        response = self._sync_client.request(
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
        test: Optional[bool] = None,
        default_withdrawal_memo: Optional[str] = None,
        default_deposit_memo: Optional[str] = None,
        supports_multiple_order_transfers_per_partner: Optional[bool] = None,
        adjust_settlement_date_after_holiday_if_earlier: Optional[bool] = None,
        deduct_wht: Optional[bool] = None,
        settlement_amount_type: Optional[SettlementAmountType] = None,
    ) -> UpdatePlatformSettingResponse:
        """플랫폼 설정 업데이트

        설정 정보를 업데이트합니다.

        Args:
            test (bool, optional):
                테스트 모드 여부

                테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
            default_withdrawal_memo (str, optional):
                기본 보내는 이 통장 메모
            default_deposit_memo (str, optional):
                기본 받는 이 통장 메모
            supports_multiple_order_transfers_per_partner (bool, optional):
                paymentId, storeId, partnerId가 같은 주문 정산건에 대한 중복 정산 지원 여부
            adjust_settlement_date_after_holiday_if_earlier (bool, optional):
                정산일이 정산시작일보다 작거나 같을 경우 공휴일 후 영업일로 정산일 다시 계산 여부
            deduct_wht (bool, optional):
                지급 금액에서 원천징수세 차감 여부
            settlement_amount_type (SettlementAmountType, optional):
                정산 금액 취급 기준


        Raises:
            UpdatePlatformSettingError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        if default_withdrawal_memo is not None:
            request_body["defaultWithdrawalMemo"] = default_withdrawal_memo
        if default_deposit_memo is not None:
            request_body["defaultDepositMemo"] = default_deposit_memo
        if supports_multiple_order_transfers_per_partner is not None:
            request_body["supportsMultipleOrderTransfersPerPartner"] = supports_multiple_order_transfers_per_partner
        if adjust_settlement_date_after_holiday_if_earlier is not None:
            request_body["adjustSettlementDateAfterHolidayIfEarlier"] = adjust_settlement_date_after_holiday_if_earlier
        if deduct_wht is not None:
            request_body["deductWht"] = deduct_wht
        if settlement_amount_type is not None:
            request_body["settlementAmountType"] = _serialize_settlement_amount_type(settlement_amount_type)
        query = []
        if test is not None:
            query.append(("test", test))
        response = await self._async_client.request(
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
