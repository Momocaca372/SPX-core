# SPX: Structize Prompt eXchange

**Version**: v1.0  
**Author**: Jiancheng  
**Style**: Clear, open-source, developer-oriented  
**Target Audience**: Developers, AI engineers, software architects, and collaborative teams.

---

## 📌 What is SPX?

SPX (Structize Prompt eXchange) is a semantic-first, structure-driven task modeling language designed to bridge human and AI collaboration in software development. Rather than issuing commands, SPX describes logic, roles, workflows, and output expectations in a composable format.

---

## 🎯 Design Philosophy

- Structure before syntax, intention before implementation  
- Describe the world rather than command it  
- Semantic-driven logic enabling multimodal output  
- Encourages self-expanding modules and inheritance  

---

## 🚀 Quick Start

From prompt to DSL to output:

```
"Help me build a query API with permission validation and error handling"
→ SPX definition FindOneByIdx.spx
→ Generates C# code + Swagger definitions
```

---

## 🧩 Use Modes & Roles

| Mode        | Role               | Edit DSL? | Description |
|-------------|--------------------|-----------|-------------|
| Prompt      | PM, Designer, Analyst | ❌        | Only describe needs; AI transforms into DSL |
| SPX Module  | Developer, AI Integrator | ✅    | Manually edit .spx files, AI handles execution |
| Project/Team | Architect, Tech Lead | ✅      | Maintains `Main.yml` for team-wide consistency |

---

## 🎨 Main.yml: Semantic Style Profile

Defines development conventions:

- Null handling policies  
- Naming and logic patterns  
- Error handling strategy (e.g., Handle500V2)  
- Default parameters for modules (pagination, async, etc.)

---

## ♻️ Expandability & Evolving Style

- Each interaction can generate new style rules  
- Version-controlled, reusable across teams  
- AI can self-patch missing logic styles  

---

## 🤖 AI Integration

- **SPX → Code**: C#, Python, TypeScript  
- **SPX → Text**: Character dialogues, story scripting  
- **SPX → Logic**: Task flows, API definitions, behavioral logic  

---

## 📚 References

- [JetBrains MPS – DSL Concepts](https://www.jetbrains.com/mps/concepts/domain-specific-languages/)
- [Microsoft DSL Tools](https://learn.microsoft.com/en-us/visualstudio/modeling/about-domain-specific-languages)
- [Martin Fowler's DSL Book](https://martinfowler.com/books/dsl.html)
- [Open Source DSL Examples](https://opensource.com/article/20/2/domain-specific-languages)
- [DSLs in Data Engineering (Dagster)](https://medium.com/@dagster-io/standardize-pipelines-with-domain-specific-languages-1f5729fc0f65)

---

## 🚀 Quick Links

- 🔧 [SPX Examples](examples/)
  - [CreateMailData](examples/api/CreateMailData.yml)
  - [Story: Queen Rebellion](examples/story/queen_rebellion.yml)
  - [Image Prompt: Battle Poster](examples/drawing/battle_scene_poster.yml)
  - [AI Role: Tutor Agent](examples/ai/tutor_code_agent.yml)

- 🧱 [Main Structure Template](main.yml)
- 📘 [Framework Description](framework.yml)

## 🙌 Authors and Contributors

This framework was designed by Jiancheng to enable structure-first, collaborative AI-enhanced development. Open contribution encouraged.

---

## 📄 License

SPX is open-sourced under the **MIT License**.  
You are free to use, modify, and distribute this project.  
We ask that you retain the name `SPX` when building extensions, to help the community maintain alignment around its semantic intent.

---

# SPX 語意交換描述框架

**版本**: v1.0  
**作者**: 建程  
**風格**: 清晰、開源、工程導向  
**適用對象**: 開發者、AI 工程師、架構設計師、開發團隊

---

## 📌 什麼是 SPX？

SPX（Structize Prompt eXchange）是一種語意優先、結構驅動的任務建模語言，用來與 AI 或團隊進行一致性的開發協作。與其說是命令語言，不如說是描述結構與邏輯的語意容器。

---

## 🎯 設計理念

- 結構先於語句，意圖先於實作  
- 描述世界，而不是控制它  
- 語意驅動，多模態輸出  
- 鼓勵模組自擴展與繼承

---

## 🚀 快速起手

從 prompt 到 DSL 到產出：

```
「幫我建一支查詢 API，需有權限與錯誤處理」
→ DSL 描述 FindOneByIdx.spx
→ 自動生成 C# 程式 + Swagger 定義
```

---

## 🧩 應用方法與角色

| 模式         | 使用者       | 編輯 DSL？ | 說明 |
|--------------|--------------|-------------|------|
| Prompt 模式  | PM、設計師    | ❌          | 僅下達需求，由 AI 建構 DSL |
| 模組模式     | 開發工程師    | ✅          | 撰寫 `.spx` 文件，AI 輔助執行產出 |
| 團隊/專案模式 | 架構師、主管 | ✅          | 維護 `Main.yml`，作為團隊語意中心 |

---

## 🎨 Main.yml：語意風格設定檔

用來統一全專案風格：

- null 檢查策略  
- 命名與邏輯格式  
- 錯誤處理方式（如 Handle500V2）  
- 預設參數（如分頁、非同步）

---

## ♻️ 模組擴展與風格遞增

- 每次互動可增補語意規則  
- 可版本化、共享給其他團隊  
- AI 可自動補強風格邏輯

---

## 🤖 與 AI 整合應用

- **SPX → 程式碼**：C#, Python, TypeScript  
- **SPX → 敘事文本**：角色對話、世界觀語料  
- **SPX → 邏輯建模**：任務流程、API、決策模型

---

## 📚 參考資料

- [JetBrains MPS – DSL 概念](https://www.jetbrains.com/mps/concepts/domain-specific-languages/)
- [Microsoft DSL Tools](https://learn.microsoft.com/en-us/visualstudio/modeling/about-domain-specific-languages)
- [Martin Fowler's DSL Book](https://martinfowler.com/books/dsl.html)
- [Open Source DSL Use Cases](https://opensource.com/article/20/2/domain-specific-languages)
- [Dagster 的資料工程 DSL](https://medium.com/@dagster-io/standardize-pipelines-with-domain-specific-languages-1f5729fc0f65)

---

## 🙌 作者與貢獻者

此語意框架由建程構思，來自多場景開發經驗與 AI 互動實驗成果。歡迎 Fork、共創與演進。


## 📄 License

SPX is open-sourced under the **MIT License**.  
You are free to use, modify, and distribute this project.  
We ask that you retain the name `SPX` when building extensions, to help the community maintain alignment around its semantic intent.
