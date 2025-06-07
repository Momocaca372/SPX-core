# SPX 使用手冊：互動教學流程

**System:**

⚠️ 使用前閱讀事項：
      SPX 並非傳統 YAML 語言，而是一種為 AI 模型解析優化的語意描述格式。
      雖然語法接近 YAML，但其功能多數仰賴大型語言模型或代理框架進行語義解譯與行為執行。

**System:**

歡迎使用 SPX（Structize Prompt eXchange）語言。SPX 是一種語意優先、結構驅動的描述語言，設計目的是促進人機協作與可重用的任務建模結構。

**User:**

SPX 是什麼？為什麼我要使用它？

**Assistant:**

SPX 是一種用來描述任務結構與邏輯的 DSL（Domain-Specific Language）。它允許開發者清晰地表達任務需求、上下文、角色與輸出格式，有效提升 AI 理解與交互效率。

**User:**

我要如何開始使用 SPX？

**Assistant:**

1. 初始化專案：建立一個包含 `main.spx.yml` 的資料夾，作為專案入口並新增在畫布內。
      2. 啟用自動監聽：在提示流程中導入 `trigger` 區塊，AI 模型將自動根據其中所有定義條目（如 `yaml_update`、`user_command_expand`）的條件與事件觸發對應動作，包括但不限於區塊重構、調用、更新或刪除等操作。

**User:**

SPX 檔案長什麼樣子？

**Assistant:**

以下為基本範例：
      ```yaml
      task:
        id: translate-article
        role: translator
        description: 將技術文件從英文翻譯成繁體中文。
        input:
          - article_en: string
        output:
          - article_zh: string
      ```

**User:**

我可以擴充自己的模組嗎？

**Assistant:**

可以。SPX 支援模組化開發。您可以將常用的任務區塊或子結構封裝為模組，並透過 `include:` 引入。

**User:**

是否有推薦的專案結構？

**Assistant:**

建議如下：
      ```
      /my-spx-project
      ├── main.spx.yml
      ├── modules/
      │   ├── common.spx.yml
      │   └── translation.spx.yml
      └── prompts/
          └── tech-doc.txt
      ```

**User:**

若出現錯誤該怎麼辦？

**Assistant:**

請參考以下建議：
      - 確認語法符合 YAML 標準。
      - 檢查欄位是否遺漏，例如 `role` 或 `input`。
      - 使用驗證工具進行檢查。
      - 查看官方 GitHub issue 或 Discord 社群尋求協助。

**System:**

📌 提醒：與其被動閱讀本文，建議您使用 AI 對本文件進行提問，例如：
      - 「這段 SPX 是什麼意思？」
      - 「幫我修改這段 SPX 讓它支援摘要功能」
      - 「我要如何結合 ChatGPT 回應這個任務？」
      本手冊本身即為可解析的 SPX 資料格式，您可直接讀取、修改，或作為提示輸入至大型語言模型。
