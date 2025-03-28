import io.portone.sdk.server.build.GenerateVersionCodeTask
import org.jetbrains.kotlin.gradle.dsl.JvmTarget
import org.jetbrains.kotlin.gradle.dsl.jvm.JvmTargetValidationMode
import org.jetbrains.kotlin.gradle.tasks.KotlinJvmCompile

plugins {
    `java-library`
    signing

    alias(libs.plugins.kotlin.jvm)
    alias(libs.plugins.kotlin.plugin.serialization)
    alias(libs.plugins.ktlint)
    alias(libs.plugins.binary.compatibility.validator)
    alias(libs.plugins.maven.publish)
    alias(libs.plugins.shadow)
}

group = "io.portone"
description = "JVM library for integrating PortOne payment infrastructure."

version = project.findProperty("version") as String

val generateVersionCode =
    tasks.register<GenerateVersionCodeTask>("generateVersionCode") {
        version = project.version.toString()
        outputDirectory = layout.buildDirectory.dir("generated/sources/versionCode/kotlin/main")
    }

sourceSets {
    main {
        kotlin {
            srcDir(generateVersionCode)
            srcDir("src/generated/kotlin")
        }
    }
}

tasks.withType<KotlinJvmCompile>().configureEach {
    jvmTargetValidationMode = JvmTargetValidationMode.ERROR
}

kotlin {
    jvmToolchain(21)
    explicitApi()
    compilerOptions {
        jvmTarget = JvmTarget.JVM_21
        progressiveMode = true
        allWarningsAsErrors = true
        freeCompilerArgs.addAll(
            "-Xjdk-release=21",
            "-Xjsr305=strict",
            "-opt-in=kotlinx.coroutines.DelicateCoroutinesApi",
            "-opt-in=kotlinx.serialization.ExperimentalSerializationApi",
            "-Xjvm-default=all-compatibility",
        )
    }
}

java {
    sourceCompatibility = JavaVersion.VERSION_21
    targetCompatibility = JavaVersion.VERSION_21
}

tasks.compileJava {
    options.javaModuleVersion = provider { version as String }
    options.compilerArgumentProviders.add(
        CommandLineArgumentProvider {
            listOf("--patch-module", "io.portone.sdk.server=${sourceSets["main"].output.asPath}")
        },
    )
}

dependencies {
    api(libs.kotlinx.serialization.json)
    implementation(libs.ktor.client.core)
    implementation(libs.ktor.client.okhttp)

    testImplementation(libs.kotlinx.coroutines.test)
    testImplementation("io.mockk:mockk:1.13.9")
}

repositories {
    mavenCentral()
}

testing {
    suites {
        val test by getting(JvmTestSuite::class) {
            useKotlinTest(libs.versions.kotlin.test)
        }
    }
}

tasks.apiBuild {
    inputJar.value(tasks.jar.flatMap { it.archiveFile })
}

tasks.jar {
    manifest {
        attributes(
            "Implementation-Title" to "PortOne Server SDK for Rapportlabs JVM",
            "Implementation-Version" to project.version,
            "Implementation-Vendor" to "Rapportlabs",
            "Sealed" to "true",
        )
    }
}

tasks.shadowJar {
    relocate("kotlinx.serialization", "kr.rapportlabs.portone.sdk.internal.serialization")
    relocate("kotlinx.coroutines", "kr.rapportlabs.portone.sdk.internal.coroutines")
    relocate("io.ktor", "kr.rapportlabs.portone.sdk.internal.ktor")
    relocate("kotlin", "kr.rapportlabs.portone.sdk.internal.kotlin")
}

publishing {
    val sourcesJar by tasks.registering(Jar::class) {
        archiveClassifier.set("sources")
        from(sourceSets.main.get().allSource)
    }

    publications {
        create<MavenPublication>("mavenJava") {
            from(components["java"])
            groupId = "kr.rapportlabs"
            artifactId = "portone-server-sdk"
            version = project.version.toString()
            // artifact(sourcesJar.get())
        }

        create<MavenPublication>("shadow") {
            from(components["shadow"])
            groupId = "kr.rapportlabs"
            version = project.version.toString()
            artifactId = "portone-server-sdk-all"
        }
    }

    repositories {
        maven {
            name = "GitHubPackages"
            url = uri("https://maven.pkg.github.com/rapportlabs/portone-server-sdk")
            credentials {
                username = System.getenv("API_MVN_USERNAME")
                password = System.getenv("API_MVN_TOKEN")
            }
        }
    }
}
