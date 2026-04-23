package io.portone.sdk.server.pgspecific

import io.portone.sdk.server.common.Country
import io.portone.sdk.server.pgspecific.PaymentwallDeliveryStatus
import io.portone.sdk.server.pgspecific.PaymentwallDeliveryType
import io.portone.sdk.server.serializers.InstantSerializer
import java.time.Instant
import kotlin.Array
import kotlin.String
import kotlinx.serialization.Serializable

/** 페이먼트월 배송 정보 등록 입력 정보 */
@Serializable
internal data class ConfirmPaymentwallDeliveryBody(
  /** 결제 건 포트원 채번 아이디 */
  val transactionId: String,
  /** 배송 유형 */
  val deliveryType: PaymentwallDeliveryType,
  /** 배송 상태 */
  val deliveryStatus: PaymentwallDeliveryStatus,
  /**
   * 배송 완료 예상 일시
   *
   * 배송 유형이 DIGITAL인 경우 현재 시각을 입력해도 무방합니다.
   */
  val estimatedDeliveryDatetime: @Serializable(InstantSerializer::class) Instant,
  /**
   * 배송 상태 업데이트 예정 일시
   *
   * 배송 유형이 DIGITAL인 경우 현재 시각을 입력해도 무방합니다.
   */
  val estimatedUpdateDatetime: @Serializable(InstantSerializer::class) Instant,
  /** 상태 변경 사유 */
  val reason: String? = null,
  /** 환불 가능 여부 */
  val refundable: Boolean,
  /** 상세 설명 */
  val details: String,
  /** 고객 이메일 주소 */
  val shippingAddressEmail: String,
  /**
   * 운송장 번호
   *
   * 배송 유형이 PHYSICAL인 경우 필수입니다.
   */
  val carrierTrackingId: String? = null,
  /**
   * 운송사 이름
   *
   * 배송 유형이 PHYSICAL인 경우 필수입니다.
   */
  val carrierType: String? = null,
  /**
   * 수신자 국가
   *
   * 배송 유형이 PHYSICAL인 경우 필수입니다.
   */
  val shippingAddressCountry: Country? = null,
  /**
   * 수신자 도시
   *
   * 배송 유형이 PHYSICAL인 경우 필수입니다.
   */
  val shippingAddressCity: String? = null,
  /**
   * 수신자 우편번호
   *
   * 배송 유형이 PHYSICAL인 경우 필수입니다.
   */
  val shippingAddressZip: String? = null,
  /**
   * 수신자 주
   *
   * 배송 유형이 PHYSICAL인 경우 필수입니다.
   */
  val shippingAddressState: String? = null,
  /**
   * 수신자 도로명 주소
   *
   * 배송 유형이 PHYSICAL인 경우 필수입니다.
   */
  val shippingAddressStreet: String? = null,
  /**
   * 수신자 전화번호
   *
   * 배송 유형이 PHYSICAL인 경우 필수입니다.
   */
  val shippingAddressPhone: String? = null,
  /**
   * 수신자 이름
   *
   * 배송 유형이 PHYSICAL인 경우 필수입니다.
   */
  val shippingAddressFirstname: String? = null,
  /**
   * 수신자 성
   *
   * 배송 유형이 PHYSICAL인 경우 필수입니다.
   */
  val shippingAddressLastname: String? = null,
  /**
   * 배송 증빙 첨부 파일 URL 목록
   *
   * 배송 증빙 자료의 URL(이미지 등)을 입력합니다. 증빙 자료를 제공하기 어려운 경우 생략할 수 있습니다.
   */
  val attachments: List<String>? = null,
)


