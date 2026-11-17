---
type: Topic
title: Residual Connections
description: Identity shortcuts that let gradients flow through very deep networks.
tags: [architecture, optimization, topic]
papers: ["/papers/05-deep-residual-learning-resnet.md", "/papers/06-identity-mappings-in-deep-residual-networks.md"]
status: stable
generated: { by: okf_builder/1.0, at: 2026-11-17T16:30:00Z }
verified: { by: process:okf-validator, at: 2026-11-17T16:30:00Z }
---

# Residual Connections

Identity shortcuts that let gradients flow through very deep networks.

## Why it matters in this list

Residual streams are now structural, not optional: a Transformer block is two residual updates.

## Papers

- [05 - Deep Residual Learning for Image Recognition](/papers/05-deep-residual-learning-resnet.md) (2015) - ResNet: reformulates a layer as learning a residual on top of an identity mapping, which lets networks train at 100+ layers.
- [06 - Identity Mappings in Deep Residual Networks](/papers/06-identity-mappings-in-deep-residual-networks.md) (2016) - The pre-activation follow-up to ResNet: an analysis of why identity shortcuts keep gradients healthy, and a redesign that makes very deep residual networks easier to optimise..

## Related topics

[Transformer Architecture](/topics/transformer-architecture.md), [Convolutional Networks](/topics/convolutional-networks.md), [Memory-Augmented Networks](/topics/memory-augmented-networks.md), [Graph Neural Networks](/topics/graph-neural-networks.md)