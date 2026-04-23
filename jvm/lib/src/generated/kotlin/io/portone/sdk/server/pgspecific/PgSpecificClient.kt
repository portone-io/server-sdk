package io.portone.sdk.server.pgspecific

import io.ktor.client.HttpClient
import io.ktor.client.call.body
import io.ktor.client.engine.okhttp.OkHttp
import io.ktor.client.plugins.HttpTimeout
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
import io.portone.sdk.server.common.Country
import io.portone.sdk.server.errors.ConfirmPaymentwallDeliveryError
import io.portone.sdk.server.errors.ConfirmPaymentwallDeliveryException
import io.portone.sdk.server.errors.GetKakaopayPaymentOrderError
import io.portone.sdk.server.errors.GetKakaopayPaymentOrderException
import io.portone.sdk.server.errors.InvalidRequestError
import io.portone.sdk.server.errors.InvalidRequestException
import io.portone.sdk.server.errors.PaymentNotFoundError
import io.portone.sdk.server.errors.PaymentNotFoundException
import io.portone.sdk.server.errors.UnauthorizedError
import io.portone.sdk.server.errors.UnauthorizedException
import io.portone.sdk.server.errors.UnknownException
import io.portone.sdk.server.pgspecific.ConfirmPaymentwallDeliveryBody
import io.portone.sdk.server.pgspecific.ConfirmPaymentwallDeliveryResponse
import io.portone.sdk.server.pgspecific.GetKakaopayPaymentOrderResponse
import io.portone.sdk.server.pgspecific.PaymentwallDeliveryStatus
import io.portone.sdk.server.pgspecific.PaymentwallDeliveryType
import java.io.Closeable
import java.time.Instant
import java.util.concurrent.CompletableFuture
import kotlin.Array
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
public class PgSpecificClient(
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
   * 카카오페이 주문 조회 API
   *
   * 주어진 아이디에 대응되는 카카오페이 주문 건을 조회합니다.
   * 해당 API 사용이 필요한 경우 포트원 기술지원팀으로 문의 주시길 바랍니다.
   *
   * @param pgTxId
   * 카카오페이 주문 번호 (tid)
   * @param channelKey
   * 채널 키
   *
   * @throws GetKakaopayPaymentOrderException
   */
  @JvmName("getKakaopayPaymentOrderSuspend")
  public suspend fun getKakaopayPaymentOrder(
    pgTxId: String,
    channelKey: String,
  ): GetKakaopayPaymentOrderResponse {
    val httpResponse = client.get(apiBase) {
      url {
        this.appendPathSegments("kakaopay", "payment", "order")
        this.parameters.append("pgTxId", pgTxId.toString())
        this.parameters.append("channelKey", channelKey.toString())
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
        json.decodeFromString<GetKakaopayPaymentOrderError.Recognized>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<GetKakaopayPaymentOrderResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getKakaopayPaymentOrder")
  public fun getKakaopayPaymentOrderFuture(
    pgTxId: String,
    channelKey: String,
  ): CompletableFuture<GetKakaopayPaymentOrderResponse> = GlobalScope.future { getKakaopayPaymentOrder(pgTxId, channelKey) }


  /**
   * 페이먼트월 배송 정보 등록
   *
   * 배송 정보를 페이먼트월에 등록합니다.
   * 등록된 배송 정보는 차지백 발생 시 고객사의 상품 배송 완료 증빙 자료로 활용되므로, 반드시 연동해야 합니다.
   *
   * @param transactionId
   * 결제 건 포트원 채번 아이디
   * @param deliveryType
   * 배송 유형
   * @param deliveryStatus
   * 배송 상태
   * @param estimatedDeliveryDatetime
   * 배송 완료 예상 일시
   *
   * 배송 유형이 DIGITAL인 경우 현재 시각을 입력해도 무방합니다.
   * @param estimatedUpdateDatetime
   * 배송 상태 업데이트 예정 일시
   *
   * 배송 유형이 DIGITAL인 경우 현재 시각을 입력해도 무방합니다.
   * @param reason
   * 상태 변경 사유
   * @param refundable
   * 환불 가능 여부
   * @param details
   * 상세 설명
   * @param shippingAddressEmail
   * 고객 이메일 주소
   * @param carrierTrackingId
   * 운송장 번호
   *
   * 배송 유형이 PHYSICAL인 경우 필수입니다.
   * @param carrierType
   * 운송사 이름
   *
   * 배송 유형이 PHYSICAL인 경우 필수입니다.
   * @param shippingAddressCountry
   * 수신자 국가
   *
   * 배송 유형이 PHYSICAL인 경우 필수입니다.
   * @param shippingAddressCity
   * 수신자 도시
   *
   * 배송 유형이 PHYSICAL인 경우 필수입니다.
   * @param shippingAddressZip
   * 수신자 우편번호
   *
   * 배송 유형이 PHYSICAL인 경우 필수입니다.
   * @param shippingAddressState
   * 수신자 주
   *
   * 배송 유형이 PHYSICAL인 경우 필수입니다.
   * @param shippingAddressStreet
   * 수신자 도로명 주소
   *
   * 배송 유형이 PHYSICAL인 경우 필수입니다.
   * @param shippingAddressPhone
   * 수신자 전화번호
   *
   * 배송 유형이 PHYSICAL인 경우 필수입니다.
   * @param shippingAddressFirstname
   * 수신자 이름
   *
   * 배송 유형이 PHYSICAL인 경우 필수입니다.
   * @param shippingAddressLastname
   * 수신자 성
   *
   * 배송 유형이 PHYSICAL인 경우 필수입니다.
   * @param attachments
   * 배송 증빙 첨부 파일 URL 목록
   *
   * 배송 증빙 자료의 URL(이미지 등)을 입력합니다. 증빙 자료를 제공하기 어려운 경우 생략할 수 있습니다.
   *
   * @throws ConfirmPaymentwallDeliveryException
   */
  @JvmName("confirmPaymentwallDeliverySuspend")
  public suspend fun confirmPaymentwallDelivery(
    transactionId: String,
    deliveryType: PaymentwallDeliveryType,
    deliveryStatus: PaymentwallDeliveryStatus,
    estimatedDeliveryDatetime: Instant,
    estimatedUpdateDatetime: Instant,
    reason: String? = null,
    refundable: Boolean,
    details: String,
    shippingAddressEmail: String,
    carrierTrackingId: String? = null,
    carrierType: String? = null,
    shippingAddressCountry: Country? = null,
    shippingAddressCity: String? = null,
    shippingAddressZip: String? = null,
    shippingAddressState: String? = null,
    shippingAddressStreet: String? = null,
    shippingAddressPhone: String? = null,
    shippingAddressFirstname: String? = null,
    shippingAddressLastname: String? = null,
    attachments: List<String>? = null,
  ): ConfirmPaymentwallDeliveryResponse {
    val requestBody = ConfirmPaymentwallDeliveryBody(
      transactionId = transactionId,
      deliveryType = deliveryType,
      deliveryStatus = deliveryStatus,
      estimatedDeliveryDatetime = estimatedDeliveryDatetime,
      estimatedUpdateDatetime = estimatedUpdateDatetime,
      reason = reason,
      refundable = refundable,
      details = details,
      shippingAddressEmail = shippingAddressEmail,
      carrierTrackingId = carrierTrackingId,
      carrierType = carrierType,
      shippingAddressCountry = shippingAddressCountry,
      shippingAddressCity = shippingAddressCity,
      shippingAddressZip = shippingAddressZip,
      shippingAddressState = shippingAddressState,
      shippingAddressStreet = shippingAddressStreet,
      shippingAddressPhone = shippingAddressPhone,
      shippingAddressFirstname = shippingAddressFirstname,
      shippingAddressLastname = shippingAddressLastname,
      attachments = attachments,
    )
    val httpResponse = client.post(apiBase) {
      url {
        this.appendPathSegments("paymentwall", "delivery", "confirm")
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
        json.decodeFromString<ConfirmPaymentwallDeliveryError.Recognized>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is PaymentNotFoundError -> throw PaymentNotFoundException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<ConfirmPaymentwallDeliveryResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("confirmPaymentwallDelivery")
  public fun confirmPaymentwallDeliveryFuture(
    transactionId: String,
    deliveryType: PaymentwallDeliveryType,
    deliveryStatus: PaymentwallDeliveryStatus,
    estimatedDeliveryDatetime: Instant,
    estimatedUpdateDatetime: Instant,
    reason: String? = null,
    refundable: Boolean,
    details: String,
    shippingAddressEmail: String,
    carrierTrackingId: String? = null,
    carrierType: String? = null,
    shippingAddressCountry: Country? = null,
    shippingAddressCity: String? = null,
    shippingAddressZip: String? = null,
    shippingAddressState: String? = null,
    shippingAddressStreet: String? = null,
    shippingAddressPhone: String? = null,
    shippingAddressFirstname: String? = null,
    shippingAddressLastname: String? = null,
    attachments: List<String>? = null,
  ): CompletableFuture<ConfirmPaymentwallDeliveryResponse> = GlobalScope.future { confirmPaymentwallDelivery(transactionId, deliveryType, deliveryStatus, estimatedDeliveryDatetime, estimatedUpdateDatetime, reason, refundable, details, shippingAddressEmail, carrierTrackingId, carrierType, shippingAddressCountry, shippingAddressCity, shippingAddressZip, shippingAddressState, shippingAddressStreet, shippingAddressPhone, shippingAddressFirstname, shippingAddressLastname, attachments) }

  override fun close() {
    client.close()
  }
}
