import spawnAsync from "@expo/spawn-async";
import * as fs from "node:fs/promises";
import { createRequire } from "node:module";
import { beforeAll, describe, expect, test } from "vitest";

let uuid: string;

const crypto = globalThis.crypto ?? (await import("node:crypto")).webcrypto;

// To simulate a real build, since we have different package.json entries on development because of package.json#publishConfig
beforeAll(async () => {
	uuid = crypto.randomUUID();
	await fs.mkdir(`./temp/${uuid}`, { recursive: true });
	await spawnAsync("pnpm", ["build"]);
	const result = await spawnAsync("pnpm", [
		"pack",
		"--json",
		"--pack-destination",
		`./temp/${uuid}`,
	]);
	const json = JSON.parse(result.stdout);
	await spawnAsync("tar", ["-xf", json.filename, "-C", `./temp/${uuid}`]);

	return async () => {
		await fs.rm(`./temp/${uuid}`, { recursive: true, force: true });
	};
});

describe.concurrent("can be imported", () => {
	test("import", async () => {
		const sdk = await import(`../temp/${uuid}/package`);
		expect(sdk).toMatchObject({});
	});
	test("require", async () => {
		const require = createRequire(import.meta.url);
		const sdk = require(`../temp/${uuid}/package`);
		expect(sdk).toMatchObject({});
	});
});
