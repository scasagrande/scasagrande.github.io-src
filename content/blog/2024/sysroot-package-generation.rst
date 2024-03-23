Sysroot package generation for use with toolchains_llvm
#######################################################

:date: 2024-03-23
:modified: 2024-03-23
:tags: bazel, sysroot, toolchains_llvm
:category: bazel
:slug: sysroot-generation-toolchains-llvm
:author: Steven Casagrande
:status: published
:summary: How to generate a sysroot package for use with the Bazel ruleset `toolchains_llvm`_ in order to utilize a hermetic llvm-clang C/C++ compiler toolchain.

Bazel aims to provide a hermetic environment for your build & test operations ("actions") to run in. However by default Bazel does not provide a hermetic C / C++ (CC) toolchain. If you would like to learn more about this and why it is important, then I suggest you read `this article by Thulio Ferraz Assis at Aspect <https://blog.aspect.dev/hermetic-c-toolchain>`__.

Alongside their article, `they developed a solution <https://github.com/f0rmiga/gcc-toolchain>`__ to enable a hermetic GCC compiler and associated Linux sysroot package. Their solution is great if you want to use GCC. But if you instead want to use a hermetic llvm-clang compiler toolchain, then we are going to have to make some modifications.

By the end of this article you will be able generate your own Linux sysroot package and combine it together with llvm-clang in order to provide a hermetic CC toolchain capable of cross-compilation.

Link to source code: https://github.com/scasagrande/toolchains_llvm_sysroot

Please leave your questions and comments `under the discussions tab on the repository <https://github.com/scasagrande/toolchains_llvm_sysroot/discussions/1>`__.

toolchains_llvm ruleset
-----------------------

To start with, we are going to use the `toolchains_llvm`_ ruleset in order to fetch and setup the actual toolchain. This ruleset allows you to `specify a Bazel target that contains your sysroot package files <https://github.com/bazel-contrib/toolchains_llvm?tab=readme-ov-file#sysroots>`__.

Before we set it up, you'll need to choose if you're going to use :code:`llvm-libc++` or if you are going to use :code:`libstdc++`. The former is the default for the ruleset (when doing native compilation builds), it is the common libc++ implementation for macOS builds, and is included as part of the `standard llvm packages <https://github.com/llvm/llvm-project/releases>`__. The latter, :code:`libstdc++`, is more common for Linux builds. In both cases we will still require a separate sysroot package in order to provide a hermetic CC toolchain environment. Here I will be using :code:`libstdc++` for our Linux target platform builds, and :code:`libc++` for our macOS target platform builds.

Without a sysroot package, you might use this ruleset to define your CC toolchain as follows. This will enable a CC toolchain for Linux and macOS on both x86_64/amd64 and aarch64/arm64.

:code:`WORKSPACE.bazel`

.. code-block:: python

    load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

    http_archive(
        name = "toolchains_llvm",
        sha256 = "e91c4361f99011a54814e1afbe5c436e0d329871146a3cd58c23a2b4afb50737",
        strip_prefix = "toolchains_llvm-1.0.0",
        url = "https://github.com/bazel-contrib/toolchains_llvm/releases/download/1.0.0/toolchains_llvm-1.0.0.tar.gz",
    )

    load("@toolchains_llvm//toolchain:deps.bzl", "bazel_toolchain_dependencies")

    bazel_toolchain_dependencies()

    load("@toolchains_llvm//toolchain:rules.bzl", "llvm_toolchain")

    llvm_toolchain(
        name = "llvm_toolchain",
        llvm_version = "15.0.2",
        stdlib = {
            "linux-x86_64": "stdc++",
            "linux-aarch64": "stdc++",
        }
    )

    load("@llvm_toolchain//:toolchains.bzl", "llvm_register_toolchains")

    llvm_register_toolchains()

or for `bzlmod`_ enabled projects:

:code:`MODULE.bazel`

.. code-block:: python

    bazel_dep(name = "toolchains_llvm", version = "1.0.0")

    # Configure and register the toolchain.
    llvm = use_extension("@toolchains_llvm//toolchain/extensions:llvm.bzl", "llvm")
    llvm.toolchain(
        name = "llvm_toolchain",
        llvm_version = "15.0.2",
        stdlib = {
            "linux-x86_64": "stdc++",
            "linux-aarch64": "stdc++",
        }
    )

    use_repo(llvm, "llvm_toolchain", "llvm_toolchain_llvm")

    register_toolchains("@llvm_toolchain//:all")

.. note::
    Version 15.0.2 was chosen for this example because `there exists release packages <https://github.com/llvm/llvm-project/releases/tag/llvmorg-15.0.2>`__ for all four of our build platform configurations. Choose whatever versions suit your needs. However, I suggest that you ultimately build your own copies and host the packages yourselves.

Sysroot package generation
--------------------------

Link to source code: https://github.com/scasagrande/toolchains_llvm_sysroot

Now we need to provide a sysroot package in order to ensure that the build is using a consistent version of our system libraries. As a bonus, we will generate a matching package for both x86_64 and aarch64 CPU architectures.

To programmatically construct these packages, I started with the `sysroot generation code in the gcc-toolchain repo <https://github.com/f0rmiga/gcc-toolchain/tree/main/sysroot>`__. Although its designed to build a sysroot package for that specific toolchain ruleset, we can modify it to meet the needs of `toolchains_llvm`_. It's also already set up to enable the generation of sysroot packages for both x86_64 and aarch64.

With this starting point, I made the following changes:

- Updated the following system libraries to target a Red Hat Enterprise Linux (RHEL) 8 environment
    - Kernel 4.18
    - glibc 2.28
    - libstdc++ 10.3
