package io.portone.sdk.server.payment.paymentschedule

import io.ktor.client.HttpClient
import io.ktor.client.call.body
import io.ktor.client.engine.okhttp.OkHttp
import io.ktor.client.request.`get`
import io.ktor.client.request.accept
import io.ktor.client.request.delete
import io.ktor.client.request.headers
import io.ktor.client.request.post
import io.ktor.client.request.setBody
import io.ktor.http.ContentType
import io.ktor.http.HttpHeaders
import io.ktor.http.appendPathSegments
import io.ktor.http.contentType
import io.ktor.http.userAgent
import io.portone.sdk.server.USER_AGENT
import io.portone.sdk.server.common.BillingKeyPaymentInput
import io.portone.sdk.server.common.PageInput
import io.portone.sdk.server.errors.AlreadyPaidOrWaitingError
import io.portone.sdk.server.errors.AlreadyPaidOrWaitingException
import io.portone.sdk.server.errors.BillingKeyAlreadyDeletedError
import io.portone.sdk.server.errors.BillingKeyAlreadyDeletedException
import io.portone.sdk.server.errors.BillingKeyNotFoundError
import io.portone.sdk.server.errors.BillingKeyNotFoundException
import io.portone.sdk.server.errors.CreatePaymentScheduleError
import io.portone.sdk.server.errors.ForbiddenError
import io.portone.sdk.server.errors.ForbiddenException
import io.portone.sdk.server.errors.GetPaymentScheduleError
import io.portone.sdk.server.errors.GetPaymentSchedulesError
import io.portone.sdk.server.errors.InvalidRequestError
import io.portone.sdk.server.errors.InvalidRequestException
import io.portone.sdk.server.errors.PaymentScheduleAlreadyExistsError
import io.portone.sdk.server.errors.PaymentScheduleAlreadyExistsException
import io.portone.sdk.server.errors.PaymentScheduleAlreadyProcessedError
import io.portone.sdk.server.errors.PaymentScheduleAlreadyProcessedException
import io.portone.sdk.server.errors.PaymentScheduleAlreadyRevokedError
import io.portone.sdk.server.errors.PaymentScheduleAlreadyRevokedException
import io.portone.sdk.server.errors.PaymentScheduleNotFoundError
import io.portone.sdk.server.errors.PaymentScheduleNotFoundException
import io.portone.sdk.server.errors.RevokePaymentSchedulesError
import io.portone.sdk.server.errors.SumOfPartsExceedsTotalAmountError
import io.portone.sdk.server.errors.SumOfPartsExceedsTotalAmountException
import io.portone.sdk.server.errors.UnauthorizedError
import io.portone.sdk.server.errors.UnauthorizedException
import io.portone.sdk.server.errors.UnknownException
import io.portone.sdk.server.payment.paymentschedule.CreatePaymentScheduleBody
import io.portone.sdk.server.payment.paymentschedule.CreatePaymentScheduleResponse
import io.portone.sdk.server.payment.paymentschedule.GetPaymentSchedulesBody
import io.portone.sdk.server.payment.paymentschedule.GetPaymentSchedulesResponse
import io.portone.sdk.server.payment.paymentschedule.PaymentSchedule
import io.portone.sdk.server.payment.paymentschedule.PaymentScheduleFilterInput
import io.portone.sdk.server.payment.paymentschedule.PaymentScheduleSortInput
import io.portone.sdk.server.payment.paymentschedule.RevokePaymentSchedulesBody
import io.portone.sdk.server.payment.paymentschedule.RevokePaymentSchedulesResponse
import java.io.Closeable
import java.time.Instant
import java.util.concurrent.CompletableFuture
import kotlin.Array
import kotlin.String
import kotlinx.coroutines.GlobalScope
import kotlinx.coroutines.future.future
import kotlinx.serialization.encodeToString
import kotlinx.serialization.json.Json

