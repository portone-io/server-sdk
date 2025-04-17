import { webhook, webhookCommonProperties } from "./common.ts"
import { Definition, extendType } from "./definition.ts"

export const webhookTransactionData = {
  name: "WebhookTransactionData",
  description: "결제 관련 웹훅을 트리거한 이벤트의 실제 세부 내용입니다.",
  type: "object",
  properties: [
    {
      name: "paymentId",
      description: "고객사에서 채번한 결제 건의 고유 주문 번호입니다.",
      required: true,
      overrides: false,
      type: "string",
      format: null,
    },
    {
      name: "storeId",
      description: "웹훅을 트리거한 상점의 아이디입니다.",
      required: true,
      overrides: false,
      type: "string",
      format: null,
    },
    {
      name: "transactionId",
      description:
        "포트원에서 채번한 고유 거래 번호입니다. 한 결제 건에 여러 시도가 있을 경우 `transactionId` 가 달라질 수 있습니다.",
      required: true,
      overrides: false,
      type: "string",
      format: null,
    },
  ],
  extends: [],
  interface: {
    discriminant: null,
    coproduct: [
      "Ready",
      "Paid",
      "VirtualAccountIssued",
      "Failed",
      "PayPending",
      "Confirm",
      "DisputeCreated",
      "DisputeResolved",
    ].map((name) => `WebhookTransactionData${name}`)
      .concat("WebhookTransactionCancelledData"),
    open: false,
  },
} satisfies Definition

export const webhookTransactionCancelledData = extendType({
  name: "WebhookTransactionCancelledData",
  description: "결제 취소 관련 웹훅을 트리거한 이벤트의 실제 세부 내용입니다.",
  type: "object",
  properties: [
    {
      name: "cancellationId",
      description: "포트원에서 채번한 결제건의 취소 고유 번호입니다.",
      required: true,
      overrides: false,
      type: "string",
      format: null,
    },
  ],
  interface: {
    discriminant: null,
    coproduct: ["PartialCancelled", "Cancelled", "CancelPending"].map((name) =>
      `WebhookTransactionCancelledData${name}`
    ),
    open: false,
  },
}, webhookTransactionData)

export const webhookTransactionDataVariants = [
  extendType({
    name: "WebhookTransactionDataReady",
    description: "결제창이 열렸을 때 이벤트의 실제 세부 내용입니다.",
    type: "object",
    properties: [],
    interface: null,
  }, webhookTransactionData),
  extendType({
    name: "WebhookTransactionDataPaid",
    description:
      "결제(예약 결제 포함)가 승인되었을 때 이벤트의 실제 세부 내용입니다. (모든 결제 수단)",
    type: "object",
    properties: [],
    interface: null,
  }, webhookTransactionData),
  extendType({
    name: "WebhookTransactionDataVirtualAccountIssued",
    description: "가상계좌가 발급되었을 때 이벤트의 실제 세부 내용입니다.",
    type: "object",
    properties: [],
    interface: null,
  }, webhookTransactionData),
  extendType({
    name: "WebhookTransactionCancelledDataPartialCancelled",
    description: "결제가 부분 취소되었을 때 이벤트의 실제 세부 내용입니다.",
    type: "object",
    properties: [],
    interface: null,
  }, webhookTransactionCancelledData),
  extendType({
    name: "WebhookTransactionCancelledDataCancelled",
    description: "결제가 완전 취소되었을 때 이벤트의 실제 세부 내용입니다.",
    type: "object",
    properties: [],
    interface: null,
  }, webhookTransactionCancelledData),
  extendType({
    name: "WebhookTransactionDataFailed",
    description:
      "결제(예약 결제 포함)가 실패했을 때 이벤트의 실제 세부 내용입니다.",
    type: "object",
    properties: [],
    interface: null,
  }, webhookTransactionData),
  extendType({
    name: "WebhookTransactionDataPayPending",
    description:
      "결제 승인 대기 상태가 되었을 때 이벤트의 실제 세부 내용입니다. (해외 결제시 발생 가능)",
    type: "object",
    properties: [],
    interface: null,
  }, webhookTransactionData),
  extendType({
    name: "WebhookTransactionDataDisputeCreated",
    description: "분쟁이 발생되었을 때 이벤트의 실제 세부 내용입니다.",
    type: "object",
    properties: [],
    interface: null,
  }, webhookTransactionData),
  extendType({
    name: "WebhookTransactionDataDisputeResolved",
    description: "분쟁이 해소되었을 때 이벤트의 실제 세부 내용입니다.",
    type: "object",
    properties: [],
    interface: null,
  }, webhookTransactionData),
  extendType({
    name: "WebhookTransactionCancelledDataCancelPending",
    description:
      "(결제 취소가 비동기로 수행되는 경우) 결제 취소를 요청했을 때 이벤트의 실제 세부 내용입니다.",
    type: "object",
    properties: [],
    interface: null,
  }, webhookTransactionCancelledData),
  extendType({
    name: "WebhookTransactionDataConfirm",
    description:
      "(결제 취소가 비동기로 수행되는 경우) 결제 취소를 요청했을 때 이벤트의 실제 세부 내용입니다.",
    type: "object",
    properties: [{
      name: "totalAmount",
      description: "결제건의 결제 요청 금액입니다.",
      required: true,
      overrides: false,
      type: "integer",
    }],
    interface: null,
  }, webhookTransactionData),
]

