---
title: Spring 核心
nav_title: Spring 核心
description: IoC、依赖注入、Bean、AOP 与 Spring MVC 的复习入口
series: java-learning-path
order: 40
tags:
  - java
  - spring
---

# Spring 核心

本模块作为 Java Web 与 Spring Boot 之间的桥梁，重点理解框架替应用管理对象、依赖和横切逻辑的方式。

## 核心概念地图

- IoC（控制反转）与依赖注入
- Bean 定义、作用域与生命周期
- 容器启动和依赖装配
- AOP、切点与通知
- Spring MVC 请求处理链
- 事务边界的基本思想

## 推荐复习顺序

先理解 IoC 容器为何存在，再跟踪 Bean 从定义到注入的过程；之后学习 AOP 与 Spring MVC。这样进入 Spring Boot 时，自动配置不会只是需要背诵的注解集合。

## 快速自测

1. IoC 改变了对象由谁创建、由谁连接？
2. 构造器注入相比字段注入有什么优势？
3. AOP 适合处理哪些横切关注点？
4. Spring MVC 如何把 HTTP 请求交给控制器方法？
