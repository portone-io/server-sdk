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
import io.portone.sdk.server.common.PaymentAmountInput
import io.portone.sdk.server.common.PaymentProductType
import io.portone.sdk.server.errors.CancelCashReceiptError
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
import io.portone.sdk.server.errors.InvalidRequestError
import io.portone.sdk.server.errors.InvalidRequestException
import io.portone.sdk.server.errors.IssueCashReceiptError
import io.portone.sdk.server.errors.PgProviderError
import io.portone.sdk.server.errors.PgProviderException
import io.portone.sdk.server.errors.UnauthorizedError
import io.portone.sdk.server.errors.UnauthorizedException
import io.portone.sdk.server.errors.UnknownException
import io.portone.sdk.server.payment.cashreceipt.CancelCashReceiptResponse
import io.portone.sdk.server.payment.cashreceipt.CashReceipt
import io.portone.sdk.server.payment.cashreceipt.IssueCashReceiptBody
import io.portone.sdk.server.payment.cashreceipt.IssueCashReceiptCustomerInput
import io.portone.sdk.server.payment.cashreceipt.IssueCashReceiptResponse
import java.io.Closeable
import java.time.Instant
import java.util.concurrent.CompletableFuture
import kotlin.String
import kotlinx.coroutines.GlobalScope
import kotlinx.coroutines.future.future
import kotlinx.serialization.encodeToString
import kotlinx.serialization.json.Json

public class CashReceiptClient internal constructor(
  private val apiSecret: String,
  private val apiBase: String,
  private val storeId: String?,
) {
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
   * @throws CashReceiptNotFoundException 현금영수증이 존재하지 않는 경우
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
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
        json.decodeFromString<GetCashReceiptError>(httpBody)
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
  public suspend fun getCashReceiptByPaymentIdFuture(
    paymentId: String,
  ): CompletableFuture<CashReceipt> = GlobalScope.future { getCashReceiptByPaymentId(paymentId) }


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
   *
   * @throws CashReceiptAlreadyIssuedException 현금영수증이 이미 발급된 경우
   * @throws ChannelNotFoundException 요청된 채널이 존재하지 않는 경우
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws PgProviderException PG사에서 오류를 전달한 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
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
        json.decodeFromString<IssueCashReceiptError>(httpBody)
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
  public suspend fun issueCashReceiptFuture(
    paymentId: String,
    channelKey: String,
    type: CashReceiptType,
    orderName: String,
    currency: Currency,
    amount: PaymentAmountInput,
    productType: PaymentProductType? = null,
    customer: IssueCashReceiptCustomerInput,
    paidAt: Instant? = null,
  ): CompletableFuture<IssueCashReceiptResponse> = GlobalScope.future { issueCashReceipt(paymentId, channelKey, type, orderName, currency, amount, productType, customer, paidAt) }


  /**
   * 현금 영수증 취소
   *
   * 현금 영수증 취소를 요청합니다.
   *
   * @param paymentId
   * 결제 건 아이디
   *
   * @throws CashReceiptNotFoundException 현금영수증이 존재하지 않는 경우
   * @throws CashReceiptNotIssuedException 현금영수증이 발급되지 않은 경우
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws PgProviderException PG사에서 오류를 전달한 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
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
        json.decodeFromString<CancelCashReceiptError>(httpBody)
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
  public suspend fun cancelCashReceiptByPaymentIdFuture(
    paymentId: String,
  ): CompletableFuture<CancelCashReceiptResponse> = GlobalScope.future { cancelCashReceiptByPaymentId(paymentId) }

  internal fun close() {
    client.close()
  }
}
