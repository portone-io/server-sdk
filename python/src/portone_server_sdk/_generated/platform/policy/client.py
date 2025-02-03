from __future__ import annotations
import httpx
import json
from httpx import AsyncClient
from ...._user_agent import USER_AGENT
from typing import Optional
from ...errors import ForbiddenError, InvalidRequestError, PlatformAdditionalFeePolicyAlreadyExistsError, PlatformAdditionalFeePolicyNotFoundError, PlatformArchivedAdditionalFeePolicyError, PlatformArchivedContractError, PlatformArchivedDiscountSharePolicyError, PlatformCannotArchiveScheduledAdditionalFeePolicyError, PlatformCannotArchiveScheduledContractError, PlatformCannotArchiveScheduledDiscountSharePolicyError, PlatformContractAlreadyExistsError, PlatformContractNotFoundError, PlatformDiscountSharePolicyAlreadyExistsError, PlatformDiscountSharePolicyNotFoundError, PlatformNotEnabledError, UnauthorizedError, UnknownError
from ...common.forbidden_error import _deserialize_forbidden_error
from ...common.invalid_request_error import _deserialize_invalid_request_error
from ...platform.policy.platform_additional_fee_policy_already_exists_error import _deserialize_platform_additional_fee_policy_already_exists_error
from ...platform.platform_additional_fee_policy_not_found_error import _deserialize_platform_additional_fee_policy_not_found_error
from ...platform.platform_archived_additional_fee_policy_error import _deserialize_platform_archived_additional_fee_policy_error
from ...platform.platform_archived_contract_error import _deserialize_platform_archived_contract_error
from ...platform.platform_archived_discount_share_policy_error import _deserialize_platform_archived_discount_share_policy_error
from ...platform.policy.platform_cannot_archive_scheduled_additional_fee_policy_error import _deserialize_platform_cannot_archive_scheduled_additional_fee_policy_error
from ...platform.policy.platform_cannot_archive_scheduled_contract_error import _deserialize_platform_cannot_archive_scheduled_contract_error
from ...platform.policy.platform_cannot_archive_scheduled_discount_share_policy_error import _deserialize_platform_cannot_archive_scheduled_discount_share_policy_error
from ...platform.policy.platform_contract_already_exists_error import _deserialize_platform_contract_already_exists_error
from ...platform.platform_contract_not_found_error import _deserialize_platform_contract_not_found_error
from ...platform.policy.platform_discount_share_policy_already_exists_error import _deserialize_platform_discount_share_policy_already_exists_error
from ...platform.platform_discount_share_policy_not_found_error import _deserialize_platform_discount_share_policy_not_found_error
from ...platform.platform_not_enabled_error import _deserialize_platform_not_enabled_error
from ...common.unauthorized_error import _deserialize_unauthorized_error
from ...platform.policy.archive_platform_additional_fee_policy_response import ArchivePlatformAdditionalFeePolicyResponse, _deserialize_archive_platform_additional_fee_policy_response, _serialize_archive_platform_additional_fee_policy_response
from ...platform.policy.archive_platform_contract_response import ArchivePlatformContractResponse, _deserialize_archive_platform_contract_response, _serialize_archive_platform_contract_response
from ...platform.policy.archive_platform_discount_share_policy_response import ArchivePlatformDiscountSharePolicyResponse, _deserialize_archive_platform_discount_share_policy_response, _serialize_archive_platform_discount_share_policy_response
from ...platform.policy.create_platform_additional_fee_policy_response import CreatePlatformAdditionalFeePolicyResponse, _deserialize_create_platform_additional_fee_policy_response, _serialize_create_platform_additional_fee_policy_response
from ...platform.policy.create_platform_contract_response import CreatePlatformContractResponse, _deserialize_create_platform_contract_response, _serialize_create_platform_contract_response
from ...platform.policy.create_platform_discount_share_policy_response import CreatePlatformDiscountSharePolicyResponse, _deserialize_create_platform_discount_share_policy_response, _serialize_create_platform_discount_share_policy_response
from ...platform.policy.get_platform_additional_fee_policies_response import GetPlatformAdditionalFeePoliciesResponse, _deserialize_get_platform_additional_fee_policies_response, _serialize_get_platform_additional_fee_policies_response
from ...platform.policy.get_platform_contracts_response import GetPlatformContractsResponse, _deserialize_get_platform_contracts_response, _serialize_get_platform_contracts_response
from ...platform.policy.get_platform_discount_share_policies_response import GetPlatformDiscountSharePoliciesResponse, _deserialize_get_platform_discount_share_policies_response, _serialize_get_platform_discount_share_policies_response
from ...common.page_input import PageInput, _deserialize_page_input, _serialize_page_input
from ...platform.platform_additional_fee_policy import PlatformAdditionalFeePolicy, _deserialize_platform_additional_fee_policy, _serialize_platform_additional_fee_policy
from ...platform.policy.platform_additional_fee_policy_filter_input import PlatformAdditionalFeePolicyFilterInput, _deserialize_platform_additional_fee_policy_filter_input, _serialize_platform_additional_fee_policy_filter_input
from ...platform.platform_contract import PlatformContract, _deserialize_platform_contract, _serialize_platform_contract
from ...platform.policy.platform_contract_filter_input import PlatformContractFilterInput, _deserialize_platform_contract_filter_input, _serialize_platform_contract_filter_input
from ...platform.platform_discount_share_policy import PlatformDiscountSharePolicy, _deserialize_platform_discount_share_policy, _serialize_platform_discount_share_policy
from ...platform.policy.platform_discount_share_policy_filter_input import PlatformDiscountSharePolicyFilterInput, _deserialize_platform_discount_share_policy_filter_input, _serialize_platform_discount_share_policy_filter_input
from ...platform.platform_fee_input import PlatformFeeInput, _deserialize_platform_fee_input, _serialize_platform_fee_input
from ...platform.platform_payer import PlatformPayer, _deserialize_platform_payer, _serialize_platform_payer
from ...platform.platform_settlement_cycle_input import PlatformSettlementCycleInput, _deserialize_platform_settlement_cycle_input, _serialize_platform_settlement_cycle_input
from ...platform.policy.recover_platform_additional_fee_policy_response import RecoverPlatformAdditionalFeePolicyResponse, _deserialize_recover_platform_additional_fee_policy_response, _serialize_recover_platform_additional_fee_policy_response
from ...platform.policy.recover_platform_contract_response import RecoverPlatformContractResponse, _deserialize_recover_platform_contract_response, _serialize_recover_platform_contract_response
from ...platform.policy.recover_platform_discount_share_policy_response import RecoverPlatformDiscountSharePolicyResponse, _deserialize_recover_platform_discount_share_policy_response, _serialize_recover_platform_discount_share_policy_response
from ...platform.policy.update_platform_additional_fee_policy_response import UpdatePlatformAdditionalFeePolicyResponse, _deserialize_update_platform_additional_fee_policy_response, _serialize_update_platform_additional_fee_policy_response
from ...platform.policy.update_platform_contract_response import UpdatePlatformContractResponse, _deserialize_update_platform_contract_response, _serialize_update_platform_contract_response
from ...platform.policy.update_platform_discount_share_policy_response import UpdatePlatformDiscountSharePolicyResponse, _deserialize_update_platform_discount_share_policy_response, _serialize_update_platform_discount_share_policy_response
from urllib.parse import quote
class PolicyClient:
    _secret: str
    _base_url: str
    _store_id: Optional[str]
    _client: AsyncClient

    def __init__(self, *, secret: str, base_url: str = "https://api.portone.io", store_id: Optional[str] = None):
        """API Secret을 사용해 포트원 API 클라이언트를 생성합니다."""
        self._secret = secret
        self._base_url = base_url
        self._store_id = store_id
        self._client = AsyncClient()
    def get_platform_discount_share_policies(
        self,
        *,
        page: Optional[PageInput] = None,
        filter: Optional[PlatformDiscountSharePolicyFilterInput] = None,
    ) -> GetPlatformDiscountSharePoliciesResponse:
        """할인 분담 정책 다건 조회

        여러 할인 분담을 조회합니다.

        Args:
            page (PageInput, optional):
                요청할 페이지 정보
            filter (PlatformDiscountSharePolicyFilterInput, optional):
                조회할 할인 분담 정책 조건 필터


        Raises:
            GetPlatformDiscountSharePoliciesError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        if page is not None:
            request_body["page"] = _serialize_page_input(page)
        if filter is not None:
            request_body["filter"] = _serialize_platform_discount_share_policy_filter_input(filter)
        query = []
        query.append(("requestBody", json.dumps(request_body)))
        response = httpx.request(
            "GET",
            f"{self._base_url}/platform/discount-share-policies",
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
        return _deserialize_get_platform_discount_share_policies_response(response.json())
    async def get_platform_discount_share_policies_async(
        self,
        *,
        page: Optional[PageInput] = None,
        filter: Optional[PlatformDiscountSharePolicyFilterInput] = None,
    ) -> GetPlatformDiscountSharePoliciesResponse:
        """할인 분담 정책 다건 조회

        여러 할인 분담을 조회합니다.

        Args:
            page (PageInput, optional):
                요청할 페이지 정보
            filter (PlatformDiscountSharePolicyFilterInput, optional):
                조회할 할인 분담 정책 조건 필터


        Raises:
            GetPlatformDiscountSharePoliciesError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        if page is not None:
            request_body["page"] = _serialize_page_input(page)
        if filter is not None:
            request_body["filter"] = _serialize_platform_discount_share_policy_filter_input(filter)
        query = []
        query.append(("requestBody", json.dumps(request_body)))
        response = await self._client.request(
            "GET",
            f"{self._base_url}/platform/discount-share-policies",
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
        return _deserialize_get_platform_discount_share_policies_response(response.json())
    def create_platform_discount_share_policy(
        self,
        *,
        id: Optional[str] = None,
        name: str,
        partner_share_rate: int,
        memo: Optional[str] = None,
    ) -> CreatePlatformDiscountSharePolicyResponse:
        """할인 분담 정책 생성

        새로운 할인 분담을 생성합니다.

        Args:
            id (str, optional):
                할인 분담에 부여할 고유 아이디

                명시하지 않는 경우 포트원이 임의의 아이디를 발급해드립니다.
            name (str):
                할인 분담에 부여할 이름
            partner_share_rate (int):
                파트너가 분담할 할인금액의 비율을 의미하는 밀리 퍼센트 단위 (10^-5) 의 음이 아닌 정수이며, 파트너가 부담할 금액은 `할인금액 * partnerShareRate * 10^5` 로 책정합니다.
            memo (str, optional):
                해당 할인 분담에 대한 메모 ex) 파트너 브랜드 쿠폰


        Raises:
            CreatePlatformDiscountSharePolicyError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        if id is not None:
            request_body["id"] = id
        request_body["name"] = name
        request_body["partnerShareRate"] = partner_share_rate
        if memo is not None:
            request_body["memo"] = memo
        query = []
        response = httpx.request(
            "POST",
            f"{self._base_url}/platform/discount-share-policies",
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
                error = _deserialize_platform_discount_share_policy_already_exists_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformDiscountSharePolicyAlreadyExistsError(error)
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
        return _deserialize_create_platform_discount_share_policy_response(response.json())
    async def create_platform_discount_share_policy_async(
        self,
        *,
        id: Optional[str] = None,
        name: str,
        partner_share_rate: int,
        memo: Optional[str] = None,
    ) -> CreatePlatformDiscountSharePolicyResponse:
        """할인 분담 정책 생성

        새로운 할인 분담을 생성합니다.

        Args:
            id (str, optional):
                할인 분담에 부여할 고유 아이디

                명시하지 않는 경우 포트원이 임의의 아이디를 발급해드립니다.
            name (str):
                할인 분담에 부여할 이름
            partner_share_rate (int):
                파트너가 분담할 할인금액의 비율을 의미하는 밀리 퍼센트 단위 (10^-5) 의 음이 아닌 정수이며, 파트너가 부담할 금액은 `할인금액 * partnerShareRate * 10^5` 로 책정합니다.
            memo (str, optional):
                해당 할인 분담에 대한 메모 ex) 파트너 브랜드 쿠폰


        Raises:
            CreatePlatformDiscountSharePolicyError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        if id is not None:
            request_body["id"] = id
        request_body["name"] = name
        request_body["partnerShareRate"] = partner_share_rate
        if memo is not None:
            request_body["memo"] = memo
        query = []
        response = await self._client.request(
            "POST",
            f"{self._base_url}/platform/discount-share-policies",
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
                error = _deserialize_platform_discount_share_policy_already_exists_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformDiscountSharePolicyAlreadyExistsError(error)
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
        return _deserialize_create_platform_discount_share_policy_response(response.json())
    def get_platform_discount_share_policy(
        self,
        *,
        id: str,
    ) -> PlatformDiscountSharePolicy:
        """할인 분담 정책 조회

        주어진 아이디에 대응되는 할인 분담을 조회합니다.

        Args:
            id (str):
                조회할 할인 분담 정책 아이디


        Raises:
            GetPlatformDiscountSharePolicyError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        response = httpx.request(
            "GET",
            f"{self._base_url}/platform/discount-share-policies/{quote(id, safe='')}",
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
    async def get_platform_discount_share_policy_async(
        self,
        *,
        id: str,
    ) -> PlatformDiscountSharePolicy:
        """할인 분담 정책 조회

        주어진 아이디에 대응되는 할인 분담을 조회합니다.

        Args:
            id (str):
                조회할 할인 분담 정책 아이디


        Raises:
            GetPlatformDiscountSharePolicyError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        response = await self._client.request(
            "GET",
            f"{self._base_url}/platform/discount-share-policies/{quote(id, safe='')}",
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
    def update_platform_discount_share_policy(
        self,
        *,
        id: str,
        name: Optional[str] = None,
        partner_share_rate: Optional[int] = None,
        memo: Optional[str] = None,
    ) -> UpdatePlatformDiscountSharePolicyResponse:
        """할인 분담 정책 수정

        주어진 아이디에 대응되는 할인 분담을 업데이트합니다.

        Args:
            id (str):
                업데이트할 할인 분담 정책 아이디
            name (str, optional):
                할인 분담 정책 이름
            partner_share_rate (int, optional):
                할인 분담율

                파트너가 분담할 할인금액의 비율을 의미하는 밀리 퍼센트 단위 (10^-5) 의 음이 아닌 정수이며, 파트너가 부담할 금액은 `할인금액 * partnerShareRate * 10^5` 로 책정합니다.
            memo (str, optional):
                해당 할인 분담에 대한 메모


        Raises:
            UpdatePlatformDiscountSharePolicyError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        if name is not None:
            request_body["name"] = name
        if partner_share_rate is not None:
            request_body["partnerShareRate"] = partner_share_rate
        if memo is not None:
            request_body["memo"] = memo
        query = []
        response = httpx.request(
            "PATCH",
            f"{self._base_url}/platform/discount-share-policies/{quote(id, safe='')}",
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
        return _deserialize_update_platform_discount_share_policy_response(response.json())
    async def update_platform_discount_share_policy_async(
        self,
        *,
        id: str,
        name: Optional[str] = None,
        partner_share_rate: Optional[int] = None,
        memo: Optional[str] = None,
    ) -> UpdatePlatformDiscountSharePolicyResponse:
        """할인 분담 정책 수정

        주어진 아이디에 대응되는 할인 분담을 업데이트합니다.

        Args:
            id (str):
                업데이트할 할인 분담 정책 아이디
            name (str, optional):
                할인 분담 정책 이름
            partner_share_rate (int, optional):
                할인 분담율

                파트너가 분담할 할인금액의 비율을 의미하는 밀리 퍼센트 단위 (10^-5) 의 음이 아닌 정수이며, 파트너가 부담할 금액은 `할인금액 * partnerShareRate * 10^5` 로 책정합니다.
            memo (str, optional):
                해당 할인 분담에 대한 메모


        Raises:
            UpdatePlatformDiscountSharePolicyError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        if name is not None:
            request_body["name"] = name
        if partner_share_rate is not None:
            request_body["partnerShareRate"] = partner_share_rate
        if memo is not None:
            request_body["memo"] = memo
        query = []
        response = await self._client.request(
            "PATCH",
            f"{self._base_url}/platform/discount-share-policies/{quote(id, safe='')}",
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
        return _deserialize_update_platform_discount_share_policy_response(response.json())
    def archive_platform_discount_share_policy(
        self,
        *,
        id: str,
    ) -> ArchivePlatformDiscountSharePolicyResponse:
        """할인 분담 정책 보관

        주어진 아이디에 대응되는 할인 분담을 보관합니다.

        Args:
            id (str):
                할인 분담 아이디


        Raises:
            ArchivePlatformDiscountSharePolicyError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        response = httpx.request(
            "POST",
            f"{self._base_url}/platform/discount-share-policies/{quote(id, safe='')}/archive",
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
                error = _deserialize_platform_cannot_archive_scheduled_discount_share_policy_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformCannotArchiveScheduledDiscountSharePolicyError(error)
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
        return _deserialize_archive_platform_discount_share_policy_response(response.json())
    async def archive_platform_discount_share_policy_async(
        self,
        *,
        id: str,
    ) -> ArchivePlatformDiscountSharePolicyResponse:
        """할인 분담 정책 보관

        주어진 아이디에 대응되는 할인 분담을 보관합니다.

        Args:
            id (str):
                할인 분담 아이디


        Raises:
            ArchivePlatformDiscountSharePolicyError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        response = await self._client.request(
            "POST",
            f"{self._base_url}/platform/discount-share-policies/{quote(id, safe='')}/archive",
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
                error = _deserialize_platform_cannot_archive_scheduled_discount_share_policy_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformCannotArchiveScheduledDiscountSharePolicyError(error)
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
        return _deserialize_archive_platform_discount_share_policy_response(response.json())
    def recover_platform_discount_share_policy(
        self,
        *,
        id: str,
    ) -> RecoverPlatformDiscountSharePolicyResponse:
        """할인 분담 정책 복원

        주어진 아이디에 대응되는 할인 분담을 복원합니다.

        Args:
            id (str):
                할인 분담 아이디


        Raises:
            RecoverPlatformDiscountSharePolicyError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        response = httpx.request(
            "POST",
            f"{self._base_url}/platform/discount-share-policies/{quote(id, safe='')}/recover",
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
        return _deserialize_recover_platform_discount_share_policy_response(response.json())
    async def recover_platform_discount_share_policy_async(
        self,
        *,
        id: str,
    ) -> RecoverPlatformDiscountSharePolicyResponse:
        """할인 분담 정책 복원

        주어진 아이디에 대응되는 할인 분담을 복원합니다.

        Args:
            id (str):
                할인 분담 아이디


        Raises:
            RecoverPlatformDiscountSharePolicyError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        response = await self._client.request(
            "POST",
            f"{self._base_url}/platform/discount-share-policies/{quote(id, safe='')}/recover",
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
        return _deserialize_recover_platform_discount_share_policy_response(response.json())
    def get_platform_additional_fee_policies(
        self,
        *,
        page: Optional[PageInput] = None,
        filter: Optional[PlatformAdditionalFeePolicyFilterInput] = None,
    ) -> GetPlatformAdditionalFeePoliciesResponse:
        """추가 수수료 정책 다건 조회

        여러 추가 수수료 정책을 조회합니다.

        Args:
            page (PageInput, optional):
                요청할 페이지 정보
            filter (PlatformAdditionalFeePolicyFilterInput, optional):
                조회할 추가 수수료 정책 조건 필터


        Raises:
            GetPlatformAdditionalFeePoliciesError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        if page is not None:
            request_body["page"] = _serialize_page_input(page)
        if filter is not None:
            request_body["filter"] = _serialize_platform_additional_fee_policy_filter_input(filter)
        query = []
        query.append(("requestBody", json.dumps(request_body)))
        response = httpx.request(
            "GET",
            f"{self._base_url}/platform/additional-fee-policies",
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
        return _deserialize_get_platform_additional_fee_policies_response(response.json())
    async def get_platform_additional_fee_policies_async(
        self,
        *,
        page: Optional[PageInput] = None,
        filter: Optional[PlatformAdditionalFeePolicyFilterInput] = None,
    ) -> GetPlatformAdditionalFeePoliciesResponse:
        """추가 수수료 정책 다건 조회

        여러 추가 수수료 정책을 조회합니다.

        Args:
            page (PageInput, optional):
                요청할 페이지 정보
            filter (PlatformAdditionalFeePolicyFilterInput, optional):
                조회할 추가 수수료 정책 조건 필터


        Raises:
            GetPlatformAdditionalFeePoliciesError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        if page is not None:
            request_body["page"] = _serialize_page_input(page)
        if filter is not None:
            request_body["filter"] = _serialize_platform_additional_fee_policy_filter_input(filter)
        query = []
        query.append(("requestBody", json.dumps(request_body)))
        response = await self._client.request(
            "GET",
            f"{self._base_url}/platform/additional-fee-policies",
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
        return _deserialize_get_platform_additional_fee_policies_response(response.json())
    def create_platform_additional_fee_policy(
        self,
        *,
        id: Optional[str] = None,
        name: str,
        fee: PlatformFeeInput,
        memo: Optional[str] = None,
        vat_payer: PlatformPayer,
    ) -> CreatePlatformAdditionalFeePolicyResponse:
        """추가 수수료 정책 생성

        새로운 추가 수수료 정책을 생성합니다.

        Args:
            id (str, optional):
                생성할 추가 수수료 정책 아이디

                명시하지 않으면 id 가 임의로 생성됩니다.
            name (str):
                이름
            fee (PlatformFeeInput):
                수수료 정보
            memo (str, optional):
                메모
            vat_payer (PlatformPayer):
                부가세 부담 주체


        Raises:
            CreatePlatformAdditionalFeePolicyError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        if id is not None:
            request_body["id"] = id
        request_body["name"] = name
        request_body["fee"] = _serialize_platform_fee_input(fee)
        if memo is not None:
            request_body["memo"] = memo
        request_body["vatPayer"] = _serialize_platform_payer(vat_payer)
        query = []
        response = httpx.request(
            "POST",
            f"{self._base_url}/platform/additional-fee-policies",
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
                error = _deserialize_platform_additional_fee_policy_already_exists_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformAdditionalFeePolicyAlreadyExistsError(error)
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
        return _deserialize_create_platform_additional_fee_policy_response(response.json())
    async def create_platform_additional_fee_policy_async(
        self,
        *,
        id: Optional[str] = None,
        name: str,
        fee: PlatformFeeInput,
        memo: Optional[str] = None,
        vat_payer: PlatformPayer,
    ) -> CreatePlatformAdditionalFeePolicyResponse:
        """추가 수수료 정책 생성

        새로운 추가 수수료 정책을 생성합니다.

        Args:
            id (str, optional):
                생성할 추가 수수료 정책 아이디

                명시하지 않으면 id 가 임의로 생성됩니다.
            name (str):
                이름
            fee (PlatformFeeInput):
                수수료 정보
            memo (str, optional):
                메모
            vat_payer (PlatformPayer):
                부가세 부담 주체


        Raises:
            CreatePlatformAdditionalFeePolicyError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        if id is not None:
            request_body["id"] = id
        request_body["name"] = name
        request_body["fee"] = _serialize_platform_fee_input(fee)
        if memo is not None:
            request_body["memo"] = memo
        request_body["vatPayer"] = _serialize_platform_payer(vat_payer)
        query = []
        response = await self._client.request(
            "POST",
            f"{self._base_url}/platform/additional-fee-policies",
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
                error = _deserialize_platform_additional_fee_policy_already_exists_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformAdditionalFeePolicyAlreadyExistsError(error)
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
        return _deserialize_create_platform_additional_fee_policy_response(response.json())
    def get_platform_additional_fee_policy(
        self,
        *,
        id: str,
    ) -> PlatformAdditionalFeePolicy:
        """추가 수수료 정책 조회

        주어진 아이디에 대응되는 추가 수수료 정책을 조회합니다.

        Args:
            id (str):
                조회할 추가 수수료 정책 아이디


        Raises:
            GetPlatformAdditionalFeePolicyError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        response = httpx.request(
            "GET",
            f"{self._base_url}/platform/additional-fee-policies/{quote(id, safe='')}",
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
    async def get_platform_additional_fee_policy_async(
        self,
        *,
        id: str,
    ) -> PlatformAdditionalFeePolicy:
        """추가 수수료 정책 조회

        주어진 아이디에 대응되는 추가 수수료 정책을 조회합니다.

        Args:
            id (str):
                조회할 추가 수수료 정책 아이디


        Raises:
            GetPlatformAdditionalFeePolicyError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        response = await self._client.request(
            "GET",
            f"{self._base_url}/platform/additional-fee-policies/{quote(id, safe='')}",
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
    def update_platform_additional_fee_policy(
        self,
        *,
        id: str,
        fee: Optional[PlatformFeeInput] = None,
        name: Optional[str] = None,
        memo: Optional[str] = None,
        vat_payer: Optional[PlatformPayer] = None,
    ) -> UpdatePlatformAdditionalFeePolicyResponse:
        """추가 수수료 정책 수정

        주어진 아이디에 대응되는 추가 수수료 정책을 업데이트합니다.

        Args:
            id (str):
                업데이트할 추가 수수료 정책 아이디
            fee (PlatformFeeInput, optional):
                책정 수수료
            name (str, optional):
                추가 수수료 정책 이름
            memo (str, optional):
                해당 추가 수수료 정책에 대한 메모
            vat_payer (PlatformPayer, optional):
                부가세를 부담할 주체


        Raises:
            UpdatePlatformAdditionalFeePolicyError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        if fee is not None:
            request_body["fee"] = _serialize_platform_fee_input(fee)
        if name is not None:
            request_body["name"] = name
        if memo is not None:
            request_body["memo"] = memo
        if vat_payer is not None:
            request_body["vatPayer"] = _serialize_platform_payer(vat_payer)
        query = []
        response = httpx.request(
            "PATCH",
            f"{self._base_url}/platform/additional-fee-policies/{quote(id, safe='')}",
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
        return _deserialize_update_platform_additional_fee_policy_response(response.json())
    async def update_platform_additional_fee_policy_async(
        self,
        *,
        id: str,
        fee: Optional[PlatformFeeInput] = None,
        name: Optional[str] = None,
        memo: Optional[str] = None,
        vat_payer: Optional[PlatformPayer] = None,
    ) -> UpdatePlatformAdditionalFeePolicyResponse:
        """추가 수수료 정책 수정

        주어진 아이디에 대응되는 추가 수수료 정책을 업데이트합니다.

        Args:
            id (str):
                업데이트할 추가 수수료 정책 아이디
            fee (PlatformFeeInput, optional):
                책정 수수료
            name (str, optional):
                추가 수수료 정책 이름
            memo (str, optional):
                해당 추가 수수료 정책에 대한 메모
            vat_payer (PlatformPayer, optional):
                부가세를 부담할 주체


        Raises:
            UpdatePlatformAdditionalFeePolicyError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        if fee is not None:
            request_body["fee"] = _serialize_platform_fee_input(fee)
        if name is not None:
            request_body["name"] = name
        if memo is not None:
            request_body["memo"] = memo
        if vat_payer is not None:
            request_body["vatPayer"] = _serialize_platform_payer(vat_payer)
        query = []
        response = await self._client.request(
            "PATCH",
            f"{self._base_url}/platform/additional-fee-policies/{quote(id, safe='')}",
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
        return _deserialize_update_platform_additional_fee_policy_response(response.json())
    def archive_platform_additional_fee_policy(
        self,
        *,
        id: str,
    ) -> ArchivePlatformAdditionalFeePolicyResponse:
        """추가 수수료 정책 보관

        주어진 아이디에 대응되는 추가 수수료 정책을 보관합니다.

        Args:
            id (str):
                추가 수수료 정책 아이디


        Raises:
            ArchivePlatformAdditionalFeePolicyError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        response = httpx.request(
            "POST",
            f"{self._base_url}/platform/additional-fee-policies/{quote(id, safe='')}/archive",
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
                error = _deserialize_platform_cannot_archive_scheduled_additional_fee_policy_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformCannotArchiveScheduledAdditionalFeePolicyError(error)
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
        return _deserialize_archive_platform_additional_fee_policy_response(response.json())
    async def archive_platform_additional_fee_policy_async(
        self,
        *,
        id: str,
    ) -> ArchivePlatformAdditionalFeePolicyResponse:
        """추가 수수료 정책 보관

        주어진 아이디에 대응되는 추가 수수료 정책을 보관합니다.

        Args:
            id (str):
                추가 수수료 정책 아이디


        Raises:
            ArchivePlatformAdditionalFeePolicyError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        response = await self._client.request(
            "POST",
            f"{self._base_url}/platform/additional-fee-policies/{quote(id, safe='')}/archive",
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
                error = _deserialize_platform_cannot_archive_scheduled_additional_fee_policy_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformCannotArchiveScheduledAdditionalFeePolicyError(error)
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
        return _deserialize_archive_platform_additional_fee_policy_response(response.json())
    def recover_platform_additional_fee_policy(
        self,
        *,
        id: str,
    ) -> RecoverPlatformAdditionalFeePolicyResponse:
        """추가 수수료 정책 복원

        주어진 아이디에 대응되는 추가 수수료 정책을 복원합니다.

        Args:
            id (str):
                추가 수수료 정책 아이디


        Raises:
            RecoverPlatformAdditionalFeePolicyError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        response = httpx.request(
            "POST",
            f"{self._base_url}/platform/additional-fee-policies/{quote(id, safe='')}/recover",
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
        return _deserialize_recover_platform_additional_fee_policy_response(response.json())
    async def recover_platform_additional_fee_policy_async(
        self,
        *,
        id: str,
    ) -> RecoverPlatformAdditionalFeePolicyResponse:
        """추가 수수료 정책 복원

        주어진 아이디에 대응되는 추가 수수료 정책을 복원합니다.

        Args:
            id (str):
                추가 수수료 정책 아이디


        Raises:
            RecoverPlatformAdditionalFeePolicyError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        response = await self._client.request(
            "POST",
            f"{self._base_url}/platform/additional-fee-policies/{quote(id, safe='')}/recover",
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
        return _deserialize_recover_platform_additional_fee_policy_response(response.json())
    def get_platform_contracts(
        self,
        *,
        page: Optional[PageInput] = None,
        filter: Optional[PlatformContractFilterInput] = None,
    ) -> GetPlatformContractsResponse:
        """계약 다건 조회

        여러 계약을 조회합니다.

        Args:
            page (PageInput, optional):
                요청할 페이지 정보
            filter (PlatformContractFilterInput, optional):
                조회할 계약 조건 필터


        Raises:
            GetPlatformContractsError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        if page is not None:
            request_body["page"] = _serialize_page_input(page)
        if filter is not None:
            request_body["filter"] = _serialize_platform_contract_filter_input(filter)
        query = []
        query.append(("requestBody", json.dumps(request_body)))
        response = httpx.request(
            "GET",
            f"{self._base_url}/platform/contracts",
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
        return _deserialize_get_platform_contracts_response(response.json())
    async def get_platform_contracts_async(
        self,
        *,
        page: Optional[PageInput] = None,
        filter: Optional[PlatformContractFilterInput] = None,
    ) -> GetPlatformContractsResponse:
        """계약 다건 조회

        여러 계약을 조회합니다.

        Args:
            page (PageInput, optional):
                요청할 페이지 정보
            filter (PlatformContractFilterInput, optional):
                조회할 계약 조건 필터


        Raises:
            GetPlatformContractsError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        if page is not None:
            request_body["page"] = _serialize_page_input(page)
        if filter is not None:
            request_body["filter"] = _serialize_platform_contract_filter_input(filter)
        query = []
        query.append(("requestBody", json.dumps(request_body)))
        response = await self._client.request(
            "GET",
            f"{self._base_url}/platform/contracts",
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
        return _deserialize_get_platform_contracts_response(response.json())
    def create_platform_contract(
        self,
        *,
        id: Optional[str] = None,
        name: str,
        memo: Optional[str] = None,
        platform_fee: PlatformFeeInput,
        settlement_cycle: PlatformSettlementCycleInput,
        platform_fee_vat_payer: PlatformPayer,
        subtract_payment_vat_amount: bool,
    ) -> CreatePlatformContractResponse:
        """계약 생성

        새로운 계약을 생성합니다.

        Args:
            id (str, optional):
                계약에 부여할 고유 아이디

                명시하지 않는 경우 포트원이 임의의 아이디를 발급해드립니다.
            name (str):
                계약 이름
            memo (str, optional):
                계약 내부 표기를 위한 메모
            platform_fee (PlatformFeeInput):
                중개수수료
            settlement_cycle (PlatformSettlementCycleInput):
                정산 주기
            platform_fee_vat_payer (PlatformPayer):
                중개수수료에 대한 부가세 부담 주체
            subtract_payment_vat_amount (bool):
                정산 시 결제금액 부가세 감액 여부


        Raises:
            CreatePlatformContractError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        if id is not None:
            request_body["id"] = id
        request_body["name"] = name
        if memo is not None:
            request_body["memo"] = memo
        request_body["platformFee"] = _serialize_platform_fee_input(platform_fee)
        request_body["settlementCycle"] = _serialize_platform_settlement_cycle_input(settlement_cycle)
        request_body["platformFeeVatPayer"] = _serialize_platform_payer(platform_fee_vat_payer)
        request_body["subtractPaymentVatAmount"] = subtract_payment_vat_amount
        query = []
        response = httpx.request(
            "POST",
            f"{self._base_url}/platform/contracts",
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
                error = _deserialize_platform_contract_already_exists_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformContractAlreadyExistsError(error)
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
        return _deserialize_create_platform_contract_response(response.json())
    async def create_platform_contract_async(
        self,
        *,
        id: Optional[str] = None,
        name: str,
        memo: Optional[str] = None,
        platform_fee: PlatformFeeInput,
        settlement_cycle: PlatformSettlementCycleInput,
        platform_fee_vat_payer: PlatformPayer,
        subtract_payment_vat_amount: bool,
    ) -> CreatePlatformContractResponse:
        """계약 생성

        새로운 계약을 생성합니다.

        Args:
            id (str, optional):
                계약에 부여할 고유 아이디

                명시하지 않는 경우 포트원이 임의의 아이디를 발급해드립니다.
            name (str):
                계약 이름
            memo (str, optional):
                계약 내부 표기를 위한 메모
            platform_fee (PlatformFeeInput):
                중개수수료
            settlement_cycle (PlatformSettlementCycleInput):
                정산 주기
            platform_fee_vat_payer (PlatformPayer):
                중개수수료에 대한 부가세 부담 주체
            subtract_payment_vat_amount (bool):
                정산 시 결제금액 부가세 감액 여부


        Raises:
            CreatePlatformContractError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        if id is not None:
            request_body["id"] = id
        request_body["name"] = name
        if memo is not None:
            request_body["memo"] = memo
        request_body["platformFee"] = _serialize_platform_fee_input(platform_fee)
        request_body["settlementCycle"] = _serialize_platform_settlement_cycle_input(settlement_cycle)
        request_body["platformFeeVatPayer"] = _serialize_platform_payer(platform_fee_vat_payer)
        request_body["subtractPaymentVatAmount"] = subtract_payment_vat_amount
        query = []
        response = await self._client.request(
            "POST",
            f"{self._base_url}/platform/contracts",
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
                error = _deserialize_platform_contract_already_exists_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformContractAlreadyExistsError(error)
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
        return _deserialize_create_platform_contract_response(response.json())
    def get_platform_contract(
        self,
        *,
        id: str,
    ) -> PlatformContract:
        """계약 조회

        주어진 아이디에 대응되는 계약을 조회합니다.

        Args:
            id (str):
                조회할 계약 아이디


        Raises:
            GetPlatformContractError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        response = httpx.request(
            "GET",
            f"{self._base_url}/platform/contracts/{quote(id, safe='')}",
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
    async def get_platform_contract_async(
        self,
        *,
        id: str,
    ) -> PlatformContract:
        """계약 조회

        주어진 아이디에 대응되는 계약을 조회합니다.

        Args:
            id (str):
                조회할 계약 아이디


        Raises:
            GetPlatformContractError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        response = await self._client.request(
            "GET",
            f"{self._base_url}/platform/contracts/{quote(id, safe='')}",
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
    def update_platform_contract(
        self,
        *,
        id: str,
        name: Optional[str] = None,
        memo: Optional[str] = None,
        platform_fee: Optional[PlatformFeeInput] = None,
        settlement_cycle: Optional[PlatformSettlementCycleInput] = None,
        platform_fee_vat_payer: Optional[PlatformPayer] = None,
        subtract_payment_vat_amount: Optional[bool] = None,
    ) -> UpdatePlatformContractResponse:
        """계약 수정

        주어진 아이디에 대응되는 계약을 업데이트합니다.

        Args:
            id (str):
                업데이트할 계약 아이디
            name (str, optional):
                계약 이름
            memo (str, optional):
                계약 내부 표기를 위한 메모
            platform_fee (PlatformFeeInput, optional):
                중개수수료
            settlement_cycle (PlatformSettlementCycleInput, optional):
                정산 주기
            platform_fee_vat_payer (PlatformPayer, optional):
                중개수수료에 대한 부가세 부담 주체
            subtract_payment_vat_amount (bool, optional):
                정산 시 결제금액 부가세 감액 여부


        Raises:
            UpdatePlatformContractError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        if name is not None:
            request_body["name"] = name
        if memo is not None:
            request_body["memo"] = memo
        if platform_fee is not None:
            request_body["platformFee"] = _serialize_platform_fee_input(platform_fee)
        if settlement_cycle is not None:
            request_body["settlementCycle"] = _serialize_platform_settlement_cycle_input(settlement_cycle)
        if platform_fee_vat_payer is not None:
            request_body["platformFeeVatPayer"] = _serialize_platform_payer(platform_fee_vat_payer)
        if subtract_payment_vat_amount is not None:
            request_body["subtractPaymentVatAmount"] = subtract_payment_vat_amount
        query = []
        response = httpx.request(
            "PATCH",
            f"{self._base_url}/platform/contracts/{quote(id, safe='')}",
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
        return _deserialize_update_platform_contract_response(response.json())
    async def update_platform_contract_async(
        self,
        *,
        id: str,
        name: Optional[str] = None,
        memo: Optional[str] = None,
        platform_fee: Optional[PlatformFeeInput] = None,
        settlement_cycle: Optional[PlatformSettlementCycleInput] = None,
        platform_fee_vat_payer: Optional[PlatformPayer] = None,
        subtract_payment_vat_amount: Optional[bool] = None,
    ) -> UpdatePlatformContractResponse:
        """계약 수정

        주어진 아이디에 대응되는 계약을 업데이트합니다.

        Args:
            id (str):
                업데이트할 계약 아이디
            name (str, optional):
                계약 이름
            memo (str, optional):
                계약 내부 표기를 위한 메모
            platform_fee (PlatformFeeInput, optional):
                중개수수료
            settlement_cycle (PlatformSettlementCycleInput, optional):
                정산 주기
            platform_fee_vat_payer (PlatformPayer, optional):
                중개수수료에 대한 부가세 부담 주체
            subtract_payment_vat_amount (bool, optional):
                정산 시 결제금액 부가세 감액 여부


        Raises:
            UpdatePlatformContractError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        if name is not None:
            request_body["name"] = name
        if memo is not None:
            request_body["memo"] = memo
        if platform_fee is not None:
            request_body["platformFee"] = _serialize_platform_fee_input(platform_fee)
        if settlement_cycle is not None:
            request_body["settlementCycle"] = _serialize_platform_settlement_cycle_input(settlement_cycle)
        if platform_fee_vat_payer is not None:
            request_body["platformFeeVatPayer"] = _serialize_platform_payer(platform_fee_vat_payer)
        if subtract_payment_vat_amount is not None:
            request_body["subtractPaymentVatAmount"] = subtract_payment_vat_amount
        query = []
        response = await self._client.request(
            "PATCH",
            f"{self._base_url}/platform/contracts/{quote(id, safe='')}",
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
        return _deserialize_update_platform_contract_response(response.json())
    def archive_platform_contract(
        self,
        *,
        id: str,
    ) -> ArchivePlatformContractResponse:
        """계약 보관

        주어진 아이디에 대응되는 계약을 보관합니다.

        Args:
            id (str):
                계약 아이디


        Raises:
            ArchivePlatformContractError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        response = httpx.request(
            "POST",
            f"{self._base_url}/platform/contracts/{quote(id, safe='')}/archive",
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
                error = _deserialize_platform_cannot_archive_scheduled_contract_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformCannotArchiveScheduledContractError(error)
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
        return _deserialize_archive_platform_contract_response(response.json())
    async def archive_platform_contract_async(
        self,
        *,
        id: str,
    ) -> ArchivePlatformContractResponse:
        """계약 보관

        주어진 아이디에 대응되는 계약을 보관합니다.

        Args:
            id (str):
                계약 아이디


        Raises:
            ArchivePlatformContractError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        response = await self._client.request(
            "POST",
            f"{self._base_url}/platform/contracts/{quote(id, safe='')}/archive",
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
                error = _deserialize_platform_cannot_archive_scheduled_contract_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformCannotArchiveScheduledContractError(error)
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
        return _deserialize_archive_platform_contract_response(response.json())
    def recover_platform_contract(
        self,
        *,
        id: str,
    ) -> RecoverPlatformContractResponse:
        """계약 복원

        주어진 아이디에 대응되는 계약을 복원합니다.

        Args:
            id (str):
                계약 아이디


        Raises:
            RecoverPlatformContractError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        response = httpx.request(
            "POST",
            f"{self._base_url}/platform/contracts/{quote(id, safe='')}/recover",
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
        return _deserialize_recover_platform_contract_response(response.json())
    async def recover_platform_contract_async(
        self,
        *,
        id: str,
    ) -> RecoverPlatformContractResponse:
        """계약 복원

        주어진 아이디에 대응되는 계약을 복원합니다.

        Args:
            id (str):
                계약 아이디


        Raises:
            RecoverPlatformContractError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        response = await self._client.request(
            "POST",
            f"{self._base_url}/platform/contracts/{quote(id, safe='')}/recover",
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
        return _deserialize_recover_platform_contract_response(response.json())
