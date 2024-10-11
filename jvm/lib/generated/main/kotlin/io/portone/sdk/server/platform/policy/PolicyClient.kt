package io.portone.sdk.server.policy

import io.ktor.client.HttpClient
import io.portone.sdk.server.ArchivePlatformAdditionalFeePolicyResponse
import io.portone.sdk.server.ArchivePlatformContractResponse
import io.portone.sdk.server.ArchivePlatformDiscountSharePolicyResponse
import io.portone.sdk.server.CreatePlatformAdditionalFeePolicyResponse
import io.portone.sdk.server.CreatePlatformContractResponse
import io.portone.sdk.server.CreatePlatformDiscountSharePolicyResponse
import io.portone.sdk.server.GetPlatformAdditionalFeePoliciesResponse
import io.portone.sdk.server.GetPlatformContractsResponse
import io.portone.sdk.server.GetPlatformDiscountSharePoliciesResponse
import io.portone.sdk.server.PlatformAdditionalFeePolicy
import io.portone.sdk.server.PlatformContract
import io.portone.sdk.server.PlatformDiscountSharePolicy
import io.portone.sdk.server.RecoverPlatformAdditionalFeePolicyResponse
import io.portone.sdk.server.RecoverPlatformContractResponse
import io.portone.sdk.server.RecoverPlatformDiscountSharePolicyResponse
import io.portone.sdk.server.UpdatePlatformAdditionalFeePolicyResponse
import io.portone.sdk.server.UpdatePlatformContractResponse
import io.portone.sdk.server.UpdatePlatformDiscountSharePolicyResponse
import io.portone.sdk.server.common.PageInput
import io.portone.sdk.server.platform.PlatformAdditionalFeePolicy
import io.portone.sdk.server.platform.PlatformContract
import io.portone.sdk.server.platform.PlatformDiscountSharePolicy
import io.portone.sdk.server.platform.PlatformFeeInput
import io.portone.sdk.server.platform.PlatformPayer
import io.portone.sdk.server.platform.PlatformSettlementCycleInput
import io.portone.sdk.server.platform.policy.ArchivePlatformAdditionalFeePolicyResponse
import io.portone.sdk.server.platform.policy.ArchivePlatformContractResponse
import io.portone.sdk.server.platform.policy.ArchivePlatformDiscountSharePolicyResponse
import io.portone.sdk.server.platform.policy.CreatePlatformAdditionalFeePolicyResponse
import io.portone.sdk.server.platform.policy.CreatePlatformContractResponse
import io.portone.sdk.server.platform.policy.CreatePlatformDiscountSharePolicyResponse
import io.portone.sdk.server.platform.policy.GetPlatformAdditionalFeePoliciesResponse
import io.portone.sdk.server.platform.policy.GetPlatformContractsResponse
import io.portone.sdk.server.platform.policy.GetPlatformDiscountSharePoliciesResponse
import io.portone.sdk.server.platform.policy.PlatformAdditionalFeePolicyFilterInput
import io.portone.sdk.server.platform.policy.PlatformContractFilterInput
import io.portone.sdk.server.platform.policy.PlatformDiscountSharePolicyFilterInput
import io.portone.sdk.server.platform.policy.RecoverPlatformAdditionalFeePolicyResponse
import io.portone.sdk.server.platform.policy.RecoverPlatformContractResponse
import io.portone.sdk.server.platform.policy.RecoverPlatformDiscountSharePolicyResponse
import io.portone.sdk.server.platform.policy.UpdatePlatformAdditionalFeePolicyResponse
import io.portone.sdk.server.platform.policy.UpdatePlatformContractResponse
import io.portone.sdk.server.platform.policy.UpdatePlatformDiscountSharePolicyResponse
import java.io.Closeable
import kotlin.String
import kotlinx.serialization.json.Json

