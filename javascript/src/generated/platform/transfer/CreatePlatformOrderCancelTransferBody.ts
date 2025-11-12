import type { CreatePlatformOrderCancelTransferBodyDiscount } from "./../../platform/transfer/CreatePlatformOrderCancelTransferBodyDiscount"
import type { CreatePlatformOrderCancelTransferBodyExternalCancellationDetail } from "./../../platform/transfer/CreatePlatformOrderCancelTransferBodyExternalCancellationDetail"
import type { CreatePlatformOrderCancelTransferBodyOrderDetail } from "./../../platform/transfer/CreatePlatformOrderCancelTransferBodyOrderDetail"
import type { PlatformUserDefinedPropertyKeyValue } from "./../../platform/transfer/PlatformUserDefinedPropertyKeyValue"
/**
 * 주문 취소 정산 등록을 위한 입력 정보
 *
 * 하나의 payment에 하나의 정산 건만 존재하는 경우에는 (partnerId, paymentId)로 취소 정산을 등록하실 수 있습니다.
 * 하나의 payment에 여러 개의 정산 건이 존재하는 경우에는 transferId를 필수로 입력해야 합니다.
 * transferId를 입력한 경우 (partnerId, paymentId)는 생략 가능합니다.
 */
export type CreatePlatformOrderCancelTransferBody = {
	/** 파트너 아이디 */
	partnerId?: string
	/** 결제 아이디 */
	paymentId?: string
	/** 정산건 아이디 */
	transferId?: string
	/** 취소 내역 아이디 */
	cancellationId: string
	/** 메모 */
	memo?: string
	/** 주문 취소 정보 */
	orderDetail?: CreatePlatformOrderCancelTransferBodyOrderDetail
	/**
	 * 주문 취소 면세 금액
	 *
	 * 주문 취소 항목과 취소 면세 금액을 같이 전달하시면 최종 취소 면세 금액은 주문 취소 항목의 면세 금액이 아닌 전달해주신 취소 면세 금액으로 적용됩니다.
	 * (int64)
	 */
	taxFreeAmount?: number
	/** 할인 정보 */
	discounts: CreatePlatformOrderCancelTransferBodyDiscount[]
	/**
	 * 정산 시작일
	 *
	 * 날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
	 * (yyyy-MM-dd)
	 */
	settlementStartDate?: string
	/**
	 * 정산일
	 *
	 * 날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
	 * (yyyy-MM-dd)
	 */
	settlementDate?: string
	/**
	 * 외부 결제 상세 정보
	 *
	 * 해당 정보가 존재하는 경우 외부 결제 취소 정산건으로 등록되고, 존재하지않은 경우 포트원 결제 취소 정산건으로 등록됩니다.
	 */
	externalCancellationDetail?: CreatePlatformOrderCancelTransferBodyExternalCancellationDetail
	/**
	 * 테스트 모드 여부
	 *
	 * Query Parameter의 test에 값이 제공된 경우 Query Parameter의 test를 사용하고 해당 값은 무시됩니다.
	 * Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
	 */
	isForTest?: boolean
	/** 사용자 정의 속성 */
	userDefinedProperties?: PlatformUserDefinedPropertyKeyValue[]
}
