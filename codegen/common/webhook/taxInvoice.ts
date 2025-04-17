import { webhook, webhookCommonProperties } from "./common.ts"
import { Definition, extendType } from "./definition.ts"

export const webhookBillingKeyData = {
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

export const webhookBillingKeyDataVariants = [
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

export const webhookBillingKey = extendType({
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

export const webhookBillingKeyVariants = [
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