export const webhookTransaction = extendType({
  name: "WebhookTransaction",
  description: "결제 관련",
  type: "object",
  properties: [
    ...webhookCommonProperties,
    {
      name: "data",
      description: "웹훅을 트리거한 이벤트의 실제 세부 내용입니다.",
      required: true,
      overrides: false,
      type: "ref",
      value: webhookTransactionData.name,
    },
  ],
  interface: {
    discriminant: "type",
    coproduct: [
      "Ready",
      "Paid",
      "VirtualAccountIssued",
      "Failed",
      "PayPending",
      "Confirm",
      "DisputeCreated",
      "DisputeResolved",
    ].map((name) => `WebhookTransaction${name}`).concat(
      "WebhookTransactionCancelled",
    ),
    open: false,
  },
}, webhook)

export const webhookTransactionCancelled = extendType({
  name: "WebhookTransactionCancelled",
  description: "결제 취소 관련",
  type: "object",
  properties: [
    {
      name: "data",
      description:
        "결제 취소 관련 웹훅을 트리거한 이벤트의 실제 세부 내용입니다.",
      required: true,
      overrides: true,
      type: "ref",
      value: webhookTransactionCancelledData.name,
    },
  ],
  interface: {
    discriminant: "type",
    coproduct: ["PartialCancelled", "Cancelled", "CancelPending"].map((name) =>
      `WebhookTransactionCancelled${name}`
    ),
    open: false,
  },
}, webhookTransaction)

