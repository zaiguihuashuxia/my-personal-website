## Purpose

Defines the first public learning area as a revision-oriented Java guide that combines a learning path, curated resources, concept explanations, and lightweight self-check material.

## ADDED Requirements

### Requirement: Confirmed Java module map
The Java learning area SHALL provide navigable module entry points for Java fundamentals, object-oriented programming, Java Web, Spring fundamentals, Spring Boot, and Spring Cloud.

#### Scenario: View the Java learning map
- **WHEN** a reader opens the Java topic home page
- **THEN** the six confirmed modules are presented in a progression from language fundamentals through Spring Cloud, with Spring fundamentals bridging Java Web and Spring Boot

### Requirement: Java module overview
Each published Java module SHALL have an overview that explains its learning purpose, core concepts, available articles, and recommended reading or revision order.

#### Scenario: Enter the object-oriented programming module
- **WHEN** a reader opens the object-oriented programming module
- **THEN** the reader can see what the module covers, which published concept articles belong to it, and where to begin reviewing

### Requirement: Curated Java learning resources
The Java area SHALL support curated course, book, and official-documentation entries that record the source link, suitable learning stage, prerequisites, recommendation rationale, and links to related local notes when available.

#### Scenario: Review a recommended course
- **WHEN** a reader opens a curated Java resource entry
- **THEN** the reader can understand why it is recommended, who it suits, what preparation it expects, and which published notes relate to it

### Requirement: Concept-focused Java articles
The Java area SHALL support articles centered on coherent concepts or questions, and SHALL allow those articles to present a concise conclusion, explanation, minimal example, common pitfalls, self-check questions, and related knowledge links.

#### Scenario: Review a Java concept
- **WHEN** a reader opens a published concept article such as interface-versus-abstract-class or equals-and-hashCode
- **THEN** the page provides enough explanation and review aids to restore the concept without requiring the reader to traverse a monolithic module note

### Requirement: Module review outlines
Every Java module containing published concept articles SHALL provide a review outline with key terms, important comparisons or relationships, common mistakes, self-check questions, and links back to detailed articles.

#### Scenario: Use a review outline
- **WHEN** the author or another reader reviews a populated Java module
- **THEN** they can scan its key points, identify an uncertain concept through self-check questions, and navigate to the corresponding detailed article

### Requirement: Honest first-version completeness
The first version SHALL distinguish published material from unfilled curriculum ambitions and SHALL NOT present unavailable Java chapters or resources as completed content.

#### Scenario: A planned Java topic has not been written
- **WHEN** a concept is part of the long-term Java learning map but has no public article
- **THEN** the website avoids linking to an empty or placeholder article as if it were finished