public class PolicyClient(
  private val apiSecret: String,
  private val storeId: String,
  private val apiBase: String,
) : Closeable {
  private val client: HttpClient = HttpClient(OkHttp)

  private val json: Json = Json { ignoreUnknownKeys = true }

  /**
   * 할인 분담 정책 다건 조회
   *
   * 여러 할인 분담을 조회합니다.
   *
   * @param page
   * 요청할 페이지 정보
   * @param filter
   * 조회할 할인 분담 정책 조건 필터
   *
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws PlatformNotEnabledException 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("getPlatformDiscountSharePoliciesSuspend")
  public suspend fun getPlatformDiscountSharePolicies(
    page: PageInput? = null,
    filter: PlatformDiscountSharePolicyFilterInput? = null,
  ): GetPlatformDiscountSharePoliciesResponse {
    val requestBody = GetPlatformDiscountSharePoliciesBody(
      page = page,
      filter = filter,
    )
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("platform", "discount-share-policies")
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
        json.decodeFromString<GetPlatformDiscountSharePoliciesError>(httpBody)
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
      json.decodeFromString<GetPlatformDiscountSharePoliciesResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownError("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getPlatformDiscountSharePolicies")
  public suspend fun getPlatformDiscountSharePoliciesFuture(
    page: PageInput? = null,
    filter: PlatformDiscountSharePolicyFilterInput? = null,
  ): CompletableFuture<GetPlatformDiscountSharePoliciesResponse> = GlobalScope.future { getPlatformDiscountSharePolicies(page, filter) }


  /**
   * 할인 분담 정책 생성
   *
   * 새로운 할인 분담을 생성합니다.
   *
   * @param id
   * 할인 분담에 부여할 고유 아이디
   *
   * 명시하지 않는 경우 포트원이 임의의 아이디를 발급해드립니다.
   * @param name
   * 할인 분담에 부여할 이름
   * @param partnerShareRate
   * 파트너가 분담할 할인금액의 비율을 의미하는 밀리 퍼센트 단위 (10^-5) 의 음이 아닌 정수이며, 파트너가 부담할 금액은 `할인금액 * partnerShareRate * 10^5` 로 책정합니다.
   * @param memo
   * 해당 할인 분담에 대한 메모 ex) 파트너 브랜드 쿠폰
   *
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws PlatformDiscountSharePolicyAlreadyExistsException PlatformDiscountSharePolicyAlreadyExistsError
   * @throws PlatformNotEnabledException 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("createPlatformDiscountSharePolicySuspend")
  public suspend fun createPlatformDiscountSharePolicy(
    id: string? = null,
    name: string,
    partnerShareRate: Int,
    memo: string? = null,
  ): CreatePlatformDiscountSharePolicyResponse {
    val requestBody = CreatePlatformDiscountSharePolicyBody(
      id = id,
      name = name,
      partnerShareRate = partnerShareRate,
      memo = memo,
    )
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("platform", "discount-share-policies")
      }
      headers {
        append(HttpHeaders.Authorization, "PortOne $apiSecret")
      }
      contentType(ContentType.Application.Json)
      accept(ContentType.Application.Json)
      userAgent(USER_AGENT)
    }
    if (httpResponse.status.value !in 200..299) {
      val httpBody = httpResponse.body<String>()
      val httpBodyDecoded = try {
        json.decodeFromString<CreatePlatformDiscountSharePolicyError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is PlatformDiscountSharePolicyAlreadyExistsError -> throw PlatformDiscountSharePolicyAlreadyExistsException(httpBodyDecoded)
        is PlatformNotEnabledError -> throw PlatformNotEnabledException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<CreatePlatformDiscountSharePolicyResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownError("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("createPlatformDiscountSharePolicy")
  public suspend fun createPlatformDiscountSharePolicyFuture(
    id: string? = null,
    name: string,
    partnerShareRate: Int,
    memo: string? = null,
  ): CompletableFuture<CreatePlatformDiscountSharePolicyResponse> = GlobalScope.future { createPlatformDiscountSharePolicy(id, name, partnerShareRate, memo) }


  /**
   * 할인 분담 정책 조회
   *
   * 주어진 아이디에 대응되는 할인 분담을 조회합니다.
   *
   * @param id
   * 조회할 할인 분담 정책 아이디
   *
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws PlatformDiscountSharePolicyNotFoundException PlatformDiscountSharePolicyNotFoundError
   * @throws PlatformNotEnabledException 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("getPlatformDiscountSharePolicySuspend")
  public suspend fun getPlatformDiscountSharePolicy(
    id: string,
  ): PlatformDiscountSharePolicy {
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("platform", "discount-share-policies", id)
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
        json.decodeFromString<GetPlatformDiscountSharePolicyError>(httpBody)
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
      throw UnknownError("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getPlatformDiscountSharePolicy")
  public suspend fun getPlatformDiscountSharePolicyFuture(
    id: string,
  ): CompletableFuture<PlatformDiscountSharePolicy> = GlobalScope.future { getPlatformDiscountSharePolicy(id) }


  /**
   * 할인 분담 정책 수정
   *
   * 주어진 아이디에 대응되는 할인 분담을 업데이트합니다.
   *
   * @param id
   * 업데이트할 할인 분담 정책 아이디
   * @param name
   * 할인 분담 정책 이름
   * @param partnerShareRate
   * 할인 분담율
   *
   * 파트너가 분담할 할인금액의 비율을 의미하는 밀리 퍼센트 단위 (10^-5) 의 음이 아닌 정수이며, 파트너가 부담할 금액은 `할인금액 * partnerShareRate * 10^5` 로 책정합니다.
   * @param memo
   * 해당 할인 분담에 대한 메모
   *
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws PlatformArchivedDiscountSharePolicyException 보관된 할인 분담 정책을 업데이트하려고 하는 경우
   * @throws PlatformDiscountSharePolicyNotFoundException PlatformDiscountSharePolicyNotFoundError
   * @throws PlatformNotEnabledException 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("updatePlatformDiscountSharePolicySuspend")
  public suspend fun updatePlatformDiscountSharePolicy(
    id: string,
    name: string? = null,
    partnerShareRate: Int? = null,
    memo: string? = null,
  ): UpdatePlatformDiscountSharePolicyResponse {
    val requestBody = UpdatePlatformDiscountSharePolicyBody(
      name = name,
      partnerShareRate = partnerShareRate,
      memo = memo,
    )
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("platform", "discount-share-policies", id)
      }
      headers {
        append(HttpHeaders.Authorization, "PortOne $apiSecret")
      }
      contentType(ContentType.Application.Json)
      accept(ContentType.Application.Json)
      userAgent(USER_AGENT)
    }
    if (httpResponse.status.value !in 200..299) {
      val httpBody = httpResponse.body<String>()
      val httpBodyDecoded = try {
        json.decodeFromString<UpdatePlatformDiscountSharePolicyError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is PlatformArchivedDiscountSharePolicyError -> throw PlatformArchivedDiscountSharePolicyException(httpBodyDecoded)
        is PlatformDiscountSharePolicyNotFoundError -> throw PlatformDiscountSharePolicyNotFoundException(httpBodyDecoded)
        is PlatformNotEnabledError -> throw PlatformNotEnabledException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<UpdatePlatformDiscountSharePolicyResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownError("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("updatePlatformDiscountSharePolicy")
  public suspend fun updatePlatformDiscountSharePolicyFuture(
    id: string,
    name: string? = null,
    partnerShareRate: Int? = null,
    memo: string? = null,
  ): CompletableFuture<UpdatePlatformDiscountSharePolicyResponse> = GlobalScope.future { updatePlatformDiscountSharePolicy(id, name, partnerShareRate, memo) }


  /**
   * 할인 분담 정책 보관
   *
   * 주어진 아이디에 대응되는 할인 분담을 보관합니다.
   *
   * @param id
   * 할인 분담 아이디
   *
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws PlatformCannotArchiveScheduledDiscountSharePolicyException 예약된 업데이트가 있는 할인 분담 정책을 보관하려고 하는 경우
   * @throws PlatformDiscountSharePolicyNotFoundException PlatformDiscountSharePolicyNotFoundError
   * @throws PlatformNotEnabledException 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("archivePlatformDiscountSharePolicySuspend")
  public suspend fun archivePlatformDiscountSharePolicy(
    id: string,
  ): ArchivePlatformDiscountSharePolicyResponse {
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("platform", "discount-share-policies", id, "archive")
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
        json.decodeFromString<ArchivePlatformDiscountSharePolicyError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is PlatformCannotArchiveScheduledDiscountSharePolicyError -> throw PlatformCannotArchiveScheduledDiscountSharePolicyException(httpBodyDecoded)
        is PlatformDiscountSharePolicyNotFoundError -> throw PlatformDiscountSharePolicyNotFoundException(httpBodyDecoded)
        is PlatformNotEnabledError -> throw PlatformNotEnabledException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<ArchivePlatformDiscountSharePolicyResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownError("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("archivePlatformDiscountSharePolicy")
  public suspend fun archivePlatformDiscountSharePolicyFuture(
    id: string,
  ): CompletableFuture<ArchivePlatformDiscountSharePolicyResponse> = GlobalScope.future { archivePlatformDiscountSharePolicy(id) }


  /**
   * 할인 분담 정책 복원
   *
   * 주어진 아이디에 대응되는 할인 분담을 복원합니다.
   *
   * @param id
   * 할인 분담 아이디
   *
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws PlatformDiscountSharePolicyNotFoundException PlatformDiscountSharePolicyNotFoundError
   * @throws PlatformNotEnabledException 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("recoverPlatformDiscountSharePolicySuspend")
  public suspend fun recoverPlatformDiscountSharePolicy(
    id: string,
  ): RecoverPlatformDiscountSharePolicyResponse {
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("platform", "discount-share-policies", id, "recover")
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
        json.decodeFromString<RecoverPlatformDiscountSharePolicyError>(httpBody)
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
      json.decodeFromString<RecoverPlatformDiscountSharePolicyResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownError("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("recoverPlatformDiscountSharePolicy")
  public suspend fun recoverPlatformDiscountSharePolicyFuture(
    id: string,
  ): CompletableFuture<RecoverPlatformDiscountSharePolicyResponse> = GlobalScope.future { recoverPlatformDiscountSharePolicy(id) }


  /**
   * 추가 수수료 정책 다건 조회
   *
   * 여러 추가 수수료 정책을 조회합니다.
   *
   * @param page
   * 요청할 페이지 정보
   * @param filter
   * 조회할 추가 수수료 정책 조건 필터
   *
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws PlatformNotEnabledException 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("getPlatformAdditionalFeePoliciesSuspend")
  public suspend fun getPlatformAdditionalFeePolicies(
    page: PageInput? = null,
    filter: PlatformAdditionalFeePolicyFilterInput? = null,
  ): GetPlatformAdditionalFeePoliciesResponse {
    val requestBody = GetPlatformAdditionalFeePoliciesBody(
      page = page,
      filter = filter,
    )
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("platform", "additional-fee-policies")
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
        json.decodeFromString<GetPlatformAdditionalFeePoliciesError>(httpBody)
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
      json.decodeFromString<GetPlatformAdditionalFeePoliciesResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownError("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getPlatformAdditionalFeePolicies")
  public suspend fun getPlatformAdditionalFeePoliciesFuture(
    page: PageInput? = null,
    filter: PlatformAdditionalFeePolicyFilterInput? = null,
  ): CompletableFuture<GetPlatformAdditionalFeePoliciesResponse> = GlobalScope.future { getPlatformAdditionalFeePolicies(page, filter) }


  /**
   * 추가 수수료 정책 생성
   *
   * 새로운 추가 수수료 정책을 생성합니다.
   *
   * @param id
   * 생성할 추가 수수료 정책 아이디
   *
   * 명시하지 않으면 id 가 임의로 생성됩니다.
   * @param name
   * 이름
   * @param fee
   * 수수료 정보
   * @param memo
   * 메모
   * @param vatPayer
   * 부가세 부담 주체
   *
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws PlatformAdditionalFeePolicyAlreadyExistsException PlatformAdditionalFeePolicyAlreadyExistsError
   * @throws PlatformNotEnabledException 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("createPlatformAdditionalFeePolicySuspend")
  public suspend fun createPlatformAdditionalFeePolicy(
    id: string? = null,
    name: string,
    fee: PlatformFeeInput,
    memo: string? = null,
    vatPayer: PlatformPayer,
  ): CreatePlatformAdditionalFeePolicyResponse {
    val requestBody = CreatePlatformAdditionalFeePolicyBody(
      id = id,
      name = name,
      fee = fee,
      memo = memo,
      vatPayer = vatPayer,
    )
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("platform", "additional-fee-policies")
      }
      headers {
        append(HttpHeaders.Authorization, "PortOne $apiSecret")
      }
      contentType(ContentType.Application.Json)
      accept(ContentType.Application.Json)
      userAgent(USER_AGENT)
    }
    if (httpResponse.status.value !in 200..299) {
      val httpBody = httpResponse.body<String>()
      val httpBodyDecoded = try {
        json.decodeFromString<CreatePlatformAdditionalFeePolicyError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is PlatformAdditionalFeePolicyAlreadyExistsError -> throw PlatformAdditionalFeePolicyAlreadyExistsException(httpBodyDecoded)
        is PlatformNotEnabledError -> throw PlatformNotEnabledException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<CreatePlatformAdditionalFeePolicyResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownError("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("createPlatformAdditionalFeePolicy")
  public suspend fun createPlatformAdditionalFeePolicyFuture(
    id: string? = null,
    name: string,
    fee: PlatformFeeInput,
    memo: string? = null,
    vatPayer: PlatformPayer,
  ): CompletableFuture<CreatePlatformAdditionalFeePolicyResponse> = GlobalScope.future { createPlatformAdditionalFeePolicy(id, name, fee, memo, vatPayer) }


  /**
   * 추가 수수료 정책 조회
   *
   * 주어진 아이디에 대응되는 추가 수수료 정책을 조회합니다.
   *
   * @param id
   * 조회할 추가 수수료 정책 아이디
   *
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws PlatformAdditionalFeePolicyNotFoundException PlatformAdditionalFeePolicyNotFoundError
   * @throws PlatformNotEnabledException 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("getPlatformAdditionalFeePolicySuspend")
  public suspend fun getPlatformAdditionalFeePolicy(
    id: string,
  ): PlatformAdditionalFeePolicy {
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("platform", "additional-fee-policies", id)
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
        json.decodeFromString<GetPlatformAdditionalFeePolicyError>(httpBody)
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
      throw UnknownError("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getPlatformAdditionalFeePolicy")
  public suspend fun getPlatformAdditionalFeePolicyFuture(
    id: string,
  ): CompletableFuture<PlatformAdditionalFeePolicy> = GlobalScope.future { getPlatformAdditionalFeePolicy(id) }


  /**
   * 추가 수수료 정책 수정
   *
   * 주어진 아이디에 대응되는 추가 수수료 정책을 업데이트합니다.
   *
   * @param id
   * 업데이트할 추가 수수료 정책 아이디
   * @param fee
   * 책정 수수료
   * @param name
   * 추가 수수료 정책 이름
   * @param memo
   * 해당 추가 수수료 정책에 대한 메모
   * @param vatPayer
   * 부가세를 부담할 주체
   *
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws PlatformAdditionalFeePolicyNotFoundException PlatformAdditionalFeePolicyNotFoundError
   * @throws PlatformArchivedAdditionalFeePolicyException 보관된 추가 수수료 정책을 업데이트하려고 하는 경우
   * @throws PlatformNotEnabledException 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("updatePlatformAdditionalFeePolicySuspend")
  public suspend fun updatePlatformAdditionalFeePolicy(
    id: string,
    fee: PlatformFeeInput? = null,
    name: string? = null,
    memo: string? = null,
    vatPayer: PlatformPayer? = null,
  ): UpdatePlatformAdditionalFeePolicyResponse {
    val requestBody = UpdatePlatformAdditionalFeePolicyBody(
      fee = fee,
      name = name,
      memo = memo,
      vatPayer = vatPayer,
    )
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("platform", "additional-fee-policies", id)
      }
      headers {
        append(HttpHeaders.Authorization, "PortOne $apiSecret")
      }
      contentType(ContentType.Application.Json)
      accept(ContentType.Application.Json)
      userAgent(USER_AGENT)
    }
    if (httpResponse.status.value !in 200..299) {
      val httpBody = httpResponse.body<String>()
      val httpBodyDecoded = try {
        json.decodeFromString<UpdatePlatformAdditionalFeePolicyError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is PlatformAdditionalFeePolicyNotFoundError -> throw PlatformAdditionalFeePolicyNotFoundException(httpBodyDecoded)
        is PlatformArchivedAdditionalFeePolicyError -> throw PlatformArchivedAdditionalFeePolicyException(httpBodyDecoded)
        is PlatformNotEnabledError -> throw PlatformNotEnabledException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<UpdatePlatformAdditionalFeePolicyResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownError("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("updatePlatformAdditionalFeePolicy")
  public suspend fun updatePlatformAdditionalFeePolicyFuture(
    id: string,
    fee: PlatformFeeInput? = null,
    name: string? = null,
    memo: string? = null,
    vatPayer: PlatformPayer? = null,
  ): CompletableFuture<UpdatePlatformAdditionalFeePolicyResponse> = GlobalScope.future { updatePlatformAdditionalFeePolicy(id, fee, name, memo, vatPayer) }


  /**
   * 추가 수수료 정책 보관
   *
   * 주어진 아이디에 대응되는 추가 수수료 정책을 보관합니다.
   *
   * @param id
   * 추가 수수료 정책 아이디
   *
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws PlatformAdditionalFeePolicyNotFoundException PlatformAdditionalFeePolicyNotFoundError
   * @throws PlatformCannotArchiveScheduledAdditionalFeePolicyException 예약된 업데이트가 있는 추가 수수료 정책을 보관하려고 하는 경우
   * @throws PlatformNotEnabledException 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("archivePlatformAdditionalFeePolicySuspend")
  public suspend fun archivePlatformAdditionalFeePolicy(
    id: string,
  ): ArchivePlatformAdditionalFeePolicyResponse {
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("platform", "additional-fee-policies", id, "archive")
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
        json.decodeFromString<ArchivePlatformAdditionalFeePolicyError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is PlatformAdditionalFeePolicyNotFoundError -> throw PlatformAdditionalFeePolicyNotFoundException(httpBodyDecoded)
        is PlatformCannotArchiveScheduledAdditionalFeePolicyError -> throw PlatformCannotArchiveScheduledAdditionalFeePolicyException(httpBodyDecoded)
        is PlatformNotEnabledError -> throw PlatformNotEnabledException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<ArchivePlatformAdditionalFeePolicyResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownError("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("archivePlatformAdditionalFeePolicy")
  public suspend fun archivePlatformAdditionalFeePolicyFuture(
    id: string,
  ): CompletableFuture<ArchivePlatformAdditionalFeePolicyResponse> = GlobalScope.future { archivePlatformAdditionalFeePolicy(id) }


  /**
   * 추가 수수료 정책 복원
   *
   * 주어진 아이디에 대응되는 추가 수수료 정책을 복원합니다.
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
  @JvmName("recoverPlatformAdditionalFeePolicySuspend")
  public suspend fun recoverPlatformAdditionalFeePolicy(
    id: string,
  ): RecoverPlatformAdditionalFeePolicyResponse {
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("platform", "additional-fee-policies", id, "recover")
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
        json.decodeFromString<RecoverPlatformAdditionalFeePolicyError>(httpBody)
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
      json.decodeFromString<RecoverPlatformAdditionalFeePolicyResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownError("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("recoverPlatformAdditionalFeePolicy")
  public suspend fun recoverPlatformAdditionalFeePolicyFuture(
    id: string,
  ): CompletableFuture<RecoverPlatformAdditionalFeePolicyResponse> = GlobalScope.future { recoverPlatformAdditionalFeePolicy(id) }


  /**
   * 계약 다건 조회
   *
   * 여러 계약을 조회합니다.
   *
   * @param page
   * 요청할 페이지 정보
   * @param filter
   * 조회할 계약 조건 필터
   *
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws PlatformNotEnabledException 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("getPlatformContractsSuspend")
  public suspend fun getPlatformContracts(
    page: PageInput? = null,
    filter: PlatformContractFilterInput? = null,
  ): GetPlatformContractsResponse {
    val requestBody = GetPlatformContractsBody(
      page = page,
      filter = filter,
    )
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("platform", "contracts")
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
        json.decodeFromString<GetPlatformContractsError>(httpBody)
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
      json.decodeFromString<GetPlatformContractsResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownError("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getPlatformContracts")
  public suspend fun getPlatformContractsFuture(
    page: PageInput? = null,
    filter: PlatformContractFilterInput? = null,
  ): CompletableFuture<GetPlatformContractsResponse> = GlobalScope.future { getPlatformContracts(page, filter) }


  /**
   * 계약 생성
   *
   * 새로운 계약을 생성합니다.
   *
   * @param id
   * 계약에 부여할 고유 아이디
   *
   * 명시하지 않는 경우 포트원이 임의의 아이디를 발급해드립니다.
   * @param name
   * 계약 이름
   * @param memo
   * 계약 내부 표기를 위한 메모
   * @param platformFee
   * 중개수수료
   * @param settlementCycle
   * 정산 주기
   * @param platformFeeVatPayer
   * 중개수수료에 대한 부가세 부담 주체
   * @param subtractPaymentVatAmount
   * 정산 시 결제금액 부가세 감액 여부
   *
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws PlatformContractAlreadyExistsException PlatformContractAlreadyExistsError
   * @throws PlatformNotEnabledException 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("createPlatformContractSuspend")
  public suspend fun createPlatformContract(
    id: string? = null,
    name: string,
    memo: string? = null,
    platformFee: PlatformFeeInput,
    settlementCycle: PlatformSettlementCycleInput,
    platformFeeVatPayer: PlatformPayer,
    subtractPaymentVatAmount: Boolean,
  ): CreatePlatformContractResponse {
    val requestBody = CreatePlatformContractBody(
      id = id,
      name = name,
      memo = memo,
      platformFee = platformFee,
      settlementCycle = settlementCycle,
      platformFeeVatPayer = platformFeeVatPayer,
      subtractPaymentVatAmount = subtractPaymentVatAmount,
    )
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("platform", "contracts")
      }
      headers {
        append(HttpHeaders.Authorization, "PortOne $apiSecret")
      }
      contentType(ContentType.Application.Json)
      accept(ContentType.Application.Json)
      userAgent(USER_AGENT)
    }
    if (httpResponse.status.value !in 200..299) {
      val httpBody = httpResponse.body<String>()
      val httpBodyDecoded = try {
        json.decodeFromString<CreatePlatformContractError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is PlatformContractAlreadyExistsError -> throw PlatformContractAlreadyExistsException(httpBodyDecoded)
        is PlatformNotEnabledError -> throw PlatformNotEnabledException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<CreatePlatformContractResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownError("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("createPlatformContract")
  public suspend fun createPlatformContractFuture(
    id: string? = null,
    name: string,
    memo: string? = null,
    platformFee: PlatformFeeInput,
    settlementCycle: PlatformSettlementCycleInput,
    platformFeeVatPayer: PlatformPayer,
    subtractPaymentVatAmount: Boolean,
  ): CompletableFuture<CreatePlatformContractResponse> = GlobalScope.future { createPlatformContract(id, name, memo, platformFee, settlementCycle, platformFeeVatPayer, subtractPaymentVatAmount) }


  /**
   * 계약 조회
   *
   * 주어진 아이디에 대응되는 계약을 조회합니다.
   *
   * @param id
   * 조회할 계약 아이디
   *
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws PlatformContractNotFoundException PlatformContractNotFoundError
   * @throws PlatformNotEnabledException 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("getPlatformContractSuspend")
  public suspend fun getPlatformContract(
    id: string,
  ): PlatformContract {
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("platform", "contracts", id)
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
        json.decodeFromString<GetPlatformContractError>(httpBody)
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
      throw UnknownError("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getPlatformContract")
  public suspend fun getPlatformContractFuture(
    id: string,
  ): CompletableFuture<PlatformContract> = GlobalScope.future { getPlatformContract(id) }


  /**
   * 계약 수정
   *
   * 주어진 아이디에 대응되는 계약을 업데이트합니다.
   *
   * @param id
   * 업데이트할 계약 아이디
   * @param name
   * 계약 이름
   * @param memo
   * 계약 내부 표기를 위한 메모
   * @param platformFee
   * 중개수수료
   * @param settlementCycle
   * 정산 주기
   * @param platformFeeVatPayer
   * 중개수수료에 대한 부가세 부담 주체
   * @param subtractPaymentVatAmount
   * 정산 시 결제금액 부가세 감액 여부
   *
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws PlatformArchivedContractException 보관된 계약을 업데이트하려고 하는 경우
   * @throws PlatformContractNotFoundException PlatformContractNotFoundError
   * @throws PlatformNotEnabledException 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("updatePlatformContractSuspend")
  public suspend fun updatePlatformContract(
    id: string,
    name: string? = null,
    memo: string? = null,
    platformFee: PlatformFeeInput? = null,
    settlementCycle: PlatformSettlementCycleInput? = null,
    platformFeeVatPayer: PlatformPayer? = null,
    subtractPaymentVatAmount: Boolean? = null,
  ): UpdatePlatformContractResponse {
    val requestBody = UpdatePlatformContractBody(
      name = name,
      memo = memo,
      platformFee = platformFee,
      settlementCycle = settlementCycle,
      platformFeeVatPayer = platformFeeVatPayer,
      subtractPaymentVatAmount = subtractPaymentVatAmount,
    )
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("platform", "contracts", id)
      }
      headers {
        append(HttpHeaders.Authorization, "PortOne $apiSecret")
      }
      contentType(ContentType.Application.Json)
      accept(ContentType.Application.Json)
      userAgent(USER_AGENT)
    }
    if (httpResponse.status.value !in 200..299) {
      val httpBody = httpResponse.body<String>()
      val httpBodyDecoded = try {
        json.decodeFromString<UpdatePlatformContractError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is PlatformArchivedContractError -> throw PlatformArchivedContractException(httpBodyDecoded)
        is PlatformContractNotFoundError -> throw PlatformContractNotFoundException(httpBodyDecoded)
        is PlatformNotEnabledError -> throw PlatformNotEnabledException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<UpdatePlatformContractResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownError("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("updatePlatformContract")
  public suspend fun updatePlatformContractFuture(
    id: string,
    name: string? = null,
    memo: string? = null,
    platformFee: PlatformFeeInput? = null,
    settlementCycle: PlatformSettlementCycleInput? = null,
    platformFeeVatPayer: PlatformPayer? = null,
    subtractPaymentVatAmount: Boolean? = null,
  ): CompletableFuture<UpdatePlatformContractResponse> = GlobalScope.future { updatePlatformContract(id, name, memo, platformFee, settlementCycle, platformFeeVatPayer, subtractPaymentVatAmount) }


  /**
   * 계약 보관
   *
   * 주어진 아이디에 대응되는 계약을 보관합니다.
   *
   * @param id
   * 계약 아이디
   *
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws PlatformCannotArchiveScheduledContractException 예약된 업데이트가 있는 계약을 보관하려고 하는 경우
   * @throws PlatformContractNotFoundException PlatformContractNotFoundError
   * @throws PlatformNotEnabledException 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("archivePlatformContractSuspend")
  public suspend fun archivePlatformContract(
    id: string,
  ): ArchivePlatformContractResponse {
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("platform", "contracts", id, "archive")
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
        json.decodeFromString<ArchivePlatformContractError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is PlatformCannotArchiveScheduledContractError -> throw PlatformCannotArchiveScheduledContractException(httpBodyDecoded)
        is PlatformContractNotFoundError -> throw PlatformContractNotFoundException(httpBodyDecoded)
        is PlatformNotEnabledError -> throw PlatformNotEnabledException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<ArchivePlatformContractResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownError("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("archivePlatformContract")
  public suspend fun archivePlatformContractFuture(
    id: string,
  ): CompletableFuture<ArchivePlatformContractResponse> = GlobalScope.future { archivePlatformContract(id) }


  /**
   * 계약 복원
   *
   * 주어진 아이디에 대응되는 계약을 복원합니다.
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
  @JvmName("recoverPlatformContractSuspend")
  public suspend fun recoverPlatformContract(
    id: string,
  ): RecoverPlatformContractResponse {
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("platform", "contracts", id, "recover")
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
        json.decodeFromString<RecoverPlatformContractError>(httpBody)
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
      json.decodeFromString<RecoverPlatformContractResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownError("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("recoverPlatformContract")
  public suspend fun recoverPlatformContractFuture(
    id: string,
  ): CompletableFuture<RecoverPlatformContractResponse> = GlobalScope.future { recoverPlatformContract(id) }

  override fun close() {
    client.close()
  }
}
