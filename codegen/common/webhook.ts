export type Definition =
  & {
    name: string
    description: string | null
  }
  & (
    | DiscriminantDefinition
    | StringDefinition
    | ObjectDefinition
    | RefDefinition
    | IntegerDefinition
  )

export type Property = {
  required: boolean
  overrides: boolean
} & Definition

type DiscriminantDefinition = {
  type: "discriminant"
  value: string
}

type StringDefinition = {
  type: "string"
  format: string | null
}

type IntegerDefinition = {
  type: "integer"
}

type ObjectDefinition = {
  type: "object"
  extends: string[]
  properties: Property[]
  interface: ObjectInterface | null
}

type ObjectInterface = {
  discriminant: string | null
  coproduct: string[]
  open: boolean
}

type Variant = {
  name: string
  value: string
}

type RefDefinition = {
  type: "ref"
  value: string
}

const webhook = {
  name: "Webhook",
  description: "2024-04-25 버전의 웹훅 형식",
  type: "object",
  properties: [],
  extends: [],
  interface: {
    discriminant: "type",
    coproduct: ["WebhookTransaction", "WebhookBillingKey"],
    open: true,
  },
} satisfies Definition

const webhookCommonProperties = [
  {
    name: "timestamp",
    description:
      "해당 웹훅을 트리거한 이벤트의 발생 시각(RFC 3339 형식)입니다. 고객사 서버가 웹훅을 수신하는 데 실패하여 재시도가 일어나도 이 값은 동일하게 유지됩니다.",
    required: true,
    overrides: false,
    type: "string",
    format: "date-time",
  },
] satisfies Property[]

const webhookTransactionData = {
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
    ].map((name) => `WebhookTransactionData${name}`)
      .concat("WebhookTransactionCancelledData"),
    open: false,
  },
} satisfies Definition