- Updated toolchains used to versions that support building those above libraries
- Removed a bunch of the files that we aren't going to need, such as binaries
- Moved the files around, renamed some folders, and placed everything under a standard :code:`/usr` layout

With these changes, you'll have the basics that you need to provide a hermetic CC toolchain to Bazel.

In my case, I also decided to expand the sysroot package with :code:`openssl` and :code:`cyrus-sasl`, copied from a `RHEL-UBI 8 container image <https://catalog.redhat.com/software/containers/search?build_categories_list=Scratch%20image&p=1&product_listings_names=Red%20Hat%20Universal%20Base%20Image%208>`__. Openssl is a very common build dependency and is useful to have in your sysroot. For those of us targeting a RHEL 8 production environment, it can be very helpful to have this specific copy of openssl for FIPS compliance. But we're not going to get into that today, and instead just focus on the fact that we are including these optional libraries in our sysroot package.

.. note::
    If your deliverable is an OCI image, you should not be shipping these libraries into your final artifacts. These are just to ensure that they are hermetically available for any Bazel build and test operations, and that we are dynamically linking against these production-like copies. Your base image should already have the exact versions that you need. You may even have regulation compliance requirements where you must use the copies already present in your base image. If you think that this may apply to you, be sure to consult the rest of your team!

So now lets go ahead and build it. These commands will build our two sysroot packages with these extra ssl libraries bundled in, and output them into our current directory.

.. code-block:: bash

    $ ./build.sh x86_64 . ssl
    $ ./build.sh aarch64 . ssl

If you want to omit these ssl related packages, then replace :code:`ssl` with :code:`base`.

After some processing time, you will be left with 2 :code:`tar.xz` files. If you have been following along, the x86_64 file should be approximately 55MB, and the aarch64 file approximately 35MB.

Using the sysroot package
-------------------------

First we need to make the :code:`tar.xz` files available to Bazel. I have not yet worked with `bzlmod`_ so I will just be showing you how to use this with the legacy :code:`WORKSPACE` workflow. It should be straightforward though if you look up the `example in the toolchains_llvm repository <https://github.com/bazel-contrib/toolchains_llvm/blob/1.0.0/tests/MODULE.bazel#L135>`__.

You'll need to make your sysroot package available somewhere for your team to download, such as in `Artifactory`_. How you do that is up to you. For testing, you can put in a fake URL and use the :code:`--override_repository=` CLI argument built into Bazel.

:code:`WORKSPACE.bazel`

.. code-block:: python

    http_archive(
        name = "sysroot_linux_x86_64_2_28",
        url = "https://example.com/sysroot-x86_64-ssl.tar.xz",
        sha256 = "ABCD1234"
        build_file = "//external:BUILD.sysroot.bazel"
    )

    http_archive(
        name = "sysroot_linux_aarch64_2_28",
        url = "https://example.com/sysroot-aarch64-ssl.tar.xz",
        sha256 = "1234ABCD"
        build_file = "//external:BUILD.sysroot.bazel"
    )

:code:`external/BUILD.sysroot.bazel`

.. code-block:: python

    filegroup(
        name = "sysroot",
        srcs = glob(["**"]),
        visibility = ["//visibility:public"]
    )

And then we just need to update our toolchain definition to use these new sysroot package when building and targeting linux x86_64 and aarch64.

.. code-block:: python

    llvm_toolchain(
        name = "llvm_toolchain",
        llvm_version = "15.0.2",
        stdlib = {
            "linux-x86_64": "stdc++",
            "linux-aarch64": "stdc++",
        }
        sysroot = {
            "linux-x86_64": "@sysroot_linux_x86_64_2_28//:sysroot",
            "linux-aarch64": "@sysroot_linux_aarch64_2_28//:sysroot",
        }
    )

Optionally, we can test our build without having uploaded the :code:`tar.xz`. Start with unpacking the tar file into a folder on your filesystem. Next make a :code:`BUILD.bazel` file located at the root of this extracted folder (that is, beside the extracted :code:`usr/` folder) with the contents from your :code:`BUILD.sysroot.bazel` file.

Finally, to execute your test, run the following if you are building on a Linux x86_64 machine:

.. code-block:: bash

    $ bazel build --override_repository=sysroot_linux_x86_64_2_28=/path/to/sysroot-x86_64-ssl //...

Result
------

In the end you should now be able to build and test targeting linux x86_64 or aarch64, both with native builds or cross compilation, including from macOS!

But does that mean that you now have a fully hermetic CC build? Well, that is going to depend on the rest of your project. For example, if you have rust dependencies fetched via `rules_rust`_ , some of them may include :code:`build.rs` files that perform their own CC compilation that breaks out of the Bazel sandbox, such as `rdkafka-sys`_, `openssl-sys`_, or `sasl2-sys`_. In the future I will cover how best to deal with these cases, while also using our new sysroot packages.

Feedback
--------

Please leave your questions and comments `in this discussions thread on the repository <https://github.com/scasagrande/toolchains_llvm_sysroot/discussions/1>`__.

I can also be reached on the `Bazel slack community <https://bazelbuild.slack.com>`__ under my full name.

.. _Artifactory: https://jfrog.com/artifactory/
.. _bzlmod: https://bazel.build/external/overview#bzlmod
.. _openssl-sys: https://github.com/sfackler/rust-openssl/blob/master/openssl-sys/build/main.rs
.. _rdkafka-sys: https://github.com/onsails/rust-rdkafka/blob/master/rdkafka-sys/build.rs
.. _rules_rust: https://github.com/bazelbuild/rules_rust
.. _sasl2-sys: https://github.com/MaterializeInc/rust-sasl/blob/master/sasl2-sys/build.rs
.. _toolchains_llvm: https://github.com/bazel-contrib/toolchains_llvm