public class PaymentScheduleClient internal constructor(
  private val apiSecret: String,
  private val apiBase: String,
  private val storeId: String?,
) {
  private val client: HttpClient = HttpClient(OkHttp)

  private val json: Json = Json { ignoreUnknownKeys = true }

  /**
   * 결제 예약 단건 조회
   *
   * 주어진 아이디에 대응되는 결제 예약 건을 조회합니다.
   *
   * @param paymentScheduleId
   * 조회할 결제 예약 건 아이디
   *
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws PaymentScheduleNotFoundException 결제 예약건이 존재하지 않는 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("getPaymentScheduleSuspend")
  public suspend fun getPaymentSchedule(
    paymentScheduleId: String,
  ): PaymentSchedule {
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("payment-schedules", paymentScheduleId.toString())
        if (storeId != null) parameters.append("storeId", storeId.toString())
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
        json.decodeFromString<GetPaymentScheduleError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is PaymentScheduleNotFoundError -> throw PaymentScheduleNotFoundException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<PaymentSchedule>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getPaymentSchedule")
  public suspend fun getPaymentScheduleFuture(
    paymentScheduleId: String,
  ): CompletableFuture<PaymentSchedule> = GlobalScope.future { getPaymentSchedule(paymentScheduleId) }


  /**
   * 결제 예약 다건 조회
   *
   * 주어진 조건에 맞는 결제 예약 건들을 조회합니다.
   * `filter.from`, `filter.until` 파라미터의 기본값이 결제 시점 기준 지난 90일에 속하는 건을 조회하도록 되어 있으니, 미래 예약 상태의 건을 조회하기 위해서는 해당 파라미터를 직접 설정해 주셔야 합니다.
   *
   * @param page
   * 요청할 페이지 정보
   *
   * 미 입력 시 number: 0, size: 10 으로 기본값이 적용됩니다.
   * @param sort
   * 정렬 조건
   *
   * 미 입력 시 sortBy: TIME_TO_PAY, sortOrder: DESC 으로 기본값이 적용됩니다.
   * @param filter
   * 조회할 결제 예약 건의 조건 필터
   *
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("getPaymentSchedulesSuspend")
  public suspend fun getPaymentSchedules(
    page: PageInput? = null,
    sort: PaymentScheduleSortInput? = null,
    filter: PaymentScheduleFilterInput? = null,
  ): GetPaymentSchedulesResponse {
    val requestBody = GetPaymentSchedulesBody(
      page = page,
      sort = sort,
      filter = filter,
    )
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("payment-schedules")
        parameters.append("requestBody", json.encodeToString(requestBody))
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
        json.decodeFromString<GetPaymentSchedulesError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<GetPaymentSchedulesResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getPaymentSchedules")
  public suspend fun getPaymentSchedulesFuture(
    page: PageInput? = null,
    sort: PaymentScheduleSortInput? = null,
    filter: PaymentScheduleFilterInput? = null,
  ): CompletableFuture<GetPaymentSchedulesResponse> = GlobalScope.future { getPaymentSchedules(page, sort, filter) }


  /**
   * 결제 예약 취소
   *
   * 결제 예약 건을 취소합니다.
   *
   * @param billingKey
   * 빌링키
   * @param scheduleIds
   * 결제 예약 건 아이디 목록
   *
   * @throws BillingKeyAlreadyDeletedException 빌링키가 이미 삭제된 경우
   * @throws BillingKeyNotFoundException 빌링키가 존재하지 않는 경우
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws PaymentScheduleAlreadyProcessedException 결제 예약건이 이미 처리된 경우
   * @throws PaymentScheduleAlreadyRevokedException 결제 예약건이 이미 취소된 경우
   * @throws PaymentScheduleNotFoundException 결제 예약건이 존재하지 않는 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("revokePaymentSchedulesSuspend")
  public suspend fun revokePaymentSchedules(
    billingKey: String? = null,
    scheduleIds: List<String>? = null,
  ): RevokePaymentSchedulesResponse {
    val requestBody = RevokePaymentSchedulesBody(
      storeId = storeId,
      billingKey = billingKey,
      scheduleIds = scheduleIds,
    )
    val httpResponse = client.delete(apiBase) {
      url {
        appendPathSegments("payment-schedules")
        parameters.append("requestBody", json.encodeToString(requestBody))
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
        json.decodeFromString<RevokePaymentSchedulesError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is BillingKeyAlreadyDeletedError -> throw BillingKeyAlreadyDeletedException(httpBodyDecoded)
        is BillingKeyNotFoundError -> throw BillingKeyNotFoundException(httpBodyDecoded)
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is PaymentScheduleAlreadyProcessedError -> throw PaymentScheduleAlreadyProcessedException(httpBodyDecoded)
        is PaymentScheduleAlreadyRevokedError -> throw PaymentScheduleAlreadyRevokedException(httpBodyDecoded)
        is PaymentScheduleNotFoundError -> throw PaymentScheduleNotFoundException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<RevokePaymentSchedulesResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("revokePaymentSchedules")
  public suspend fun revokePaymentSchedulesFuture(
    billingKey: String? = null,
    scheduleIds: List<String>? = null,
  ): CompletableFuture<RevokePaymentSchedulesResponse> = GlobalScope.future { revokePaymentSchedules(billingKey, scheduleIds) }


  /**
   * 결제 예약
   *
   * 결제를 예약합니다.
   *
   * @param paymentId
   * 결제 건 아이디
   * @param payment
   * 빌링키 결제 입력 정보
   * @param timeToPay
   * 결제 예정 시점
   *
   * @throws AlreadyPaidOrWaitingException 결제가 이미 완료되었거나 대기중인 경우
   * @throws BillingKeyAlreadyDeletedException 빌링키가 이미 삭제된 경우
   * @throws BillingKeyNotFoundException 빌링키가 존재하지 않는 경우
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws PaymentScheduleAlreadyExistsException 결제 예약건이 이미 존재하는 경우
   * @throws SumOfPartsExceedsTotalAmountException 면세 금액 등 하위 항목들의 합이 전체 결제 금액을 초과한 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("createPaymentScheduleSuspend")
  public suspend fun createPaymentSchedule(
    paymentId: String,
    payment: BillingKeyPaymentInput,
    timeToPay: Instant,
  ): CreatePaymentScheduleResponse {
    val requestBody = CreatePaymentScheduleBody(
      payment = payment,
      timeToPay = timeToPay,
    )
    val httpResponse = client.post(apiBase) {
      url {
        appendPathSegments("payments", paymentId.toString(), "schedule")
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
        json.decodeFromString<CreatePaymentScheduleError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is AlreadyPaidOrWaitingError -> throw AlreadyPaidOrWaitingException(httpBodyDecoded)
        is BillingKeyAlreadyDeletedError -> throw BillingKeyAlreadyDeletedException(httpBodyDecoded)
        is BillingKeyNotFoundError -> throw BillingKeyNotFoundException(httpBodyDecoded)
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is PaymentScheduleAlreadyExistsError -> throw PaymentScheduleAlreadyExistsException(httpBodyDecoded)
        is SumOfPartsExceedsTotalAmountError -> throw SumOfPartsExceedsTotalAmountException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<CreatePaymentScheduleResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("createPaymentSchedule")
  public suspend fun createPaymentScheduleFuture(
    paymentId: String,
    payment: BillingKeyPaymentInput,
    timeToPay: Instant,
  ): CompletableFuture<CreatePaymentScheduleResponse> = GlobalScope.future { createPaymentSchedule(paymentId, payment, timeToPay) }

  internal fun close() {
    client.close()
  }
}
