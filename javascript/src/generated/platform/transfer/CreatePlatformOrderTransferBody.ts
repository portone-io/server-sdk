import type { CreatePlatformOrderTransferBodyAdditionalFee } from "./../../platform/transfer/CreatePlatformOrderTransferBodyAdditionalFee"
import type { CreatePlatformOrderTransferBodyDiscount } from "./../../platform/transfer/CreatePlatformOrderTransferBodyDiscount"
import type { CreatePlatformOrderTransferBodyExternalPaymentDetail } from "./../../platform/transfer/CreatePlatformOrderTransferBodyExternalPaymentDetail"
import type { CreatePlatformOrderTransferBodyOrderDetail } from "./../../platform/transfer/CreatePlatformOrderTransferBodyOrderDetail"
import type { PlatformUserDefinedPropertyKeyValue } from "./../../platform/transfer/PlatformUserDefinedPropertyKeyValue"
import type { TransferParameters } from "./../../platform/transfer/TransferParameters"

/** 주문 정산건 생성을 위한 입력 정보 */
export type CreatePlatformOrderTransferBody = {
	/** 파트너 아이디 */
	partnerId: string
	/**
	 * 계약 아이디
	 *
	 * 기본값은 파트너의 기본 계약 아이디 입니다.
	 */
	contractId?: string
	/** 메모 */
	memo?: string
	/** 결제 아이디 */
	paymentId: string
	/** 주문 정보 */
	orderDetail: CreatePlatformOrderTransferBodyOrderDetail
	/**
	 * 주문 면세 금액
	 *
	 * 주문 항목과 면세 금액을 같이 전달하시면 최종 면세 금액은 주문 항목의 면세 금액이 아닌 전달해주신 면세 금액으로 적용됩니다.
	 * (int64)
	 */
	taxFreeAmount?: number
	/**
	 * 정산 시작일
	 *
	 * 기본값은 결제 일시 입니다.
	 */
	settlementStartDate?: string
	/** 할인 정보 */
	discounts: CreatePlatformOrderTransferBodyDiscount[]
	/** 추가 수수료 정보 */
	additionalFees: CreatePlatformOrderTransferBodyAdditionalFee[]
	/**
	 * 외부 결제 상세 정보
	 *
	 * 해당 정보가 존재하는 경우 외부 결제 정산건 으로 등록되고, 존재하지않은 경우 포트원 결제 정산건으로 등록됩니다.
	 */
	externalPaymentDetail?: CreatePlatformOrderTransferBodyExternalPaymentDetail
	/**
	 * 테스트 모드 여부
	 *
	 * 기본값은 false 입니다.
	 */
	isForTest?: boolean
	/** 정산 파라미터 (실험기능) */
	parameters?: TransferParameters
	/** 사용자 정의 속성 */
	userDefinedProperties?: PlatformUserDefinedPropertyKeyValue[]
}
