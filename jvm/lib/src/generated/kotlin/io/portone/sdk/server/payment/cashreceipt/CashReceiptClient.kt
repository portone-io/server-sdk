package io.portone.sdk.server.payment.cashreceipt

import io.ktor.client.HttpClient
import io.ktor.client.call.body
import io.ktor.client.engine.okhttp.OkHttp
import io.ktor.client.request.`get`
import io.ktor.client.request.accept
import io.ktor.client.request.headers
import io.ktor.client.request.post
import io.ktor.client.request.setBody
import io.ktor.http.ContentType
import io.ktor.http.HttpHeaders
import io.ktor.http.appendPathSegments
import io.ktor.http.contentType
import io.ktor.http.userAgent
import io.portone.sdk.server.USER_AGENT
import io.portone.sdk.server.common.CashReceiptType
import io.portone.sdk.server.common.Currency
import io.portone.sdk.server.common.PageInput
import io.portone.sdk.server.common.PaymentAmountInput
import io.portone.sdk.server.common.PaymentProductType
import io.portone.sdk.server.errors.CancelCashReceiptError
import io.portone.sdk.server.errors.CancelCashReceiptException
import io.portone.sdk.server.errors.CashReceiptAlreadyIssuedError
import io.portone.sdk.server.errors.CashReceiptAlreadyIssuedException
import io.portone.sdk.server.errors.CashReceiptNotFoundError
import io.portone.sdk.server.errors.CashReceiptNotFoundException
import io.portone.sdk.server.errors.CashReceiptNotIssuedError
import io.portone.sdk.server.errors.CashReceiptNotIssuedException
import io.portone.sdk.server.errors.ChannelNotFoundError
import io.portone.sdk.server.errors.ChannelNotFoundException
import io.portone.sdk.server.errors.ForbiddenError
import io.portone.sdk.server.errors.ForbiddenException
import io.portone.sdk.server.errors.GetCashReceiptError
import io.portone.sdk.server.errors.GetCashReceiptException
import io.portone.sdk.server.errors.GetCashReceiptsError
import io.portone.sdk.server.errors.GetCashReceiptsException
import io.portone.sdk.server.errors.InvalidRequestError
import io.portone.sdk.server.errors.InvalidRequestException
import io.portone.sdk.server.errors.IssueCashReceiptError
import io.portone.sdk.server.errors.IssueCashReceiptException
import io.portone.sdk.server.errors.PgProviderError
import io.portone.sdk.server.errors.PgProviderException
import io.portone.sdk.server.errors.UnauthorizedError
import io.portone.sdk.server.errors.UnauthorizedException
import io.portone.sdk.server.errors.UnknownException
import io.portone.sdk.server.payment.cashreceipt.CancelCashReceiptResponse
import io.portone.sdk.server.payment.cashreceipt.CashReceipt
import io.portone.sdk.server.payment.cashreceipt.CashReceiptFilterInput
import io.portone.sdk.server.payment.cashreceipt.CashReceiptSortInput
import io.portone.sdk.server.payment.cashreceipt.GetCashReceiptsBody
import io.portone.sdk.server.payment.cashreceipt.GetCashReceiptsResponse
import io.portone.sdk.server.payment.cashreceipt.IssueCashReceiptBody
import io.portone.sdk.server.payment.cashreceipt.IssueCashReceiptCustomerInput
import io.portone.sdk.server.payment.cashreceipt.IssueCashReceiptPaymentMethodType
import io.portone.sdk.server.payment.cashreceipt.IssueCashReceiptResponse
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
public class CashReceiptClient(
  private val apiSecret: String,
  private val apiBase: String = "https://api.portone.io",
  private val storeId: String? = null,
): Closeable {
  private val client: HttpClient = HttpClient(OkHttp)

  private val json: Json = Json { ignoreUnknownKeys = true }

  /**
   * 현금 영수증 단건 조회
   *
   * 주어진 결제 아이디에 대응되는 현금 영수증 내역을 조회합니다.
   *
   * @param paymentId
   * 결제 건 아이디
   *
   * @throws GetCashReceiptException
   */
  @JvmName("getCashReceiptByPaymentIdSuspend")
  public suspend fun getCashReceiptByPaymentId(
    paymentId: String,
  ): CashReceipt {
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("payments", paymentId.toString(), "cash-receipt")
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
        json.decodeFromString<GetCashReceiptError.Recognized>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is CashReceiptNotFoundError -> throw CashReceiptNotFoundException(httpBodyDecoded)
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<CashReceipt>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getCashReceiptByPaymentId")
  public fun getCashReceiptByPaymentIdFuture(
    paymentId: String,
  ): CompletableFuture<CashReceipt> = GlobalScope.future { getCashReceiptByPaymentId(paymentId) }


  /**
   * 현금영수증 다건 조회
   *
   * 주어진 조건에 맞는 현금영수증들을 페이지 기반으로 조회합니다.
   *
   * @param page
   * 요청할 페이지 정보
   *
   * 미 입력 시 number: 0, size: 10 으로 기본값이 적용됩니다.
   * @param sort
   * 정렬 조건
   *
   * 미 입력 시 sortBy: ISSUED_AT, sortOrder: DESC 으로 기본값이 적용됩니다.
   * @param filter
   * 조회할 현금영수증 조건 필터
   *
   * @throws GetCashReceiptsException
   */
  @JvmName("getCashReceiptsSuspend")
  public suspend fun getCashReceipts(
    page: PageInput? = null,
    sort: CashReceiptSortInput? = null,
    filter: CashReceiptFilterInput? = null,
  ): GetCashReceiptsResponse {
    val requestBody = GetCashReceiptsBody(
      page = page,
      sort = sort,
      filter = filter,
    )
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("cash-receipts")
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
        json.decodeFromString<GetCashReceiptsError.Recognized>(httpBody)
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
      json.decodeFromString<GetCashReceiptsResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getCashReceipts")
  public fun getCashReceiptsFuture(
    page: PageInput? = null,
    sort: CashReceiptSortInput? = null,
    filter: CashReceiptFilterInput? = null,
  ): CompletableFuture<GetCashReceiptsResponse> = GlobalScope.future { getCashReceipts(page, sort, filter) }


  /**
   * 현금 영수증 수동 발급
   *
   * 현금 영수증 발급을 요청합니다.
   *
   * @param paymentId
   * 결제 건 아이디
   *
   * 외부 결제 건에 대한 수동 발급의 경우, 아이디를 직접 채번하여 입력합니다.
   * @param channelKey
   * 채널 키
   * @param type
   * 현금 영수증 유형
   * @param orderName
   * 주문명
   * @param currency
   * 화폐
   * @param amount
   * 금액 세부 입력 정보
   * @param productType
   * 상품 유형
   * @param customer
   * 고객 정보
   * @param paidAt
   * 결제 일자
   * @param businessRegistrationNumber
   * 사업자등록번호
   *
   * 웰컴페이먼츠의 경우에만 입력합니다.
   * @param paymentMethod
   * 결제 수단
   *
   * 웰컴페이먼츠의 경우에만 입력합니다.
   *
   * @throws IssueCashReceiptException
   */
  @JvmName("issueCashReceiptSuspend")
  public suspend fun issueCashReceipt(
    paymentId: String,
    channelKey: String,
    type: CashReceiptType,
    orderName: String,
    currency: Currency,
    amount: PaymentAmountInput,
    productType: PaymentProductType? = null,
    customer: IssueCashReceiptCustomerInput,
    paidAt: Instant? = null,
    businessRegistrationNumber: String? = null,
    paymentMethod: IssueCashReceiptPaymentMethodType? = null,
  ): IssueCashReceiptResponse {
    val requestBody = IssueCashReceiptBody(
      storeId = storeId,
      paymentId = paymentId,
      channelKey = channelKey,
      type = type,
      orderName = orderName,
      currency = currency,
      amount = amount,
      productType = productType,
      customer = customer,
      paidAt = paidAt,
      businessRegistrationNumber = businessRegistrationNumber,
      paymentMethod = paymentMethod,
    )
    val httpResponse = client.post(apiBase) {
      url {
        appendPathSegments("cash-receipts")
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
        json.decodeFromString<IssueCashReceiptError.Recognized>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is CashReceiptAlreadyIssuedError -> throw CashReceiptAlreadyIssuedException(httpBodyDecoded)
        is ChannelNotFoundError -> throw ChannelNotFoundException(httpBodyDecoded)
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is PgProviderError -> throw PgProviderException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<IssueCashReceiptResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("issueCashReceipt")
  public fun issueCashReceiptFuture(
    paymentId: String,
    channelKey: String,
    type: CashReceiptType,
    orderName: String,
    currency: Currency,
    amount: PaymentAmountInput,
    productType: PaymentProductType? = null,
    customer: IssueCashReceiptCustomerInput,
    paidAt: Instant? = null,
    businessRegistrationNumber: String? = null,
    paymentMethod: IssueCashReceiptPaymentMethodType? = null,
  ): CompletableFuture<IssueCashReceiptResponse> = GlobalScope.future { issueCashReceipt(paymentId, channelKey, type, orderName, currency, amount, productType, customer, paidAt, businessRegistrationNumber, paymentMethod) }


  /**
   * 현금 영수증 취소
   *
   * 현금 영수증 취소를 요청합니다.
   *
   * @param paymentId
   * 결제 건 아이디
   *
   * @throws CancelCashReceiptException
   */
  @JvmName("cancelCashReceiptByPaymentIdSuspend")
  public suspend fun cancelCashReceiptByPaymentId(
    paymentId: String,
  ): CancelCashReceiptResponse {
    val httpResponse = client.post(apiBase) {
      url {
        appendPathSegments("payments", paymentId.toString(), "cash-receipt", "cancel")
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
        json.decodeFromString<CancelCashReceiptError.Recognized>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is CashReceiptNotFoundError -> throw CashReceiptNotFoundException(httpBodyDecoded)
        is CashReceiptNotIssuedError -> throw CashReceiptNotIssuedException(httpBodyDecoded)
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is PgProviderError -> throw PgProviderException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<CancelCashReceiptResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("cancelCashReceiptByPaymentId")
  public fun cancelCashReceiptByPaymentIdFuture(
    paymentId: String,
  ): CompletableFuture<CancelCashReceiptResponse> = GlobalScope.future { cancelCashReceiptByPaymentId(paymentId) }

  override fun close() {
    client.close()
  }
}
