package io.portone.sdk.server.platform

import io.ktor.client.HttpClient
import io.ktor.client.call.body
import io.ktor.client.engine.okhttp.OkHttp
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
import io.portone.sdk.server.errors.CancelPlatformAdditionalFeePolicyScheduleError
import io.portone.sdk.server.errors.CancelPlatformContractScheduleError
import io.portone.sdk.server.errors.CancelPlatformDiscountSharePolicyScheduleError
import io.portone.sdk.server.errors.CancelPlatformPartnerScheduleError
import io.portone.sdk.server.errors.ForbiddenError
import io.portone.sdk.server.errors.ForbiddenException
import io.portone.sdk.server.errors.GetPlatformAdditionalFeePolicyScheduleError
import io.portone.sdk.server.errors.GetPlatformContractScheduleError
import io.portone.sdk.server.errors.GetPlatformDiscountSharePolicyFilterOptionsError
import io.portone.sdk.server.errors.GetPlatformDiscountSharePolicyScheduleError
import io.portone.sdk.server.errors.GetPlatformError
import io.portone.sdk.server.errors.GetPlatformPartnerFilterOptionsError
import io.portone.sdk.server.errors.GetPlatformPartnerScheduleError
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
import io.portone.sdk.server.errors.PlatformInvalidSettlementFormulaError
import io.portone.sdk.server.errors.PlatformInvalidSettlementFormulaException
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
import io.portone.sdk.server.errors.RescheduleContractError
import io.portone.sdk.server.errors.RescheduleDiscountSharePolicyError
import io.portone.sdk.server.errors.ReschedulePartnerError
import io.portone.sdk.server.errors.ScheduleAdditionalFeePolicyError
import io.portone.sdk.server.errors.ScheduleContractError
import io.portone.sdk.server.errors.ScheduleDiscountSharePolicyError
import io.portone.sdk.server.errors.SchedulePartnerError
import io.portone.sdk.server.errors.SchedulePlatformPartnersError
import io.portone.sdk.server.errors.UnauthorizedError
import io.portone.sdk.server.errors.UnauthorizedException
import io.portone.sdk.server.errors.UnknownException
import io.portone.sdk.server.errors.UpdatePlatformError
import io.portone.sdk.server.platform.CancelPlatformAdditionalFeePolicyScheduleResponse
import io.portone.sdk.server.platform.CancelPlatformContractScheduleResponse
import io.portone.sdk.server.platform.CancelPlatformDiscountSharePolicyScheduleResponse
import io.portone.sdk.server.platform.CancelPlatformPartnerScheduleResponse
import io.portone.sdk.server.platform.Platform
import io.portone.sdk.server.platform.PlatformAdditionalFeePolicy
import io.portone.sdk.server.platform.PlatformContract
import io.portone.sdk.server.platform.PlatformDiscountSharePolicy
import io.portone.sdk.server.platform.PlatformDiscountSharePolicyFilterOptions
import io.portone.sdk.server.platform.PlatformPartner
import io.portone.sdk.server.platform.PlatformPartnerFilterInput
import io.portone.sdk.server.platform.PlatformPartnerFilterOptions
import io.portone.sdk.server.platform.PlatformRoundType
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
import io.portone.sdk.server.platform.UpdatePlatformAdditionalFeePolicyBody
import io.portone.sdk.server.platform.UpdatePlatformBody
import io.portone.sdk.server.platform.UpdatePlatformBodySettlementFormula
import io.portone.sdk.server.platform.UpdatePlatformBodySettlementRule
import io.portone.sdk.server.platform.UpdatePlatformContractBody
import io.portone.sdk.server.platform.UpdatePlatformDiscountSharePolicyBody
import io.portone.sdk.server.platform.UpdatePlatformPartnerBody
import io.portone.sdk.server.platform.UpdatePlatformResponse
import io.portone.sdk.server.platform.account.AccountClient
import io.portone.sdk.server.platform.accounttransfer.AccountTransferClient
import io.portone.sdk.server.platform.bulkpayout.BulkPayoutClient
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

