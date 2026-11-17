---
type: Topic
title: Generative Models
description: Models that learn a data distribution and can sample from it.
tags: [generation, probability, topic]
papers: ["/papers/28-generative-adversarial-nets.md", "/papers/29-variational-lossy-autoencoder.md"]
status: stable
generated: { by: okf_builder/1.0, at: 2026-11-17T16:30:00Z }
verified: { by: process:okf-validator, at: 2026-11-17T16:30:00Z }
---

# Generative Models

Models that learn a data distribution and can sample from it.

## Why it matters in this list

GANs and VAEs are the two classical answers to 'can a network imagine data', and their trade-offs still shape diffusion and autoregressive generation.

## Papers

- [28 - Generative Adversarial Nets](/papers/28-generative-adversarial-nets.md) (2014) - Two networks trained against each other: a generator that produces samples and a discriminator that tries to tell them from real data.
- [29 - Variational Lossy Autoencoder](/papers/29-variational-lossy-autoencoder.md) (2016) - Combines variational autoencoders with expressive autoregressive decoders and explicit control over what the latent code is allowed to keep, giving much sharper generative models and a clean information-theoretic reading of why..