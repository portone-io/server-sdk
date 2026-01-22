package io.portone.sdk.server.platform

import io.ktor.client.HttpClient
import io.ktor.client.call.body
import io.ktor.client.engine.okhttp.OkHttp
import io.ktor.client.plugins.HttpTimeout
import io.ktor.client.request.`get`
import io.ktor.client.request.accept
import io.ktor.client.request.delete
import io.ktor.client.request.headers
import io.ktor.client.request.patch
import io.ktor.client.request.post
import io.ktor.client.request.put
import io.ktor.client.request.setBody
import io.ktor.http.ContentType
import io.ktor.http.HttpHeaders
import io.ktor.http.appendPathSegments
import io.ktor.http.contentType
import io.ktor.http.userAgent
import io.portone.sdk.server.USER_AGENT
import io.portone.sdk.server.annotations.PortOneUnstable
import io.portone.sdk.server.errors.CancelPlatformAdditionalFeePolicyScheduleError
import io.portone.sdk.server.errors.CancelPlatformAdditionalFeePolicyScheduleException
import io.portone.sdk.server.errors.CancelPlatformContractScheduleError
import io.portone.sdk.server.errors.CancelPlatformContractScheduleException
import io.portone.sdk.server.errors.CancelPlatformDiscountSharePolicyScheduleError
import io.portone.sdk.server.errors.CancelPlatformDiscountSharePolicyScheduleException
import io.portone.sdk.server.errors.CancelPlatformPartnerScheduleError
import io.portone.sdk.server.errors.CancelPlatformPartnerScheduleException
import io.portone.sdk.server.errors.ForbiddenError
import io.portone.sdk.server.errors.ForbiddenException
import io.portone.sdk.server.errors.GetPlatformAdditionalFeePolicyScheduleError
import io.portone.sdk.server.errors.GetPlatformAdditionalFeePolicyScheduleException
import io.portone.sdk.server.errors.GetPlatformContractScheduleError
import io.portone.sdk.server.errors.GetPlatformContractScheduleException
import io.portone.sdk.server.errors.GetPlatformDiscountSharePolicyFilterOptionsError
import io.portone.sdk.server.errors.GetPlatformDiscountSharePolicyFilterOptionsException
import io.portone.sdk.server.errors.GetPlatformDiscountSharePolicyScheduleError
import io.portone.sdk.server.errors.GetPlatformDiscountSharePolicyScheduleException
import io.portone.sdk.server.errors.GetPlatformPartnerFilterOptionsError
import io.portone.sdk.server.errors.GetPlatformPartnerFilterOptionsException
import io.portone.sdk.server.errors.GetPlatformPartnerScheduleError
import io.portone.sdk.server.errors.GetPlatformPartnerScheduleException
import io.portone.sdk.server.errors.GetPlatformSettingError
import io.portone.sdk.server.errors.GetPlatformSettingException
import io.portone.sdk.server.errors.InvalidRequestError
import io.portone.sdk.server.errors.InvalidRequestException
import io.portone.sdk.server.errors.PlatformAccountVerificationAlreadyUsedError
import io.portone.sdk.server.errors.PlatformAccountVerificationAlreadyUsedException
import io.portone.sdk.server.errors.PlatformAccountVerificationFailedError
import io.portone.sdk.server.errors.PlatformAccountVerificationFailedException
import io.portone.sdk.server.errors.PlatformAccountVerificationNotFoundError
import io.portone.sdk.server.errors.PlatformAccountVerificationNotFoundException
import io.portone.sdk.server.errors.PlatformAdditionalFeePolicyNotFoundError
import io.portone.sdk.server.errors.PlatformAdditionalFeePolicyNotFoundException
import io.portone.sdk.server.errors.PlatformAdditionalFeePolicyScheduleAlreadyExistsError
import io.portone.sdk.server.errors.PlatformAdditionalFeePolicyScheduleAlreadyExistsException
import io.portone.sdk.server.errors.PlatformArchivedAdditionalFeePolicyError
import io.portone.sdk.server.errors.PlatformArchivedAdditionalFeePolicyException
import io.portone.sdk.server.errors.PlatformArchivedContractError
import io.portone.sdk.server.errors.PlatformArchivedContractException
import io.portone.sdk.server.errors.PlatformArchivedDiscountSharePolicyError
import io.portone.sdk.server.errors.PlatformArchivedDiscountSharePolicyException
import io.portone.sdk.server.errors.PlatformArchivedPartnerError
import io.portone.sdk.server.errors.PlatformArchivedPartnerException
import io.portone.sdk.server.errors.PlatformArchivedPartnersCannotBeScheduledError
import io.portone.sdk.server.errors.PlatformArchivedPartnersCannotBeScheduledException
import io.portone.sdk.server.errors.PlatformCompanyVerificationAlreadyUsedError
import io.portone.sdk.server.errors.PlatformCompanyVerificationAlreadyUsedException
import io.portone.sdk.server.errors.PlatformContractNotFoundError
import io.portone.sdk.server.errors.PlatformContractNotFoundException
import io.portone.sdk.server.errors.PlatformContractScheduleAlreadyExistsError
import io.portone.sdk.server.errors.PlatformContractScheduleAlreadyExistsException
import io.portone.sdk.server.errors.PlatformDiscountSharePolicyNotFoundError
import io.portone.sdk.server.errors.PlatformDiscountSharePolicyNotFoundException
import io.portone.sdk.server.errors.PlatformDiscountSharePolicyScheduleAlreadyExistsError
import io.portone.sdk.server.errors.PlatformDiscountSharePolicyScheduleAlreadyExistsException
import io.portone.sdk.server.errors.PlatformInsufficientDataToChangePartnerTypeError
import io.portone.sdk.server.errors.PlatformInsufficientDataToChangePartnerTypeException
import io.portone.sdk.server.errors.PlatformMemberCompanyConnectedPartnerBrnUnchangeableError
import io.portone.sdk.server.errors.PlatformMemberCompanyConnectedPartnerBrnUnchangeableException
import io.portone.sdk.server.errors.PlatformMemberCompanyConnectedPartnerCannotBeScheduledError
import io.portone.sdk.server.errors.PlatformMemberCompanyConnectedPartnerCannotBeScheduledException
import io.portone.sdk.server.errors.PlatformMemberCompanyConnectedPartnerTypeUnchangeableError
import io.portone.sdk.server.errors.PlatformMemberCompanyConnectedPartnerTypeUnchangeableException
import io.portone.sdk.server.errors.PlatformMemberCompanyConnectedPartnersCannotBeScheduledError
import io.portone.sdk.server.errors.PlatformMemberCompanyConnectedPartnersCannotBeScheduledException
import io.portone.sdk.server.errors.PlatformNotEnabledError
import io.portone.sdk.server.errors.PlatformNotEnabledException
import io.portone.sdk.server.errors.PlatformPartnerNotFoundError
import io.portone.sdk.server.errors.PlatformPartnerNotFoundException
import io.portone.sdk.server.errors.PlatformPartnerScheduleAlreadyExistsError
import io.portone.sdk.server.errors.PlatformPartnerScheduleAlreadyExistsException
import io.portone.sdk.server.errors.PlatformPartnerSchedulesAlreadyExistError
import io.portone.sdk.server.errors.PlatformPartnerSchedulesAlreadyExistException
import io.portone.sdk.server.errors.PlatformUserDefinedPropertyNotFoundError
import io.portone.sdk.server.errors.PlatformUserDefinedPropertyNotFoundException
import io.portone.sdk.server.errors.RescheduleAdditionalFeePolicyError
import io.portone.sdk.server.errors.RescheduleAdditionalFeePolicyException
import io.portone.sdk.server.errors.RescheduleContractError
import io.portone.sdk.server.errors.RescheduleContractException
import io.portone.sdk.server.errors.RescheduleDiscountSharePolicyError
import io.portone.sdk.server.errors.RescheduleDiscountSharePolicyException
import io.portone.sdk.server.errors.ReschedulePartnerError
import io.portone.sdk.server.errors.ReschedulePartnerException
import io.portone.sdk.server.errors.ScheduleAdditionalFeePolicyError
import io.portone.sdk.server.errors.ScheduleAdditionalFeePolicyException
import io.portone.sdk.server.errors.ScheduleContractError
import io.portone.sdk.server.errors.ScheduleContractException
import io.portone.sdk.server.errors.ScheduleDiscountSharePolicyError
import io.portone.sdk.server.errors.ScheduleDiscountSharePolicyException
import io.portone.sdk.server.errors.SchedulePartnerError
import io.portone.sdk.server.errors.SchedulePartnerException
import io.portone.sdk.server.errors.SchedulePlatformPartnersError
import io.portone.sdk.server.errors.SchedulePlatformPartnersException
import io.portone.sdk.server.errors.UnauthorizedError
import io.portone.sdk.server.errors.UnauthorizedException
import io.portone.sdk.server.errors.UnknownException
import io.portone.sdk.server.errors.UpdatePlatformSettingError
import io.portone.sdk.server.errors.UpdatePlatformSettingException
import io.portone.sdk.server.platform.CancelPlatformAdditionalFeePolicyScheduleResponse
import io.portone.sdk.server.platform.CancelPlatformContractScheduleResponse
import io.portone.sdk.server.platform.CancelPlatformDiscountSharePolicyScheduleResponse
import io.portone.sdk.server.platform.CancelPlatformPartnerScheduleResponse
import io.portone.sdk.server.platform.PlatformAdditionalFeePolicy
import io.portone.sdk.server.platform.PlatformContract
import io.portone.sdk.server.platform.PlatformDiscountSharePolicy
import io.portone.sdk.server.platform.PlatformDiscountSharePolicyFilterOptions
import io.portone.sdk.server.platform.PlatformPartner
import io.portone.sdk.server.platform.PlatformPartnerFilterInput
import io.portone.sdk.server.platform.PlatformPartnerFilterOptions
import io.portone.sdk.server.platform.PlatformSetting
import io.portone.sdk.server.platform.ReschedulePlatformAdditionalFeePolicyBody
import io.portone.sdk.server.platform.ReschedulePlatformAdditionalFeePolicyResponse
import io.portone.sdk.server.platform.ReschedulePlatformContractBody
import io.portone.sdk.server.platform.ReschedulePlatformContractResponse
import io.portone.sdk.server.platform.ReschedulePlatformDiscountSharePolicyBody
import io.portone.sdk.server.platform.ReschedulePlatformDiscountSharePolicyResponse
import io.portone.sdk.server.platform.ReschedulePlatformPartnerBody
import io.portone.sdk.server.platform.ReschedulePlatformPartnerResponse
import io.portone.sdk.server.platform.SchedulePlatformAdditionalFeePolicyBody
import io.portone.sdk.server.platform.SchedulePlatformAdditionalFeePolicyResponse
import io.portone.sdk.server.platform.SchedulePlatformContractBody
import io.portone.sdk.server.platform.SchedulePlatformContractResponse
import io.portone.sdk.server.platform.SchedulePlatformDiscountSharePolicyBody
import io.portone.sdk.server.platform.SchedulePlatformDiscountSharePolicyResponse
import io.portone.sdk.server.platform.SchedulePlatformPartnerBody
import io.portone.sdk.server.platform.SchedulePlatformPartnerResponse
import io.portone.sdk.server.platform.SchedulePlatformPartnersBody
import io.portone.sdk.server.platform.SchedulePlatformPartnersBodyUpdate
import io.portone.sdk.server.platform.SchedulePlatformPartnersResponse
import io.portone.sdk.server.platform.SettlementAmountType
import io.portone.sdk.server.platform.UpdatePlatformAdditionalFeePolicyBody
import io.portone.sdk.server.platform.UpdatePlatformContractBody
import io.portone.sdk.server.platform.UpdatePlatformDiscountSharePolicyBody
import io.portone.sdk.server.platform.UpdatePlatformPartnerBody
import io.portone.sdk.server.platform.UpdatePlatformSettingBody
import io.portone.sdk.server.platform.UpdatePlatformSettingResponse
import io.portone.sdk.server.platform.account.AccountClient
import io.portone.sdk.server.platform.accounttransfer.AccountTransferClient
import io.portone.sdk.server.platform.bulkaccounttransfer.BulkAccountTransferClient
import io.portone.sdk.server.platform.bulkpayout.BulkPayoutClient
import io.portone.sdk.server.platform.company.CompanyClient
import io.portone.sdk.server.platform.partner.PartnerClient
import io.portone.sdk.server.platform.partnersettlement.PartnerSettlementClient
import io.portone.sdk.server.platform.payout.PayoutClient
import io.portone.sdk.server.platform.policy.PolicyClient
import io.portone.sdk.server.platform.transfer.TransferClient
import java.io.Closeable
import java.time.Instant
import java.util.concurrent.CompletableFuture
import kotlin.String
import kotlinx.coroutines.GlobalScope
import kotlinx.coroutines.future.future
import kotlinx.serialization.encodeToString
import kotlinx.serialization.json.Json