public class PlatformClient internal constructor(
  private val apiSecret: String,
  private val apiBase: String,
  private val storeId: String?,
) {
  private val client: HttpClient = HttpClient(OkHttp)

  private val json: Json = Json { ignoreUnknownKeys = true }

  /**
   * 고객사의 플랫폼 정보를 조회합니다.
   * 요청된 Authorization header 를 통해 자동으로 요청자의 고객사를 특정합니다.
   *
   *
   *
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws PlatformNotEnabledException 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("getPlatformSuspend")
  public suspend fun getPlatform(
  ): Platform {
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("platform")
      }
      headers {
        append(HttpHeaders.Authorization, "PortOne $apiSecret")
      }
      accept(ContentType.Application.Json)
      userAgent(USER_AGENT)
    }
    if (httpResponse.status.value !in 200..299) {
      val httpBody = httpResponse.body<String>()
      val httpBodyDecoded = try {
        json.decodeFromString<GetPlatformError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is PlatformNotEnabledError -> throw PlatformNotEnabledException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<Platform>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getPlatform")
  public fun getPlatformFuture(
  ): CompletableFuture<Platform> = GlobalScope.future { getPlatform() }


  /**
   * 고객사의 플랫폼 관련 정보를 업데이트합니다.
   * 요청된 Authorization header 를 통해 자동으로 요청자의 고객사를 특정합니다.
   *
   * @param roundType
   * 파트너 정산금액의 소수점 처리 방식
   * @param settlementFormula
   * 수수료 및 할인 분담 정책 관련 계산식
   * @param settlementRule
   * 정산 규칙
   *
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws PlatformInvalidSettlementFormulaException PlatformInvalidSettlementFormulaError
   * @throws PlatformNotEnabledException 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("updatePlatformSuspend")
  public suspend fun updatePlatform(
    roundType: PlatformRoundType? = null,
    settlementFormula: UpdatePlatformBodySettlementFormula? = null,
    settlementRule: UpdatePlatformBodySettlementRule? = null,
  ): UpdatePlatformResponse {
    val requestBody = UpdatePlatformBody(
      roundType = roundType,
      settlementFormula = settlementFormula,
      settlementRule = settlementRule,
    )
    val httpResponse = client.patch(apiBase) {
      url {
        appendPathSegments("platform")
      }
      headers {
        append(HttpHeaders.Authorization, "PortOne $apiSecret")
      }
      contentType(ContentType.Application.Json)
      accept(ContentType.Application.Json)
      userAgent(USER_AGENT)
      setBody(json.encodeToString(requestBody))
    }
    if (httpResponse.status.value !in 200..299) {
      val httpBody = httpResponse.body<String>()
      val httpBodyDecoded = try {
        json.decodeFromString<UpdatePlatformError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is PlatformInvalidSettlementFormulaError -> throw PlatformInvalidSettlementFormulaException(httpBodyDecoded)
        is PlatformNotEnabledError -> throw PlatformNotEnabledException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<UpdatePlatformResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("updatePlatform")
  public fun updatePlatformFuture(
    roundType: PlatformRoundType? = null,
    settlementFormula: UpdatePlatformBodySettlementFormula? = null,
    settlementRule: UpdatePlatformBodySettlementRule? = null,
  ): CompletableFuture<UpdatePlatformResponse> = GlobalScope.future { updatePlatform(roundType, settlementFormula, settlementRule) }


  /**
   * 할인 분담 정책 다건 조회 시 필요한 필터 옵션을 조회합니다.
   *
   * @param isArchived
   * 보관 조회 여부
   *
   * true 이면 보관된 할인 분담의 필터 옵션을 조회하고, false 이면 보관되지 않은 할인 분담의 필터 옵션을 조회합니다. 기본값은 false 입니다.
   *
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws PlatformNotEnabledException 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("getPlatformDiscountSharePolicyFilterOptionsSuspend")
  public suspend fun getPlatformDiscountSharePolicyFilterOptions(
    isArchived: Boolean? = null,
  ): PlatformDiscountSharePolicyFilterOptions {
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("platform", "discount-share-policy-filter-options")
        if (isArchived != null) parameters.append("isArchived", isArchived.toString())
      }
      headers {
        append(HttpHeaders.Authorization, "PortOne $apiSecret")
      }
      accept(ContentType.Application.Json)
      userAgent(USER_AGENT)
    }
    if (httpResponse.status.value !in 200..299) {
      val httpBody = httpResponse.body<String>()
      val httpBodyDecoded = try {
        json.decodeFromString<GetPlatformDiscountSharePolicyFilterOptionsError>(httpBody)
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
  @JvmName("getPlatformDiscountSharePolicyFilterOptions")
  public fun getPlatformDiscountSharePolicyFilterOptionsFuture(
    isArchived: Boolean? = null,
  ): CompletableFuture<PlatformDiscountSharePolicyFilterOptions> = GlobalScope.future { getPlatformDiscountSharePolicyFilterOptions(isArchived) }


  /**
   * 주어진 아이디에 대응되는 할인 분담의 예약 업데이트를 조회합니다.
   *
   * @param id
   * 할인 분담 정책 아이디
   *
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws PlatformDiscountSharePolicyNotFoundException PlatformDiscountSharePolicyNotFoundError
   * @throws PlatformNotEnabledException 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("getPlatformDiscountSharePolicyScheduleSuspend")
  public suspend fun getPlatformDiscountSharePolicySchedule(
    id: String,
  ): PlatformDiscountSharePolicy {
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("platform", "discount-share-policies", id.toString(), "schedule")
      }
      headers {
        append(HttpHeaders.Authorization, "PortOne $apiSecret")
      }
      accept(ContentType.Application.Json)
      userAgent(USER_AGENT)
    }
    if (httpResponse.status.value !in 200..299) {
      val httpBody = httpResponse.body<String>()
      val httpBodyDecoded = try {
        json.decodeFromString<GetPlatformDiscountSharePolicyScheduleError>(httpBody)
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
  @JvmName("getPlatformDiscountSharePolicySchedule")
  public fun getPlatformDiscountSharePolicyScheduleFuture(
    id: String,
  ): CompletableFuture<PlatformDiscountSharePolicy> = GlobalScope.future { getPlatformDiscountSharePolicySchedule(id) }


  /**
   * 주어진 아이디에 대응되는 할인 분담에 예약 업데이트를 재설정합니다.
   *
   * @param id
   * 할인 분담 정책 아이디
   * @param update
   * 반영할 업데이트 내용
   * @param appliedAt
   * 업데이트 적용 시점
   *
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws PlatformDiscountSharePolicyNotFoundException PlatformDiscountSharePolicyNotFoundError
   * @throws PlatformNotEnabledException 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("rescheduleDiscountSharePolicySuspend")
  public suspend fun rescheduleDiscountSharePolicy(
    id: String,
    update: UpdatePlatformDiscountSharePolicyBody,
    appliedAt: Instant,
  ): ReschedulePlatformDiscountSharePolicyResponse {
    val requestBody = ReschedulePlatformDiscountSharePolicyBody(
      update = update,
      appliedAt = appliedAt,
    )
    val httpResponse = client.put(apiBase) {
      url {
        appendPathSegments("platform", "discount-share-policies", id.toString(), "schedule")
      }
      headers {
        append(HttpHeaders.Authorization, "PortOne $apiSecret")
      }
      contentType(ContentType.Application.Json)
      accept(ContentType.Application.Json)
      userAgent(USER_AGENT)
      setBody(json.encodeToString(requestBody))
    }
    if (httpResponse.status.value !in 200..299) {
      val httpBody = httpResponse.body<String>()
      val httpBodyDecoded = try {
        json.decodeFromString<RescheduleDiscountSharePolicyError>(httpBody)
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
  @JvmName("rescheduleDiscountSharePolicy")
  public fun rescheduleDiscountSharePolicyFuture(
    id: String,
    update: UpdatePlatformDiscountSharePolicyBody,
    appliedAt: Instant,
  ): CompletableFuture<ReschedulePlatformDiscountSharePolicyResponse> = GlobalScope.future { rescheduleDiscountSharePolicy(id, update, appliedAt) }


  /**
   * 주어진 아이디에 대응되는 할인 분담에 업데이트를 예약합니다.
   *
   * @param id
   * 할인 분담 정책 아이디
   * @param update
   * 반영할 업데이트 내용
   * @param appliedAt
   * 업데이트 적용 시점
   *
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws PlatformArchivedDiscountSharePolicyException 보관된 할인 분담 정책을 업데이트하려고 하는 경우
   * @throws PlatformDiscountSharePolicyNotFoundException PlatformDiscountSharePolicyNotFoundError
   * @throws PlatformDiscountSharePolicyScheduleAlreadyExistsException PlatformDiscountSharePolicyScheduleAlreadyExistsError
   * @throws PlatformNotEnabledException 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("scheduleDiscountSharePolicySuspend")
  public suspend fun scheduleDiscountSharePolicy(
    id: String,
    update: UpdatePlatformDiscountSharePolicyBody,
    appliedAt: Instant,
  ): SchedulePlatformDiscountSharePolicyResponse {
    val requestBody = SchedulePlatformDiscountSharePolicyBody(
      update = update,
      appliedAt = appliedAt,
    )
    val httpResponse = client.post(apiBase) {
      url {
        appendPathSegments("platform", "discount-share-policies", id.toString(), "schedule")
      }
      headers {
        append(HttpHeaders.Authorization, "PortOne $apiSecret")
      }
      contentType(ContentType.Application.Json)
      accept(ContentType.Application.Json)
      userAgent(USER_AGENT)
      setBody(json.encodeToString(requestBody))
    }
    if (httpResponse.status.value !in 200..299) {
      val httpBody = httpResponse.body<String>()
      val httpBodyDecoded = try {
        json.decodeFromString<ScheduleDiscountSharePolicyError>(httpBody)
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
  @JvmName("scheduleDiscountSharePolicy")
  public fun scheduleDiscountSharePolicyFuture(
    id: String,
    update: UpdatePlatformDiscountSharePolicyBody,
    appliedAt: Instant,
  ): CompletableFuture<SchedulePlatformDiscountSharePolicyResponse> = GlobalScope.future { scheduleDiscountSharePolicy(id, update, appliedAt) }


  /**
   * 주어진 아이디에 대응되는 할인 분담의 예약 업데이트를 취소합니다.
   *
   * @param id
   * 할인 분담 정책 아이디
   *
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws PlatformDiscountSharePolicyNotFoundException PlatformDiscountSharePolicyNotFoundError
   * @throws PlatformNotEnabledException 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("cancelPlatformDiscountSharePolicyScheduleSuspend")
  public suspend fun cancelPlatformDiscountSharePolicySchedule(
    id: String,
  ): CancelPlatformDiscountSharePolicyScheduleResponse {
    val httpResponse = client.delete(apiBase) {
      url {
        appendPathSegments("platform", "discount-share-policies", id.toString(), "schedule")
      }
      headers {
        append(HttpHeaders.Authorization, "PortOne $apiSecret")
      }
      accept(ContentType.Application.Json)
      userAgent(USER_AGENT)
    }
    if (httpResponse.status.value !in 200..299) {
      val httpBody = httpResponse.body<String>()
      val httpBodyDecoded = try {
        json.decodeFromString<CancelPlatformDiscountSharePolicyScheduleError>(httpBody)
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
  @JvmName("cancelPlatformDiscountSharePolicySchedule")
  public fun cancelPlatformDiscountSharePolicyScheduleFuture(
    id: String,
  ): CompletableFuture<CancelPlatformDiscountSharePolicyScheduleResponse> = GlobalScope.future { cancelPlatformDiscountSharePolicySchedule(id) }


  /**
   * 주어진 아이디에 대응되는 추가 수수료 정책의 예약 업데이트를 조회합니다.
   *
   * @param id
   * 추가 수수료 정책 아이디
   *
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws PlatformAdditionalFeePolicyNotFoundException PlatformAdditionalFeePolicyNotFoundError
   * @throws PlatformNotEnabledException 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("getPlatformAdditionalFeePolicyScheduleSuspend")
  public suspend fun getPlatformAdditionalFeePolicySchedule(
    id: String,
  ): PlatformAdditionalFeePolicy {
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("platform", "additional-fee-policies", id.toString(), "schedule")
      }
      headers {
        append(HttpHeaders.Authorization, "PortOne $apiSecret")
      }
      accept(ContentType.Application.Json)
      userAgent(USER_AGENT)
    }
    if (httpResponse.status.value !in 200..299) {
      val httpBody = httpResponse.body<String>()
      val httpBodyDecoded = try {
        json.decodeFromString<GetPlatformAdditionalFeePolicyScheduleError>(httpBody)
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
  @JvmName("getPlatformAdditionalFeePolicySchedule")
  public fun getPlatformAdditionalFeePolicyScheduleFuture(
    id: String,
  ): CompletableFuture<PlatformAdditionalFeePolicy> = GlobalScope.future { getPlatformAdditionalFeePolicySchedule(id) }


  /**
   * @param id
   * 추가 수수료 정책 아이디
   * @param update
   * 반영할 업데이트 내용
   * @param appliedAt
   * 업데이트 적용 시점
   *
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws PlatformAdditionalFeePolicyNotFoundException PlatformAdditionalFeePolicyNotFoundError
   * @throws PlatformNotEnabledException 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("rescheduleAdditionalFeePolicySuspend")
  public suspend fun rescheduleAdditionalFeePolicy(
    id: String,
    update: UpdatePlatformAdditionalFeePolicyBody,
    appliedAt: Instant,
  ): ReschedulePlatformAdditionalFeePolicyResponse {
    val requestBody = ReschedulePlatformAdditionalFeePolicyBody(
      update = update,
      appliedAt = appliedAt,
    )
    val httpResponse = client.put(apiBase) {
      url {
        appendPathSegments("platform", "additional-fee-policies", id.toString(), "schedule")
      }
      headers {
        append(HttpHeaders.Authorization, "PortOne $apiSecret")
      }
      contentType(ContentType.Application.Json)
      accept(ContentType.Application.Json)
      userAgent(USER_AGENT)
      setBody(json.encodeToString(requestBody))
    }
    if (httpResponse.status.value !in 200..299) {
      val httpBody = httpResponse.body<String>()
      val httpBodyDecoded = try {
        json.decodeFromString<RescheduleAdditionalFeePolicyError>(httpBody)
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
  @JvmName("rescheduleAdditionalFeePolicy")
  public fun rescheduleAdditionalFeePolicyFuture(
    id: String,
    update: UpdatePlatformAdditionalFeePolicyBody,
    appliedAt: Instant,
  ): CompletableFuture<ReschedulePlatformAdditionalFeePolicyResponse> = GlobalScope.future { rescheduleAdditionalFeePolicy(id, update, appliedAt) }


  /**
   * 주어진 아이디에 대응되는 추가 수수료 정책에 업데이트를 예약합니다.
   *
   * @param id
   * 추가 수수료 정책 아이디
   * @param update
   * 반영할 업데이트 내용
   * @param appliedAt
   * 업데이트 적용 시점
   *
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws PlatformAdditionalFeePolicyNotFoundException PlatformAdditionalFeePolicyNotFoundError
   * @throws PlatformAdditionalFeePolicyScheduleAlreadyExistsException PlatformAdditionalFeePolicyScheduleAlreadyExistsError
   * @throws PlatformArchivedAdditionalFeePolicyException 보관된 추가 수수료 정책을 업데이트하려고 하는 경우
   * @throws PlatformNotEnabledException 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("scheduleAdditionalFeePolicySuspend")
  public suspend fun scheduleAdditionalFeePolicy(
    id: String,
    update: UpdatePlatformAdditionalFeePolicyBody,
    appliedAt: Instant,
  ): SchedulePlatformAdditionalFeePolicyResponse {
    val requestBody = SchedulePlatformAdditionalFeePolicyBody(
      update = update,
      appliedAt = appliedAt,
    )
    val httpResponse = client.post(apiBase) {
      url {
        appendPathSegments("platform", "additional-fee-policies", id.toString(), "schedule")
      }
      headers {
        append(HttpHeaders.Authorization, "PortOne $apiSecret")
      }
      contentType(ContentType.Application.Json)
      accept(ContentType.Application.Json)
      userAgent(USER_AGENT)
      setBody(json.encodeToString(requestBody))
    }
    if (httpResponse.status.value !in 200..299) {
      val httpBody = httpResponse.body<String>()
      val httpBodyDecoded = try {
        json.decodeFromString<ScheduleAdditionalFeePolicyError>(httpBody)
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
  @JvmName("scheduleAdditionalFeePolicy")
  public fun scheduleAdditionalFeePolicyFuture(
    id: String,
    update: UpdatePlatformAdditionalFeePolicyBody,
    appliedAt: Instant,
  ): CompletableFuture<SchedulePlatformAdditionalFeePolicyResponse> = GlobalScope.future { scheduleAdditionalFeePolicy(id, update, appliedAt) }


  /**
   * 주어진 아이디에 대응되는 추가 수수료 정책의 예약 업데이트를 취소합니다.
   *
   * @param id
   * 추가 수수료 정책 아이디
   *
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws PlatformAdditionalFeePolicyNotFoundException PlatformAdditionalFeePolicyNotFoundError
   * @throws PlatformNotEnabledException 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("cancelPlatformAdditionalFeePolicyScheduleSuspend")
  public suspend fun cancelPlatformAdditionalFeePolicySchedule(
    id: String,
  ): CancelPlatformAdditionalFeePolicyScheduleResponse {
    val httpResponse = client.delete(apiBase) {
      url {
        appendPathSegments("platform", "additional-fee-policies", id.toString(), "schedule")
      }
      headers {
        append(HttpHeaders.Authorization, "PortOne $apiSecret")
      }
      accept(ContentType.Application.Json)
      userAgent(USER_AGENT)
    }
    if (httpResponse.status.value !in 200..299) {
      val httpBody = httpResponse.body<String>()
      val httpBodyDecoded = try {
        json.decodeFromString<CancelPlatformAdditionalFeePolicyScheduleError>(httpBody)
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
  @JvmName("cancelPlatformAdditionalFeePolicySchedule")
  public fun cancelPlatformAdditionalFeePolicyScheduleFuture(
    id: String,
  ): CompletableFuture<CancelPlatformAdditionalFeePolicyScheduleResponse> = GlobalScope.future { cancelPlatformAdditionalFeePolicySchedule(id) }


  /**
   * 파트너 다건 조회 시 필요한 필터 옵션을 조회합니다.
   *
   * @param isArchived
   * 보관 조회 여부
   *
   * true 이면 보관된 파트너의 필터 옵션을 조회하고, false 이면 보관되지 않은 파트너의 필터 옵션을 조회합니다. 기본값은 false 입니다.
   *
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws PlatformNotEnabledException 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("getPlatformPartnerFilterOptionsSuspend")
  public suspend fun getPlatformPartnerFilterOptions(
    isArchived: Boolean? = null,
  ): PlatformPartnerFilterOptions {
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("platform", "partner-filter-options")
        if (isArchived != null) parameters.append("isArchived", isArchived.toString())
      }
      headers {
        append(HttpHeaders.Authorization, "PortOne $apiSecret")
      }
      accept(ContentType.Application.Json)
      userAgent(USER_AGENT)
    }
    if (httpResponse.status.value !in 200..299) {
      val httpBody = httpResponse.body<String>()
      val httpBodyDecoded = try {
        json.decodeFromString<GetPlatformPartnerFilterOptionsError>(httpBody)
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
  @JvmName("getPlatformPartnerFilterOptions")
  public fun getPlatformPartnerFilterOptionsFuture(
    isArchived: Boolean? = null,
  ): CompletableFuture<PlatformPartnerFilterOptions> = GlobalScope.future { getPlatformPartnerFilterOptions(isArchived) }


  /**
   * 주어진 아이디에 대응되는 파트너의 예약 업데이트를 조회합니다.
   *
   * @param id
   * 파트너 아이디
   *
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws PlatformNotEnabledException 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
   * @throws PlatformPartnerNotFoundException PlatformPartnerNotFoundError
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("getPlatformPartnerScheduleSuspend")
  public suspend fun getPlatformPartnerSchedule(
    id: String,
  ): PlatformPartner {
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("platform", "partners", id.toString(), "schedule")
      }
      headers {
        append(HttpHeaders.Authorization, "PortOne $apiSecret")
      }
      accept(ContentType.Application.Json)
      userAgent(USER_AGENT)
    }
    if (httpResponse.status.value !in 200..299) {
      val httpBody = httpResponse.body<String>()
      val httpBodyDecoded = try {
        json.decodeFromString<GetPlatformPartnerScheduleError>(httpBody)
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
  @JvmName("getPlatformPartnerSchedule")
  public fun getPlatformPartnerScheduleFuture(
    id: String,
  ): CompletableFuture<PlatformPartner> = GlobalScope.future { getPlatformPartnerSchedule(id) }


  /**
   * 주어진 아이디에 대응되는 파트너에 예약 업데이트를 재설정합니다.
   *
   * @param id
   * 파트너 아이디
   * @param update
   * 반영할 업데이트 내용
   * @param appliedAt
   * 업데이트 적용 시점
   *
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws PlatformContractNotFoundException PlatformContractNotFoundError
   * @throws PlatformNotEnabledException 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
   * @throws PlatformPartnerNotFoundException PlatformPartnerNotFoundError
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("reschedulePartnerSuspend")
  public suspend fun reschedulePartner(
    id: String,
    update: UpdatePlatformPartnerBody,
    appliedAt: Instant,
  ): ReschedulePlatformPartnerResponse {
    val requestBody = ReschedulePlatformPartnerBody(
      update = update,
      appliedAt = appliedAt,
    )
    val httpResponse = client.put(apiBase) {
      url {
        appendPathSegments("platform", "partners", id.toString(), "schedule")
      }
      headers {
        append(HttpHeaders.Authorization, "PortOne $apiSecret")
      }
      contentType(ContentType.Application.Json)
      accept(ContentType.Application.Json)
      userAgent(USER_AGENT)
      setBody(json.encodeToString(requestBody))
    }
    if (httpResponse.status.value !in 200..299) {
      val httpBody = httpResponse.body<String>()
      val httpBodyDecoded = try {
        json.decodeFromString<ReschedulePartnerError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is PlatformContractNotFoundError -> throw PlatformContractNotFoundException(httpBodyDecoded)
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
  @JvmName("reschedulePartner")
  public fun reschedulePartnerFuture(
    id: String,
    update: UpdatePlatformPartnerBody,
    appliedAt: Instant,
  ): CompletableFuture<ReschedulePlatformPartnerResponse> = GlobalScope.future { reschedulePartner(id, update, appliedAt) }


  /**
   * 주어진 아이디에 대응되는 파트너에 업데이트를 예약합니다.
   *
   * @param id
   * 파트너 아이디
   * @param update
   * 반영할 업데이트 내용
   * @param appliedAt
   * 업데이트 적용 시점
   *
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws PlatformAccountVerificationAlreadyUsedException 파트너 계좌 검증 아이디를 이미 사용한 경우
   * @throws PlatformAccountVerificationFailedException 파트너 계좌 인증이 실패한 경우
   * @throws PlatformAccountVerificationNotFoundException 파트너 계좌 검증 아이디를 찾을 수 없는 경우
   * @throws PlatformArchivedPartnerException 보관된 파트너를 업데이트하려고 하는 경우
   * @throws PlatformContractNotFoundException PlatformContractNotFoundError
   * @throws PlatformInsufficientDataToChangePartnerTypeException 파트너 타입 수정에 필요한 데이터가 부족한 경우
   * @throws PlatformNotEnabledException 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
   * @throws PlatformPartnerNotFoundException PlatformPartnerNotFoundError
   * @throws PlatformPartnerScheduleAlreadyExistsException PlatformPartnerScheduleAlreadyExistsError
   * @throws PlatformUserDefinedPropertyNotFoundException 사용자 정의 속성이 존재 하지 않는 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("schedulePartnerSuspend")
  public suspend fun schedulePartner(
    id: String,
    update: UpdatePlatformPartnerBody,
    appliedAt: Instant,
  ): SchedulePlatformPartnerResponse {
    val requestBody = SchedulePlatformPartnerBody(
      update = update,
      appliedAt = appliedAt,
    )
    val httpResponse = client.post(apiBase) {
      url {
        appendPathSegments("platform", "partners", id.toString(), "schedule")
      }
      headers {
        append(HttpHeaders.Authorization, "PortOne $apiSecret")
      }
      contentType(ContentType.Application.Json)
      accept(ContentType.Application.Json)
      userAgent(USER_AGENT)
      setBody(json.encodeToString(requestBody))
    }
    if (httpResponse.status.value !in 200..299) {
      val httpBody = httpResponse.body<String>()
      val httpBodyDecoded = try {
        json.decodeFromString<SchedulePartnerError>(httpBody)
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
        is PlatformContractNotFoundError -> throw PlatformContractNotFoundException(httpBodyDecoded)
        is PlatformInsufficientDataToChangePartnerTypeError -> throw PlatformInsufficientDataToChangePartnerTypeException(httpBodyDecoded)
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
  @JvmName("schedulePartner")
  public fun schedulePartnerFuture(
    id: String,
    update: UpdatePlatformPartnerBody,
    appliedAt: Instant,
  ): CompletableFuture<SchedulePlatformPartnerResponse> = GlobalScope.future { schedulePartner(id, update, appliedAt) }


  /**
   * 주어진 아이디에 대응되는 파트너의 예약 업데이트를 취소합니다.
   *
   * @param id
   * 파트너 아이디
   *
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws PlatformNotEnabledException 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
   * @throws PlatformPartnerNotFoundException PlatformPartnerNotFoundError
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("cancelPlatformPartnerScheduleSuspend")
  public suspend fun cancelPlatformPartnerSchedule(
    id: String,
  ): CancelPlatformPartnerScheduleResponse {
    val httpResponse = client.delete(apiBase) {
      url {
        appendPathSegments("platform", "partners", id.toString(), "schedule")
      }
      headers {
        append(HttpHeaders.Authorization, "PortOne $apiSecret")
      }
      accept(ContentType.Application.Json)
      userAgent(USER_AGENT)
    }
    if (httpResponse.status.value !in 200..299) {
      val httpBody = httpResponse.body<String>()
      val httpBodyDecoded = try {
        json.decodeFromString<CancelPlatformPartnerScheduleError>(httpBody)
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
  @JvmName("cancelPlatformPartnerSchedule")
  public fun cancelPlatformPartnerScheduleFuture(
    id: String,
  ): CompletableFuture<CancelPlatformPartnerScheduleResponse> = GlobalScope.future { cancelPlatformPartnerSchedule(id) }


  /**
   * @param filter
   *
   * @param update
   *
   * @param appliedAt
   *
   *
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws PlatformArchivedPartnersCannotBeScheduledException 보관된 파트너들을 예약 업데이트하려고 하는 경우
   * @throws PlatformContractNotFoundException PlatformContractNotFoundError
   * @throws PlatformNotEnabledException 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
   * @throws PlatformPartnerSchedulesAlreadyExistException PlatformPartnerSchedulesAlreadyExistError
   * @throws PlatformUserDefinedPropertyNotFoundException 사용자 정의 속성이 존재 하지 않는 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("schedulePlatformPartnersSuspend")
  public suspend fun schedulePlatformPartners(
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
        appendPathSegments("platform", "partners", "schedule")
      }
      headers {
        append(HttpHeaders.Authorization, "PortOne $apiSecret")
      }
      contentType(ContentType.Application.Json)
      accept(ContentType.Application.Json)
      userAgent(USER_AGENT)
      setBody(json.encodeToString(requestBody))
    }
    if (httpResponse.status.value !in 200..299) {
      val httpBody = httpResponse.body<String>()
      val httpBodyDecoded = try {
        json.decodeFromString<SchedulePlatformPartnersError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is PlatformArchivedPartnersCannotBeScheduledError -> throw PlatformArchivedPartnersCannotBeScheduledException(httpBodyDecoded)
        is PlatformContractNotFoundError -> throw PlatformContractNotFoundException(httpBodyDecoded)
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
  @JvmName("schedulePlatformPartners")
  public fun schedulePlatformPartnersFuture(
    filter: PlatformPartnerFilterInput? = null,
    update: SchedulePlatformPartnersBodyUpdate,
    appliedAt: Instant,
  ): CompletableFuture<SchedulePlatformPartnersResponse> = GlobalScope.future { schedulePlatformPartners(filter, update, appliedAt) }


  /**
   * 주어진 아이디에 대응되는 계약의 예약 업데이트를 조회합니다.
   *
   * @param id
   * 계약 아이디
   *
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws PlatformContractNotFoundException PlatformContractNotFoundError
   * @throws PlatformNotEnabledException 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("getPlatformContractScheduleSuspend")
  public suspend fun getPlatformContractSchedule(
    id: String,
  ): PlatformContract {
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("platform", "contracts", id.toString(), "schedule")
      }
      headers {
        append(HttpHeaders.Authorization, "PortOne $apiSecret")
      }
      accept(ContentType.Application.Json)
      userAgent(USER_AGENT)
    }
    if (httpResponse.status.value !in 200..299) {
      val httpBody = httpResponse.body<String>()
      val httpBodyDecoded = try {
        json.decodeFromString<GetPlatformContractScheduleError>(httpBody)
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
  @JvmName("getPlatformContractSchedule")
  public fun getPlatformContractScheduleFuture(
    id: String,
  ): CompletableFuture<PlatformContract> = GlobalScope.future { getPlatformContractSchedule(id) }


  /**
   * 주어진 아이디에 대응되는 계약에 예약 업데이트를 재설정합니다.
   *
   * @param id
   * 계약 아이디
   * @param update
   * 반영할 업데이트 내용
   * @param appliedAt
   * 업데이트 적용 시점
   *
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws PlatformContractNotFoundException PlatformContractNotFoundError
   * @throws PlatformNotEnabledException 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("rescheduleContractSuspend")
  public suspend fun rescheduleContract(
    id: String,
    update: UpdatePlatformContractBody,
    appliedAt: Instant,
  ): ReschedulePlatformContractResponse {
    val requestBody = ReschedulePlatformContractBody(
      update = update,
      appliedAt = appliedAt,
    )
    val httpResponse = client.put(apiBase) {
      url {
        appendPathSegments("platform", "contracts", id.toString(), "schedule")
      }
      headers {
        append(HttpHeaders.Authorization, "PortOne $apiSecret")
      }
      contentType(ContentType.Application.Json)
      accept(ContentType.Application.Json)
      userAgent(USER_AGENT)
      setBody(json.encodeToString(requestBody))
    }
    if (httpResponse.status.value !in 200..299) {
      val httpBody = httpResponse.body<String>()
      val httpBodyDecoded = try {
        json.decodeFromString<RescheduleContractError>(httpBody)
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
  @JvmName("rescheduleContract")
  public fun rescheduleContractFuture(
    id: String,
    update: UpdatePlatformContractBody,
    appliedAt: Instant,
  ): CompletableFuture<ReschedulePlatformContractResponse> = GlobalScope.future { rescheduleContract(id, update, appliedAt) }


  /**
   * 주어진 아이디에 대응되는 계약에 업데이트를 예약합니다.
   *
   * @param id
   * 계약 아이디
   * @param update
   * 반영할 업데이트 내용
   * @param appliedAt
   * 업데이트 적용 시점
   *
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws PlatformArchivedContractException 보관된 계약을 업데이트하려고 하는 경우
   * @throws PlatformContractNotFoundException PlatformContractNotFoundError
   * @throws PlatformContractScheduleAlreadyExistsException PlatformContractScheduleAlreadyExistsError
   * @throws PlatformNotEnabledException 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("scheduleContractSuspend")
  public suspend fun scheduleContract(
    id: String,
    update: UpdatePlatformContractBody,
    appliedAt: Instant,
  ): SchedulePlatformContractResponse {
    val requestBody = SchedulePlatformContractBody(
      update = update,
      appliedAt = appliedAt,
    )
    val httpResponse = client.post(apiBase) {
      url {
        appendPathSegments("platform", "contracts", id.toString(), "schedule")
      }
      headers {
        append(HttpHeaders.Authorization, "PortOne $apiSecret")
      }
      contentType(ContentType.Application.Json)
      accept(ContentType.Application.Json)
      userAgent(USER_AGENT)
      setBody(json.encodeToString(requestBody))
    }
    if (httpResponse.status.value !in 200..299) {
      val httpBody = httpResponse.body<String>()
      val httpBodyDecoded = try {
        json.decodeFromString<ScheduleContractError>(httpBody)
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
  @JvmName("scheduleContract")
  public fun scheduleContractFuture(
    id: String,
    update: UpdatePlatformContractBody,
    appliedAt: Instant,
  ): CompletableFuture<SchedulePlatformContractResponse> = GlobalScope.future { scheduleContract(id, update, appliedAt) }


  /**
   * 주어진 아이디에 대응되는 계약의 예약 업데이트를 취소합니다.
   *
   * @param id
   * 계약 아이디
   *
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws PlatformContractNotFoundException PlatformContractNotFoundError
   * @throws PlatformNotEnabledException 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("cancelPlatformContractScheduleSuspend")
  public suspend fun cancelPlatformContractSchedule(
    id: String,
  ): CancelPlatformContractScheduleResponse {
    val httpResponse = client.delete(apiBase) {
      url {
        appendPathSegments("platform", "contracts", id.toString(), "schedule")
      }
      headers {
        append(HttpHeaders.Authorization, "PortOne $apiSecret")
      }
      accept(ContentType.Application.Json)
      userAgent(USER_AGENT)
    }
    if (httpResponse.status.value !in 200..299) {
      val httpBody = httpResponse.body<String>()
      val httpBodyDecoded = try {
        json.decodeFromString<CancelPlatformContractScheduleError>(httpBody)
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
  @JvmName("cancelPlatformContractSchedule")
  public fun cancelPlatformContractScheduleFuture(
    id: String,
  ): CompletableFuture<CancelPlatformContractScheduleResponse> = GlobalScope.future { cancelPlatformContractSchedule(id) }

  public val policy: PolicyClient = PolicyClient(apiSecret, apiBase, storeId)
  public val partner: PartnerClient = PartnerClient(apiSecret, apiBase, storeId)
  public val transfer: TransferClient = TransferClient(apiSecret, apiBase, storeId)
  public val partnerSettlement: PartnerSettlementClient = PartnerSettlementClient(apiSecret, apiBase, storeId)
  public val payout: PayoutClient = PayoutClient(apiSecret, apiBase, storeId)
  public val bulkPayout: BulkPayoutClient = BulkPayoutClient(apiSecret, apiBase, storeId)
  public val account: AccountClient = AccountClient(apiSecret, apiBase, storeId)
  public val accountTransfer: AccountTransferClient = AccountTransferClient(apiSecret, apiBase, storeId)
  internal fun close() {
    policy.close()
    partner.close()
    transfer.close()
    partnerSettlement.close()
    payout.close()
    bulkPayout.close()
    account.close()
    accountTransfer.close()
    client.close()
  }
}