const webhookTransactionCancelledData = extendType({
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

const webhookTransactionDataVariants = [
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

const webhookTransaction = extendType({
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
    ].map((name) => `WebhookTransaction${name}`).concat(
      "WebhookTransactionCancelled",
    ),
    open: false,
  },
}, webhook)

const webhookTransactionCancelled = extendType({
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

const webhookTransactionVariants = [
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

const webhookBillingKeyData = {
  name: "WebhookBillingKeyData",
  description:
    "빌링키 발급 관련 웹훅을 트리거한 이벤트의 실제 세부 내용입니다.",
  type: "object",
  properties: [
    {
      name: "billingKey",
      description: "포트원에서 채번한 빌링키입니다.",
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
  ],
  extends: [],
  interface: {
    discriminant: null,
    coproduct: ["Ready", "Issued", "Failed", "Deleted", "Updated"].map((name) =>
      `WebhookBillingKeyData${name}`
    ),
    open: false,
  },
} satisfies Definition

const webhookBillingKeyDataVariants = [
  extendType({
    name: "WebhookBillingKeyDataReady",
    description: "빌링키 발급창이 열렸을 때 이벤트의 실제 세부 내용입니다.",
    type: "object",
    properties: [],
    interface: null,
  }, webhookBillingKeyData),
  extendType({
    name: "WebhookBillingKeyDataIssued",
    description: "빌링키가 발급되었을 때 이벤트의 실제 세부 내용입니다.",
    type: "object",
    properties: [],
    interface: null,
  }, webhookBillingKeyData),
  extendType({
    name: "WebhookBillingKeyDataFailed",
    description: "빌링키 발급이 실패했을 때 이벤트의 실제 세부 내용입니다.",
    type: "object",
    properties: [],
    interface: null,
  }, webhookBillingKeyData),
  extendType({
    name: "WebhookBillingKeyDataDeleted",
    description: "빌링키가 삭제되었을 때 이벤트의 실제 세부 내용입니다.",
    type: "object",
    properties: [],
    interface: null,
  }, webhookBillingKeyData),
  extendType({
    name: "WebhookBillingKeyDataUpdated",
    description: "빌링키가 업데이트되었을 때 이벤트의 실제 세부 내용입니다.",
    type: "object",
    properties: [],
    interface: null,
  }, webhookBillingKeyData),
]

const webhookBillingKey = extendType({
  name: "WebhookBillingKey",
  description: "빌링키 발급 관련",
  type: "object",
  properties: [
    ...webhookCommonProperties,
    {
      name: "data",
      description: "웹훅을 트리거한 이벤트의 실제 세부 내용입니다.",
      required: true,
      overrides: false,
      type: "ref",
      value: webhookBillingKeyData.name,
    },
  ],
  interface: {
    discriminant: "type",
    coproduct: ["Ready", "Issued", "Failed", "Deleted", "Updated"].map((name) =>
      `WebhookBillingKey${name}`
    ),
    open: false,
  },
}, webhook)

const webhookBillingKeyVariants = [
  extendType({
    name: "WebhookBillingKeyReady",
    description: "빌링키 발급창이 열렸을 때",
    type: "object",
    properties: [
      {
        name: "type",
        description: "웹훅을 트리거한 이벤트의 타입입니다.",
        required: true,
        overrides: false,
        type: "discriminant",
        value: "BillingKey.Ready",
      },
      {
        name: "data",
        description: "웹훅을 트리거한 이벤트의 실제 세부 내용입니다.",
        required: true,
        overrides: true,
        type: "ref",
        value: "WebhookBillingKeyDataReady",
      },
    ],
    interface: null,
  }, webhookBillingKey),
  extendType({
    name: "WebhookBillingKeyIssued",
    description: "빌링키가 발급되었을 때",
    type: "object",
    properties: [
      {
        name: "type",
        description: "웹훅을 트리거한 이벤트의 타입입니다.",
        required: true,
        overrides: false,
        type: "discriminant",
        value: "BillingKey.Issued",
      },
      {
        name: "data",
        description: "웹훅을 트리거한 이벤트의 실제 세부 내용입니다.",
        required: true,
        overrides: true,
        type: "ref",
        value: "WebhookBillingKeyDataIssued",
      },
    ],
    interface: null,
  }, webhookBillingKey),
  extendType({
    name: "WebhookBillingKeyFailed",
    description: "빌링키 발급이 실패했을 때",
    type: "object",
    properties: [
      {
        name: "type",
        description: "웹훅을 트리거한 이벤트의 타입입니다.",
        required: true,
        overrides: false,
        type: "discriminant",
        value: "BillingKey.Failed",
      },
      {
        name: "data",
        description: "웹훅을 트리거한 이벤트의 실제 세부 내용입니다.",
        required: true,
        overrides: true,
        type: "ref",
        value: "WebhookBillingKeyDataFailed",
      },
    ],
    interface: null,
  }, webhookBillingKey),
  extendType({
    name: "WebhookBillingKeyDeleted",
    description: "빌링키가 삭제되었을 때",
    type: "object",
    properties: [
      {
        name: "type",
        description: "웹훅을 트리거한 이벤트의 타입입니다.",
        required: true,
        overrides: false,
        type: "discriminant",
        value: "BillingKey.Deleted",
      },
      {
        name: "data",
        description: "웹훅을 트리거한 이벤트의 실제 세부 내용입니다.",
        required: true,
        overrides: true,
        type: "ref",
        value: "WebhookBillingKeyDataDeleted",
      },
    ],
    interface: null,
  }, webhookBillingKey),
  extendType({
    name: "WebhookBillingKeyUpdated",
    description: "빌링키가 업데이트되었을 때",
    type: "object",
    properties: [
      {
        name: "type",
        description: "웹훅을 트리거한 이벤트의 타입입니다.",
        required: true,
        overrides: false,
        type: "discriminant",
        value: "BillingKey.Updated",
      },
      {
        name: "data",
        description: "웹훅을 트리거한 이벤트의 실제 세부 내용입니다.",
        required: true,
        overrides: true,
        type: "ref",
        value: "WebhookBillingKeyDataUpdated",
      },
    ],
    interface: null,
  }, webhookBillingKey),
]

export const entities = [
  webhook,
  webhookTransaction,
  webhookTransactionCancelled,
  ...webhookTransactionVariants,
  webhookTransactionData,
  webhookTransactionCancelledData,
  ...webhookTransactionDataVariants,
  webhookBillingKey,
  ...webhookBillingKeyVariants,
  webhookBillingKeyData,
  ...webhookBillingKeyDataVariants,
]

export const types = [
  ...webhookTransactionVariants.flatMap(extractDiscriminant),
  ...webhookBillingKeyVariants.flatMap(extractDiscriminant),
]

function extractDiscriminant(definition: Definition): [string, string][] {
  if (definition.type === "object") {
    for (const property of definition.properties) {
      if (property.type === "discriminant") {
        return [[property.value, definition.name]]
      }
    }
  }
  return []
}

function extendType(
  self: Omit<Definition & ObjectDefinition, "extends">,
  parent: Definition & ObjectDefinition,
): Definition & ObjectDefinition {
  return {
    ...self,
    properties: self.properties.filter(({ type }) => type === "discriminant")
      .concat(
        parent.properties.filter(({ name }) =>
          self.properties.every(({ name: selfName }) => selfName !== name)
        ).map((property) => ({
          ...property,
          overrides: true,
        })),
      ).concat(self.properties.filter(({ type }) => type !== "discriminant")),
    extends: [parent.name],
  }
}