/**
 * API Secret을 사용해 포트원 API 클라이언트를 생성합니다.
 *
 * @param apiSecret 포트원 API Secret입니다.
 * @param apiBase 포트원 REST API 주소입니다. 기본값은 `"https://api.portone.io"`입니다.
 * @param storeId 하위 상점에 대해 기능을 사용할 때 필요한 하위 상점의 ID입니다.
 */
public class PlatformClient(
  private val apiSecret: String,
  private val apiBase: String = "https://api.portone.io",
  private val storeId: String? = null,
): Closeable {
  private val client: HttpClient = HttpClient(OkHttp) {
    install(HttpTimeout) {
      requestTimeoutMillis = 60_000
      connectTimeoutMillis = 60_000
      socketTimeoutMillis = 60_000
    }
  }

  private val json: Json = Json { ignoreUnknownKeys = true }

  /**
   * 주어진 아이디에 대응되는 추가 수수료 정책의 예약 업데이트를 조회합니다.
   *
   * @param id
   * 추가 수수료 정책 아이디
   * @param test
   * 테스트 모드 여부
   *
   * 테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
   *
   * @throws GetPlatformAdditionalFeePolicyScheduleException
   */
  @PortOneUnstable
  @JvmName("getPlatformAdditionalFeePolicyScheduleSuspend")
  public suspend fun getPlatformAdditionalFeePolicySchedule(
    id: String,
    test: Boolean? = null,
  ): PlatformAdditionalFeePolicy {
    val httpResponse = client.get(apiBase) {
      url {
        this.appendPathSegments("platform", "additional-fee-policies", id.toString(), "schedule")
        if (test != null) this.parameters.append("test", test.toString())
      }
      headers {
        this.append(HttpHeaders.Authorization, "PortOne $apiSecret")
      }
      this.accept(ContentType.Application.Json)
      this.userAgent(USER_AGENT)
    }
    if (httpResponse.status.value !in 200..299) {
      val httpBody = httpResponse.body<String>()
      val httpBodyDecoded = try {
        json.decodeFromString<GetPlatformAdditionalFeePolicyScheduleError.Recognized>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is PlatformAdditionalFeePolicyNotFoundError -> throw PlatformAdditionalFeePolicyNotFoundException(httpBodyDecoded)
        is PlatformNotEnabledError -> throw PlatformNotEnabledException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<PlatformAdditionalFeePolicy>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @PortOneUnstable
  @JvmName("getPlatformAdditionalFeePolicySchedule")
  public fun getPlatformAdditionalFeePolicyScheduleFuture(
    id: String,
    test: Boolean? = null,
  ): CompletableFuture<PlatformAdditionalFeePolicy> = GlobalScope.future { getPlatformAdditionalFeePolicySchedule(id, test) }


  /**
   * @param id
   * 추가 수수료 정책 아이디
   * @param test
   * 테스트 모드 여부
   *
   * 테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
   * @param update
   * 반영할 업데이트 내용
   * @param appliedAt
   * 업데이트 적용 시점
   *
   * @throws RescheduleAdditionalFeePolicyException
   */
  @PortOneUnstable
  @JvmName("rescheduleAdditionalFeePolicySuspend")
  public suspend fun rescheduleAdditionalFeePolicy(
    id: String,
    test: Boolean? = null,
    update: UpdatePlatformAdditionalFeePolicyBody,
    appliedAt: Instant,
  ): ReschedulePlatformAdditionalFeePolicyResponse {
    val requestBody = ReschedulePlatformAdditionalFeePolicyBody(
      update = update,
      appliedAt = appliedAt,
    )
    val httpResponse = client.put(apiBase) {
      url {
        this.appendPathSegments("platform", "additional-fee-policies", id.toString(), "schedule")
        if (test != null) this.parameters.append("test", test.toString())
      }
      headers {
        this.append(HttpHeaders.Authorization, "PortOne $apiSecret")
      }
      this.contentType(ContentType.Application.Json)
      this.accept(ContentType.Application.Json)
      this.userAgent(USER_AGENT)
      this.setBody(json.encodeToString(requestBody))
    }
    if (httpResponse.status.value !in 200..299) {
      val httpBody = httpResponse.body<String>()
      val httpBodyDecoded = try {
        json.decodeFromString<RescheduleAdditionalFeePolicyError.Recognized>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is PlatformAdditionalFeePolicyNotFoundError -> throw PlatformAdditionalFeePolicyNotFoundException(httpBodyDecoded)
        is PlatformNotEnabledError -> throw PlatformNotEnabledException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<ReschedulePlatformAdditionalFeePolicyResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @PortOneUnstable
  @JvmName("rescheduleAdditionalFeePolicy")
  public fun rescheduleAdditionalFeePolicyFuture(
    id: String,
    test: Boolean? = null,
    update: UpdatePlatformAdditionalFeePolicyBody,
    appliedAt: Instant,
  ): CompletableFuture<ReschedulePlatformAdditionalFeePolicyResponse> = GlobalScope.future { rescheduleAdditionalFeePolicy(id, test, update, appliedAt) }


  /**
   * 주어진 아이디에 대응되는 추가 수수료 정책에 업데이트를 예약합니다.
   *
   * @param id
   * 추가 수수료 정책 아이디
   * @param test
   * 테스트 모드 여부
   *
   * 테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
   * @param update
   * 반영할 업데이트 내용
   * @param appliedAt
   * 업데이트 적용 시점
   *
   * @throws ScheduleAdditionalFeePolicyException
   */
  @PortOneUnstable
  @JvmName("scheduleAdditionalFeePolicySuspend")
  public suspend fun scheduleAdditionalFeePolicy(
    id: String,
    test: Boolean? = null,
    update: UpdatePlatformAdditionalFeePolicyBody,
    appliedAt: Instant,
  ): SchedulePlatformAdditionalFeePolicyResponse {
    val requestBody = SchedulePlatformAdditionalFeePolicyBody(
      update = update,
      appliedAt = appliedAt,
    )
    val httpResponse = client.post(apiBase) {
      url {
        this.appendPathSegments("platform", "additional-fee-policies", id.toString(), "schedule")
        if (test != null) this.parameters.append("test", test.toString())
      }
      headers {
        this.append(HttpHeaders.Authorization, "PortOne $apiSecret")
      }
      this.contentType(ContentType.Application.Json)
      this.accept(ContentType.Application.Json)
      this.userAgent(USER_AGENT)
      this.setBody(json.encodeToString(requestBody))
    }
    if (httpResponse.status.value !in 200..299) {
      val httpBody = httpResponse.body<String>()
      val httpBodyDecoded = try {
        json.decodeFromString<ScheduleAdditionalFeePolicyError.Recognized>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is PlatformAdditionalFeePolicyNotFoundError -> throw PlatformAdditionalFeePolicyNotFoundException(httpBodyDecoded)
        is PlatformAdditionalFeePolicyScheduleAlreadyExistsError -> throw PlatformAdditionalFeePolicyScheduleAlreadyExistsException(httpBodyDecoded)
        is PlatformArchivedAdditionalFeePolicyError -> throw PlatformArchivedAdditionalFeePolicyException(httpBodyDecoded)
        is PlatformNotEnabledError -> throw PlatformNotEnabledException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<SchedulePlatformAdditionalFeePolicyResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @PortOneUnstable
  @JvmName("scheduleAdditionalFeePolicy")
  public fun scheduleAdditionalFeePolicyFuture(
    id: String,
    test: Boolean? = null,
    update: UpdatePlatformAdditionalFeePolicyBody,
    appliedAt: Instant,
  ): CompletableFuture<SchedulePlatformAdditionalFeePolicyResponse> = GlobalScope.future { scheduleAdditionalFeePolicy(id, test, update, appliedAt) }


  /**
   * 주어진 아이디에 대응되는 추가 수수료 정책의 예약 업데이트를 취소합니다.
   *
   * @param id
   * 추가 수수료 정책 아이디
   * @param test
   * 테스트 모드 여부
   *
   * 테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
   *
   * @throws CancelPlatformAdditionalFeePolicyScheduleException
   */
  @PortOneUnstable
  @JvmName("cancelPlatformAdditionalFeePolicyScheduleSuspend")
  public suspend fun cancelPlatformAdditionalFeePolicySchedule(
    id: String,
    test: Boolean? = null,
  ): CancelPlatformAdditionalFeePolicyScheduleResponse {
    val httpResponse = client.delete(apiBase) {
      url {
        this.appendPathSegments("platform", "additional-fee-policies", id.toString(), "schedule")
        if (test != null) this.parameters.append("test", test.toString())
      }
      headers {
        this.append(HttpHeaders.Authorization, "PortOne $apiSecret")
      }
      this.accept(ContentType.Application.Json)
      this.userAgent(USER_AGENT)
    }
    if (httpResponse.status.value !in 200..299) {
      val httpBody = httpResponse.body<String>()
      val httpBodyDecoded = try {
        json.decodeFromString<CancelPlatformAdditionalFeePolicyScheduleError.Recognized>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is PlatformAdditionalFeePolicyNotFoundError -> throw PlatformAdditionalFeePolicyNotFoundException(httpBodyDecoded)
        is PlatformNotEnabledError -> throw PlatformNotEnabledException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<CancelPlatformAdditionalFeePolicyScheduleResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @PortOneUnstable
  @JvmName("cancelPlatformAdditionalFeePolicySchedule")
  public fun cancelPlatformAdditionalFeePolicyScheduleFuture(
    id: String,
    test: Boolean? = null,
  ): CompletableFuture<CancelPlatformAdditionalFeePolicyScheduleResponse> = GlobalScope.future { cancelPlatformAdditionalFeePolicySchedule(id, test) }


  /**
   * 주어진 아이디에 대응되는 계약의 예약 업데이트를 조회합니다.
   *
   * @param id
   * 계약 아이디
   * @param test
   * 테스트 모드 여부
   *
   * 테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
   *
   * @throws GetPlatformContractScheduleException
   */
  @PortOneUnstable
  @JvmName("getPlatformContractScheduleSuspend")
  public suspend fun getPlatformContractSchedule(
    id: String,
    test: Boolean? = null,
  ): PlatformContract {
    val httpResponse = client.get(apiBase) {
      url {
        this.appendPathSegments("platform", "contracts", id.toString(), "schedule")
        if (test != null) this.parameters.append("test", test.toString())
      }
      headers {
        this.append(HttpHeaders.Authorization, "PortOne $apiSecret")
      }
      this.accept(ContentType.Application.Json)
      this.userAgent(USER_AGENT)
    }
    if (httpResponse.status.value !in 200..299) {
      val httpBody = httpResponse.body<String>()
      val httpBodyDecoded = try {
        json.decodeFromString<GetPlatformContractScheduleError.Recognized>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is PlatformContractNotFoundError -> throw PlatformContractNotFoundException(httpBodyDecoded)
        is PlatformNotEnabledError -> throw PlatformNotEnabledException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<PlatformContract>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @PortOneUnstable
  @JvmName("getPlatformContractSchedule")
  public fun getPlatformContractScheduleFuture(
    id: String,
    test: Boolean? = null,
  ): CompletableFuture<PlatformContract> = GlobalScope.future { getPlatformContractSchedule(id, test) }


  /**
   * 주어진 아이디에 대응되는 계약에 예약 업데이트를 재설정합니다.
   *
   * @param id
   * 계약 아이디
   * @param test
   * 테스트 모드 여부
   *
   * 테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
   * @param update
   * 반영할 업데이트 내용
   * @param appliedAt
   * 업데이트 적용 시점
   *
   * @throws RescheduleContractException
   */
  @PortOneUnstable
  @JvmName("rescheduleContractSuspend")
  public suspend fun rescheduleContract(
    id: String,
    test: Boolean? = null,
    update: UpdatePlatformContractBody,
    appliedAt: Instant,
  ): ReschedulePlatformContractResponse {
    val requestBody = ReschedulePlatformContractBody(
      update = update,
      appliedAt = appliedAt,
    )
    val httpResponse = client.put(apiBase) {
      url {
        this.appendPathSegments("platform", "contracts", id.toString(), "schedule")
        if (test != null) this.parameters.append("test", test.toString())
      }
      headers {
        this.append(HttpHeaders.Authorization, "PortOne $apiSecret")
      }
      this.contentType(ContentType.Application.Json)
      this.accept(ContentType.Application.Json)
      this.userAgent(USER_AGENT)
      this.setBody(json.encodeToString(requestBody))
    }
    if (httpResponse.status.value !in 200..299) {
      val httpBody = httpResponse.body<String>()
      val httpBodyDecoded = try {
        json.decodeFromString<RescheduleContractError.Recognized>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is PlatformContractNotFoundError -> throw PlatformContractNotFoundException(httpBodyDecoded)
        is PlatformNotEnabledError -> throw PlatformNotEnabledException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<ReschedulePlatformContractResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @PortOneUnstable
  @JvmName("rescheduleContract")
  public fun rescheduleContractFuture(
    id: String,
    test: Boolean? = null,
    update: UpdatePlatformContractBody,
    appliedAt: Instant,
  ): CompletableFuture<ReschedulePlatformContractResponse> = GlobalScope.future { rescheduleContract(id, test, update, appliedAt) }


  /**
   * 주어진 아이디에 대응되는 계약에 업데이트를 예약합니다.
   *
   * @param id
   * 계약 아이디
   * @param test
   * 테스트 모드 여부
   *
   * 테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
   * @param update
   * 반영할 업데이트 내용
   * @param appliedAt
   * 업데이트 적용 시점
   *
   * @throws ScheduleContractException
   */
  @PortOneUnstable
  @JvmName("scheduleContractSuspend")
  public suspend fun scheduleContract(
    id: String,
    test: Boolean? = null,
    update: UpdatePlatformContractBody,
    appliedAt: Instant,
  ): SchedulePlatformContractResponse {
    val requestBody = SchedulePlatformContractBody(
      update = update,
      appliedAt = appliedAt,
    )
    val httpResponse = client.post(apiBase) {
      url {
        this.appendPathSegments("platform", "contracts", id.toString(), "schedule")
        if (test != null) this.parameters.append("test", test.toString())
      }
      headers {
        this.append(HttpHeaders.Authorization, "PortOne $apiSecret")
      }
      this.contentType(ContentType.Application.Json)
      this.accept(ContentType.Application.Json)
      this.userAgent(USER_AGENT)
      this.setBody(json.encodeToString(requestBody))
    }
    if (httpResponse.status.value !in 200..299) {
      val httpBody = httpResponse.body<String>()
      val httpBodyDecoded = try {
        json.decodeFromString<ScheduleContractError.Recognized>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is PlatformArchivedContractError -> throw PlatformArchivedContractException(httpBodyDecoded)
        is PlatformContractNotFoundError -> throw PlatformContractNotFoundException(httpBodyDecoded)
        is PlatformContractScheduleAlreadyExistsError -> throw PlatformContractScheduleAlreadyExistsException(httpBodyDecoded)
        is PlatformNotEnabledError -> throw PlatformNotEnabledException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<SchedulePlatformContractResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @PortOneUnstable
  @JvmName("scheduleContract")
  public fun scheduleContractFuture(
    id: String,
    test: Boolean? = null,
    update: UpdatePlatformContractBody,
    appliedAt: Instant,
  ): CompletableFuture<SchedulePlatformContractResponse> = GlobalScope.future { scheduleContract(id, test, update, appliedAt) }


  /**
   * 주어진 아이디에 대응되는 계약의 예약 업데이트를 취소합니다.
   *
   * @param id
   * 계약 아이디
   * @param test
   * 테스트 모드 여부
   *
   * 테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
   *
   * @throws CancelPlatformContractScheduleException
   */
  @PortOneUnstable
  @JvmName("cancelPlatformContractScheduleSuspend")
  public suspend fun cancelPlatformContractSchedule(
    id: String,
    test: Boolean? = null,
  ): CancelPlatformContractScheduleResponse {
    val httpResponse = client.delete(apiBase) {
      url {
        this.appendPathSegments("platform", "contracts", id.toString(), "schedule")
        if (test != null) this.parameters.append("test", test.toString())
      }
      headers {
        this.append(HttpHeaders.Authorization, "PortOne $apiSecret")
      }
      this.accept(ContentType.Application.Json)
      this.userAgent(USER_AGENT)
    }
    if (httpResponse.status.value !in 200..299) {
      val httpBody = httpResponse.body<String>()
      val httpBodyDecoded = try {
        json.decodeFromString<CancelPlatformContractScheduleError.Recognized>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is PlatformContractNotFoundError -> throw PlatformContractNotFoundException(httpBodyDecoded)
        is PlatformNotEnabledError -> throw PlatformNotEnabledException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<CancelPlatformContractScheduleResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @PortOneUnstable
  @JvmName("cancelPlatformContractSchedule")
  public fun cancelPlatformContractScheduleFuture(
    id: String,
    test: Boolean? = null,
  ): CompletableFuture<CancelPlatformContractScheduleResponse> = GlobalScope.future { cancelPlatformContractSchedule(id, test) }


  /**
   * 주어진 아이디에 대응되는 할인 분담의 예약 업데이트를 조회합니다.
   *
   * @param id
   * 할인 분담 정책 아이디
   * @param test
   * 테스트 모드 여부
   *
   * 테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
   *
   * @throws GetPlatformDiscountSharePolicyScheduleException
   */
  @PortOneUnstable
  @JvmName("getPlatformDiscountSharePolicyScheduleSuspend")
  public suspend fun getPlatformDiscountSharePolicySchedule(
    id: String,
    test: Boolean? = null,
  ): PlatformDiscountSharePolicy {
    val httpResponse = client.get(apiBase) {
      url {
        this.appendPathSegments("platform", "discount-share-policies", id.toString(), "schedule")
        if (test != null) this.parameters.append("test", test.toString())
      }
      headers {
        this.append(HttpHeaders.Authorization, "PortOne $apiSecret")
      }
      this.accept(ContentType.Application.Json)
      this.userAgent(USER_AGENT)
    }
    if (httpResponse.status.value !in 200..299) {
      val httpBody = httpResponse.body<String>()
      val httpBodyDecoded = try {
        json.decodeFromString<GetPlatformDiscountSharePolicyScheduleError.Recognized>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is PlatformDiscountSharePolicyNotFoundError -> throw PlatformDiscountSharePolicyNotFoundException(httpBodyDecoded)
        is PlatformNotEnabledError -> throw PlatformNotEnabledException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<PlatformDiscountSharePolicy>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @PortOneUnstable
  @JvmName("getPlatformDiscountSharePolicySchedule")
  public fun getPlatformDiscountSharePolicyScheduleFuture(
    id: String,
    test: Boolean? = null,
  ): CompletableFuture<PlatformDiscountSharePolicy> = GlobalScope.future { getPlatformDiscountSharePolicySchedule(id, test) }


  /**
   * 주어진 아이디에 대응되는 할인 분담에 예약 업데이트를 재설정합니다.
   *
   * @param id
   * 할인 분담 정책 아이디
   * @param test
   * 테스트 모드 여부
   *
   * 테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
   * @param update
   * 반영할 업데이트 내용
   * @param appliedAt
   * 업데이트 적용 시점
   *
   * @throws RescheduleDiscountSharePolicyException
   */
  @PortOneUnstable
  @JvmName("rescheduleDiscountSharePolicySuspend")
  public suspend fun rescheduleDiscountSharePolicy(
    id: String,
    test: Boolean? = null,
    update: UpdatePlatformDiscountSharePolicyBody,
    appliedAt: Instant,
  ): ReschedulePlatformDiscountSharePolicyResponse {
    val requestBody = ReschedulePlatformDiscountSharePolicyBody(
      update = update,
      appliedAt = appliedAt,
    )
    val httpResponse = client.put(apiBase) {
      url {
        this.appendPathSegments("platform", "discount-share-policies", id.toString(), "schedule")
        if (test != null) this.parameters.append("test", test.toString())
      }
      headers {
        this.append(HttpHeaders.Authorization, "PortOne $apiSecret")
      }
      this.contentType(ContentType.Application.Json)
      this.accept(ContentType.Application.Json)
      this.userAgent(USER_AGENT)
      this.setBody(json.encodeToString(requestBody))
    }
    if (httpResponse.status.value !in 200..299) {
      val httpBody = httpResponse.body<String>()
      val httpBodyDecoded = try {
        json.decodeFromString<RescheduleDiscountSharePolicyError.Recognized>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is PlatformDiscountSharePolicyNotFoundError -> throw PlatformDiscountSharePolicyNotFoundException(httpBodyDecoded)
        is PlatformNotEnabledError -> throw PlatformNotEnabledException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<ReschedulePlatformDiscountSharePolicyResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @PortOneUnstable
  @JvmName("rescheduleDiscountSharePolicy")
  public fun rescheduleDiscountSharePolicyFuture(
    id: String,
    test: Boolean? = null,
    update: UpdatePlatformDiscountSharePolicyBody,
    appliedAt: Instant,
  ): CompletableFuture<ReschedulePlatformDiscountSharePolicyResponse> = GlobalScope.future { rescheduleDiscountSharePolicy(id, test, update, appliedAt) }


  /**
   * 주어진 아이디에 대응되는 할인 분담에 업데이트를 예약합니다.
   *
   * @param id
   * 할인 분담 정책 아이디
   * @param test
   * 테스트 모드 여부
   *
   * 테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
   * @param update
   * 반영할 업데이트 내용
   * @param appliedAt
   * 업데이트 적용 시점
   *
   * @throws ScheduleDiscountSharePolicyException
   */
  @PortOneUnstable
  @JvmName("scheduleDiscountSharePolicySuspend")
  public suspend fun scheduleDiscountSharePolicy(
    id: String,
    test: Boolean? = null,
    update: UpdatePlatformDiscountSharePolicyBody,
    appliedAt: Instant,
  ): SchedulePlatformDiscountSharePolicyResponse {
    val requestBody = SchedulePlatformDiscountSharePolicyBody(
      update = update,
      appliedAt = appliedAt,
    )
    val httpResponse = client.post(apiBase) {
      url {
        this.appendPathSegments("platform", "discount-share-policies", id.toString(), "schedule")
        if (test != null) this.parameters.append("test", test.toString())
      }
      headers {
        this.append(HttpHeaders.Authorization, "PortOne $apiSecret")
      }
      this.contentType(ContentType.Application.Json)
      this.accept(ContentType.Application.Json)
      this.userAgent(USER_AGENT)
      this.setBody(json.encodeToString(requestBody))
    }
    if (httpResponse.status.value !in 200..299) {
      val httpBody = httpResponse.body<String>()
      val httpBodyDecoded = try {
        json.decodeFromString<ScheduleDiscountSharePolicyError.Recognized>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is PlatformArchivedDiscountSharePolicyError -> throw PlatformArchivedDiscountSharePolicyException(httpBodyDecoded)
        is PlatformDiscountSharePolicyNotFoundError -> throw PlatformDiscountSharePolicyNotFoundException(httpBodyDecoded)
        is PlatformDiscountSharePolicyScheduleAlreadyExistsError -> throw PlatformDiscountSharePolicyScheduleAlreadyExistsException(httpBodyDecoded)
        is PlatformNotEnabledError -> throw PlatformNotEnabledException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<SchedulePlatformDiscountSharePolicyResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @PortOneUnstable
  @JvmName("scheduleDiscountSharePolicy")
  public fun scheduleDiscountSharePolicyFuture(
    id: String,
    test: Boolean? = null,
    update: UpdatePlatformDiscountSharePolicyBody,
    appliedAt: Instant,
  ): CompletableFuture<SchedulePlatformDiscountSharePolicyResponse> = GlobalScope.future { scheduleDiscountSharePolicy(id, test, update, appliedAt) }


  /**
   * 주어진 아이디에 대응되는 할인 분담의 예약 업데이트를 취소합니다.
   *
   * @param id
   * 할인 분담 정책 아이디
   * @param test
   * 테스트 모드 여부
   *
   * 테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
   *
   * @throws CancelPlatformDiscountSharePolicyScheduleException
   */
  @PortOneUnstable
  @JvmName("cancelPlatformDiscountSharePolicyScheduleSuspend")
  public suspend fun cancelPlatformDiscountSharePolicySchedule(
    id: String,
    test: Boolean? = null,
  ): CancelPlatformDiscountSharePolicyScheduleResponse {
    val httpResponse = client.delete(apiBase) {
      url {
        this.appendPathSegments("platform", "discount-share-policies", id.toString(), "schedule")
        if (test != null) this.parameters.append("test", test.toString())
      }
      headers {
        this.append(HttpHeaders.Authorization, "PortOne $apiSecret")
      }
      this.accept(ContentType.Application.Json)
      this.userAgent(USER_AGENT)
    }
    if (httpResponse.status.value !in 200..299) {
      val httpBody = httpResponse.body<String>()
      val httpBodyDecoded = try {
        json.decodeFromString<CancelPlatformDiscountSharePolicyScheduleError.Recognized>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is PlatformDiscountSharePolicyNotFoundError -> throw PlatformDiscountSharePolicyNotFoundException(httpBodyDecoded)
        is PlatformNotEnabledError -> throw PlatformNotEnabledException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<CancelPlatformDiscountSharePolicyScheduleResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @PortOneUnstable
  @JvmName("cancelPlatformDiscountSharePolicySchedule")
  public fun cancelPlatformDiscountSharePolicyScheduleFuture(
    id: String,
    test: Boolean? = null,
  ): CompletableFuture<CancelPlatformDiscountSharePolicyScheduleResponse> = GlobalScope.future { cancelPlatformDiscountSharePolicySchedule(id, test) }


  /**
   * 할인 분담 정책 다건 조회 시 필요한 필터 옵션을 조회합니다.
   *
   * @param test
   * 테스트 모드 여부
   *
   * 테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
   * @param isArchived
   * 보관 조회 여부
   *
   * true 이면 보관된 할인 분담의 필터 옵션을 조회하고, false 이면 보관되지 않은 할인 분담의 필터 옵션을 조회합니다. 기본값은 false 입니다.
   *
   * @throws GetPlatformDiscountSharePolicyFilterOptionsException
   */
  @PortOneUnstable
  @JvmName("getPlatformDiscountSharePolicyFilterOptionsSuspend")
  public suspend fun getPlatformDiscountSharePolicyFilterOptions(
    test: Boolean? = null,
    isArchived: Boolean? = null,
  ): PlatformDiscountSharePolicyFilterOptions {
    val httpResponse = client.get(apiBase) {
      url {
        this.appendPathSegments("platform", "discount-share-policy-filter-options")
        if (test != null) this.parameters.append("test", test.toString())
        if (isArchived != null) this.parameters.append("isArchived", isArchived.toString())
      }
      headers {
        this.append(HttpHeaders.Authorization, "PortOne $apiSecret")
      }
      this.accept(ContentType.Application.Json)
      this.userAgent(USER_AGENT)
    }
    if (httpResponse.status.value !in 200..299) {
      val httpBody = httpResponse.body<String>()
      val httpBodyDecoded = try {
        json.decodeFromString<GetPlatformDiscountSharePolicyFilterOptionsError.Recognized>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is PlatformNotEnabledError -> throw PlatformNotEnabledException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<PlatformDiscountSharePolicyFilterOptions>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @PortOneUnstable
  @JvmName("getPlatformDiscountSharePolicyFilterOptions")
  public fun getPlatformDiscountSharePolicyFilterOptionsFuture(
    test: Boolean? = null,
    isArchived: Boolean? = null,
  ): CompletableFuture<PlatformDiscountSharePolicyFilterOptions> = GlobalScope.future { getPlatformDiscountSharePolicyFilterOptions(test, isArchived) }


  /**
   * 파트너 다건 조회 시 필요한 필터 옵션을 조회합니다.
   *
   * @param test
   * 테스트 모드 여부
   *
   * 테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
   * @param isArchived
   * 보관 조회 여부
   *
   * true 이면 보관된 파트너의 필터 옵션을 조회하고, false 이면 보관되지 않은 파트너의 필터 옵션을 조회합니다. 기본값은 false 입니다.
   *
   * @throws GetPlatformPartnerFilterOptionsException
   */
  @PortOneUnstable
  @JvmName("getPlatformPartnerFilterOptionsSuspend")
  public suspend fun getPlatformPartnerFilterOptions(
    test: Boolean? = null,
    isArchived: Boolean? = null,
  ): PlatformPartnerFilterOptions {
    val httpResponse = client.get(apiBase) {
      url {
        this.appendPathSegments("platform", "partner-filter-options")
        if (test != null) this.parameters.append("test", test.toString())
        if (isArchived != null) this.parameters.append("isArchived", isArchived.toString())
      }
      headers {
        this.append(HttpHeaders.Authorization, "PortOne $apiSecret")
      }
      this.accept(ContentType.Application.Json)
      this.userAgent(USER_AGENT)
    }
    if (httpResponse.status.value !in 200..299) {
      val httpBody = httpResponse.body<String>()
      val httpBodyDecoded = try {
        json.decodeFromString<GetPlatformPartnerFilterOptionsError.Recognized>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is PlatformNotEnabledError -> throw PlatformNotEnabledException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<PlatformPartnerFilterOptions>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @PortOneUnstable
  @JvmName("getPlatformPartnerFilterOptions")
  public fun getPlatformPartnerFilterOptionsFuture(
    test: Boolean? = null,
    isArchived: Boolean? = null,
  ): CompletableFuture<PlatformPartnerFilterOptions> = GlobalScope.future { getPlatformPartnerFilterOptions(test, isArchived) }


  /**
   * @param test
   * 테스트 모드 여부
   *
   * 테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
   * @param filter
   *
   * @param update
   *
   * @param appliedAt
   *
   *
   * @throws SchedulePlatformPartnersException
   */
  @PortOneUnstable
  @JvmName("schedulePlatformPartnersSuspend")
  public suspend fun schedulePlatformPartners(
    test: Boolean? = null,
    filter: PlatformPartnerFilterInput? = null,
    update: SchedulePlatformPartnersBodyUpdate,
    appliedAt: Instant,
  ): SchedulePlatformPartnersResponse {
    val requestBody = SchedulePlatformPartnersBody(
      filter = filter,
      update = update,
      appliedAt = appliedAt,
    )
    val httpResponse = client.post(apiBase) {
      url {
        this.appendPathSegments("platform", "partners", "schedule")
        if (test != null) this.parameters.append("test", test.toString())
      }
      headers {
        this.append(HttpHeaders.Authorization, "PortOne $apiSecret")
      }
      this.contentType(ContentType.Application.Json)
      this.accept(ContentType.Application.Json)
      this.userAgent(USER_AGENT)
      this.setBody(json.encodeToString(requestBody))
    }
    if (httpResponse.status.value !in 200..299) {
      val httpBody = httpResponse.body<String>()
      val httpBodyDecoded = try {
        json.decodeFromString<SchedulePlatformPartnersError.Recognized>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is PlatformArchivedPartnersCannotBeScheduledError -> throw PlatformArchivedPartnersCannotBeScheduledException(httpBodyDecoded)
        is PlatformContractNotFoundError -> throw PlatformContractNotFoundException(httpBodyDecoded)
        is PlatformMemberCompanyConnectedPartnersCannotBeScheduledError -> throw PlatformMemberCompanyConnectedPartnersCannotBeScheduledException(httpBodyDecoded)
        is PlatformNotEnabledError -> throw PlatformNotEnabledException(httpBodyDecoded)
        is PlatformPartnerSchedulesAlreadyExistError -> throw PlatformPartnerSchedulesAlreadyExistException(httpBodyDecoded)
        is PlatformUserDefinedPropertyNotFoundError -> throw PlatformUserDefinedPropertyNotFoundException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<SchedulePlatformPartnersResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @PortOneUnstable
  @JvmName("schedulePlatformPartners")
  public fun schedulePlatformPartnersFuture(
    test: Boolean? = null,
    filter: PlatformPartnerFilterInput? = null,
    update: SchedulePlatformPartnersBodyUpdate,
    appliedAt: Instant,
  ): CompletableFuture<SchedulePlatformPartnersResponse> = GlobalScope.future { schedulePlatformPartners(test, filter, update, appliedAt) }


  /**
   * 주어진 아이디에 대응되는 파트너의 예약 업데이트를 조회합니다.
   *
   * @param id
   * 파트너 아이디
   * @param test
   * 테스트 모드 여부
   *
   * 테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
   *
   * @throws GetPlatformPartnerScheduleException
   */
  @PortOneUnstable
  @JvmName("getPlatformPartnerScheduleSuspend")
  public suspend fun getPlatformPartnerSchedule(
    id: String,
    test: Boolean? = null,
  ): PlatformPartner {
    val httpResponse = client.get(apiBase) {
      url {
        this.appendPathSegments("platform", "partners", id.toString(), "schedule")
        if (test != null) this.parameters.append("test", test.toString())
      }
      headers {
        this.append(HttpHeaders.Authorization, "PortOne $apiSecret")
      }
      this.accept(ContentType.Application.Json)
      this.userAgent(USER_AGENT)
    }
    if (httpResponse.status.value !in 200..299) {
      val httpBody = httpResponse.body<String>()
      val httpBodyDecoded = try {
        json.decodeFromString<GetPlatformPartnerScheduleError.Recognized>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is PlatformNotEnabledError -> throw PlatformNotEnabledException(httpBodyDecoded)
        is PlatformPartnerNotFoundError -> throw PlatformPartnerNotFoundException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<PlatformPartner>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @PortOneUnstable
  @JvmName("getPlatformPartnerSchedule")
  public fun getPlatformPartnerScheduleFuture(
    id: String,
    test: Boolean? = null,
  ): CompletableFuture<PlatformPartner> = GlobalScope.future { getPlatformPartnerSchedule(id, test) }


  /**
   * 주어진 아이디에 대응되는 파트너에 예약 업데이트를 재설정합니다.
   *
   * @param id
   * 파트너 아이디
   * @param test
   * 테스트 모드 여부
   *
   * 테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
   * @param update
   * 반영할 업데이트 내용
   * @param appliedAt
   * 업데이트 적용 시점
   *
   * @throws ReschedulePartnerException
   */
  @PortOneUnstable
  @JvmName("reschedulePartnerSuspend")
  public suspend fun reschedulePartner(
    id: String,
    test: Boolean? = null,
    update: UpdatePlatformPartnerBody,
    appliedAt: Instant,
  ): ReschedulePlatformPartnerResponse {
    val requestBody = ReschedulePlatformPartnerBody(
      update = update,
      appliedAt = appliedAt,
    )
    val httpResponse = client.put(apiBase) {
      url {
        this.appendPathSegments("platform", "partners", id.toString(), "schedule")
        if (test != null) this.parameters.append("test", test.toString())
      }
      headers {
        this.append(HttpHeaders.Authorization, "PortOne $apiSecret")
      }
      this.contentType(ContentType.Application.Json)
      this.accept(ContentType.Application.Json)
      this.userAgent(USER_AGENT)
      this.setBody(json.encodeToString(requestBody))
    }
    if (httpResponse.status.value !in 200..299) {
      val httpBody = httpResponse.body<String>()
      val httpBodyDecoded = try {
        json.decodeFromString<ReschedulePartnerError.Recognized>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is PlatformContractNotFoundError -> throw PlatformContractNotFoundException(httpBodyDecoded)
        is PlatformMemberCompanyConnectedPartnerCannotBeScheduledError -> throw PlatformMemberCompanyConnectedPartnerCannotBeScheduledException(httpBodyDecoded)
        is PlatformNotEnabledError -> throw PlatformNotEnabledException(httpBodyDecoded)
        is PlatformPartnerNotFoundError -> throw PlatformPartnerNotFoundException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<ReschedulePlatformPartnerResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @PortOneUnstable
  @JvmName("reschedulePartner")
  public fun reschedulePartnerFuture(
    id: String,
    test: Boolean? = null,
    update: UpdatePlatformPartnerBody,
    appliedAt: Instant,
  ): CompletableFuture<ReschedulePlatformPartnerResponse> = GlobalScope.future { reschedulePartner(id, test, update, appliedAt) }


  /**
   * 주어진 아이디에 대응되는 파트너에 업데이트를 예약합니다.
   *
   * @param id
   * 파트너 아이디
   * @param test
   * 테스트 모드 여부
   *
   * 테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
   * @param update
   * 반영할 업데이트 내용
   * @param appliedAt
   * 업데이트 적용 시점
   *
   * @throws SchedulePartnerException
   */
  @PortOneUnstable
  @JvmName("schedulePartnerSuspend")
  public suspend fun schedulePartner(
    id: String,
    test: Boolean? = null,
    update: UpdatePlatformPartnerBody,
    appliedAt: Instant,
  ): SchedulePlatformPartnerResponse {
    val requestBody = SchedulePlatformPartnerBody(
      update = update,
      appliedAt = appliedAt,
    )
    val httpResponse = client.post(apiBase) {
      url {
        this.appendPathSegments("platform", "partners", id.toString(), "schedule")
        if (test != null) this.parameters.append("test", test.toString())
      }
      headers {
        this.append(HttpHeaders.Authorization, "PortOne $apiSecret")
      }
      this.contentType(ContentType.Application.Json)
      this.accept(ContentType.Application.Json)
      this.userAgent(USER_AGENT)
      this.setBody(json.encodeToString(requestBody))
    }
    if (httpResponse.status.value !in 200..299) {
      val httpBody = httpResponse.body<String>()
      val httpBodyDecoded = try {
        json.decodeFromString<SchedulePartnerError.Recognized>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is PlatformAccountVerificationAlreadyUsedError -> throw PlatformAccountVerificationAlreadyUsedException(httpBodyDecoded)
        is PlatformAccountVerificationFailedError -> throw PlatformAccountVerificationFailedException(httpBodyDecoded)
        is PlatformAccountVerificationNotFoundError -> throw PlatformAccountVerificationNotFoundException(httpBodyDecoded)
        is PlatformArchivedPartnerError -> throw PlatformArchivedPartnerException(httpBodyDecoded)
        is PlatformCompanyVerificationAlreadyUsedError -> throw PlatformCompanyVerificationAlreadyUsedException(httpBodyDecoded)
        is PlatformContractNotFoundError -> throw PlatformContractNotFoundException(httpBodyDecoded)
        is PlatformInsufficientDataToChangePartnerTypeError -> throw PlatformInsufficientDataToChangePartnerTypeException(httpBodyDecoded)
        is PlatformMemberCompanyConnectedPartnerBrnUnchangeableError -> throw PlatformMemberCompanyConnectedPartnerBrnUnchangeableException(httpBodyDecoded)
        is PlatformMemberCompanyConnectedPartnerCannotBeScheduledError -> throw PlatformMemberCompanyConnectedPartnerCannotBeScheduledException(httpBodyDecoded)
        is PlatformMemberCompanyConnectedPartnerTypeUnchangeableError -> throw PlatformMemberCompanyConnectedPartnerTypeUnchangeableException(httpBodyDecoded)
        is PlatformNotEnabledError -> throw PlatformNotEnabledException(httpBodyDecoded)
        is PlatformPartnerNotFoundError -> throw PlatformPartnerNotFoundException(httpBodyDecoded)
        is PlatformPartnerScheduleAlreadyExistsError -> throw PlatformPartnerScheduleAlreadyExistsException(httpBodyDecoded)
        is PlatformUserDefinedPropertyNotFoundError -> throw PlatformUserDefinedPropertyNotFoundException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<SchedulePlatformPartnerResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @PortOneUnstable
  @JvmName("schedulePartner")
  public fun schedulePartnerFuture(
    id: String,
    test: Boolean? = null,
    update: UpdatePlatformPartnerBody,
    appliedAt: Instant,
  ): CompletableFuture<SchedulePlatformPartnerResponse> = GlobalScope.future { schedulePartner(id, test, update, appliedAt) }


  /**
   * 주어진 아이디에 대응되는 파트너의 예약 업데이트를 취소합니다.
   *
   * @param id
   * 파트너 아이디
   * @param test
   * 테스트 모드 여부
   *
   * 테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
   *
   * @throws CancelPlatformPartnerScheduleException
   */
  @PortOneUnstable
  @JvmName("cancelPlatformPartnerScheduleSuspend")
  public suspend fun cancelPlatformPartnerSchedule(
    id: String,
    test: Boolean? = null,
  ): CancelPlatformPartnerScheduleResponse {
    val httpResponse = client.delete(apiBase) {
      url {
        this.appendPathSegments("platform", "partners", id.toString(), "schedule")
        if (test != null) this.parameters.append("test", test.toString())
      }
      headers {
        this.append(HttpHeaders.Authorization, "PortOne $apiSecret")
      }
      this.accept(ContentType.Application.Json)
      this.userAgent(USER_AGENT)
    }
    if (httpResponse.status.value !in 200..299) {
      val httpBody = httpResponse.body<String>()
      val httpBodyDecoded = try {
        json.decodeFromString<CancelPlatformPartnerScheduleError.Recognized>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is PlatformNotEnabledError -> throw PlatformNotEnabledException(httpBodyDecoded)
        is PlatformPartnerNotFoundError -> throw PlatformPartnerNotFoundException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<CancelPlatformPartnerScheduleResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @PortOneUnstable
  @JvmName("cancelPlatformPartnerSchedule")
  public fun cancelPlatformPartnerScheduleFuture(
    id: String,
    test: Boolean? = null,
  ): CompletableFuture<CancelPlatformPartnerScheduleResponse> = GlobalScope.future { cancelPlatformPartnerSchedule(id, test) }


  /**
   * 플랫폼 설정 조회
   *
   * 설정 정보를 조회합니다.
   *
   * @param test
   * 테스트 모드 여부
   *
   * 테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
   *
   * @throws GetPlatformSettingException
   */
  @JvmName("getPlatformSettingSuspend")
  public suspend fun getPlatformSetting(
    test: Boolean? = null,
  ): PlatformSetting {
    val httpResponse = client.get(apiBase) {
      url {
        this.appendPathSegments("platform", "setting")
        if (test != null) this.parameters.append("test", test.toString())
      }
      headers {
        this.append(HttpHeaders.Authorization, "PortOne $apiSecret")
      }
      this.accept(ContentType.Application.Json)
      this.userAgent(USER_AGENT)
    }
    if (httpResponse.status.value !in 200..299) {
      val httpBody = httpResponse.body<String>()
      val httpBodyDecoded = try {
        json.decodeFromString<GetPlatformSettingError.Recognized>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is PlatformNotEnabledError -> throw PlatformNotEnabledException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<PlatformSetting>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getPlatformSetting")
  public fun getPlatformSettingFuture(
    test: Boolean? = null,
  ): CompletableFuture<PlatformSetting> = GlobalScope.future { getPlatformSetting(test) }


  /**
   * 플랫폼 설정 업데이트
   *
   * 설정 정보를 업데이트합니다.
   *
   * @param test
   * 테스트 모드 여부
   *
   * 테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
   * @param defaultWithdrawalMemo
   * 기본 보내는 이 통장 메모
   * @param defaultDepositMemo
   * 기본 받는 이 통장 메모
   * @param supportsMultipleOrderTransfersPerPartner
   * paymentId, storeId, partnerId가 같은 주문 정산건에 대한 중복 정산 지원 여부
   * @param adjustSettlementDateAfterHolidayIfEarlier
   * 정산일이 정산시작일보다 작거나 같을 경우 공휴일 후 영업일로 정산일 다시 계산 여부
   * @param deductWht
   * 지급 금액에서 원천징수세 차감 여부
   * @param settlementAmountType
   * 정산 금액 취급 기준
   *
   * @throws UpdatePlatformSettingException
   */
  @JvmName("updatePlatformSettingSuspend")
  public suspend fun updatePlatformSetting(
    test: Boolean? = null,
    defaultWithdrawalMemo: String? = null,
    defaultDepositMemo: String? = null,
    supportsMultipleOrderTransfersPerPartner: Boolean? = null,
    adjustSettlementDateAfterHolidayIfEarlier: Boolean? = null,
    deductWht: Boolean? = null,
    settlementAmountType: SettlementAmountType? = null,
  ): UpdatePlatformSettingResponse {
    val requestBody = UpdatePlatformSettingBody(
      defaultWithdrawalMemo = defaultWithdrawalMemo,
      defaultDepositMemo = defaultDepositMemo,
      supportsMultipleOrderTransfersPerPartner = supportsMultipleOrderTransfersPerPartner,
      adjustSettlementDateAfterHolidayIfEarlier = adjustSettlementDateAfterHolidayIfEarlier,
      deductWht = deductWht,
      settlementAmountType = settlementAmountType,
    )
    val httpResponse = client.patch(apiBase) {
      url {
        this.appendPathSegments("platform", "setting")
        if (test != null) this.parameters.append("test", test.toString())
      }
      headers {
        this.append(HttpHeaders.Authorization, "PortOne $apiSecret")
      }
      this.contentType(ContentType.Application.Json)
      this.accept(ContentType.Application.Json)
      this.userAgent(USER_AGENT)
      this.setBody(json.encodeToString(requestBody))
    }
    if (httpResponse.status.value !in 200..299) {
      val httpBody = httpResponse.body<String>()
      val httpBodyDecoded = try {
        json.decodeFromString<UpdatePlatformSettingError.Recognized>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is PlatformNotEnabledError -> throw PlatformNotEnabledException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<UpdatePlatformSettingResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("updatePlatformSetting")
  public fun updatePlatformSettingFuture(
    test: Boolean? = null,
    defaultWithdrawalMemo: String? = null,
    defaultDepositMemo: String? = null,
    supportsMultipleOrderTransfersPerPartner: Boolean? = null,
    adjustSettlementDateAfterHolidayIfEarlier: Boolean? = null,
    deductWht: Boolean? = null,
    settlementAmountType: SettlementAmountType? = null,
  ): CompletableFuture<UpdatePlatformSettingResponse> = GlobalScope.future { updatePlatformSetting(test, defaultWithdrawalMemo, defaultDepositMemo, supportsMultipleOrderTransfersPerPartner, adjustSettlementDateAfterHolidayIfEarlier, deductWht, settlementAmountType) }

  public val company: CompanyClient = CompanyClient(apiSecret, apiBase, storeId)
  public val accountTransfer: AccountTransferClient = AccountTransferClient(apiSecret, apiBase, storeId)
  public val policy: PolicyClient = PolicyClient(apiSecret, apiBase, storeId)
  public val account: AccountClient = AccountClient(apiSecret, apiBase, storeId)
  public val bulkAccountTransfer: BulkAccountTransferClient = BulkAccountTransferClient(apiSecret, apiBase, storeId)
  public val bulkPayout: BulkPayoutClient = BulkPayoutClient(apiSecret, apiBase, storeId)
  public val partnerSettlement: PartnerSettlementClient = PartnerSettlementClient(apiSecret, apiBase, storeId)
  public val partner: PartnerClient = PartnerClient(apiSecret, apiBase, storeId)
  public val payout: PayoutClient = PayoutClient(apiSecret, apiBase, storeId)
  public val transfer: TransferClient = TransferClient(apiSecret, apiBase, storeId)
  override fun close() {
    company.close()
    accountTransfer.close()
    policy.close()
    account.close()
    bulkAccountTransfer.close()
    bulkPayout.close()
    partnerSettlement.close()
    partner.close()
    payout.close()
    transfer.close()
    client.close()
  }
}
