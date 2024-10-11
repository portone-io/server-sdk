package io.portone.sdk.server.payment

import io.portone.sdk.server.common.ChannelGroupSummary
import io.portone.sdk.server.common.Country
import io.portone.sdk.server.common.Currency
import io.portone.sdk.server.common.Customer
import io.portone.sdk.server.common.PaymentProduct
import io.portone.sdk.server.common.PortOneVersion
import io.portone.sdk.server.common.SelectedChannel
import io.portone.sdk.server.payment.PaymentAmount
import io.portone.sdk.server.payment.PaymentEscrow
import io.portone.sdk.server.payment.PaymentMethod
import io.portone.sdk.server.payment.PaymentWebhook
import kotlin.String
import kotlinx.datetime.Instant
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator

/** 결제 건 */
@Serializable
@JsonClassDiscriminator("status")
public sealed interface Payment {
  /** 결제 건 아이디 */
  val id: String
  /** 고객사 아이디 */
  val merchantId: String
  /** 상점 아이디 */
  val storeId: String
  /** 결제수단 정보 */
  val method: PaymentMethod?
  /** 결제 채널 */
  val channel: SelectedChannel
  /** 결제 채널 그룹 정보 */
  val channelGroup: ChannelGroupSummary?
  /** 포트원 버전 */
  val version: PortOneVersion
  /**
   * 결제 예약 건 아이디
   *
   * 결제 예약을 이용한 경우에만 존재
   */
  val scheduleId: String?
  /**
   * 결제 시 사용된 빌링키
   *
   * 빌링키 결제인 경우에만 존재
   */
  val billingKey: String?
  /** 웹훅 발송 내역 */
  val webhooks: Array<PaymentWebhook>?
  /** 결제 요청 시점 */
  val requestedAt: Instant,
  /** 업데이트 시점 */
  val updatedAt: Instant,
  /** 상태 업데이트 시점 */
  val statusChangedAt: Instant,
  /** 주문명 */
  val orderName: String
  /** 결제 금액 관련 세부 정보 */
  val amount: PaymentAmount
  /** 통화 */
  val currency: Currency
  /** 구매자 정보 */
  val customer: Customer
  /** 프로모션 아이디 */
  val promotionId: String?
  /** 문화비 지출 여부 */
  val isCulturalExpense: Boolean?
  /**
   * 에스크로 결제 정보
   *
   * 에스크로 결제인 경우 존재합니다.
   */
  val escrow: PaymentEscrow?
  /** 상품 정보 */
  val products: Array<PaymentProduct>?
  /** 상품 갯수 */
  val productCount: Int?
  /** 사용자 지정 데이터 */
  val customData: String?
  /** 국가 코드 */
  val country: Country?
}
