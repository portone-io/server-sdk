import { type Definition, type Property } from "../parser/definition.ts"
import type { Package } from "../parser/openapi.ts"

const webhookCommonRequestProperties = [
  {
    name: "timestamp",
    required: true,
    title: null,
    description:
      "해당 웹훅을 트리거한 이벤트의 발생 시각(RFC 3339 형식)입니다. 고객사 서버가 웹훅을 수신하는 데 실패하여 재시도가 일어나도 이 값은 동일하게 유지됩니다.",
    type: "string",
    format: "date-time",
  },
] satisfies Property[]

const webhookTransactionRequestDataProperties = [
  {
    name: "paymentId",
    required: true,
    title: null,
    description: "고객사에서 채번한 결제 건의 고유 주문 번호입니다.",
    type: "string",
    format: null,
  },
  {
    name: "transactionId",
    required: true,
    title: null,
    description:
      "포트원에서 채번한 고유 거래 번호입니다. 한 결제 건에 여러 시도가 있을 경우 `transactionId` 가 달라질 수 있습니다.",
    type: "string",
    format: null,
  },
] satisfies Property[]

const webhookTransactionCancelledRequestDataProperties = [
  ...webhookTransactionRequestDataProperties,
  {
    name: "cancellationId",
    required: true,
    title: null,
    description:
      "포트원에서 채번한 결제건의 취소 고유 번호입니다. `type` 이 `Transaction.PartialCancelled` 혹은 `Transaction.Cancelled` 일 때 존재합니다.",
    type: "string",
    format: null,
  },
] satisfies Property[]

const webhookTransactionRequestType = [
  ["Ready", "결제창이 열렸을 때", webhookTransactionRequestDataProperties],
  [
    "Paid",
    "결제(예약 결제 포함)가 승인되었을 때 (모든 결제 수단)",
    webhookTransactionRequestDataProperties,
  ],
  [
    "VirtualAccountIssued",
    "가상계좌가 발급되었을 때",
    webhookTransactionRequestDataProperties,
  ],
  [
    "PartialCancelled",
    "결제가 부분 취소되었을 때",
    webhookTransactionCancelledRequestDataProperties,
  ],
  [
    "Cancelled",
    "결제가 완전 취소되었을 때",
    webhookTransactionCancelledRequestDataProperties,
  ],
  [
    "Failed",
    "결제(예약 결제 포함)가 실패했을 때",
    webhookTransactionRequestDataProperties,
  ],
  [
    "PayPending",
    "결제 승인 대기 상태가 되었을 때 (해외 결제시 발생 가능)",
    webhookTransactionRequestDataProperties,
  ],
  [
    "CancelPending",
    "(결제 취소가 비동기로 수행되는 경우) 결제 취소를 요청했을 때",
    webhookTransactionRequestDataProperties,
  ],
] as const

const webhookTransactionRequestVariants = webhookTransactionRequestType.map((
  [name, description],
) =>
  ({
    name: `WebhookTransactionRequest${name}`,
    title: null,
    description,
    type: "object",
    properties: [
      {
        name: "type",
        required: true,
        title: null,
        description: "웹훅을 트리거한 이벤트의 타입입니다.",
        type: "discriminant",
        value: `Transaction.${name}`,
      },
      ...webhookCommonRequestProperties,
      {
        name: "data",
        required: true,
        title: null,
        description: "웹훅을 트리거한 이벤트의 실제 세부 내용입니다.",
        type: "ref",
        value: `WebhookTransactionRequest${name}Data`,
      },
    ],
    additionalProperties: null,
  }) satisfies Definition
)

const webhookTransactionRequestDataVariants = webhookTransactionRequestType.map(
  ([name, , properties]) =>
    ({
      name: `WebhookTransactionRequest${name}Data`,
      title: null,
      description: null,
      type: "object",
      properties,
      additionalProperties: null,
    }) satisfies Definition,
)

const webhookBillingKeyRequestDataProperties = [
  {
    name: "billingKey",
    required: true,
    title: null,
    description: "포트원에서 채번한 빌링키입니다.",
    type: "string",
    format: null,
  },
] satisfies Property[]

const webhookBillingKeyRequestType = [
  ["Ready", "빌링키 발급창이 열렸을 때"],
  ["Issued", "빌링키가 발급되었을 때"],
  ["Failed", "빌링키 발급이 실패했을 때"],
  ["Deleted", "빌링키가 삭제되었을 때"],
  ["Updated", "빌링키가 업데이트되었을 때"],
] as const

const webhookBillingKeyRequestVariants = webhookBillingKeyRequestType.map((
  [name, description],
) =>
  ({
    name: `WebhookBillingKeyRequest${name}`,
    title: null,
    description,
    type: "object",
    properties: [
      {
        name: "type",
        required: true,
        title: null,
        description: "웹훅을 트리거한 이벤트의 타입입니다.",
        type: "discriminant",
        value: `BillingKey.${name}`,
      },
      ...webhookCommonRequestProperties,
      {
        name: "data",
        required: true,
        title: null,
        description: "웹훅을 트리거한 이벤트의 실제 세부 내용입니다.",
        type: "ref",
        value: `WebhookBillingKeyRequest${name}Data`,
      },
    ],
    additionalProperties: null,
  }) satisfies Definition
)

const webhookBillingKeyRequestDataVariants = webhookBillingKeyRequestType.map((
  [name],
) =>
  ({
    name: `WebhookBillingKeyRequest${name}Data`,
    title: null,
    description: null,
    type: "object",
    properties: webhookBillingKeyRequestDataProperties,
    additionalProperties: null,
  }) satisfies Definition
)

const webhookRequestSchema = {
  name: "WebhookRequest",
  title: null,
  description: "웹훅 형식",
  type: "oneOf",
  variants: [
    ...webhookTransactionRequestType.map(([name, description]) => ({
      name: `WebhookTransactionRequest${name}`,
      property: "type",
      value: `Transaction.${name}`,
      title: description,
    })),
    ...webhookBillingKeyRequestType.map(([name, description]) => ({
      name: `WebhookBillingKeyRequest${name}`,
      property: "type",
      value: `BillingKey.${name}`,
      title: description,
    })),
  ],
} satisfies Definition

export const webhookPackage = {
  category: "webhook",
  entities: [
    ...webhookTransactionRequestVariants,
    ...webhookTransactionRequestDataVariants,
    ...webhookBillingKeyRequestVariants,
    ...webhookBillingKeyRequestDataVariants,
    webhookRequestSchema,
  ],
  operations: [],
  subpackages: [],
} satisfies Package
