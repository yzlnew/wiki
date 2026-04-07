---
type: source-summary
status: active
tags: [bookmarks, self-hosting, homelab, networking, automation]
source_count: 14
updated: 2026-04-07
source_path: ../../sources/library/bookmarks/bookmarks.md
---

# Bookmarks Self-Hosting and Home Lab Batch 1

## Source

- 原始文件：`sources/library/bookmarks/bookmarks.md`
- 处理日期：2026-04-07
- 本批次聚焦：自托管服务、家庭网络、自动化和居家设备接入

## Summary

这批书签拼出了一条比较清晰的个人基础设施脉络：一头是知识与文档流转，一头是家庭网络、代理与自动化，中间由自托管服务和设备接入连接起来。它们并不是单纯的工具列表，而是一个“把个人系统搭起来并持续维护”的实践集合。

从内容密度看，`bookmarks`、`paperless-ngx`、`code-server` 更像个人基础设施层；`n8n` 和 `memos` 指向事件驱动的自动化；`Aqara G3`、`OpenERV` 和 `Moonlight` 则把家庭设备、环境系统和远程访问纳入同一个 home lab 视角。`SR-IOV`、`Linux` 服务器初始化、`AdGuard Home`、`mosdns`、`OpenClash`、`sing-box` 则构成网络与虚拟化的底座。

## Key Claims

- 个人自托管栈已经不只是“装服务”，而是在覆盖知识管理、文档处理、远程开发和自动化触发。
- 家庭网络相关链接高度集中，说明代理、DNS 分流和路由策略是一个独立且持续出现的子问题。
- `Aqara G3`、`OpenERV`、`Moonlight` 这类条目提示 home lab 的边界已经扩展到居家设备、环境系统和家庭娱乐。
- `SR-IOV` 与 Linux/VPS 初始化说明这批资料里还有一层偏基础设施的工程实践，而不只是应用层玩法。

## 个人基础设施

- [Frequently Asked Questions (FAQ) | Karakeep Docs](https://docs.karakeep.app/next/FAQ/) - 产品文档入口，可作为这套 bookmarks 服务的参考。
- [Bookmarks Service](https://hoarder.cloudhome.yzlnew.com:16666/signin) - 当前书签与知识入口本身，属于这套基础设施的中心。
- [GitHub - paperless-ngx/paperless-ngx](https://github.com/paperless-ngx/paperless-ngx) - 文档扫描、索引与归档，适合和 bookmarks 组成资料流转层。
- [GitHub - coder/code-server](https://github.com/coder/code-server) - 浏览器里的 VS Code，属于远程开发基础设施。
- [R86S 折腾日记二 | PVE 下给万兆网卡 CX341 开启 SR-IOV 并直通给虚拟机 | hank9999部落格](https://blog.hank.ltd/r86s-logbook-2-setup-sr-iov-for-cx341-pve/) - 偏虚拟化与网卡直通的基础设施实践。
- [新开机一台 Linux 服务器之后应该做的 N 件事](https://rennen.dev/archives/n-steps-to-do-after-buying-a-new-vps#%E5%AE%89%E8%A3%85-1panel) - 新 VPS / 服务器初始化清单，属于底层运维起点。

## 网络代理

- [全网最详细的解锁 SSH ShellCrash 搭载 mihomo 内核搭配 AdGuard Home 安装和配置教程](https://proxy-tutorials.dustinwin.top/posts/pin-shellcrashadguardhome-mihomo/#%E4%BA%94-shellcrash-%E5%AE%89%E8%A3%85%E5%92%8C%E9%85%8D%E7%BD%AE) - 代理、DNS 和本地网络控制面的组合方案。
- [AdGuard+MosDNS+OpenClash 套娃代理组合 - V2EX](https://www.v2ex.com/t/1060338) - 典型的 DNS / 代理 / 路由叠层方案。
- [基于 DNS 的内网透明代理分流方案](https://songchenwen.com/tproxy-split-by-dns) - 透明代理分流，强调 DNS 作为分流控制点。
- [sing-box 全套观看指南 - 开发调优 - LINUX DO](https://linux.do/t/topic/172323) - 代理工具链与网络配置的系统性整理。
- [节点搭建教程，Vmess + WebSocket + TLS + 网站伪装](https://rennen.dev/archives/how-to-build-a-vmess-proxy-node#update-%E5%A6%82%E4%BD%95%E4%B8%BA%E8%8A%82%E7%82%B9%E5%A5%97%E4%B8%8A-cdn) - 偏基础节点搭建和服务器侧网络配置。

## 自动化

- [Turn on a light to a specific color on any update in GitHub repository | n8n workflow template](https://n8n.io/workflows/1856-turn-on-a-light-to-a-specific-color-on-any-update-in-github-repository/) - Webhook / workflow automation 的示例。
- [Memos & n8n ，秒接入 AI](https://immmmm.com/get-ai-memos/) - `memos` 与 `n8n` 的联动，体现事件触发式个人自动化。
- [GitHub - paperless-ngx/paperless-ngx](https://github.com/paperless-ngx/paperless-ngx) - 也可作为后续自动化归档管道的终点系统。

## 居家设备

- [\[Tutorial\] Integrating Aqara G3 into Home Assistant with Video + PTZ - Aqara Products - Aqara Forum](https://forum.aqara.com/t/tutorial-integrating-aqara-g3-into-home-assistant-with-video-ptz/183357) - 摄像头、视频与 PTZ 控制接入 Home Assistant。
- [OpenERV](https://www.openerv.ca/) - 住宅新风/热回收通风，属于家庭环境系统。
- [Play Your PC Games Remotely](https://moonlight-stream.org/) - 家庭内外远程游戏流媒体，属于家庭娱乐基础设施。

## Notes

- 这一批链接内部相对一致，但后续大概率仍需要继续拆分成“家庭网络与代理”“自动化与知识流”“居家设备与环境系统”。
- `bookmarks` 与 `paperless-ngx` 的组合值得后续单独写一页，作为个人知识与文档入口层的具体方案。

## Related

- [Self-Hosting and Home Lab](../topics/self-hosting-and-home-lab.md)
- [Home Ops and Systems](../areas/home-ops-and-systems.md)
- [Software Engineering](../topics/software-engineering.md)
- [Knowledge Management](../topics/knowledge-management.md)

## Follow-ups

- 哪些网络代理与路由方案是主用，哪些只是收藏待试？
- `n8n`、`memos` 和 `paperless-ngx` 是否可以合并成一条完整的个人资料工作流？
- 家庭设备接入是否需要独立出 `home automation` 子主题页？
