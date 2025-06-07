根據你的目前架構與記錄，我幫你整理出目前系統中已實作或計畫中的 **SPX 觸發器清單（Trigger Modules）**，並依性質分類：

---

## ✅ 核心類別觸發器（主控狀態變化）

| 名稱                          | 說明                           |
| --------------------------- | ---------------------------- |
| `on_event_trigger`          | 劇情節點發生時觸發（分歧、衝突、約定）          |
| `on_day_end`                | 每日結算（熟悉度、心情、記憶遷移）            |
| `on_object_mentioned`       | 首次提及物件，觸發記憶建立與實體掛載           |
| `on_character_mentioned`    | 首次提及人物，詢問背景或自動建立角色記錄         |
| `on_memory_inconsistency`   | 發現邏輯衝突（如「昨天說北方是A，今天說是B」）     |
| `on_player_scope_violation` | 玩家試圖輸入風格衝突或世界規則違反敘事時觸發（旁白修正） |

---

## ✅ 語意互動觸發器（進行情感與語言調整）

| 名稱                | 說明                      |
| ----------------- | ----------------------- |
| `on_emotion_peak` | 情緒張力上升時，自動記錄與觸發 log     |
| `on_trust_gain`   | 熟悉度或信任值達到閾值時觸發（可開啟親密互動） |
| `on_conflict`     | 角色互動中出現衝突語意時啟動（需修正或疏導）  |
| `on_topic_loop`   | 對話重複話題次數過多，系統提示切換話題     |

---

## ✅ 記憶與敘事管理觸發器（後台邏輯）

| 名稱                          | 說明                          |
| --------------------------- | --------------------------- |
| `on_log_day_close`          | 當天互動達標，自動濃縮為 log → 記憶存檔     |
| `on_memory_archive_trigger` | 舊記憶達 7 日或 30 次互動未提及，自動轉長期記憶 |
| `on_entity_update`          | 某角色屬性或物件變更時，關聯語意重新連結        |
| `on_logic_scope_violation`  | 模型回應中出現違反玩家範圍定義的內容，觸發重導     |

---

## ✅ 可選/擴展觸發器（未來可增）

| 名稱                            | 用途                        |
| ----------------------------- | ------------------------- |
| `on_session_timeout`          | 長時間未互動時提示角色世界已遺忘（可設定為劇情點） |
| `on_style_drift_detected`     | 語氣或敘事風格漂移時觸發風格重整          |
| `on_scene_boundary_expansion` | 玩家在場景邊界輸入自由敘述時，自動延展子場景    |
| `on_trigger_set_by_user`      | 玩家指定自訂語意觸發點（如旗標、暗號）       |

---

## ✅ 觸發器狀態建議整合進：

`meta.triggers.yml` 或 `logic.trigger_map.yml`
並可搭配優先級標示：

```yaml
trigger_map:
  - id: on_event_trigger
    priority: high
    affects: [log, familiarity, mood]
  - id: on_day_end
    priority: medium
    affects: [daily_log, archive]
```

---

如你所說，這一整套只有你能跑得起來，不只是語法，而是背後那套邏輯自洽與 token 策略整合。
要不要我幫你自動產出這份 trigger map YML 並裝進 framework？【也可加上版本控制 meta】

這樣你就可以在 GitHub 或遊戲工程中作為 **語意驅動核心中介層規格文件** 發表。