export const webhookTransactionVariants = [
  extendType({
    name: "WebhookTransactionReady",
    description: "결제창이 열렸을 때",
    type: "object",
    properties: [{
      name: "type",
      description: "웹훅을 트리거한 이벤트의 타입입니다.",
      required: true,
      overrides: true,
      type: "discriminant",
      value: "Transaction.Ready",
    }, {
      name: "data",
      description: "결제창이 열렸을 때 이벤트의 실제 세부 내용입니다.",
      required: true,
      overrides: true,
      type: "ref",
      value: "WebhookTransactionDataReady",
    }],
    interface: null,
  }, webhookTransaction),
  extendType({
    name: "WebhookTransactionPaid",
    description: "결제(예약 결제 포함)가 승인되었을 때 (모든 결제 수단)",
    type: "object",
    properties: [{
      name: "type",
      description: "웹훅을 트리거한 이벤트의 타입입니다.",
      required: true,
      overrides: true,
      type: "discriminant",
      value: "Transaction.Paid",
    }, {
      name: "data",
      description:
        "결제(예약 결제 포함)가 승인되었을 때 이벤트의 실제 세부 내용입니다. (모든 결제 수단)",
      required: true,
      overrides: true,
      type: "ref",
      value: "WebhookTransactionDataPaid",
    }],
    interface: null,
  }, webhookTransaction),
  extendType({
    name: "WebhookTransactionVirtualAccountIssued",
    description: "가상계좌가 발급되었을 때",
    type: "object",
    properties: [{
      name: "type",
      description: "웹훅을 트리거한 이벤트의 타입입니다.",
      required: true,
      overrides: true,
      type: "discriminant",
      value: "Transaction.VirtualAccountIssued",
    }, {
      name: "data",
      description: "가상계좌가 발급되었을 때 이벤트의 실제 세부 내용입니다.",
      required: true,
      overrides: true,
      type: "ref",
      value: "WebhookTransactionDataVirtualAccountIssued",
    }],
    interface: null,
  }, webhookTransaction),
  extendType({
    name: "WebhookTransactionCancelledPartialCancelled",
    description: "결제가 부분 취소되었을 때",
    type: "object",
    properties: [{
      name: "type",
      description: "웹훅을 트리거한 이벤트의 타입입니다.",
      required: true,
      overrides: true,
      type: "discriminant",
      value: "Transaction.PartialCancelled",
    }, {
      name: "data",
      description: "결제가 부분 취소되었을 때 이벤트의 실제 세부 내용입니다.",
      required: true,
      overrides: true,
      type: "ref",
      value: "WebhookTransactionCancelledDataPartialCancelled",
    }],
    interface: null,
  }, webhookTransactionCancelled),
  extendType({
    name: "WebhookTransactionCancelledCancelled",
    description: "결제가 완전 취소되었을 때 이벤트의 실제 세부 내용입니다.",
    type: "object",
    properties: [{
      name: "type",
      description: "웹훅을 트리거한 이벤트의 타입입니다.",
      required: true,
      overrides: true,
      type: "discriminant",
      value: "Transaction.Cancelled",
    }, {
      name: "data",
      description: "결제창이 열렸을 때 이벤트의 실제 세부 내용입니다.",
      required: true,
      overrides: true,
      type: "ref",
      value: "WebhookTransactionCancelledDataCancelled",
    }],
    interface: null,
  }, webhookTransactionCancelled),
  extendType({
    name: "WebhookTransactionFailed",
    description: "결제(예약 결제 포함)가 실패했을 때",
    type: "object",
    properties: [{
      name: "type",
      description: "웹훅을 트리거한 이벤트의 타입입니다.",
      required: true,
      overrides: true,
      type: "discriminant",
      value: "Transaction.Failed",
    }, {
      name: "data",
      description:
        "결제(예약 결제 포함)가 실패했을 때 이벤트의 실제 세부 내용입니다.",
      required: true,
      overrides: true,
      type: "ref",
      value: "WebhookTransactionDataFailed",
    }],
    interface: null,
  }, webhookTransaction),
  extendType({
    name: "WebhookTransactionPayPending",
    description: "결제 승인 대기 상태가 되었을 때 (해외 결제시 발생 가능)",
    type: "object",
    properties: [{
      name: "type",
      description: "웹훅을 트리거한 이벤트의 타입입니다.",
      required: true,
      overrides: true,
      type: "discriminant",
      value: "Transaction.PayPending",
    }, {
      name: "data",
      description:
        "결제 승인 대기 상태가 되었을 때 이벤트의 실제 세부 내용입니다. (해외 결제시 발생 가능)",
      required: true,
      overrides: true,
      type: "ref",
      value: "WebhookTransactionDataPayPending",
    }],
    interface: null,
  }, webhookTransaction),
  extendType({
    name: "WebhookTransactionDisputeCreated",
    description: "분쟁이 발생되었을 때",
    type: "object",
    properties: [{
      name: "type",
      description: "웹훅을 트리거한 이벤트의 타입입니다.",
      required: true,
      overrides: true,
      type: "discriminant",
      value: "Transaction.DisputeCreated",
    }, {
      name: "data",
      description: "분쟁이 발생되었을 때 이벤트의 실제 세부 내용입니다.",
      required: true,
      overrides: true,
      type: "ref",
      value: "WebhookTransactionDataDisputeCreated",
    }],
    interface: null,
  }, webhookTransaction),
  extendType({
    name: "WebhookTransactionDisputeResolved",
    description: "분쟁이 해소되었을 때",
    type: "object",
    properties: [{
      name: "type",
      description: "웹훅을 트리거한 이벤트의 타입입니다.",
      required: true,
      overrides: true,
      type: "discriminant",
      value: "Transaction.DisputeResolved",
    }, {
      name: "data",
      description: "분쟁이 해소되었을 때 이벤트의 실제 세부 내용입니다.",
      required: true,
      overrides: true,
      type: "ref",
      value: "WebhookTransactionDataDisputeResolved",
    }],
    interface: null,
  }, webhookTransaction),
  extendType({
    name: "WebhookTransactionCancelledCancelPending",
    description: "(결제 취소가 비동기로 수행되는 경우) 결제 취소를 요청했을 때",
    type: "object",
    properties: [{
      name: "type",
      description: "웹훅을 트리거한 이벤트의 타입입니다.",
      required: true,
      overrides: true,
      type: "discriminant",
      value: "Transaction.CancelPending",
    }, {
      name: "data",
      description:
        "(결제 취소가 비동기로 수행되는 경우) 결제 취소를 요청했을 때 이벤트의 실제 세부 내용입니다.",
      required: true,
      overrides: true,
      type: "ref",
      value: "WebhookTransactionCancelledDataCancelPending",
    }],
    interface: null,
  }, webhookTransactionCancelled),
  extendType({
    name: "WebhookTransactionConfirm",
    description: "컨펌 프로세스에서 승인 요청을 받았을 때",
    type: "object",
    properties: [{
      name: "type",
      description: "웹훅을 트리거한 이벤트의 타입입니다.",
      required: true,
      overrides: true,
      type: "discriminant",
      value: "Transaction.Confirm",
    }, {
      name: "data",
      description:
        "컨펌 프로세스에서 승인 요청을 받았을 때 이벤트의 실제 세부 내용입니다.",
      required: true,
      overrides: true,
      type: "ref",
      value: "WebhookTransactionDataConfirm",
    }],
    interface: null,
  }, webhookTransaction),
]
